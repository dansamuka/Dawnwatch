from __future__ import annotations

from collections.abc import Iterable

from dawnwatch.models import (
    ActivatedIndicator,
    IndicatorType,
    RiskAssessment,
    RiskEvaluationRequest,
    RiskState,
)

METHODOLOGY_VERSION = "0.1"

WEIGHTS: dict[IndicatorType, int] = {
    IndicatorType.LOCAL_REGULATOR_WARNING: 45,
    IndicatorType.FOREIGN_REGULATOR_WARNING: 35,
    IndicatorType.LICENCE_MISMATCH: 30,
    IndicatorType.NO_VERIFIED_RELEVANT_LICENCE: 15,
    IndicatorType.PAY_TO_UNLOCK_WITHDRAWAL: 35,
    IndicatorType.FAILED_PREDECESSOR_LINK: 30,
    IndicatorType.WIDESPREAD_WITHDRAWAL_FAILURE: 30,
    IndicatorType.IDENTITY_DECEPTION_EVIDENCE: 25,
    IndicatorType.EXTREME_RETURN: 20,
    IndicatorType.DETERMINISTIC_RETURN: 18,
    IndicatorType.COMPLAINT_VELOCITY_SPIKE: 15,
    IndicatorType.REFERRAL_RECRUITMENT: 12,
    IndicatorType.FOUNDER_UNVERIFIED: 12,
    IndicatorType.RECRUITMENT_VELOCITY_SPIKE: 10,
    IndicatorType.RECENT_ENTITY_OR_DOMAIN: 8,
    IndicatorType.CRYPTO_ONLY_PAYMENT: 8,
    IndicatorType.VERIFIED_RELEVANT_LICENCE: -25,
    IndicatorType.VERIFIED_REGULATED_CUSTODY: -20,
}


def _confirmed_types(indicators: Iterable[ActivatedIndicator]) -> set[IndicatorType]:
    return {item.indicator for item in indicators if item.confirmed}


def _score(indicators: Iterable[ActivatedIndicator]) -> int:
    return sum(
        round(WEIGHTS.get(item.indicator, 0) * item.confidence)
        for item in indicators
        if item.confirmed
    )


def evaluate(request: RiskEvaluationRequest) -> RiskAssessment:
    confirmed = _confirmed_types(request.indicators)
    score = _score(request.indicators)
    reasons: list[str] = []

    if IndicatorType.LOCAL_REGULATOR_WARNING in confirmed:
        state = RiskState.CRITICAL_WARNING
        reasons.append("A confirmed local regulator warning is present.")
    elif {
        IndicatorType.WIDESPREAD_WITHDRAWAL_FAILURE,
        IndicatorType.PAY_TO_UNLOCK_WITHDRAWAL,
    }.issubset(confirmed):
        state = RiskState.CRITICAL_WARNING
        reasons.append(
            "Withdrawal failure is combined with an additional payment requirement."
        )
    elif (
        IndicatorType.FAILED_PREDECESSOR_LINK in confirmed
        and IndicatorType.RECRUITMENT_VELOCITY_SPIKE in confirmed
    ):
        state = RiskState.HIGH_RISK
        reasons.append(
            "The entity is strongly linked to a failed predecessor while recruitment is accelerating."
        )
    elif {
        IndicatorType.EXTREME_RETURN,
        IndicatorType.NO_VERIFIED_RELEVANT_LICENCE,
        IndicatorType.REFERRAL_RECRUITMENT,
    }.issubset(confirmed):
        state = RiskState.HIGH_RISK
        reasons.append(
            "Extreme advertised returns, referral recruitment, and unresolved relevant licensing "
            "are present together."
        )
    elif score >= 55:
        state = RiskState.HIGH_RISK
        reasons.append("Multiple evidence-backed indicators produce a high internal priority score.")
    elif score >= 25:
        state = RiskState.ELEVATED_CAUTION
        reasons.append("Multiple risk indicators require independent verification.")
    elif request.is_new_mass_recruitment_candidate and len(confirmed) >= 3:
        state = RiskState.WATCH
        reasons.append("A newly detected mass-recruitment proposition has multiple warning signals.")
    else:
        state = RiskState.WATCH
        reasons.append("Insufficient evidence for a stronger public risk state; continue monitoring.")

    return RiskAssessment(
        entity_name=request.entity_name,
        state=state,
        internal_score=score,
        activated_indicators=sorted(confirmed, key=lambda item: item.value),
        reasons=reasons,
        methodology_version=METHODOLOGY_VERSION,
    )
