# Dawnwatch

**Mass Fraud Early Warning & Intelligence**

Dawnwatch is a provenance-first fraud intelligence platform designed to detect, investigate, document, and warn about emerging mass-recruitment schemes before widespread losses occur.

## Core modules

- **Dawnwatch Archive** — historical fraud and scam case library.
- **Dawnwatch Radar** — autonomous discovery of emerging schemes.
- **Dawnwatch Graph** — entity and relationship intelligence.
- **Dawnwatch Watchtower** — continuous monitoring and material-change alerts.
- **Dawnwatch Lens** — evidence-backed case investigation.
- **Dawnwatch Atlas** — geographic intelligence and spread.

## Product principle

Dawnwatch does not casually declare an entity fraudulent. It surfaces explainable, dated, source-backed risk indicators and distinguishes allegations, regulator warnings, enforcement actions, charges, findings, acquittals, and convictions.

## North-star metric

> **Days of credible warning before widespread losses, withdrawal failure, major media exposure, regulatory action, or enforcement.**

## Current implementation

### P1A — Kenya Historical 20
Implemented:
- 20 archive-complete historical positive cases;
- searchable Archive API/CLI;
- lifecycle, impact and legal-event models;
- no-hindsight historical replay;
- five explicit benchmark definitions.

### P1B — Historical Depth + Matched Controls
Implemented:
- deeper original-date evidence on priority positive cases;
- Public Likes warning lead improved to 46 days;
- QVSE archived recruitment + parliamentary scrutiny;
- 10 legitimate/verified matched Kenyan controls;
- source publication/observation time provenance;
- discovery and risk false-positive regression;
- fixed-return M-Akiba counterexample;
- control API/CLI and CI validation gates.

Current directly validated P1B control result:
- 10/10 quality-clean;
- 0/10 discovery false positives;
- 0/10 risk-state false positives.

This is a small curated regression cohort, **not a production accuracy claim**.

## Developer commands

```bash
pip install -e ".[dev]"

dawnwatch validate-archive
dawnwatch archive-stats
dawnwatch benchmark-all

dawnwatch validate-controls
dawnwatch control-stats
dawnwatch benchmark-controls

uvicorn dawnwatch.api:app --reload
```

## Documentation

- [DAWNWATCH_SPEC.md](./DAWNWATCH_SPEC.md)
- [Implementation status](./docs/STATUS.md)
- [Roadmap](./docs/ROADMAP.md)
- [P1A Kenya Historical 20](./docs/benchmarks/P1A_KENYA_20.md)
- [P1B Historical Depth + Matched Controls](./docs/benchmarks/P1B_DEPTH_AND_CONTROLS.md)

## Next phase

**P1C — Calibration Preparation**

The next methodological priority is to broaden negative/control coverage, add cleared/false-alarm cases, create blinded evaluation splits, and calculate confusion matrices before materially tuning risk weights.
