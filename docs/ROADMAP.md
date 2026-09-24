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
- [ ] confirm latest GitHub Actions run is green
- [ ] add production PostgreSQL/object-storage deployment configuration

**Visible outcome:** a documented, testable codebase with health/API endpoints, deterministic risk evaluation, migrations, immutable evidence handling, and historical replay.

## P1 — Historical Archive MVP — **in progress**
- [x] canonical historical case schema
- [x] source provenance model
- [x] dated indicator events
- [x] milestone model separating occurrence date from first-publication date
- [x] no-hindsight historical replay
- [x] searchable archive repository
- [x] archive list/search/detail API
- [x] date-specific replay API
- [x] developer CLI
- [x] first source-backed benchmark case: QVSE
- [x] first lead-time benchmark: Elevated Caution 45 days before reported freeze
- [ ] create first 20 deeply sourced Kenyan cases
- [ ] enrich QVSE with pre-July corporate/social/recruitment evidence
- [ ] add lifecycle-stage model to every case
- [ ] add loss/victim estimate ranges and confidence
- [ ] add court/enforcement event model
- [ ] public historical archive frontend
- [ ] archive-wide benchmark report

**Visible outcome:** searchable historical case library explaining how schemes worked, what evidence was available at each date, and how early Dawnwatch would have warned.

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
- [ ] source-tier weighting
- [ ] formal review gates
- [ ] calibrated weights from multi-case back-testing
- [ ] public explanation templates

## P8 — Watchtower
- recurring checks;
- material-change events;
- subscriptions;
- critical alert delivery.

## P9 — Historical Validation — **started**
- [x] time-travel back-test framework
- [x] no-hindsight leakage test
- [x] lead-time measurement
- [x] first QVSE benchmark
- [ ] 20-case benchmark set
- [ ] precision/recall
- [ ] false-positive analysis
- [ ] weight calibration

## P10 — Institutional Portal
- analyst dashboard;
- evidence export;
- APIs/webhooks;
- regulator/bank/newsroom workflows.

## North-star metric

> Days of credible warning before widespread loss, withdrawal failure, major media exposure, regulatory action, or enforcement.
