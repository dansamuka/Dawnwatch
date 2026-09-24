# Dawnwatch Implementation Status

**Last updated:** 24 September 2026

## Dashboard

| Phase | Status | Approx. completion | What exists now |
|---|---|---:|---|
| P0 — Foundation | In progress | 90% | Specification, governance, source policy, risk methodology, FastAPI, persistence models, Alembic migration, immutable evidence store, tests, CI workflow |
| P1 — Historical Archive MVP | In progress | 30% | Historical case schema, searchable Archive service/API, time-travel replay, QVSE seed case, lead-time benchmark, CLI |
| P2 — Entity Graph | Started structurally | 10% | Entity/alias/relationship database schema; no graph resolution engine or UI yet |
| P3 — Regulatory Watch | Not started | 0% | Source policy and regulator concepts only |
| P4 — News Radar | Prototype concepts | 10% | Text candidate-discovery primitive; no live news connectors yet |
| P5 — Public Social Radar | Prototype concepts | 5% | Recruitment/urgency/withdrawal language primitives; no live social connectors |
| P6 — Submission Intelligence | Not started | 0% | Specification only |
| P7 — Risk Engine v1 | Early implementation | 25% | Deterministic explainable engine, risk states, weights, economics analyser |
| P8 — Watchtower | Not started | 0% | Specification only |
| P9 — Historical Validation | Started | 15% | QVSE replay and lead-time tests; broad benchmark set not yet built |
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

## P1 progress

Completed:
- [x] historical source schema
- [x] dated indicator schema
- [x] milestone schema separating occurrence from first documentation
- [x] no-hindsight historical replay
- [x] case search/list/detail API
- [x] historical replay API
- [x] developer CLI
- [x] first benchmark case: QVSE

Remaining:
- [ ] reconstruct 19 additional high-quality Kenyan cases for the first 20-case tranche
- [ ] enrich QVSE with pre-July recruitment/social/corporate evidence
- [ ] case lifecycle stages
- [ ] victim/loss estimate fields with uncertainty ranges
- [ ] court/enforcement event model
- [ ] public archive frontend
- [ ] archive-wide benchmark report

## Current demonstrated capability

Dawnwatch can now:

1. inspect text for mass-recruitment/income proposition signals;
2. mathematically analyse advertised returns;
3. apply deterministic explainable risk indicators;
4. store intelligence entities, observations, evidence, relationships and snapshots;
5. preserve raw evidence by SHA-256;
6. load and search historical cases;
7. replay what Dawnwatch would have known at a historical date;
8. calculate warning lead time to a real-world milestone.

For the current QVSE fixture, the system produces **Elevated Caution 45 days before the reported 5 September 2026 freeze**, based on the Ghana SEC notice dated 22 July 2026.

## Immediate next build target

**P1A — Kenya Historical 20**

Build the first 20-case archive with source-complete timelines and use it to calibrate:
- indicator weights;
- source-quality thresholds;
- false-positive controls;
- lead-time performance;
- successor/predecessor detection.

The objective is not to make QVSE fit the model. It is to test whether the same rules perform consistently across many unrelated historical cases.
