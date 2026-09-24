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
