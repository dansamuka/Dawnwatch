from __future__ import annotations

import re

from pydantic import BaseModel, Field


class DiscoverySignal(BaseModel):
    category: str
    matched_terms: list[str]


class DiscoveryAnalysis(BaseModel):
    should_open_candidate: bool
    signal_count: int
    signals: list[DiscoverySignal]
    phones: list[str] = Field(default_factory=list)
    urls: list[str] = Field(default_factory=list)
    explanation: str


SIGNAL_PATTERNS: dict[str, tuple[str, ...]] = {
    "financial_offer": (
        r"\bdeposit\b",
        r"\binvest\b",
        r"\bcapital\b",
        r"\bprincipal\b",
        r"\btrading\b",
        r"\bforex\b",
        r"\bcrypto\b",
    ),
    "income_claim": (
        r"\bearn\b",
        r"\breturn(?:s)?\b",
        r"\bprofit(?:s)?\b",
        r"\bincome\b",
        r"\bper day\b",
        r"\bdaily\b",
        r"\bguaranteed\b",
    ),
    "recruitment": (
        r"\bjoin my team\b",
        r"\breferral\b",
        r"\brefer\b",
        r"\brecruit\b",
        r"\bdownline\b",
        r"\bteam bonus\b",
    ),
    "urgency": (
        r"\blimited slots\b",
        r"\bregister today\b",
        r"\bdeposit today\b",
        r"\bends today\b",
        r"\bdeadline\b",
    ),
    "withdrawal_or_unlock": (
        r"\bwithdraw(?:al|als)?\b",
        r"\bunlock\b",
        r"\bactivation fee\b",
        r"\bverification fee\b",
        r"\breactivat(?:e|ion)\b",
    ),
}

PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+?254|0)?7\d{8}(?!\d)")
URL_PATTERN = re.compile(r"https?://[^\s<>\]\)]+", re.IGNORECASE)


def analyze_text(text: str) -> DiscoveryAnalysis:
    normalized = text.lower()
    signals: list[DiscoverySignal] = []

    for category, patterns in SIGNAL_PATTERNS.items():
        matches: list[str] = []
        for pattern in patterns:
            hit = re.search(pattern, normalized, flags=re.IGNORECASE)
            if hit:
                matches.append(hit.group(0))
        if matches:
            signals.append(DiscoverySignal(category=category, matched_terms=sorted(set(matches))))

    categories = {signal.category for signal in signals}
    core_offer = "financial_offer" in categories and "income_claim" in categories
    supporting = len(categories & {"recruitment", "urgency", "withdrawal_or_unlock"})
    should_open = core_offer and (supporting >= 1 or len(categories) >= 3)

    phones = sorted(set(PHONE_PATTERN.findall(text)))
    urls = sorted(set(URL_PATTERN.findall(text)))

    return DiscoveryAnalysis(
        should_open_candidate=should_open,
        signal_count=len(signals),
        signals=signals,
        phones=phones,
        urls=urls,
        explanation=(
            "This is a triage classifier for opening an investigation candidate. "
            "A match is not a finding of fraud and must be followed by evidence enrichment."
        ),
    )
