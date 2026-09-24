# Dawnwatch Delivery Roadmap

## P0 — Foundation — **in progress**
- [x] repository initialization
- [x] full product/technical specification
- [x] architecture baseline
- [x] source policy
- [x] governance policy
- [x] risk-state methodology
- [ ] persistent database schema + migrations
- [ ] immutable evidence storage abstraction
- [ ] CI passing against API/risk-engine tests

**Visible outcome:** a documented, testable codebase with health/API endpoints and deterministic risk evaluation.

## P1 — Historical Archive MVP
- build canonical case schema;
- create first 20 deeply sourced Kenyan cases;
- timeline and lifecycle model;
- universal search;
- public historical case pages;
- time-sliced snapshots.

**Visible outcome:** searchable historical case library explaining how schemes worked and what warning signs existed.

## P2 — Entity Graph
- aliases, people, companies, domains, phones, wallets, social accounts;
- evidence-backed relationships;
- reversible merge workflow;
- predecessor/successor relationships.

**Visible outcome:** interactive scheme relationship graph.

## P3 — Regulatory Watch
- CMA, CBK, SASRA and other relevant official feeds/registers;
- licence verification;
- foreign-regulator warnings;
- alert creation.

**Visible outcome:** new official warnings and licence mismatches appear automatically.

## P4 — News Radar
- news ingestion;
- article clustering;
- emerging entity extraction;
- candidate creation.

**Visible outcome:** Dawnwatch can discover an unknown scheme from monitored news without manual seeding.

## P5 — Public Social Radar
- supported public social sources;
- recruitment classifier;
- velocity tracking;
- complaint-phase transition detection.

**Visible outcome:** emerging mass recruitment can trigger a Watch candidate.

## P6 — Submission Intelligence
- screenshot/URL/phone/wallet ingestion;
- extraction and clustering;
- privacy redaction;
- moderation.

**Visible outcome:** multiple WhatsApp-style reports can create or strengthen a candidate.

## P7 — Risk Engine v1
- source-weighted indicators;
- state transitions;
- review gates;
- risk snapshot history;
- clear public explanations.

## P8 — Watchtower
- recurring checks;
- material-change events;
- subscriptions;
- critical alert delivery.

## P9 — Historical Validation
- time-travel back-tests;
- lead-time measurement;
- precision/recall;
- false-positive analysis;
- weight calibration.

## P10 — Institutional Portal
- analyst dashboard;
- evidence export;
- APIs/webhooks;
- regulator/bank/newsroom workflows.

## North-star metric

> Days of credible warning before widespread loss, withdrawal failure, major media exposure, regulatory action, or enforcement.
