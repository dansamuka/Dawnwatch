# Dawnwatch Detection Pipeline

## Objective

Dawnwatch should discover a previously unknown mass-recruitment proposition without a user first entering its name.

## v0.1 implementation

The repository now contains a deliberately conservative text triage primitive in `dawnwatch/discovery.py`. It detects combinations of:
- financial/investment language;
- income/return claims;
- recruitment/referral language;
- urgency;
- withdrawal/unlock language;
- Kenyan-style mobile phone identifiers;
- public URLs.

The classifier only decides whether content is interesting enough to **open an investigation candidate**. It does not label the subject fraudulent.

## Target pipeline

```text
PUBLIC / USER-PROVIDED OBSERVATION
        ↓
Offer / recruitment detection
        ↓
Entity + identifier extraction
        ↓
Candidate clustering
        ↓
Velocity analysis
        ↓
Regulatory/company/domain enrichment
        ↓
Economics analysis
        ↓
Historical pattern matching
        ↓
Evidence-backed indicators
        ↓
Risk engine
        ↓
Review gate
        ↓
Alert / case page
```

## Next engineering work

1. Replace keyword-only triage with a benchmarked multilingual classifier while retaining rules as transparent features.
2. Normalize extracted phone numbers, domains, wallets, companies, and handles.
3. Cluster observations into candidate entities.
4. Add source-independent mention/recruitment velocity.
5. Create connector interfaces for official regulator and news sources.
6. Store evidence and candidate state in PostgreSQL.
7. Run historical replay against the first Kenyan seed cases.

A model-generated discovery must never be promoted directly to a public fraud accusation.
