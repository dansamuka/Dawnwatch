from datetime import datetime

from dawnwatch.archive import ArchiveRepository
from dawnwatch.history import first_reached_state, lead_time_days, replay_case
from dawnwatch.models import RiskState


ARCHIVE = ArchiveRepository("data/seed_cases")


def dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def test_public_likes_depth_moves_warning_to_june_8() -> None:
    case = ARCHIVE.get("kenya-public-likes-2017")
    assert case is not None
    assert first_reached_state(case, RiskState.ELEVATED_CAUTION) == dt(
        "2017-06-08T00:00:00+03:00"
    )
    assert lead_time_days(
        case,
        RiskState.ELEVATED_CAUTION,
        "MPESA_PAYBILL_SUSPENDED",
    ) == 46


def test_qvse_archived_referral_signal_does_not_over_escalate() -> None:
    case = ARCHIVE.get("kenya-qvse-2026")
    assert case is not None

    referral_day = replay_case(case, dt("2026-07-21T23:59:00+03:00"))
    ghana_day = replay_case(case, dt("2026-07-22T23:59:00+03:00"))

    assert referral_day.state == RiskState.WATCH
    assert ghana_day.state == RiskState.ELEVATED_CAUTION


def test_bitstream_referenced_warning_is_not_used_without_original_date() -> None:
    case = ARCHIVE.get("kenya-bitstream-circle-2022")
    assert case is not None
    assert case.benchmark_eligible is False
    assert any(
        stage.stage == "PRE_COLLAPSE_WARNING_REFERENCED_LATER"
        for stage in case.lifecycle_stages
    )


def test_goldenscape_has_domain_expert_scrutiny_stage() -> None:
    case = ARCHIVE.get("kenya-goldenscape-2021")
    assert case is not None
    assert any(
        stage.stage == "INDEPENDENT_MODEL_SCRUTINY"
        for stage in case.lifecycle_stages
    )
