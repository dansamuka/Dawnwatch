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
