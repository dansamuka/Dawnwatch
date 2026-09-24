from __future__ import annotations

from pydantic import BaseModel, Field


class ReturnClaim(BaseModel):
    principal: float = Field(gt=0)
    payout: float = Field(gt=0)
    payout_frequency_days: float = Field(default=1.0, gt=0)
    trading_days_per_month: int = Field(default=20, gt=0, le=31)


class ReturnAnalysis(BaseModel):
    principal: float
    payout: float
    payout_frequency_days: float
    implied_daily_return_pct: float
    implied_monthly_simple_return_pct: float
    implied_monthly_compounded_return_pct: float
    extreme_return_flag: bool
    deterministic_return_flag: bool
    explanation: str


def analyze_return_claim(claim: ReturnClaim) -> ReturnAnalysis:
    payout_period_return = claim.payout / claim.principal
    daily_rate = payout_period_return / claim.payout_frequency_days
    monthly_simple = daily_rate * claim.trading_days_per_month
    monthly_compounded = (1 + daily_rate) ** claim.trading_days_per_month - 1

    extreme = daily_rate >= 0.01 or monthly_simple >= 0.20

    return ReturnAnalysis(
        principal=claim.principal,
        payout=claim.payout,
        payout_frequency_days=claim.payout_frequency_days,
        implied_daily_return_pct=round(daily_rate * 100, 4),
        implied_monthly_simple_return_pct=round(monthly_simple * 100, 4),
        implied_monthly_compounded_return_pct=round(monthly_compounded * 100, 4),
        extreme_return_flag=extreme,
        deterministic_return_flag=True,
        explanation=(
            "The calculation describes the advertised payout mechanics only. "
            "It does not prove that the return is achievable or fraudulent. "
            "Extreme or unusually deterministic returns should trigger independent verification."
        ),
    )
