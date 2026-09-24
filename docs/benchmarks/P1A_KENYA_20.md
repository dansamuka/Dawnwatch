# P1A — Kenya Historical 20

**Status:** Implemented  
**Corpus size:** 20 cases  
**Archive-complete:** 20 / 20  
**Benchmark-eligible:** 5 / 20  
**Primary purpose:** establish a heterogeneous Kenyan historical corpus for Dawnwatch risk-methodology calibration, entity-pattern research, and warning lead-time analysis.

---

## 1. Why this corpus exists

Dawnwatch must not be calibrated around one successful example such as QVSE.

P1A creates a first historical benchmark set spanning different eras and scheme mechanics:

- classic pyramid/deposit-taking schemes;
- SACCO/investment structures;
- click-to-earn platforms;
- crypto schemes;
- fake AI/trading apps;
- high-yield collective-investment propositions;
- agribusiness investments;
- real-estate/investment networks;
- referral-driven mass recruitment;
- cross-border schemes.

A case can be **archive-complete** without being **benchmark-eligible**.

Archive completeness means the case has enough sourced information to document its historical mechanics and impact. Benchmark eligibility additionally requires dated evidence suitable for testing what Dawnwatch could have known before a later milestone.

---

## 2. The 20-case corpus

| # | Case | Era | Primary pattern | Benchmark? |
|---:|---|---|---|:---:|
| 1 | DECI | 2000s | Pyramid / deposit-taking | No |
| 2 | Clip Investments Sacco | 2000s | Pyramid / deposit-taking | No |
| 3 | Kenya Business Community Sacco | 2000s | Pyramid / deposit-taking | No |
| 4 | Sasanet Investment Sacco | 2000s | Pyramid / deposit-taking | No |
| 5 | Jitegemee Investment Sacco | 2000s | Pyramid / deposit-taking | No |
| 6 | Circuit Investment | 2000s | Pyramid / investment | No |
| 7 | Family In Need Organisation (FINO) | 2000s | Pyramid / deposit-taking | No |
| 8 | Global Entrepreneurship | 2000s | Pyramid / mass recruitment | No |
| 9 | Spell Investment | 2000s | Pyramid / investment | No |
| 10 | Mont Blanq Afrique | 2000s | Pyramid / mass recruitment | No |
| 11 | Public Likes | 2017 | Click-to-earn / referral | Yes |
| 12 | Goldenscape | 2014–2021 | Agribusiness / high-return investment | Yes |
| 13 | Amazon Web Worker | 2021 | App / task / referral investment | Yes* |
| 14 | Bitstream Circle | 2021–2022 | Crypto / Telegram / high yield | No |
| 15 | NMK Capital | 2021–2023 | High-yield investment | No |
| 16 | Ekeza / Gakuyo network | 2015–2024 | SACCO / real estate / investment | No |
| 17 | Passy Ma Trevor / Pafrim | 2023–2024 | High-yield collective investment | No |
| 18 | KCLNL / GSIWEA | 2026 | Fake AI trading apps / impersonation | No |
| 19 | QVSE | 2026 | Copy trading / crypto / referral | Yes |
| 20 | CBEX | 2025–2026 | Cross-border crypto investment | Yes |

* Amazon Web Worker is useful for collapse-to-enforcement timing, not yet as a pre-loss warning benchmark.

---

## 3. Legacy taskforce cohort

The first ten cases are drawn from the Kenya Pyramid Schemes Taskforce historical record.

Across these ten seeded cases, the archive records:

- **121,205 registered investor claims**
- **KSh 7,262,824,632 in registered claim value**

These figures are historical taskforce claim-registration figures. They are not represented as independently audited final victim-loss totals.

The legacy cohort is deliberately **not** marked benchmark-eligible yet because the currently seeded sources primarily document the schemes after failure/taskforce intervention. Using the 2009 taskforce findings as if they were pre-collapse alerts would introduce hindsight leakage.

---

## 4. Current benchmark set

Five cases currently contain sufficiently dated evidence for repeatable benchmark calculations.

| Case | First Elevated+ signal in seeded record | Later milestone | Lead time | Benchmark interpretation |
|---|---|---|---:|---|
| QVSE | Ghana SEC warning — 22 Jul 2026 | Reported account freeze — 5 Sep 2026 | **45 days** | Early-warning / loss-prevention relevant |
| Public Likes | Public structural warning — 8 Jun 2017 | M-Pesa Paybill suspension — 24 Jul 2017 | **46 days** | Pre-disruption warning |
| CBEX | Nigeria SEC warning — 17 Apr 2025 | Kenya CMA warning — 11 Sep 2026 | **512 days** | Cross-border recurrence / jurisdiction-transfer warning |
| Goldenscape | Public payment-failure/high-return reporting — 6 Mar 2020 | DCI arrest — 27 Mar 2020 | **21 days** | Enforcement lead, not pre-loss |
| Amazon Web Worker | Public collapse/high-return reporting — 17 May 2021 | DCI arrest — 28 May 2021 | **11 days** | Enforcement lead, not pre-loss |

These lead times must **not** be averaged as though they measure the same outcome. Dawnwatch stores the milestone type because “warning before freeze,” “warning before enforcement,” and “foreign warning before Kenyan recurrence” answer different questions.

---

## 5. P1A quality rules

Every P1A case must:

1. have a unique canonical case ID;
2. contain at least two sources;
3. include at least one Tier A or Tier B source;
4. have no dangling source references;
5. include lifecycle stages;
6. include at least one impact-estimate record, including an explicit unknown where no reliable aggregate exists;
7. distinguish allegation, investigation, charge, finding, acquittal, and conviction;
8. use publication/first-documentation dates for historical replay;
9. avoid turning later knowledge into an earlier warning;
10. explicitly declare whether it is benchmark-eligible.

The command:

```bash
dawnwatch validate-archive
```

fails if any case violates the structural quality gate.

---

## 6. Benchmark commands

Validate the archive:

```bash
dawnwatch validate-archive
```

Summarize the archive:

```bash
dawnwatch archive-stats
```

Run every eligible benchmark:

```bash
dawnwatch benchmark-all
```

Replay one case at a historical date:

```bash
dawnwatch replay kenya-qvse-2026 --as-of 2026-07-22T23:59:00+00:00
```

Search the archive:

```bash
dawnwatch archive-search QVSE
```

---

## 7. API surfaces

P1A is exposed through:

```http
GET /api/v1/archive/stats
GET /api/v1/archive/benchmarks
GET /api/v1/archive/cases
GET /api/v1/archive/search?q=
GET /api/v1/archive/cases/{case_id}
GET /api/v1/archive/cases/{case_id}/replay?as_of=
```

---

## 8. What P1A proves — and what it does not

P1A proves that Dawnwatch can maintain a heterogeneous, provenance-aware historical corpus and replay evidence without deliberately leaking later discoveries backward.

It does **not** yet establish calibrated fraud-detection accuracy.

Twenty known problematic historical cases are a positive-case corpus. Measuring false-positive rates requires a separate control cohort of legitimate or ultimately cleared propositions that share superficially similar features.

Accordingly, P1A should feed the next validation work rather than justify stronger public probability claims.

---

## 9. Next research extensions

### P1B — Historical depth

Enrich the 20 cases with:
- original advertisements;
- archived websites;
- corporate records;
- domain history;
- contemporaneous social posts;
- regulator-register checks;
- payment rails;
- recruiter relationships;
- predecessor/successor schemes;
- original complaint dates.

### Control cohort

Build a matched set of legitimate/high-growth/high-yield-looking propositions that did **not** become fraud cases.

This is required to understand specificity and false positives.

### Graph extraction

Convert historical identifiers into Dawnwatch Graph nodes:
- people;
- companies;
- phone numbers;
- domains;
- wallets;
- paybills;
- social accounts;
- apps;
- regulators;
- court cases.

### Calibration

Only after the positive and control cohorts exist should Dawnwatch materially recalibrate indicator weights or publish performance claims.

---

## 10. P1A completion definition

P1A was completed as the 20-case baseline. P1B later deepened selected cases without changing the corpus membership.

P1A is complete when:

- [x] 20 unique Kenyan historical cases exist;
- [x] all 20 load through one canonical schema;
- [x] all 20 satisfy the structural quality gate;
- [x] legacy taskforce figures are regression-tested;
- [x] benchmark eligibility is explicit;
- [x] benchmark lead times are regression-tested;
- [x] archive statistics are available through API and CLI;
- [x] the archive is searchable;
- [x] historical replay is available through API and CLI;
- [x] allegations and legal outcomes are represented distinctly;
- [x] no-hindsight methodology is documented.

**P1A status: implemented.**
