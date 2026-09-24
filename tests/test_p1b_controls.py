from dawnwatch.controls import ControlRepository, control_quality_issues, evaluate_control
from dawnwatch.models import IndicatorType, RiskState


CONTROLS = ControlRepository("data/control_cases")


def test_p1b_has_ten_unique_controls() -> None:
    cases = CONTROLS.all_controls()
    assert len(cases) == 10
    assert len({case.control_id for case in cases}) == 10


def test_all_controls_pass_quality_gate() -> None:
    failures = {
        case.control_id: control_quality_issues(case)
        for case in CONTROLS.all_controls()
        if control_quality_issues(case)
    }
    assert failures == {}


def test_control_cohort_has_zero_current_false_positives() -> None:
    assessments = CONTROLS.assessments()
    assert sum(item.risk_false_positive for item in assessments) == 0
    assert sum(item.discovery_false_positive for item in assessments) == 0
    assert all(item.risk_state == RiskState.WATCH for item in assessments)


def test_makiba_is_fixed_return_counterexample() -> None:
    case = next(
        item
        for item in CONTROLS.all_controls()
        if item.control_id == "control-ke-m-akiba"
    )
    assert IndicatorType.DETERMINISTIC_RETURN in case.surface_risk_indicators
    assert IndicatorType.VERIFIED_GOVERNMENT_ISSUER in case.positive_indicators

    result = evaluate_control(case)
    assert result.risk_state == RiskState.WATCH
    assert result.risk_false_positive is False


def test_control_stats_are_stable() -> None:
    stats = CONTROLS.stats()
    assert stats.total_controls == 10
    assert stats.quality_clean == 10
    assert stats.risk_false_positives == 0
    assert stats.discovery_false_positives == 0
    assert stats.tier_a_source_references >= 15


def test_controls_cover_key_surface_patterns() -> None:
    patterns = CONTROLS.stats().matched_patterns
    for required in {
        "MASS_MARKET",
        "MOBILE_FIRST",
        "LOW_ENTRY",
        "RETURN_SEEKING",
        "MONEY_MARKET",
        "RECENT_PRODUCT",
        "FIXED_RETURN",
    }:
        assert required in patterns
