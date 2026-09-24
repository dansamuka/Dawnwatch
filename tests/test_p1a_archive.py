from dawnwatch.archive import ArchiveRepository
from dawnwatch.benchmark import benchmark_archive
from dawnwatch.history import quality_issues


ARCHIVE = ArchiveRepository("data/seed_cases")


def test_p1a_has_exactly_twenty_cases() -> None:
    cases = ARCHIVE.all_cases()
    assert len(cases) == 20
    assert len({case.case_id for case in cases}) == 20


def test_every_p1a_case_is_archive_complete_and_quality_clean() -> None:
    cases = ARCHIVE.all_cases()
    failures = {
        case.case_id: quality_issues(case)
        for case in cases
        if quality_issues(case)
    }
    assert failures == {}
    assert all(case.archive_quality == "archive-complete" for case in cases)


def test_p1a_has_five_benchmark_eligible_cases() -> None:
    cases = ARCHIVE.all_cases()
    benchmark_ids = {case.case_id for case in cases if case.benchmark_eligible}
    assert benchmark_ids == {
        "kenya-amazon-web-worker-2021",
        "kenya-cbex-2026",
        "kenya-goldenscape-2021",
        "kenya-public-likes-2017",
        "kenya-qvse-2026",
    }


def test_legacy_taskforce_top_ten_aggregate_matches_source_record() -> None:
    legacy_ids = {
        "kenya-deci-2009",
        "kenya-clip-investments-2009",
        "kenya-kbc-sacco-2009",
        "kenya-sasanet-2009",
        "kenya-jitegemee-investment-2009",
        "kenya-circuit-investment-2009",
        "kenya-fino-2009",
        "kenya-global-entrepreneurship-2009",
        "kenya-spell-investment-2009",
        "kenya-mont-blanq-afrique-2009",
    }
    cases = [case for case in ARCHIVE.all_cases() if case.case_id in legacy_ids]

    investors = sum(
        estimate.value or 0
        for case in cases
        for estimate in case.impact_estimates
        if estimate.metric == "registered_investors"
    )
    claims = sum(
        estimate.value or 0
        for case in cases
        for estimate in case.impact_estimates
        if estimate.metric == "registered_claim_value"
    )

    assert investors == 121_205
    assert claims == 7_262_824_632


def test_p1a_benchmark_lead_times_are_stable() -> None:
    results = {item.case_id: item for item in benchmark_archive(ARCHIVE)}

    assert results["kenya-qvse-2026"].lead_time_days == 45
    assert results["kenya-public-likes-2017"].lead_time_days == 11
    assert results["kenya-goldenscape-2021"].lead_time_days == 21
    assert results["kenya-amazon-web-worker-2021"].lead_time_days == 11
    assert results["kenya-cbex-2026"].lead_time_days == 512


def test_archive_stats_reflect_p1a_completion() -> None:
    stats = ARCHIVE.stats()
    assert stats.total_cases == 20
    assert stats.archive_complete == 20
    assert stats.benchmark_eligible == 5
    assert stats.cases_with_quality_issues == 0
    assert stats.source_count >= 40
    assert stats.tier_a_sources >= 10
    assert stats.tier_b_sources >= 20
