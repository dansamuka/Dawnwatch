# Dawnwatch Implementation Status

**Last updated:** 24 September 2026

## Dashboard

| Phase | Status | Approx. completion | What exists now |
|---|---|---:|---|
| P0 — Foundation | Nearing closure | 90% | Specification, governance, source policy, risk methodology, FastAPI, persistence models, Alembic migration, immutable evidence store, tests, CI workflow |
| P1 — Historical Archive MVP | In progress | 65% | **P1A Kenya Historical 20 complete**; canonical schema, lifecycle/impact/legal models, searchable Archive API/CLI, time-travel replay, archive validation, five benchmark-eligible cases |
| P2 — Entity Graph | Started structurally | 10% | Entity/alias/relationship database schema; no graph resolution engine or UI yet |
| P3 — Regulatory Watch | Not started | 0% | Source policy and regulator concepts only |
| P4 — News Radar | Prototype concepts | 10% | Text candidate-discovery primitive; no live news connectors yet |
| P5 — Public Social Radar | Prototype concepts | 5% | Recruitment/urgency/withdrawal language primitives; no live social connectors |
| P6 — Submission Intelligence | Not started | 0% | Specification only |
| P7 — Risk Engine v1 | Early implementation | 30% | Deterministic explainable engine, risk states, government/regulator findings, weights, economics analyser |
| P8 — Watchtower | Not started | 0% | Specification only |
| P9 — Historical Validation | In progress | 30% | 20-case positive corpus, no-hindsight replay, five eligible lead-time benchmarks; control cohort still required |
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

Remaining:
- [ ] confirm a green GitHub Actions run on the latest main commit
- [ ] production PostgreSQL environment configuration
- [ ] object-storage implementation alongside the local evidence adapter

## P1A — Kenya Historical 20 — **implemented**

Completed:
- [x] exactly 20 unique Kenyan historical cases
- [x] 20/20 marked archive-complete
- [x] source provenance on every case
- [x] lifecycle-stage model
- [x] victim/loss/impact estimates with confidence and explicit unknowns where necessary
- [x] legal/enforcement event model
- [x] allegation / charge / finding / acquittal distinctions
- [x] no-hindsight historical replay
- [x] archive-wide quality gate
- [x] archive statistics API
- [x] archive validation CLI
- [x] five explicitly benchmark-eligible cases
- [x] archive-wide benchmark engine
- [x] regression tests for benchmark lead times
- [x] 2009 taskforce cohort regression tests
- [x] P1A benchmark report

Current P1A corpus spans:
- classic pyramid/deposit-taking schemes;
- SACCO and real-estate structures;
- click-to-earn and task apps;
- crypto schemes;
- fake AI trading apps;
- agribusiness investment;
- high-yield collective-investment propositions;
- cross-border regulatory recurrence.

### P1A benchmark lead times currently locked

| Case | Lead time | Interpretation |
|---|---:|---|
| QVSE | 45 days | Ghana SEC warning → reported Kenya account freeze |
| Public Likes | 11 days | structural warning → M-Pesa Paybill suspension |
| Goldenscape | 21 days | public payment-failure warning → DCI arrest |
| Amazon Web Worker | 11 days | public collapse reporting → DCI arrest |
| CBEX | 512 days | Nigeria SEC warning → Kenya CMA warning |

These benchmarks are **not treated as interchangeable**. Some measure pre-disruption warning, some enforcement lead, and CBEX measures cross-border warning transfer.

## P1 remaining after P1A

- [ ] enrich QVSE with pre-July corporate/social/recruitment evidence
- [ ] build historical case-page frontend
- [ ] add original advertisements / archived websites where available
- [ ] normalize historical entities into Dawnwatch Graph nodes
- [ ] build control cohort of legitimate/cleared propositions
- [ ] archive-wide research export

## Current demonstrated capability

Dawnwatch can now:

1. inspect text for mass-recruitment/income proposition signals;
2. mathematically analyse advertised returns;
3. apply deterministic explainable risk indicators;
4. store intelligence entities, observations, evidence, relationships and snapshots;
5. preserve raw evidence by SHA-256;
6. load, validate and search a 20-case historical archive;
7. distinguish lifecycle stages, impact estimates and legal/enforcement events;
8. replay what Dawnwatch would have known at a historical date;
9. calculate and regression-test warning lead time;
10. expose archive statistics and benchmarks via API and CLI.

## Immediate next build target

**P1B — Historical Depth + Control Cohort**

P1A is a positive-case corpus. The next validation step should improve original-date evidence and create matched legitimate/cleared controls so Dawnwatch can measure false positives before risk weights are materially recalibrated or stronger accuracy claims are made.
