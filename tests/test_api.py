from fastapi.testclient import TestClient

from dawnwatch.api import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "dawnwatch"


def test_risk_evaluation_endpoint() -> None:
    response = client.post(
        "/api/v1/risk/evaluate",
        json={
            "entity_name": "Example",
            "indicators": [
                {
                    "indicator": "LOCAL_REGULATOR_WARNING",
                    "confirmed": True,
                    "confidence": 1.0,
                    "evidence": [],
                }
            ],
        },
    )
    assert response.status_code == 200
    assert response.json()["state"] == "CRITICAL WARNING"


def test_archive_lists_seed_case() -> None:
    response = client.get("/api/v1/archive/cases")
    assert response.status_code == 200
    assert any(item["case_id"] == "kenya-qvse-2026" for item in response.json())


def test_archive_search_finds_qvse() -> None:
    response = client.get("/api/v1/archive/search", params={"q": "QVSE"})
    assert response.status_code == 200
    assert response.json()[0]["case_id"] == "kenya-qvse-2026"


def test_archive_replay_respects_historical_date() -> None:
    response = client.get(
        "/api/v1/archive/cases/kenya-qvse-2026/replay",
        params={"as_of": "2026-07-22T23:59:00+00:00"},
    )
    assert response.status_code == 200
    assert response.json()["state"] == "ELEVATED CAUTION"


def test_archive_stats_show_p1a_twenty_cases() -> None:
    response = client.get("/api/v1/archive/stats")
    assert response.status_code == 200
    payload = response.json()
    assert payload["total_cases"] == 20
    assert payload["archive_complete"] == 20
    assert payload["benchmark_eligible"] == 5
    assert payload["cases_with_quality_issues"] == 0


def test_archive_benchmarks_include_qvse_lead_time() -> None:
    response = client.get("/api/v1/archive/benchmarks")
    assert response.status_code == 200
    results = {item["case_id"]: item for item in response.json()}
    assert results["kenya-qvse-2026"]["lead_time_days"] == 45


def test_control_stats_show_clean_p1b_cohort() -> None:
    response = client.get("/api/v1/controls/stats")
    assert response.status_code == 200
    payload = response.json()
    assert payload["total_controls"] == 10
    assert payload["quality_clean"] == 10
    assert payload["risk_false_positives"] == 0
    assert payload["discovery_false_positives"] == 0


def test_control_assessments_keep_makiba_at_watch() -> None:
    response = client.get("/api/v1/controls/assessments")
    assert response.status_code == 200
    results = {item["control_id"]: item for item in response.json()}
    assert results["control-ke-m-akiba"]["risk_state"] == "WATCH"
    assert results["control-ke-m-akiba"]["risk_false_positive"] is False
