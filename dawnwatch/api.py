from fastapi import FastAPI

from dawnwatch.models import RiskAssessment, RiskEvaluationRequest
from dawnwatch.returns import ReturnAnalysis, ReturnClaim, analyze_return_claim
from dawnwatch.risk_engine import METHODOLOGY_VERSION, WEIGHTS, evaluate

app = FastAPI(
    title="Dawnwatch API",
    version="0.1.0",
    description="Mass Fraud Early Warning & Intelligence",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "dawnwatch"}


@app.get("/api/v1/methodology")
def methodology() -> dict[str, object]:
    return {
        "version": METHODOLOGY_VERSION,
        "principle": (
            "Evidence-backed risk states, not an unsupported probability that an entity is fraudulent."
        ),
        "weights": {indicator.value: weight for indicator, weight in WEIGHTS.items()},
    }


@app.post("/api/v1/risk/evaluate", response_model=RiskAssessment)
def risk_evaluate(request: RiskEvaluationRequest) -> RiskAssessment:
    return evaluate(request)


@app.post("/api/v1/economics/analyze", response_model=ReturnAnalysis)
def economics_analyze(claim: ReturnClaim) -> ReturnAnalysis:
    return analyze_return_claim(claim)
