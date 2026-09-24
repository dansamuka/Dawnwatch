from dawnwatch.archive import ArchiveRepository


def test_archive_lists_qvse_seed_case() -> None:
    archive = ArchiveRepository("data/seed_cases")
    cases = archive.summaries()
    assert any(case.case_id == "kenya-qvse-2026" for case in cases)


def test_archive_searches_aliases_and_categories() -> None:
    archive = ArchiveRepository("data/seed_cases")

    by_alias = archive.search("QVSE")
    by_category = archive.search("copy-trading")

    assert by_alias[0].case_id == "kenya-qvse-2026"
    assert by_category[0].case_id == "kenya-qvse-2026"


def test_archive_get_missing_case_returns_none() -> None:
    archive = ArchiveRepository("data/seed_cases")
    assert archive.get("does-not-exist") is None
