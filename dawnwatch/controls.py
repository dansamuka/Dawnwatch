from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, Field

from dawnwatch.discovery import DiscoveryAnalysis, analyze_text
from dawnwatch.history import HistoricalSource, STATE_RANK
from dawnwatch.models import (
    ActivatedIndicator,
    IndicatorType,
    RiskAssessment,
    RiskEvaluationRequest,
    RiskState,
)
from dawnwatch.risk_engine import evaluate


class ControlVerificationEvent(BaseModel):
    observed_at: datetime
    verification_type: str
    source_ids: list[str] = Field(default_factory=list)
    note: str | None = None


class ControlCase(BaseModel):
    control_id: str
    canonical_name: str
    jurisdiction: str = "Kenya"
    control_type: str
    matched_patterns: list[str] = Field(default_factory=list)
    expected_max_state: RiskState = RiskState.WATCH
    sources: list[HistoricalSource] = Field(default_factory=list)
    verification_events: list[ControlVerificationEvent] = Field(default_factory=list)
    positive_indicators: list[IndicatorType] = Field(default_factory=list)
    surface_risk_indicators: list[IndicatorType] = Field(default_factory=list)
    sample_marketing_text: str
    notes: list[str] = Field(default_factory=list)


class ControlAssessment(BaseModel):
    control_id: str
    canonical_name: str
    risk_state: RiskState
    internal_score: int
    expected_max_state: RiskState
    risk_false_positive: bool
    discovery_should_open_candidate: bool
    discovery_false_positive: bool
    matched_patterns: list[str]


class ControlStats(BaseModel):
    total_controls: int
    quality_clean: int
    risk_false_positives: int
    discovery_false_positives: int
    tier_a_source_references: int
    tier_b_source_references: int
    matched_patterns: dict[str, int]


def load_control(path: str | Path) -> ControlCase:
    return ControlCase.model_validate_json(Path(path).read_text(encoding="utf-8"))


def control_quality_issues(case: ControlCase) -> list[str]:
    issues: list[str] = []
    known_sources = {source.source_id for source in case.sources}

    if len(case.sources) < 2:
        issues.append("fewer_than_two_sources")
    if not any(source.source_tier == "A" for source in case.sources):
        issues.append("no_tier_a_source")
    if any(
        source.published_at is None and source.observed_at is None
        for source in case.sources
    ):
        issues.append("source_without_time_provenance")
    if not case.verification_events:
        issues.append("no_verification_events")
    if not case.positive_indicators:
        issues.append("no_positive_indicators")
    if not case.matched_patterns:
        issues.append("no_matched_patterns")
    if not case.sample_marketing_text.strip():
        issues.append("no_sample_marketing_text")

    referenced = {
        source_id
        for event in case.verification_events
        for source_id in event.source_ids
    }
    missing = sorted(referenced - known_sources)
    if missing:
        issues.append("unknown_source_ids:" + ",".join(missing))

    return issues


def evaluate_control(case: ControlCase) -> ControlAssessment:
    indicators = [
        ActivatedIndicator(indicator=indicator)
        for indicator in [*case.surface_risk_indicators, *case.positive_indicators]
    ]
    risk: RiskAssessment = evaluate(
        RiskEvaluationRequest(
            entity_name=case.canonical_name,
            indicators=indicators,
            is_new_mass_recruitment_candidate=False,
        )
    )
    discovery: DiscoveryAnalysis = analyze_text(case.sample_marketing_text)

    return ControlAssessment(
        control_id=case.control_id,
        canonical_name=case.canonical_name,
        risk_state=risk.state,
        internal_score=risk.internal_score,
        expected_max_state=case.expected_max_state,
        risk_false_positive=STATE_RANK[risk.state] > STATE_RANK[case.expected_max_state],
        discovery_should_open_candidate=discovery.should_open_candidate,
        discovery_false_positive=discovery.should_open_candidate,
        matched_patterns=case.matched_patterns,
    )


class ControlRepository:
    def __init__(self, root: str | Path):
        self.root = Path(root)

    def paths(self) -> list[Path]:
        if not self.root.exists():
            return []
        return sorted(path for path in self.root.glob("*.json") if not path.name.startswith("_"))

    def all_controls(self) -> list[ControlCase]:
        return [load_control(path) for path in self.paths()]

    def assessments(self) -> list[ControlAssessment]:
        return [evaluate_control(case) for case in self.all_controls()]

    def stats(self) -> ControlStats:
        cases = self.all_controls()
        assessments = [evaluate_control(case) for case in cases]
        patterns = Counter(pattern for case in cases for pattern in case.matched_patterns)
        sources = [source for case in cases for source in case.sources]
        return ControlStats(
            total_controls=len(cases),
            quality_clean=sum(not control_quality_issues(case) for case in cases),
            risk_false_positives=sum(item.risk_false_positive for item in assessments),
            discovery_false_positives=sum(item.discovery_false_positive for item in assessments),
            tier_a_source_references=sum(source.source_tier == "A" for source in sources),
            tier_b_source_references=sum(source.source_tier == "B" for source in sources),
            matched_patterns=dict(sorted(patterns.items())),
        )


def default_controls() -> ControlRepository:
    project_root = Path(__file__).resolve().parents[1]
    return ControlRepository(project_root / "data" / "control_cases")
