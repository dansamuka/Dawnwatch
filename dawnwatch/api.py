from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from dawnwatch.archive import ArchiveStats, CaseSummary, default_archive
from dawnwatch.benchmark import CaseBenchmark, benchmark_archive
from dawnwatch.controls import (
    ControlAssessment,
    ControlCase,
    ControlStats,
    default_controls,
)
from dawnwatch.discovery import DiscoveryAnalysis, analyze_text
from dawnwatch.history import HistoricalCase, replay_case
from dawnwatch.models import RiskAssessment, RiskEvaluationRequest
from dawnwatch.returns import ReturnAnalysis, ReturnClaim, analyze_return_claim
from dawnwatch.risk_engine import METHODOLOGY_VERSION, WEIGHTS, evaluate

app = FastAPI(
    title="Dawnwatch API",
    version="0.1.0",
    description="Mass Fraud Early Warning & Intelligence",
)

archive = default_archive()
controls = default_controls()


class TextDiscoveryRequest(BaseModel):
    text: str


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


@app.get("/api/v1/archive/stats", response_model=ArchiveStats)
def archive_stats() -> ArchiveStats:
    return archive.stats()


@app.get("/api/v1/archive/benchmarks", response_model=list[CaseBenchmark])
def archive_benchmarks() -> list[CaseBenchmark]:
    return benchmark_archive(archive)


@app.get("/api/v1/archive/cases", response_model=list[CaseSummary])
def archive_cases() -> list[CaseSummary]:
    return archive.summaries()


@app.get("/api/v1/archive/search", response_model=list[CaseSummary])
def archive_search(q: Annotated[str, Query()] = "") -> list[CaseSummary]:
    return archive.search(q)


@app.get("/api/v1/archive/cases/{case_id}", response_model=HistoricalCase)
def archive_case(case_id: str) -> HistoricalCase:
    case = archive.get(case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Historical case not found")
    return case


@app.get("/api/v1/archive/cases/{case_id}/replay", response_model=RiskAssessment)
def archive_case_replay(case_id: str, as_of: datetime) -> RiskAssessment:
    case = archive.get(case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Historical case not found")
    return replay_case(case, as_of)


@app.get("/api/v1/controls/stats", response_model=ControlStats)
def control_stats() -> ControlStats:
    return controls.stats()


@app.get("/api/v1/controls", response_model=list[ControlCase])
def control_cases() -> list[ControlCase]:
    return controls.all_controls()


@app.get("/api/v1/controls/assessments", response_model=list[ControlAssessment])
def control_assessments() -> list[ControlAssessment]:
    return controls.assessments()


@app.post("/api/v1/discovery/analyze-text", response_model=DiscoveryAnalysis)
def discovery_analyze_text(request: TextDiscoveryRequest) -> DiscoveryAnalysis:
    return analyze_text(request.text)


@app.post("/api/v1/risk/evaluate", response_model=RiskAssessment)
def risk_evaluate(request: RiskEvaluationRequest) -> RiskAssessment:
    return evaluate(request)


@app.post("/api/v1/economics/analyze", response_model=ReturnAnalysis)
def economics_analyze(claim: ReturnClaim) -> ReturnAnalysis:
    return analyze_return_claim(claim)
