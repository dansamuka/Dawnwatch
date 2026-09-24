from dawnwatch.models import (
    ActivatedIndicator,
    IndicatorType,
    RiskEvaluationRequest,
    RiskState,
)
from dawnwatch.risk_engine import evaluate


def assessment(*indicators: IndicatorType):
    return evaluate(
        RiskEvaluationRequest(
            entity_name="Example",
            indicators=[ActivatedIndicator(indicator=item) for item in indicators],
        )
    )


def test_local_regulator_warning_is_critical() -> None:
    result = assessment(IndicatorType.LOCAL_REGULATOR_WARNING)
    assert result.state == RiskState.CRITICAL_WARNING


def test_pay_to_unlock_plus_withdrawal_failure_is_critical() -> None:
    result = assessment(
        IndicatorType.WIDESPREAD_WITHDRAWAL_FAILURE,
        IndicatorType.PAY_TO_UNLOCK_WITHDRAWAL,
    )
    assert result.state == RiskState.CRITICAL_WARNING


def test_extreme_return_referrals_and_unverified_licence_is_high_risk() -> None:
    result = assessment(
        IndicatorType.EXTREME_RETURN,
        IndicatorType.REFERRAL_RECRUITMENT,
        IndicatorType.NO_VERIFIED_RELEVANT_LICENCE,
    )
    assert result.state == RiskState.HIGH_RISK


def test_positive_verification_reduces_internal_score() -> None:
    base = assessment(IndicatorType.EXTREME_RETURN)
    verified = assessment(
        IndicatorType.EXTREME_RETURN,
        IndicatorType.VERIFIED_RELEVANT_LICENCE,
    )
    assert verified.internal_score < base.internal_score
