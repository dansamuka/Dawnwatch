from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel

from dawnwatch.history import HistoricalCase, load_case


class CaseSummary(BaseModel):
    case_id: str
    canonical_name: str
    aliases: list[str]
    jurisdiction: str
    category: list[str]
    outcome_status: str | None


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

    def summaries(self) -> list[CaseSummary]:
        return [
            CaseSummary(
                case_id=case.case_id,
                canonical_name=case.canonical_name,
                aliases=case.aliases,
                jurisdiction=case.jurisdiction,
                category=case.category,
                outcome_status=case.outcome_status,
            )
            for case in self.all_cases()
        ]

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
                matches.append(
                    CaseSummary(
                        case_id=case.case_id,
                        canonical_name=case.canonical_name,
                        aliases=case.aliases,
                        jurisdiction=case.jurisdiction,
                        category=case.category,
                        outcome_status=case.outcome_status,
                    )
                )
        return matches


def default_archive() -> ArchiveRepository:
    project_root = Path(__file__).resolve().parents[1]
    return ArchiveRepository(project_root / "data" / "seed_cases")
