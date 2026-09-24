# Historical Seed Cases

This directory contains structured, source-backed historical fixtures used by Dawnwatch Archive and historical replay.

Files beginning with `_` are metadata/manifests and are not loaded as cases.

## P1A status

The first historical tranche, **P1A — Kenya Historical 20**, is implemented.

Validated corpus:

- 20 unique cases;
- 20 archive-complete;
- 5 benchmark-eligible;
- 46 per-case source references;
- 11 Tier A source references;
- 25 Tier B source references;
- zero structural/source-reference failures in the repository-level validation pass.

See `_p1a_manifest.json` and `docs/benchmarks/P1A_KENYA_20.md`.

## Case requirements

A case should include:

- canonical entity and aliases;
- jurisdiction;
- scheme/category;
- source provenance and publication timestamps;
- dated indicator events;
- historical milestones;
- lifecycle stages;
- impact estimates with confidence;
- legal/enforcement events;
- final/current known outcome;
- uncertainty notes.

### Benchmark eligibility

Archive completeness is not the same as benchmark eligibility.

A benchmark-eligible case must additionally define:

- benchmark kind;
- target risk state;
- explicit target milestone;
- interpretation;
- dated indicators capable of historical replay.

This prevents a newly added milestone from silently changing what the benchmark measures.

## No-hindsight rule

Historical replay must only expose evidence that was public on or before the simulated timestamp.

The underlying event date and the date it was first documented are stored separately where relevant.

Later investigative reporting may enrich the Archive, but must not leak backward into an earlier Dawnwatch assessment.

## Legal-state discipline

Do not collapse these into one status:

- allegation;
- complaint;
- investigation;
- regulator warning;
- charge;
- guilty plea;
- acquittal;
- conviction;
- civil judgment;
- settlement;
- government finding.

A charge or arrest must not be represented as a conviction.

## Validation

Run:

```bash
dawnwatch validate-archive
```

P1A regression tests additionally enforce the 20-case count, source-reference integrity, legacy cohort totals, and five benchmark lead times.
