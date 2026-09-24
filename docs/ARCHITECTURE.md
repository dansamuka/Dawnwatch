# Dawnwatch Architecture

## 1. System shape

Dawnwatch is designed as a provenance-first intelligence pipeline:

```text
Sources
  ↓
Discovery / Fetch
  ↓
Observation normalization
  ↓
Claim + entity extraction
  ↓
Entity resolution
  ↓
Evidence graph
  ↓
Indicator evaluation
  ↓
Risk snapshot
  ↓
Human review gates
  ↓
Public case / alert / API
```

The system deliberately separates **observations**, **claims**, **evidence**, **indicators**, and **public conclusions**. A social post can be stored as an observation without being treated as true. A claim may remain unverified. A risk indicator should activate only when its evidence threshold is met.

## 2. Logical services

### Archive
Historical cases, timelines, lifecycle stages, enforcement outcomes, and time-sliced back-tests.

### Radar
Autonomous discovery of previously unknown mass-recruitment propositions.

### Graph
Relationship intelligence for people, companies, aliases, domains, phones, wallets, apps, social identities, licences, court matters, and evidence.

### Watchtower
Continuous re-checking of monitored entities and material-change detection.

### Lens
Analyst investigation workspace and evidence review.

### Atlas
Aggregate geographic spread and recruitment/complaint trends. Victim-level location must never be exposed publicly.

## 3. Initial stack

- Python 3.12
- FastAPI
- Pydantic
- PostgreSQL + pg_trgm; PostGIS when geographic intelligence starts
- OpenSearch/Elasticsearch once corpus search exceeds PostgreSQL requirements
- S3-compatible immutable evidence storage
- Redis/Temporal-style task orchestration as ingestion expands
- Next.js/TypeScript frontend in a later web phase

The initial repository keeps the risk engine deterministic and auditable. ML and LLM components may assist extraction, clustering, and prioritization, but must not be the sole authority for regulatory status, criminal status, convictions, or high-impact public classifications.

## 4. Core data boundaries

1. **Raw evidence:** immutable and content-hashed.
2. **Normalized observations:** source-specific content converted to a common model.
3. **Claims:** subject/predicate/object statements extracted from observations.
4. **Relationships:** evidence-backed graph edges.
5. **Indicators:** explainable risk signals with confidence and evidence references.
6. **Risk snapshots:** time-stamped state derived from active indicators.
7. **Public presentation:** governed rendering of reviewed facts and unresolved questions.

## 5. Time-travel requirement

Every record that can materially change a risk conclusion should preserve `first_seen`, `last_seen`, source publication time, and observation time. Historical replay must be capable of excluding evidence first available after the simulated date.

## 6. Reliability rules

- ingestion is idempotent;
- original evidence is never silently overwritten;
- public case states are versioned;
- risk transitions are auditable;
- entity merges are reversible;
- critical assertions require attributable evidence;
- automated discovery can open a candidate without automatically publishing an accusation.

See `DAWNWATCH_SPEC.md` for the full target architecture.
