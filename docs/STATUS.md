# Dawnwatch Implementation Status

**Last updated:** 24 September 2026

## Dashboard

| Phase | Status | Approx. completion | What exists now |
|---|---|---:|---|
| P0 — Foundation | Nearing closure | 92% | Specification, governance, source policy, risk methodology, FastAPI, persistence models, Alembic migration, immutable evidence store, tests, CI validation gates |
| P1 — Historical Archive MVP | Advanced | 82% | **P1A + P1B implemented**; 20-case positive archive, historical-depth enrichments, 10 matched controls, time-travel replay, quality gates, false-positive regression |
| P2 — Entity Graph | Started structurally | 10% | Entity/alias/relationship database schema; no graph resolution engine or UI yet |
| P3 — Regulatory Watch | Not started | 0% | Source policy and regulator concepts only |
| P4 — News Radar | Prototype concepts | 12% | Text candidate-discovery primitive; P1B control tests now constrain over-triggering |
| P5 — Public Social Radar | Prototype concepts | 5% | Recruitment/urgency/withdrawal language primitives; no live social connectors |
| P6 — Submission Intelligence | Not started | 0% | Specification only |
| P7 — Risk Engine v1 | Early implementation | 38% | Deterministic explainable engine, positive verification weights, government-issuer handling, economics analyser, control regression |
| P8 — Watchtower | Not started | 0% | Specification only |
| P9 — Historical Validation | In progress | 45% | Positive corpus + matched controls, no-hindsight replay, five explicit benchmark types, first false-positive checks |
| P10 — Institutional Portal | Not started | 0% | Specification only |

## P0 closure

Completed:
- [x] repository structure and packaging
- [x] full Dawnwatch specification
- [x] architecture baseline
- [x] governance policy
- [x] source/evidence quality policy
- [x] explainable risk methodology
- [x] core persistence schema
- [x] initial Alembic migration
- [x] immutable content-addressed evidence store
- [x] API, risk, discovery, persistence, evidence, archive and replay tests
- [x] GitHub Actions CI definition
- [x] CI archive-validation gate
- [x] CI matched-control-validation gate

Remaining:
- [ ] confirm a green GitHub Actions run on the latest main commit
- [ ] production PostgreSQL environment configuration
- [ ] object-storage implementation alongside the local evidence adapter

## P1A — Kenya Historical 20 — **implemented**

Current positive corpus:

- 20 unique historical cases
- 20 archive-complete
- 5 benchmark-eligible
- lifecycle, impact and legal/enforcement models
- explicit benchmark definitions
- no-hindsight replay
- searchable API/CLI
- legacy-taskforce regression checks

P1B subsequently deepened the same corpus; it did not change the 20-case membership.

## P1B — Historical Depth + Matched Controls — **implemented**

### Historical depth

Completed:
- [x] Public Likes contemporaneous warning moved to 8 June 2017
- [x] Public Likes lead time improved from 11 to **46 days**
- [x] QVSE dated 21 July archived invitation-code evidence
- [x] QVSE 12 August parliamentary-scrutiny stage
- [x] Bitstream referenced pre-collapse warning preserved without inventing the missing original date
- [x] Goldenscape independent agricultural-economics scrutiny
- [x] source provenance supports both `published_at` and `observed_at`
- [x] every source must carry time provenance

### Matched controls

Completed:
- [x] 10 legitimate/verified Kenyan controls
- [x] 10/10 quality-clean
- [x] 18 Tier A source references
- [x] 2 Tier B source references
- [x] matched surface-pattern tags
- [x] explicit verification events
- [x] discovery false-positive regression
- [x] risk-state false-positive regression
- [x] M-Akiba deterministic-return counterexample
- [x] control API and CLI
- [x] control manifest and methodology documentation

Direct validation result:

> **0 / 10 current discovery false positives**

> **0 / 10 current risk-state false positives**

This is a regression result on a small curated cohort, **not a production specificity estimate**.

## Current positive benchmarks

| Case | Type | Lead time |
|---|---|---:|
| Public Likes | Pre-disruption | **46 days** |
| QVSE | Loss-prevention | **45 days** |
| Goldenscape | Enforcement lead | **21 days** |
| Amazon Web Worker | Enforcement lead | **11 days** |
| CBEX | Cross-border recurrence | **512 days** |

The benchmark types are intentionally not averaged into one headline metric.

## Current demonstrated capability

Dawnwatch can now:

1. inspect text for mass-recruitment/income proposition signals;
2. mathematically analyse advertised returns;
3. apply deterministic explainable risk indicators;
4. apply verified licence, custody and government-issuer counter-signals;
5. store intelligence entities, observations, evidence, relationships and snapshots;
6. preserve raw evidence by SHA-256;
7. load and validate a 20-case positive historical archive;
8. load and validate a 10-case matched control cohort;
9. distinguish lifecycle stages, impact estimates and legal/enforcement events;
10. replay what Dawnwatch would have known at a historical date;
11. calculate typed warning lead times;
12. test current discovery and risk logic against legitimate controls;
13. expose archive and control statistics via API and CLI.

## Immediate next build target

**P1C — Calibration Preparation**

Recommended:
- expand controls from 10 toward 30–50;
- add cleared/false-alarm cases, not only regulated funds;
- recover more original pre-collapse evidence;
- build blinded train/validation splits;
- measure confusion matrices by benchmark type;
- calibrate weights only after those safeguards exist.

Live regulator/news Radar can then be evaluated against a methodology that has both positive and negative historical examples.
