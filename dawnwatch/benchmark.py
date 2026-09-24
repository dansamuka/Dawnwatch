from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from dawnwatch.archive import ArchiveRepository
from dawnwatch.history import HistoricalCase, first_reached_state
from dawnwatch.models import RiskState


class CaseBenchmark(BaseModel):
    case_id: str
    canonical_name: str
    benchmark_eligible: bool
    benchmark_kind: str
    target_state: RiskState
    first_target_state: datetime | None
    milestone_type: str
    milestone_at: datetime | None
    lead_time_days: int | None
    interpretation: str


def benchmark_case(case: HistoricalCase) -> CaseBenchmark:
    if not case.benchmark_eligible or case.benchmark_definition is None:
        raise ValueError(f"Case {case.case_id} is not benchmark-eligible")

    definition = case.benchmark_definition
    first = first_reached_state(case, definition.target_state)
    milestone = next(
        (
            item
            for item in case.milestones
            if item.milestone_type == definition.milestone_type
        ),
        None,
    )

    lead = None
    if first is not None and milestone is not None:
        lead = (milestone.occurred_at.date() - first.date()).days

    return CaseBenchmark(
        case_id=case.case_id,
        canonical_name=case.canonical_name,
        benchmark_eligible=True,
        benchmark_kind=definition.benchmark_kind,
        target_state=definition.target_state,
        first_target_state=first,
        milestone_type=definition.milestone_type,
        milestone_at=milestone.occurred_at if milestone else None,
        lead_time_days=lead,
        interpretation=definition.interpretation,
    )


def benchmark_archive(archive: ArchiveRepository) -> list[CaseBenchmark]:
    return [benchmark_case(case) for case in archive.all_cases() if case.benchmark_eligible]
