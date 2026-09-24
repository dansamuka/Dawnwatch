from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class RiskState(StrEnum):
    WATCH = "WATCH"
    ELEVATED_CAUTION = "ELEVATED CAUTION"
    HIGH_RISK = "HIGH RISK"
    CRITICAL_WARNING = "CRITICAL WARNING"
    REGULATORY_ENFORCEMENT_CONFIRMED = "REGULATORY / ENFORCEMENT CONFIRMED"
    RESOLVED = "RESOLVED"
    CLEARED = "CLEARED / FALSE POSITIVE"


class SourceTier(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class IndicatorType(StrEnum):
    LOCAL_REGULATOR_WARNING = "LOCAL_REGULATOR_WARNING"
    FOREIGN_REGULATOR_WARNING = "FOREIGN_REGULATOR_WARNING"
    LICENCE_MISMATCH = "LICENCE_MISMATCH"
    NO_VERIFIED_RELEVANT_LICENCE = "NO_VERIFIED_RELEVANT_LICENCE"
    PAY_TO_UNLOCK_WITHDRAWAL = "PAY_TO_UNLOCK_WITHDRAWAL"
    FAILED_PREDECESSOR_LINK = "FAILED_PREDECESSOR_LINK"
    WIDESPREAD_WITHDRAWAL_FAILURE = "WIDESPREAD_WITHDRAWAL_FAILURE"
    IDENTITY_DECEPTION_EVIDENCE = "IDENTITY_DECEPTION_EVIDENCE"
    EXTREME_RETURN = "EXTREME_RETURN"
    DETERMINISTIC_RETURN = "DETERMINISTIC_RETURN"
    COMPLAINT_VELOCITY_SPIKE = "COMPLAINT_VELOCITY_SPIKE"
    REFERRAL_RECRUITMENT = "REFERRAL_RECRUITMENT"
    FOUNDER_UNVERIFIED = "FOUNDER_UNVERIFIED"
    RECRUITMENT_VELOCITY_SPIKE = "RECRUITMENT_VELOCITY_SPIKE"
    RECENT_ENTITY_OR_DOMAIN = "RECENT_ENTITY_OR_DOMAIN"
    CRYPTO_ONLY_PAYMENT = "CRYPTO_ONLY_PAYMENT"
    VERIFIED_RELEVANT_LICENCE = "VERIFIED_RELEVANT_LICENCE"
    VERIFIED_REGULATED_CUSTODY = "VERIFIED_REGULATED_CUSTODY"
    AUTHORITATIVE_GOVERNMENT_FINDING = "AUTHORITATIVE_GOVERNMENT_FINDING"
    VERIFIED_GOVERNMENT_ISSUER = "VERIFIED_GOVERNMENT_ISSUER"


class EvidenceRef(BaseModel):
    evidence_id: str
    source_tier: SourceTier
    source_name: str | None = None
    published_at: datetime | None = None
    observed_at: datetime | None = None


class ActivatedIndicator(BaseModel):
    indicator: IndicatorType
    confirmed: bool = True
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    evidence: list[EvidenceRef] = Field(default_factory=list)


class RiskEvaluationRequest(BaseModel):
    entity_name: str
    indicators: list[ActivatedIndicator]
    is_new_mass_recruitment_candidate: bool = False


class RiskAssessment(BaseModel):
    entity_name: str
    state: RiskState
    internal_score: int
    activated_indicators: list[IndicatorType]
    reasons: list[str]
    methodology_version: str = "0.1"
