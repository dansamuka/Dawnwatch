from dawnwatch.returns import ReturnClaim, analyze_return_claim


def test_qvse_style_claim_is_flagged_as_extreme() -> None:
    result = analyze_return_claim(ReturnClaim(principal=500, payout=12))
    assert result.implied_daily_return_pct == 2.4
    assert result.implied_monthly_simple_return_pct == 48.0
    assert result.extreme_return_flag is True
