from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, Field

from dawnwatch.models import ActivatedIndicator, IndicatorType, RiskAssessment, RiskEvaluationRequest
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
    notes: list[str] = Field(default_factory=list)


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
