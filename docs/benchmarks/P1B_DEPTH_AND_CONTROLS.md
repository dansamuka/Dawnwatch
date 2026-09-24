# P1B — Historical Depth + Matched Control Cohort

**Status:** Implemented  
**Implemented:** 24 September 2026  
**Positive corpus:** 20 Kenyan historical cases  
**Matched controls:** 10 verified Kenyan investment propositions  
**Purpose:** deepen original-date evidence and introduce explicit false-positive testing before any material risk-weight recalibration.

---

## 1. P1B objective

P1A established a positive-case archive. That is useful for pattern discovery but insufficient for calibration because a system trained only on known failures can learn to overreact to ordinary investment language.

P1B therefore adds two things:

1. **Historical depth** — earlier, more original evidence for selected positive cases.
2. **Matched controls** — legitimate/verified propositions that share surface characteristics with suspicious schemes.

The goal is not to claim production accuracy. The goal is to create a stronger validation substrate.

---

## 2. Historical-depth work completed

### Public Likes

P1A's earliest seeded warning was 13 July 2017.

P1B recovered a contemporaneous Nairobi Wire warning dated **8 June 2017** that challenged:
- the economics of the paid-like model;
- recurring package earnings;
- referral-driven spread;
- the sustainability of advertiser-funded payouts.

Dawnwatch now reaches **Elevated Caution on 8 June 2017**.

Target milestone:
- M-Pesa Paybill suspension — 24 July 2017.

Lead time:
- **46 days**, up from 11 days in the initial P1A reconstruction.

### QVSE

P1B adds:
- an archived registration capture dated **21 July 2026** containing invitation-code fields;
- the **12 August 2026 National Assembly request for statement** on QVSE / Global Investment Group.

The July 21 capture adds a lower-confidence referral-recruitment signal. Because Ghana SEC's warning followed on 22 July, QVSE still reaches Elevated Caution on 22 July.

Current lead time to reported account freeze:
- **45 days**.

P1B deliberately preserves the provenance caveat:
- the retrieval route for the July 21 capture is a later Tech-ish investigation;
- the underlying capture itself is dated 21 July;
- its confidence is therefore reduced;
- it does not change the public state before the Ghana regulator warning.

### Bitstream Circle

A People Daily report dated 27 April 2022 quotes a researcher saying Techspace Africa had warned Kenyans about Bitstream **before collapse**.

P1B records this as `PRE_COLLAPSE_WARNING_REFERENCED_LATER` but does **not** admit it as a replay indicator because the original dated Techspace warning has not yet been recovered.

This is intentional anti-hindsight behavior.

### Goldenscape

P1B adds independent agricultural-economics scrutiny from The Standard / FarmKenya.

The analysis challenged:
- fixed agricultural profit promises;
- hands-off "invest and wait" farming economics;
- the implied production economics.

This enriches the explanatory record but does not move the first warning date earlier than the seeded public payment-failure reporting.

---

## 3. Matched control cohort

P1B adds 10 legitimate/verified controls.

| # | Control | Surface similarity |
|---:|---|---|
| 1 | Ziidi Money Market Fund | Mobile-first, mass market, low entry, recent launch |
| 2 | Britam Money Market Fund | Retail savings, mobile access, return language |
| 3 | CIC Money Market Fund | Pooled funds, investment income, custody structure |
| 4 | NCBA Money Market Fund (KES) | Digital access, retail investment, yield-seeking |
| 5 | ICEA Money Market Fund | Unit trust, pooled investments, return-seeking |
| 6 | Old Mutual Money Market Fund | Investment return language, pooled assets |
| 7 | Zimele Unit Trust Scheme | Low-entry recurring savings/investment plan |
| 8 | Sanlam Unit Trust Funds | Multi-fund retail investment proposition |
| 9 | ALA Money Market Fund (KES) | Recent regulated product, pooled investment |
| 10 | M-Akiba Retail Government Bond | Mobile-first, low entry, fixed/deterministic return |

Controls are deliberately not selected because they look obviously different from fraud cases.

They are selected because they overlap with patterns that a weak detector might misuse.

---

## 4. Control verification

Verification sources include:
- Capital Markets Authority approved collective-investment-scheme register;
- specific CMA approval notices;
- CMA-hosted historical reports;
- issuer documentation;
- National Treasury documentation;
- Central Depository & Settlement Corporation documentation.

Current directly validated control corpus:
- **10 unique controls**
- **10 quality-clean**
- **18 Tier A source references**
- **2 Tier B source references**

Every control has:
- at least two sources;
- at least one Tier A source;
- time provenance;
- explicit verification events;
- matched surface-pattern tags;
- a sample marketing proposition;
- an expected maximum public risk state.

---

## 5. False-positive checks

### 5.1 Discovery false positive

The control's representative marketing text is passed through the current autonomous text-discovery primitive.

The discovery system may recognize investment language and income/return language, but it should **not** open a suspicious candidate unless additional supporting patterns such as referral recruitment, urgency, or withdrawal/unlock language are present.

Current result:

> **0 / 10 discovery false positives**

### 5.2 Risk-state false positive

Verified indicators are passed into the deterministic risk engine.

Examples:
- `VERIFIED_RELEVANT_LICENCE`
- `VERIFIED_REGULATED_CUSTODY`
- `VERIFIED_GOVERNMENT_ISSUER`

Current result:

> **0 / 10 risk-state false positives**

All ten controls remain:

> `WATCH`

This is a regression result, **not a production specificity estimate**.

---

## 6. M-Akiba fixed-return counterexample

M-Akiba is the most important control conceptually.

The product shares several traits that naïve fraud rules can mishandle:
- mass-market promotion;
- mobile-phone purchase;
- low denomination;
- a deterministic fixed coupon.

Dawnwatch therefore intentionally activates:
- `DETERMINISTIC_RETURN` → caution weight

and also:
- `VERIFIED_GOVERNMENT_ISSUER` → strong verification weight

Current internal result:
- deterministic-return contribution: `+18`
- verified government issuer: `−30`
- net internal score: `−12`
- public state: `WATCH`

This demonstrates an important principle:

> A warning indicator is not a verdict. Independent verification can materially change the assessment.

---

## 7. Updated positive benchmarks

| Case | Benchmark kind | Current lead time |
|---|---|---:|
| Public Likes | pre-disruption warning | **46 days** |
| QVSE | loss-prevention | **45 days** |
| Goldenscape | enforcement lead | **21 days** |
| Amazon Web Worker | enforcement lead | **11 days** |
| CBEX | cross-border recurrence | **512 days** |

These should not be averaged as one "average warning time" because they measure different target milestones.

---

## 8. New provenance rule

P1B strengthens source provenance.

Every source must now carry at least one of:
- `published_at`
- `observed_at`

This supports dated articles, live regulator registers with no publication date, archived captures, and historical records discovered later.

The distinction is important for no-hindsight replay.

---

## 9. New API surfaces

```http
GET /api/v1/controls
GET /api/v1/controls/stats
GET /api/v1/controls/assessments
```

Existing historical endpoints remain available.

---

## 10. New CLI commands

```bash
dawnwatch control-stats
dawnwatch validate-controls
dawnwatch benchmark-controls
```

Historical commands remain:

```bash
dawnwatch validate-archive
dawnwatch archive-stats
dawnwatch benchmark-all
```

---

## 11. What P1B does not prove

P1B does not establish:
- 100% specificity;
- real-world recall;
- production false-positive rate;
- calibrated fraud probability;
- statistical representativeness.

The controls are curated and small.

The correct interpretation is:

> Dawnwatch now has explicit negative examples and regression tests that prevent several obvious forms of over-classification.

---

## 12. P1B completion checklist

- [x] matched-control schema
- [x] ten verified Kenyan controls
- [x] control quality gate
- [x] regulator/issuer verification events
- [x] matched surface-pattern tags
- [x] discovery false-positive tests
- [x] risk-state false-positive tests
- [x] fixed-return M-Akiba counterexample
- [x] source time-provenance rule
- [x] Public Likes early-warning enrichment
- [x] QVSE archived recruitment enrichment
- [x] QVSE parliamentary-scrutiny enrichment
- [x] Bitstream anti-hindsight warning record
- [x] Goldenscape domain-expert scrutiny
- [x] control API
- [x] control CLI
- [x] P1B manifests and documentation

**P1B status: implemented.**

---

## 13. Recommended next step

The most valuable next step is **P1C / calibration preparation**, not immediate aggressive weight tuning.

Recommended work:

1. expand controls from 10 to at least 30–50;
2. add cleared/false-alarm historical cases, not only licensed funds;
3. recover original pre-collapse sources for Bitstream and other positive cases;
4. run blinded rule evaluation across positive and control cohorts;
5. calculate confusion matrices by milestone type;
6. then calibrate weights;
7. only afterward move to live-news/regulator Radar evaluation.

That sequencing reduces the risk that Dawnwatch becomes very good at detecting the cases used to design it while performing poorly on new ones.
