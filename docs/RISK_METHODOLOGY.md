# Dawnwatch Risk Methodology

## Purpose

Dawnwatch produces **evidence-backed risk states**, not an unsupported probability that an entity is fraudulent.

## Public states

| State | Meaning |
|---|---|
| WATCH | Newly detected proposition requiring monitoring. |
| ELEVATED CAUTION | Multiple concerns exist, but evidence remains incomplete or mixed. |
| HIGH RISK | Strong independently observable anomalies or verification failures exist. |
| CRITICAL WARNING | Severe verified indicators exist, such as regulator warning, pay-to-unlock withdrawal, confirmed licence mismatch, or strong linkage to a failed predecessor. |
| REGULATORY / ENFORCEMENT CONFIRMED | A competent authority has formally acted. This does not imply conviction. |
| RESOLVED | The case has a defined concluded state. |
| CLEARED / FALSE POSITIVE | Material evidence contradicts the prior suspicion. |

## Initial deterministic weights

Weights are prioritization aids and must be calibrated through historical replay.

| Indicator | Weight |
|---|---:|
| LOCAL_REGULATOR_WARNING | 45 |
| FOREIGN_REGULATOR_WARNING | 35 |
| LICENCE_MISMATCH | 30 |
| PAY_TO_UNLOCK_WITHDRAWAL | 35 |
| FAILED_PREDECESSOR_LINK | 30 |
| WIDESPREAD_WITHDRAWAL_FAILURE | 30 |
| IDENTITY_DECEPTION_EVIDENCE | 25 |
| EXTREME_RETURN | 20 |
| DETERMINISTIC_RETURN | 18 |
| COMPLAINT_VELOCITY_SPIKE | 15 |
| REFERRAL_RECRUITMENT | 12 |
| FOUNDER_UNVERIFIED | 12 |
| RECRUITMENT_VELOCITY_SPIKE | 10 |
| RECENT_ENTITY_OR_DOMAIN | 8 |
| CRYPTO_ONLY_PAYMENT | 8 |
| VERIFIED_RELEVANT_LICENCE | -25 |
| VERIFIED_REGULATED_CUSTODY | -20 |

## State rules in v0.1

- A confirmed local regulator warning is sufficient for `CRITICAL WARNING`.
- Confirmed withdrawal freeze plus pay-to-unlock demand is sufficient for `CRITICAL WARNING`.
- A strong failed-predecessor link plus active mass recruitment is at least `HIGH RISK`.
- Extreme returns + no verified relevant licence + referral recruitment is at least `HIGH RISK`.
- New mass recruitment with at least three evidence-backed concerns enters `WATCH` or `ELEVATED CAUTION` depending on severity.

The numeric score is **not** displayed as “fraud probability.”

## Evidence rules

High-impact public classifications require:
- attributable evidence;
- source-quality assessment;
- entity resolution confidence;
- human review when a named person is implicated or criminal conduct is alleged.

The engine must record **which indicators caused the state**, not merely the resulting state.
