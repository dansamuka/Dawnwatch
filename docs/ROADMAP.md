# Dawnwatch Delivery Roadmap

## P0 — Foundation — **nearing closure**
- [x] repository initialization
- [x] full product/technical specification
- [x] architecture baseline
- [x] source policy
- [x] governance policy
- [x] risk-state methodology
- [x] persistent database schema + initial Alembic migration
- [x] immutable content-addressed evidence storage abstraction
- [x] compile/lint/migration/test CI workflow defined
- [x] archive/control validation added as CI gates
- [ ] confirm latest GitHub Actions run is green
- [ ] add production PostgreSQL/object-storage deployment configuration

**Visible outcome:** a documented, testable codebase with health/API endpoints, deterministic risk evaluation, migrations, immutable evidence handling, and historical replay.

## P1 — Historical Archive MVP — **advanced; P1A + P1B complete**

### P1A — Kenya Historical 20 — complete
- [x] canonical historical case schema
- [x] source provenance model
- [x] dated indicator events
- [x] milestone model separating occurrence date from first-documentation date
- [x] no-hindsight historical replay
- [x] searchable archive repository
- [x] archive list/search/detail API
- [x] date-specific replay API
- [x] developer CLI
- [x] 20 deeply sourced Kenyan positive cases
- [x] lifecycle-stage model
- [x] loss/victim/impact estimates with confidence
- [x] court/enforcement event model
- [x] explicit benchmark definitions
- [x] archive-wide benchmark report

### P1B — Historical Depth + Matched Controls — complete
- [x] Public Likes warning depth extended to 8 June 2017
- [x] QVSE pre-freeze archived referral evidence
- [x] QVSE parliamentary-scrutiny evidence
- [x] Bitstream referenced pre-collapse warning preserved without inventing a date
- [x] Goldenscape independent domain-expert scrutiny
- [x] source-level publication/observation time provenance
- [x] 10 matched legitimate/verified Kenyan controls
- [x] control quality gate
- [x] discovery false-positive regression
- [x] risk-state false-positive regression
- [x] fixed-return M-Akiba counterexample
- [x] control API and CLI

### P1 remaining
- [ ] public historical archive frontend
- [ ] normalize historical identifiers into Graph nodes
- [ ] broaden original advertisements / archived websites / domain evidence
- [ ] archive-wide research export

### P1C — Calibration Preparation — next
- [ ] expand controls toward 30–50
- [ ] add cleared/false-alarm historical cases beyond regulated funds
- [ ] create blinded development/validation splits
- [ ] calculate confusion matrices by benchmark type
- [ ] assess source-tier weighting
- [ ] calibrate risk weights only after sufficient positive/negative coverage

**Visible outcome:** a searchable historical case library with positive and negative examples, typed warning benchmarks, and explicit false-positive controls.

## P2 — Entity Graph — **structural foundation started**
- [x] entity/alias/relationship database schema
- [ ] entity resolution engine
- [ ] aliases, people, companies, domains, phones, wallets, social accounts
- [ ] evidence-backed relationship review workflow
- [ ] reversible merge workflow
- [ ] predecessor/successor detection
- [ ] interactive graph UI

**Visible outcome:** interactive scheme relationship graph.

## P3 — Regulatory Watch
- CMA, CBK, SASRA and other relevant official feeds/registers;
- licence verification;
- foreign-regulator warnings;
- alert creation.

**Visible outcome:** new official warnings and licence mismatches appear automatically.

## P4 — News Radar — **prototype started**
- [x] transparent text candidate-discovery primitive
- [x] financial-offer, return, referral, urgency, withdrawal/unlock signal extraction
- [x] Kenyan-style phone and URL extraction
- [x] matched-control regression constraining over-triggering
- [ ] live news ingestion
- [ ] article clustering
- [ ] emerging entity extraction
- [ ] candidate persistence
- [ ] mention/recruitment velocity

**Visible outcome:** Dawnwatch can discover an unknown scheme from monitored news without manual seeding.

## P5 — Public Social Radar — **prototype primitives only**
- [x] recruitment/referral language detection primitives
- [x] urgency and withdrawal-language detection primitives
- [ ] supported public social-source connectors
- [ ] multilingual recruitment classifier
- [ ] velocity tracking
- [ ] complaint-phase transition detection
- [ ] coordination/bot controls

**Visible outcome:** emerging mass recruitment can trigger a Watch candidate.

## P6 — Submission Intelligence
- screenshot/URL/phone/wallet ingestion;
- extraction and clustering;
- privacy redaction;
- moderation.

**Visible outcome:** multiple WhatsApp-style reports can create or strengthen a candidate.

## P7 — Risk Engine v1 — **early implementation**
- [x] public risk-state model
- [x] deterministic indicator weights
- [x] critical-warning escalation rules
- [x] advertised-return economics analyser
- [x] historical risk snapshots via replay
- [x] verified licence/custody counter-signals
- [x] verified government-issuer counter-signal
- [x] matched-control regression
- [ ] source-tier weighting
- [ ] formal review gates
- [ ] calibrated weights from blinded multi-case back-testing
- [ ] public explanation templates

## P8 — Watchtower
- recurring checks;
- material-change events;
- subscriptions;
- critical alert delivery.

## P9 — Historical Validation — **in progress**
- [x] time-travel back-test framework
- [x] no-hindsight leakage tests
- [x] typed lead-time measurement
- [x] five explicit positive benchmarks
- [x] 20-case positive archive
- [x] 10-case matched control cohort
- [x] first discovery false-positive checks
- [x] first risk-state false-positive checks
- [ ] larger negative/control cohort
- [ ] blinded precision/recall evaluation
- [ ] confidence intervals
- [ ] weight calibration

## P10 — Institutional Portal
- analyst dashboard;
- evidence export;
- APIs/webhooks;
- regulator/bank/newsroom workflows.

## North-star metric

> Days of credible warning before widespread loss, withdrawal failure, major media exposure, regulatory action, or enforcement.
