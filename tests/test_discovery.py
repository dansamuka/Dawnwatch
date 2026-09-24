from dawnwatch.discovery import analyze_text


def test_mass_recruitment_offer_opens_candidate() -> None:
    result = analyze_text(
        "Deposit KSh 20,000 and earn KSh 5,000 daily. "
        "Join my team for a referral bonus. WhatsApp 0712345678."
    )
    assert result.should_open_candidate is True
    assert "0712345678" in result.phones


def test_plain_investment_discussion_does_not_open_candidate() -> None:
    result = analyze_text("I am reading about long-term investing and capital markets.")
    assert result.should_open_candidate is False
