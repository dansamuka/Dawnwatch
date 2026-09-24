from datetime import datetime

from dawnwatch.history import load_case, replay_case
from dawnwatch.models import RiskState


CASE_PATH = "data/seed_cases/qvse_2026.json"


def dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def test_qvse_replay_has_no_hindsight_leakage() -> None:
    case = load_case(CASE_PATH)

    before_warning = replay_case(case, dt("2026-07-21T23:59:00+00:00"))
    ghana_warning = replay_case(case, dt("2026-07-22T23:59:00+00:00"))
    kenya_warning = replay_case(case, dt("2026-09-11T23:59:00+03:00"))

    assert before_warning.state == RiskState.WATCH
    assert before_warning.internal_score == 0

    assert ghana_warning.state == RiskState.ELEVATED_CAUTION
    assert ghana_warning.internal_score == 35

    assert kenya_warning.state == RiskState.CRITICAL_WARNING


def test_post_freeze_reporting_does_not_affect_july_snapshot() -> None:
    case = load_case(CASE_PATH)
    july = replay_case(case, dt("2026-07-31T23:59:00+03:00"))

    values = {indicator.value for indicator in july.activated_indicators}
    assert "WIDESPREAD_WITHDRAWAL_FAILURE" not in values
    assert "PAY_TO_UNLOCK_WITHDRAWAL" not in values
    assert "FAILED_PREDECESSOR_LINK" not in values
