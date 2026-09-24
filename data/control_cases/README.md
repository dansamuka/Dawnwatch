# P1B Matched Control Cases

This directory contains legitimate/verified Kenyan investment propositions used to test whether Dawnwatch overreacts to surface similarities that also occur in normal financial products.

Files beginning with `_` are manifests and are not loaded as control cases.

## Current cohort

P1B contains 10 controls:

- Ziidi Money Market Fund
- Britam Money Market Fund
- CIC Money Market Fund
- NCBA Money Market Fund (KES)
- ICEA Money Market Fund
- Old Mutual Money Market Fund
- Zimele Unit Trust Scheme
- Sanlam Unit Trust Funds
- ALA Money Market Fund (KES)
- M-Akiba Retail Government Bond

## Why these controls matter

They intentionally overlap with patterns Dawnwatch may see in suspicious propositions:

- mass-market promotion;
- mobile/digital onboarding;
- low entry barriers;
- return/yield language;
- pooled investments;
- recent product launches;
- fixed returns.

The control cohort then adds independent verification such as:

- CMA approval;
- appearance in an official CMA register;
- regulated custody evidence;
- Government of Kenya issuance;
- official market-infrastructure documentation.

## Current validation result

Direct repository validation on 24 September 2026:

- 10 unique controls;
- 10 quality-clean;
- 18 Tier A source references;
- 2 Tier B source references;
- 0 current risk-engine false positives;
- 0 current discovery false positives.

This does **not** mean Dawnwatch has 100% specificity. The sample is small, curated, and not statistically representative.

## Commands

```bash
dawnwatch validate-controls
dawnwatch control-stats
dawnwatch benchmark-controls
```
