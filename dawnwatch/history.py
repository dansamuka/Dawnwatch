from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, Field

from dawnwatch.models import (
    ActivatedIndicator,
    IndicatorType,
    RiskAssessment,
    RiskEvaluationRequest,
    RiskState,
)
from dawnwatch.risk_engine import evaluate


class HistoricalSource(BaseModel):
    source_id: str
    source_name: str
    source_tier: str
    url: str
    published_at: datetime
    title: str | None = None


class HistoricalIndicatorEvent(BaseModel):
    observed_at: datetime
    indicator: IndicatorType
    confirmed: bool = True
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    source_ids: list[str] = Field(default_factory=list)
    note: str | None = None


class HistoricalMilestone(BaseModel):
    milestone_type: str
    occurred_at: datetime
    first_documented_at: datetime
    source_ids: list[str] = Field(default_factory=list)
    note: str | None = None


class HistoricalCase(BaseModel):
    case_id: str
    canonical_name: str
    aliases: list[str] = Field(default_factory=list)
    jurisdiction: str
    category: list[str] = Field(default_factory=list)
    active_from: datetime | None = None
    active_to: datetime | None = None
    outcome_status: str | None = None
    sources: list[HistoricalSource] = Field(default_factory=list)
    indicator_events: list[HistoricalIndicatorEvent] = Field(default_factory=list)
    milestones: list[HistoricalMilestone] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


STATE_RANK: dict[RiskState, int] = {
    RiskState.WATCH: 0,
    RiskState.ELEVATED_CAUTION: 1,
    RiskState.HIGH_RISK: 2,
    RiskState.CRITICAL_WARNING: 3,
    RiskState.REGULATORY_ENFORCEMENT_CONFIRMED: 4,
    RiskState.RESOLVED: 0,
    RiskState.CLEARED: 0,
}


def load_case(path: str | Path) -> HistoricalCase:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return HistoricalCase.model_validate(data)


def replay_case(case: HistoricalCase, as_of: datetime) -> RiskAssessment:
    eligible = [event for event in case.indicator_events if event.observed_at <= as_of]
    latest: dict[IndicatorType, HistoricalIndicatorEvent] = {}

    for event in sorted(eligible, key=lambda item: item.observed_at):
        latest[event.indicator] = event

    indicators = [
        ActivatedIndicator(
            indicator=event.indicator,
            confirmed=event.confirmed,
            confidence=event.confidence,
        )
        for event in latest.values()
        if event.confirmed
    ]

    return evaluate(
        RiskEvaluationRequest(
            entity_name=case.canonical_name,
            indicators=indicators,
            is_new_mass_recruitment_candidate=bool(indicators),
        )
    )


def replay_checkpoints(case: HistoricalCase) -> list[tuple[datetime, RiskAssessment]]:
    checkpoints = sorted({event.observed_at for event in case.indicator_events})
    return [(checkpoint, replay_case(case, checkpoint)) for checkpoint in checkpoints]


def first_reached_state(case: HistoricalCase, target: RiskState) -> datetime | None:
    target_rank = STATE_RANK[target]
    for checkpoint, assessment in replay_checkpoints(case):
        if STATE_RANK[assessment.state] >= target_rank:
            return checkpoint
    return None


def lead_time_days(
    case: HistoricalCase,
    target: RiskState,
    milestone_type: str,
) -> int | None:
    first_reached = first_reached_state(case, target)
    if first_reached is None:
        return None

    milestone = next(
        (
            item
            for item in case.milestones
            if item.milestone_type == milestone_type
        ),
        None,
    )
    if milestone is None:
        return None

    return (milestone.occurred_at.date() - first_reached.date()).days
