from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from dawnwatch.archive import ArchiveRepository
from dawnwatch.history import STATE_RANK, HistoricalCase, replay_checkpoints
from dawnwatch.models import RiskState


class CaseBenchmark(BaseModel):
    case_id: str
    canonical_name: str
    benchmark_eligible: bool
    first_elevated_or_higher: datetime | None
    next_milestone_type: str | None
    next_milestone_at: datetime | None
    lead_time_days: int | None


def first_elevated_or_higher(case: HistoricalCase) -> datetime | None:
    for checkpoint, assessment in replay_checkpoints(case):
        if STATE_RANK[assessment.state] >= STATE_RANK[RiskState.ELEVATED_CAUTION]:
            return checkpoint
    return None


def benchmark_case(case: HistoricalCase) -> CaseBenchmark:
    first = first_elevated_or_higher(case)
    later_milestones = []
    if first is not None:
        later_milestones = sorted(
            (
                milestone
                for milestone in case.milestones
                if milestone.occurred_at > first
            ),
            key=lambda item: item.occurred_at,
        )
    milestone = later_milestones[0] if later_milestones else None
    lead = None
    if first is not None and milestone is not None:
        lead = (milestone.occurred_at.date() - first.date()).days

    return CaseBenchmark(
        case_id=case.case_id,
        canonical_name=case.canonical_name,
        benchmark_eligible=case.benchmark_eligible,
        first_elevated_or_higher=first,
        next_milestone_type=milestone.milestone_type if milestone else None,
        next_milestone_at=milestone.occurred_at if milestone else None,
        lead_time_days=lead,
    )


def benchmark_archive(archive: ArchiveRepository) -> list[CaseBenchmark]:
    return [benchmark_case(case) for case in archive.all_cases() if case.benchmark_eligible]
