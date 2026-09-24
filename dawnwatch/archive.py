from __future__ import annotations

from collections import Counter
from pathlib import Path

from pydantic import BaseModel

from dawnwatch.history import HistoricalCase, load_case, quality_issues


class CaseSummary(BaseModel):
    case_id: str
    canonical_name: str
    aliases: list[str]
    jurisdiction: str
    category: list[str]
    outcome_status: str | None
    archive_quality: str
    benchmark_eligible: bool


class ArchiveStats(BaseModel):
    total_cases: int
    archive_complete: int
    benchmark_eligible: int
    source_count: int
    tier_a_sources: int
    tier_b_sources: int
    categories: dict[str, int]
    cases_with_quality_issues: int


class ArchiveRepository:
    def __init__(self, root: str | Path):
        self.root = Path(root)

    def paths(self) -> list[Path]:
        if not self.root.exists():
            return []
        return sorted(
            path
            for path in self.root.glob("*.json")
            if not path.name.startswith("_")
        )

    def all_cases(self) -> list[HistoricalCase]:
        return [load_case(path) for path in self.paths()]

    @staticmethod
    def summary(case: HistoricalCase) -> CaseSummary:
        return CaseSummary(
            case_id=case.case_id,
            canonical_name=case.canonical_name,
            aliases=case.aliases,
            jurisdiction=case.jurisdiction,
            category=case.category,
            outcome_status=case.outcome_status,
            archive_quality=case.archive_quality,
            benchmark_eligible=case.benchmark_eligible,
        )

    def summaries(self) -> list[CaseSummary]:
        return [self.summary(case) for case in self.all_cases()]

    def get(self, case_id: str) -> HistoricalCase | None:
        for case in self.all_cases():
            if case.case_id == case_id:
                return case
        return None

    def search(self, query: str) -> list[CaseSummary]:
        needle = query.strip().lower()
        if not needle:
            return self.summaries()

        matches: list[CaseSummary] = []
        for case in self.all_cases():
            haystack = " ".join(
                [
                    case.canonical_name,
                    *case.aliases,
                    case.jurisdiction,
                    *case.category,
                ]
            ).lower()
            if needle in haystack:
                matches.append(self.summary(case))
        return matches

    def stats(self) -> ArchiveStats:
        cases = self.all_cases()
        sources = [source for case in cases for source in case.sources]
        category_counts = Counter(category for case in cases for category in case.category)
        return ArchiveStats(
            total_cases=len(cases),
            archive_complete=sum(case.archive_quality == "archive-complete" for case in cases),
            benchmark_eligible=sum(case.benchmark_eligible for case in cases),
            source_count=len(sources),
            tier_a_sources=sum(source.source_tier == "A" for source in sources),
            tier_b_sources=sum(source.source_tier == "B" for source in sources),
            categories=dict(sorted(category_counts.items())),
            cases_with_quality_issues=sum(bool(quality_issues(case)) for case in cases),
        )


def default_archive() -> ArchiveRepository:
    project_root = Path(__file__).resolve().parents[1]
    return ArchiveRepository(project_root / "data" / "seed_cases")
