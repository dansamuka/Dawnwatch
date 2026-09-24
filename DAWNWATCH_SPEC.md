# Dawnwatch — Mass Fraud Early Warning & Intelligence System
## Product, Data, Detection, Architecture, Governance & Delivery Specification

**Document status:** Implementation Baseline v1.0  
**Working product name:** Dawnwatch  
**Primary market:** Kenya, with East Africa / Africa expansion path  
**Product class:** Public-interest fraud intelligence, early-warning, research, and evidence platform  
**Primary users:** Consumers, journalists, regulators, banks, fintechs, researchers, law-enforcement analysts, investigators, NGOs, and platform trust & safety teams

---

## 1. Executive Summary

Dawnwatch is a continuous fraud-intelligence system designed to identify, investigate, document, and warn about mass-recruitment fraud schemes before they cause widespread harm.

The system combines four capabilities:

1. **Dawnwatch Archive** — a structured historical record of documented fraud, pyramid, Ponzi, investment, crypto, forex, fake-job, advance-fee, land, procurement, e-commerce, task, impersonation, and related schemes.
2. **Dawnwatch Radar** — autonomous discovery of new or emerging schemes from public data without requiring a user to know the scheme name in advance.
3. **Dawnwatch Graph** — relationship mapping between people, companies, websites, phone numbers, domains, wallets, social accounts, recruiters, payment rails, and predecessor/successor schemes.
4. **Dawnwatch Watchtower** — continuous monitoring, re-assessment, escalation, and alerting when evidence changes materially.

Dawnwatch must **not** function as an automated defamation engine. It should not casually declare an entity “fraudulent.” Instead, it should produce evidence-backed, explainable risk states such as:

- `WATCH`
- `ELEVATED CAUTION`
- `HIGH RISK`
- `CRITICAL WARNING`
- `REGULATORY / ENFORCEMENT CONFIRMED`
- `CLOSED / RESOLVED`
- `FALSE POSITIVE / CLEARED`

Every conclusion should be traceable to dated, attributable evidence.

The core success metric is:

> **How many days before widespread losses, withdrawal failure, regulatory warning, media exposure, or enforcement action did Dawnwatch identify credible warning signals?**

---

# 2. Vision

## 2.1 Problem

Mass-recruitment schemes often become visible only after large numbers of people lose money.

Yet before collapse, they usually leave a public trail:

- unusually high or deterministic returns;
- referral-based recruitment;
- sudden social-media growth;
- anonymous or unverifiable founders;
- recently created domains or companies;
- misleading regulatory claims;
- wallet-based or personal-account payment flows;
- early withdrawal testimonials;
- pressure tactics;
- “activation,” “verification,” or “unlock” fees;
- withdrawal complaints;
- migration into a successor platform;
- regulator warnings in another jurisdiction;
- copied legal documents or websites;
- contradictory founder histories;
- unexplained company-name changes;
- clusters of shared phone numbers, wallets, emails, or administrators.

The problem is not a complete absence of evidence.

The problem is that these signals are fragmented across regulators, news sites, social platforms, corporate records, public complaints, archived websites, app stores, and messaging screenshots.

Dawnwatch should assemble those fragments into one continuously updated intelligence layer.

## 2.2 Vision Statement

> **Dawnwatch makes emerging mass fraud visible early, explainable clearly, and historically searchable.**

## 2.3 Product Promise

A user should be able to:

- search a company, scheme, app, phone number, wallet, URL, social account, or individual;
- understand what is known and what is not known;
- see independent risk indicators;
- review regulatory and licensing status;
- inspect historical links to earlier schemes;
- see how recruitment and complaints have changed over time;
- review the sources behind every material claim;
- understand how similar historical schemes worked;
- subscribe to alerts;
- submit suspicious content;
- see whether a scheme is emerging even before mainstream media has reported it.

---

# 3. Product Principles

Dawnwatch should follow these principles throughout the product and architecture.

### 3.1 Evidence before labels
Do not call an operation fraudulent merely because it looks unusual.

### 3.2 Explainability
Every risk state must show the indicators that produced it.

### 3.3 Provenance
Every material fact must preserve:
- source;
- URL or source identifier;
- publication date;
- observation date;
- first-seen date;
- archive copy where lawful;
- extraction confidence;
- source type;
- verification status.

### 3.4 Time awareness
Dawnwatch must preserve what was knowable **at a particular date**, allowing historical back-testing without hindsight leakage.

### 3.5 Entity continuity
Renaming a company, domain, platform, Telegram channel, or app should not reset risk history.

### 3.6 Human review for high-impact claims
AI can discover and prioritize. High-impact public classifications require governed review rules.

### 3.7 Distinguish allegation from fact
Store and display:
- allegation;
- complaint;
- regulator warning;
- civil action;
- criminal charge;
- guilty plea;
- conviction;
- regulatory finding;
- judgment;
- settlement;
- verified operational fact.

### 3.8 No opaque “fraud probability”
Prefer indicator-based assessments over unsupported probability claims.

### 3.9 Safety against manipulation
The system must resist:
- coordinated false reports;
- competitor attacks;
- fake screenshots;
- brigading;
- review bombing;
- malicious entity linking.

### 3.10 Public-interest usability
Consumers should understand the output in seconds, while investigators should be able to drill down deeply.

---

# 4. Scope

## 4.1 Initial Scheme Categories

Dawnwatch Kenya v1 should support:

- Ponzi schemes;
- pyramid schemes;
- unlawful deposit-taking;
- fake investment platforms;
- copy-trading schemes;
- forex schemes;
- crypto/token schemes;
- fake exchanges;
- fake SACCO / microfinance schemes;
- fake asset-management products;
- land/property investment schemes;
- agriculture/livestock investment schemes;
- fake jobs and recruitment schemes;
- task / e-commerce commission schemes;
- advance-fee scams;
- fake procurement / tender schemes;
- impersonation scams;
- fake grants / government-programme schemes;
- social-commerce fraud;
- romance/investment hybrids where mass recruitment exists;
- “pay to unlock withdrawal” schemes;
- recovery scams targeting prior victims.

## 4.2 Out of Scope for Initial Release

Initially exclude or separately classify:

- isolated one-to-one fraud;
- ordinary contractual disputes;
- political misinformation;
- purely cyber-intrusion incidents;
- stolen-card fraud;
- insider fraud with no mass recruitment;
- single merchant complaints without a broader pattern;
- defamation / reputation scoring unrelated to fraud risk.

---

# 5. Core Product Modules

## 5.1 Dawnwatch Archive

A historical database of documented schemes.

Each historical case should include:

- scheme name;
- aliases;
- jurisdiction(s);
- category;
- status;
- active period;
- first public evidence;
- first warning signal;
- first regulator action;
- first withdrawal complaint;
- collapse date;
- enforcement timeline;
- operators;
- linked companies;
- recruiters;
- websites;
- domains;
- social channels;
- apps;
- payment mechanisms;
- cryptocurrency wallets;
- phone numbers;
- email addresses;
- claimed product;
- advertised returns;
- entry amount;
- recruitment mechanics;
- referral incentives;
- withdrawal mechanics;
- escalation tactics;
- recovery / successor scam pattern;
- estimated victims;
- estimated losses;
- confidence ranges;
- regulator actions;
- court actions;
- convictions;
- acquittals;
- unresolved allegations;
- asset recovery;
- media coverage;
- source archive;
- fraud-pattern tags;
- timeline;
- relationship graph;
- “how it worked” explainer;
- “what could have been detected early” section.

### 5.1.1 Historical Lifecycle Model

Each scheme should be mapped onto stages:

`FORMATION → CREDIBILITY BUILDING → RECRUITMENT → SOCIAL PROOF → ACCELERATION → FRICTION → EXTRACTION → WITHDRAWAL FAILURE → COLLAPSE → MIGRATION / RECOVERY SCAM → ENFORCEMENT / RESOLUTION`

A scheme may skip stages or move backwards.

Each stage should store:
- start date;
- end date;
- evidence;
- confidence;
- indicators activated.

### 5.1.2 Historical Time Slices

Dawnwatch must support snapshots such as:

- T−12 months;
- T−6 months;
- T−3 months;
- T−1 month;
- T−1 week;
- collapse;
- enforcement.

The system should be able to answer:

> “What would Dawnwatch have known on 22 July 2026?”

without using information first published later.

---

## 5.2 Dawnwatch Radar

Radar discovers unknown schemes automatically.

### 5.2.1 Discovery Objective

The system continuously asks:

> **What new entities are being promoted to large numbers of people as a way to earn, invest, work, trade, unlock money, receive grants, or recruit others?**

### 5.2.2 Discovery Sources

Subject to legal and technical availability:

#### Regulators
- Capital Markets Authority (Kenya)
- Central Bank of Kenya
- SASRA
- Insurance Regulatory Authority
- Communications Authority
- Competition Authority
- Directorate of Criminal Investigations
- Office of the Data Protection Commissioner
- Financial Reporting Centre
- Business Registration Service
- Kenya Revenue Authority public notices where relevant
- consumer-protection authorities
- foreign securities regulators
- foreign central banks
- cross-border financial crime notices

#### News
- Business Daily
- Nation
- Standard
- Citizen
- The Star
- regional media
- specialist fintech / crypto / technology media
- regulator press releases
- court reporting

#### Open Social Signals
Where lawful and technically accessible:
- Reddit;
- X;
- TikTok;
- YouTube;
- Facebook public pages/groups;
- Instagram public posts;
- Telegram public channels;
- public forums;
- public review sites;
- app-store reviews.

#### User Submissions
- forwarded WhatsApp screenshots;
- SMS screenshots;
- posters;
- flyers;
- URLs;
- phone numbers;
- mobile-money till/paybill numbers;
- crypto wallets;
- audio/video;
- referral codes;
- bank details;
- social handles.

#### Technical / Registration Sources
- company registries;
- domain registration metadata;
- DNS history;
- certificate transparency;
- website metadata;
- public GitHub/code repositories;
- app-store publisher records;
- historical website snapshots;
- public financial / licence registers.

### 5.2.3 Discovery Triggers

Candidate entities are created when the system detects combinations such as:

- a new financial/income entity receiving rapidly increasing mentions;
- repeated phrases involving deposits + daily return;
- referral/recruitment incentives;
- “VIP” signal groups;
- “activation” payment language;
- guaranteed/near-guaranteed return claims;
- rapid regional recruitment;
- repeated phone numbers across advertisements;
- multiple user reports with matching entity identifiers;
- sudden complaint velocity;
- sudden withdrawal-language changes;
- regulator warning;
- predecessor/successor similarity.

---

## 5.3 Dawnwatch Graph

Dawnwatch Graph is the relationship intelligence layer.

### 5.3.1 Node Types

Graph nodes may include:

- `Scheme`
- `Company`
- `Person`
- `Alias`
- `Domain`
- `Website`
- `App`
- `Phone`
- `Email`
- `SocialAccount`
- `MessagingChannel`
- `Wallet`
- `BankAccount`
- `Paybill`
- `TillNumber`
- `ReferralCode`
- `Address`
- `Regulator`
- `Licence`
- `CourtCase`
- `NewsArticle`
- `PublicNotice`
- `EvidenceItem`
- `Recruiter`
- `VictimReport`
- `Jurisdiction`

### 5.3.2 Edge Types

Examples:

- `OWNS`
- `DIRECTOR_OF`
- `FOUNDED`
- `PROMOTES`
- `RECRUITS_FOR`
- `USES_PHONE`
- `USES_EMAIL`
- `USES_DOMAIN`
- `USES_WALLET`
- `USES_BANK_ACCOUNT`
- `OPERATES_CHANNEL`
- `REGISTERED_AT`
- `CLAIMS_LICENCE`
- `LICENSED_BY`
- `WARNED_BY`
- `CHARGED_IN`
- `CONVICTED_IN`
- `RELATED_TO`
- `SUCCESSOR_TO`
- `PREDECESSOR_OF`
- `SHARES_INFRASTRUCTURE_WITH`
- `SHARES_CONTENT_WITH`
- `MENTIONED_IN`
- `REPORTED_BY`
- `PAID_TO`
- `REFERRED_BY`

Every edge should carry:
- evidence IDs;
- confidence;
- first seen;
- last seen;
- status;
- reviewer state.

### 5.3.3 Entity Resolution

Dawnwatch must deduplicate and connect entities using:

- exact matching;
- fuzzy-name matching;
- phone normalization;
- email normalization;
- domain matching;
- image similarity;
- website text similarity;
- company director overlap;
- wallet reuse;
- shared hosting / infrastructure;
- repeated payment identifiers;
- recurring social handles;
- linguistic fingerprints;
- referral-code clusters;
- administrator overlap.

High-impact links should not be made public solely on weak AI inference.

---

## 5.4 Dawnwatch Watchtower

Watchtower continuously monitors entities already known to Dawnwatch.

Examples of material changes:

- new regulator warning;
- new complaint cluster;
- withdrawal complaints increasing;
- website disappears;
- domain changes;
- Telegram group renamed;
- new app launched;
- founder identity changed;
- new payment wallet;
- new “unlock” payment requirement;
- new recruitment country;
- new company registration;
- legal proceedings;
- conviction or acquittal;
- victim-recovery update;
- scheme redirects users into a new platform.

Watchtower should create a `MaterialChangeEvent` and re-run the risk engine.

---

# 6. Fraud Pattern Taxonomy

Dawnwatch should create a reusable “fraud genome.”

Example tags:

### Economics
- `GUARANTEED_RETURN`
- `EXTREME_RETURN`
- `DETERMINISTIC_RETURN`
- `DAILY_RETURN`
- `RETURN_WITHOUT_DOWNSIDE`
- `UNEXPLAINED_YIELD_SOURCE`

### Recruitment
- `REFERRAL_BONUS`
- `MULTI_LEVEL_RECRUITMENT`
- `TEAM_BUILDING`
- `LIMITED_SLOTS`
- `URGENCY_PRESSURE`
- `SOCIAL_PROOF_TESTIMONIALS`

### Payments
- `CRYPTO_ONLY`
- `PERSONAL_ACCOUNT`
- `MOBILE_MONEY_PERSONAL`
- `MULTIPLE_PAYMENT_IDENTITIES`
- `CROSS_BORDER_PAYMENT`
- `UNLOCK_FEE`
- `VERIFICATION_FEE`
- `TAX_BEFORE_WITHDRAWAL`

### Identity
- `UNVERIFIED_FOUNDER`
- `STOLEN_PROFILE_IMAGE`
- `FAKE_CREDENTIAL`
- `RECENT_DIGITAL_FOOTPRINT`
- `IDENTITY_INCONSISTENCY`

### Regulation
- `NO_VERIFIED_LICENCE`
- `LICENCE_MISMATCH`
- `FOREIGN_REGULATOR_WARNING`
- `LOCAL_REGULATOR_WARNING`
- `MISLEADING_REGISTRATION_CLAIM`

### Operations
- `WITHDRAWAL_DELAY`
- `WITHDRAWAL_FREEZE`
- `RULE_CHANGE`
- `ACCOUNT_REACTIVATION_PAYMENT`
- `SUCCESSOR_PLATFORM`
- `MIGRATION_AFTER_FREEZE`

### Technology
- `RECENT_DOMAIN`
- `COPIED_WEBSITE`
- `PLACEHOLDER_LEGAL_TEXT`
- `APP_PUBLISHER_MISMATCH`
- `FAKE_MARKET_DATA`
- `TRADING_WHEN_MARKET_CLOSED`

### Social
- `RECRUITMENT_VELOCITY_SPIKE`
- `COMPLAINT_VELOCITY_SPIKE`
- `SENTIMENT_PHASE_CHANGE`
- `COORDINATED_PROMOTION`
- `INFLUENCER_PROMOTION`

---

# 7. Risk Engine

## 7.1 Philosophy

The risk engine must be:
- explainable;
- evidence-backed;
- time-bounded;
- resistant to manipulation;
- calibrated against historical cases;
- capable of uncertainty.

Do not expose a simplistic “97% scam” score unless supported by validated statistical calibration.

## 7.2 Risk State

Recommended public state model:

### `WATCH`
A newly detected or weakly evidenced proposition requiring monitoring.

### `ELEVATED CAUTION`
Multiple risk indicators exist, but evidence is incomplete or mixed.

### `HIGH RISK`
Strong independently observable anomalies exist and verification is materially deficient.

### `CRITICAL WARNING`
One or more severe indicators exist, such as:
- regulator warning;
- confirmed licence mismatch;
- systematic withdrawal failure;
- mandatory additional payment to release funds;
- strong linkage to an earlier failed scheme;
- identity deception supported by independent evidence.

### `REGULATORY / ENFORCEMENT CONFIRMED`
A competent regulator, police agency, prosecutor, or court has formally acted.

This is not automatically equivalent to a conviction.

### `RESOLVED`
Case is no longer active and has a defined outcome.

### `CLEARED / FALSE POSITIVE`
Evidence materially contradicts prior suspicion.

## 7.3 Internal Indicator Score

Internally Dawnwatch may use a weighted score for prioritization.

Example initial weights:

| Indicator | Base Weight |
|---|---:|
| Local regulator warning | +45 |
| Foreign regulator warning | +35 |
| Confirmed licence mismatch | +30 |
| Pay-to-unlock withdrawal | +35 |
| Linked predecessor failed scheme | +30 |
| Widespread withdrawal failure | +30 |
| Fake/stolen operator identity evidence | +25 |
| Guaranteed/extreme returns | +20 |
| Deterministic return claims | +18 |
| Referral economics | +12 |
| Recently created company/domain | +8 |
| Crypto-only payments | +8 |
| Recruitment velocity spike | +10 |
| Complaint velocity spike | +15 |
| Founder history unverifiable | +12 |
| Strong evidence of regulated underlying activity | −25 |
| independently verified custody / brokerage | −20 |
| successful licensing verification | −25 |

Weights must be calibrated later.

### 7.3.1 Important Rule

The score is not the public claim.

Public output should show:
- current state;
- activated indicators;
- severity;
- evidence;
- confidence;
- unresolved questions.

---

# 8. Autonomous Detection Engine

## 8.1 Stage A — Stream Collection

Collect or ingest:
- articles;
- public posts;
- public comments;
- regulator notices;
- company records;
- domain records;
- user submissions;
- app reviews.

Normalize to an `Observation` record.

## 8.2 Stage B — Offer Detection

Classifier determines whether content describes:
- an investment;
- income opportunity;
- job/recruitment opportunity;
- grant;
- trading platform;
- crypto proposition;
- business opportunity;
- withdrawal issue;
- recovery request.

## 8.3 Stage C — Entity Extraction

Extract:
- names;
- aliases;
- company names;
- URLs;
- domains;
- phone numbers;
- wallet addresses;
- paybill/till numbers;
- social handles;
- products;
- claimed returns;
- entry amount;
- referral terms;
- jurisdictions.

## 8.4 Stage D — Candidate Clustering

Cluster multiple observations into an emerging scheme candidate.

Example:

- “MaliMax”
- “Mali Max AI”
- `malimax.ai`
- `@malimaxwealth`
- phone +2547XXXXXXXX

may become one candidate entity.

## 8.5 Stage E — Velocity Analysis

Maintain:
- mentions/hour;
- mentions/day;
- unique accounts;
- unique regions;
- referral-code count;
- recruiter count;
- growth rate;
- acceleration;
- complaint/promotion ratio.

## 8.6 Stage F — Automated Investigation

Run enrichment:
- licence lookup;
- regulator lookup;
- company registration;
- domain age;
- web history;
- founder verification;
- return mathematics;
- historical-pattern similarity;
- linked entity search;
- complaint analysis.

## 8.7 Stage G — Risk Evaluation

Activate indicators and classify the candidate.

## 8.8 Stage H — Human Review

Human review required when:
- public state becomes `HIGH RISK` or above;
- named individuals are implicated;
- criminal allegations are shown;
- entity linking depends on non-obvious inference;
- user-submitted evidence drives a major escalation.

## 8.9 Stage I — Alerting

Channels:
- website alert;
- email;
- push notification;
- SMS;
- WhatsApp channel, if supported;
- API webhook;
- journalist/regulator dashboard;
- RSS/Atom feed.

---

# 9. Social Intelligence

## 9.1 Recruitment Phase Detection

Dawnwatch should classify social content into:

- promotion;
- testimonial;
- recruitment;
- question;
- skepticism;
- complaint;
- withdrawal problem;
- payment demand;
- regulator mention;
- collapse;
- recovery;
- migration to successor platform.

## 9.2 Phase-Change Signal

One powerful feature is detecting language transition:

`PROMOTION → SKEPTICISM → WITHDRAWAL QUESTION → WITHDRAWAL FAILURE → ADDITIONAL PAYMENT REQUEST`

This transition should itself be a risk feature.

## 9.3 Recruitment Velocity

Track:
- number of posts;
- number of unique promoters;
- number of referral codes;
- geographic spread;
- repost network;
- audience growth;
- influencer participation.

## 9.4 Manipulation Controls

Do not treat raw mention count as truth.

Weight:
- account age;
- independence;
- duplicate content;
- coordinated timing;
- identical copy;
- referral-linked promotion;
- bot likelihood;
- historical reliability.

---

# 10. User Submission System

## 10.1 Submission Inputs

Users may submit:
- screenshot;
- image;
- URL;
- phone number;
- company name;
- wallet;
- paybill;
- email;
- PDF;
- audio;
- video;
- social account;
- message text.

## 10.2 Extraction Pipeline

For a screenshot:

1. detect text;
2. extract entity names;
3. extract phone/payment identifiers;
4. extract return claims;
5. extract urgency language;
6. identify platform;
7. hash image for duplicate matching;
8. compare against existing cases;
9. open or append to candidate;
10. redact personal victim information before publication.

## 10.3 Submission Abuse Controls

- rate limits;
- CAPTCHA / abuse prevention;
- duplicate detection;
- reporter reputation;
- no automatic public accusation;
- private evidence state;
- moderator review;
- malicious-report flagging.

---

# 11. Historical Back-Testing

Historical replay is essential.

For each known scheme:

1. establish collapse/enforcement timeline;2. collect dated evidence;
3. freeze dataset at successive dates;
4. run Dawnwatch as if operating on that date;
5. record risk state;
6. compare to actual outcome.

## 11.1 Metrics

- days early before first regulator warning;
- days early before withdrawal failure;
- days early before mainstream press;
- days early before enforcement;
- precision;
- recall;
- false-positive rate;
- high-risk false-positive rate;
- proportion of cases detected autonomously;
- average evidence count at first alert.

## 11.2 Leakage Control

Historical back-tests must exclude evidence published after the tested date.

---

# 12. Data Model

## 12.1 Core Tables

### `entities`
- `id`
- `entity_type`
- `canonical_name`
- `normalized_name`
- `status`
- `country`
- `created_at`
- `updated_at`

### `entity_aliases`
- `entity_id`
- `alias`
- `alias_type`
- `first_seen`
- `last_seen`

### `schemes`
- `entity_id`
- `scheme_category`
- `risk_state`
- `risk_score_internal`
- `first_detected`
- `first_public_warning`
- `active_from`
- `active_to`
- `case_status`

### `observations`
- `id`
- `source_id`
- `observed_at`
- `published_at`
- `content_hash`
- `content_type`
- `language`
- `raw_text_location`
- `extraction_status`

### `claims`
- `id`
- `observation_id`
- `subject_entity_id`
- `predicate`
- `object_value`
- `claim_type`
- `confidence`
- `verification_status`

### `indicators`
- `id`
- `scheme_id`
- `indicator_type`
- `severity`
- `first_seen`
- `last_seen`
- `status`
- `confidence`

### `evidence`
- `id`
- `indicator_id`
- `observation_id`
- `source_quality`
- `review_status`
- `notes`

### `relationships`
- `source_entity_id`
- `target_entity_id`
- `relationship_type`
- `confidence`
- `first_seen`
- `last_seen`
- `review_status`

### `risk_snapshots`
- `scheme_id`
- `snapshot_at`
- `risk_state`
- `internal_score`
- `active_indicator_count`
- `explanation_json`

### `reports`
- `id`
- `scheme_id`
- `reporter_hash`
- `submitted_at`
- `report_type`
- `verification_status`
- `privacy_classification`

### `alerts`
- `id`
- `scheme_id`
- `alert_type`
- `severity`
- `created_at`
- `published_at`
- `reason_json`

---

# 13. Source Quality Model

Sources should receive an evidence class.

### Tier A — Authoritative
- court judgment;
- regulator register;
- regulator enforcement notice;
- police/prosecutor notice;
- official corporate record.

### Tier B — Strong independent reporting
- established investigative journalism;
- reputable national media;
- credible specialist reporting.

### Tier C — Corroborated public evidence
- multiple independent social reports;
- archived websites;
- user agreements;
- app-store records;
- corporate marketing content.

### Tier D — Unverified reports
- single anonymous complaint;
- isolated social post;
- screenshot with unclear provenance.

### Tier E — Weak / potentially manipulated
- anonymous accusation;
- duplicate repost;
- unverifiable image;
- coordinated complaint cluster.

Risk escalation rules should heavily weight source tier.

---

# 14. Licensing Verification Engine

For any entity advertising regulated financial activity:

1. determine claimed activity;
2. determine likely regulator;
3. search relevant official registers;
4. identify licence number if claimed;
5. verify name match;
6. verify licence category;
7. verify jurisdiction;
8. verify current status;
9. detect mismatch.

Example:

> A money-service-business registration must not be presented as authorization to operate a securities exchange.

Store:
- claimed licence;
- actual licence;
- allowed activities;
- mismatch type;
- evidence;
- verification date.

---

# 15. Return & Economics Analyzer

Parse claims such as:

- “Earn KSh 5,000 daily from KSh 20,000.”
- “2% per day guaranteed.”
- “Double your money in 30 days.”
- “$6 per trade on $500, twice daily.”

Calculate:
- daily return;
- monthly simple return;
- monthly compounded return;
- annualized equivalent;
- required turnover;
- implied payout obligations;
- sensitivity to recruitment.

Flag:
- extreme return;
- deterministic return;
- mathematically implausible sustainability;
- mismatch between claimed asset class and expected volatility.

The engine should explain the mathematics in plain language.

---

# 16. Successor-Scheme Detection

A major Dawnwatch feature.

When a new platform appears, compare with historical entities for:

- shared administrators;
- founder aliases;
- repeated phone numbers;
- repeated wallets;
- repeated referral codes;
- similar website templates;
- copied terms;
- same group/channel membership;
- same payment accounts;
- same office address;
- same company directors;
- same promotional images;
- same language patterns;
- direct “migration” instructions.

Output example:

> **Potential successor relationship detected**
>
> Apollo Exchange shares 5 independently observed identifiers with previously monitored entity QVSE.
>
> Relationship state: `UNDER REVIEW`

---

# 17. Search Experience

Universal search should accept:

- name;
- company;
- phone;
- URL;
- domain;
- wallet;
- app;
- email;
- paybill;
- social handle;
- individual.

Example:

`Search: +254712345678`

Result:
- associated entities;
- current risk state;
- linked advertisements;
- first seen;
- source summary;
- related scheme(s);
- evidence timeline.

---

# 18. Public Case Page

Each case should have:

## Header
- scheme/entity name;
- aliases;
- current state;
- last updated;
- countries;
- category.

## Evidence Summary
- top verified concerns;
- verified positive evidence;
- unresolved questions.

## Regulatory Status
- licence lookup;
- regulator warnings;
- enforcement actions.

## How It Works
Plain-English explanation of the business/recruitment mechanism.

## Timeline
Chronological evidence.

## Historical Pattern Match
Similar documented schemes with shared characteristics.

## Entity Graph
Interactive relationship visualization.

## Recruitment / Complaints Trend
Time-series charts.

## Claimed Returns
Mathematical analysis.

## Sources
Full provenance list.

## Corrections / Right of Reply
Structured response mechanism.

---

# 19. Historical Case Page

In addition to the normal case page:

- complete lifecycle;
- victim impact;
- loss estimates;
- prosecution history;
- recovery history;
- “how the scheme built trust”;
- “how withdrawals worked”;
- “how recruitment spread”;
- “what changed before collapse”;
- “earliest detectable signals”;
- “what Dawnwatch would have shown at each date”;
- lessons for future detection.

---

# 20. Dashboard

## 20.1 Public Dashboard

Display:

- active critical warnings;
- high-risk entities;
- emerging watchlist;
- newly detected schemes;
- latest regulator alerts;
- recruitment hotspots;
- top growing scheme mentions;
- top complaint accelerations;
- recent enforcement actions;
- historical case spotlight.

## 20.2 Analyst Dashboard

Additional tools:

- queue of new candidates;
- unreviewed entity links;
- risk-change queue;
- evidence review;
- source provenance;
- duplicate clustering;
- moderation queue;
- historical replay;
- graph investigation;
- case export.

---

# 21. Geographic Intelligence

Where location can be derived lawfully:

- county;
- town;
- recruitment region;
- event venue;
- phone-country code;
- business address.

Visualizations:
- recruitment heat map;
- complaint heat map;
- scheme spread over time;
- regulator/enforcement distribution.

Do not expose victim-level location.

---

# 22. Alert Design

Alerts should be concise but evidence-rich.

Example:

> **CRITICAL WARNING — XYZ Wealth**
>
> Dawnwatch detected three material developments:
>
> 1. official regulator warning issued;
> 2. withdrawal complaints increased sharply over 72 hours;
> 3. users are being asked to pay an additional “verification fee” before withdrawal.
>
> First detected: 11 Sep 2027  
> Current state: Critical Warning  
> Evidence: 14 sources  
> Last reviewed: 13 Sep 2027

Subscription options:
- entity;
- category;
- county;
- regulator;
- crypto;
- jobs;
- investments;
- daily digest;
- critical only.

---

# 23. API

Potential endpoints:

```http
GET /api/v1/search?q=
GET /api/v1/entities/{id}
GET /api/v1/schemes/{id}
GET /api/v1/schemes/{id}/timeline
GET /api/v1/schemes/{id}/indicators
GET /api/v1/schemes/{id}/relationships
GET /api/v1/schemes/{id}/risk-history
GET /api/v1/alerts
GET /api/v1/historical-cases
POST /api/v1/reports
POST /api/v1/feedback
```

Restricted analyst endpoints:

```http
POST /api/v1/analyst/cases/{id}/review
POST /api/v1/analyst/relationships/{id}/verify
POST /api/v1/analyst/indicators/{id}/resolve
POST /api/v1/analyst/cases/{id}/publish
```

---

# 24. Suggested Technical Architecture

## 24.1 Backend
- Python
- FastAPI
- Pydantic
- Celery / Dramatiq / Temporal for workflows

## 24.2 Primary Database
- PostgreSQL

Extensions:
- `pg_trgm`
- PostGIS
- pgvector if useful

## 24.3 Search
- OpenSearch or Elasticsearch

## 24.4 Graph
Phase 1:
- PostgreSQL relationship tables

Phase 2:
- Neo4j or Memgraph if graph traversal complexity justifies it

## 24.5 Object Storage
- S3-compatible evidence store

## 24.6 Stream / Queue
- Redis Streams initially
- Kafka / Redpanda later if scale requires

## 24.7 Frontend
- Next.js
- TypeScript
- React
- Tailwind
- accessible component library

## 24.8 Visualization
- MapLibre / Mapbox-compatible map layer
- Cytoscape.js / Sigma.js for graph
- ECharts / Recharts for time-series

## 24.9 AI Layer
Use language models for:
- entity extraction;
- claim extraction;
- classification;
- summarization;
- evidence comparison;
- contradiction detection;
- source clustering;
- timeline drafting.

Do not let the LLM be the sole authority for:
- licensing;
- identity matching;
- criminal status;
- conviction status;
- public high-risk classification.

---

# 25. Ingestion Architecture

Each source should implement a connector contract:

```python
class SourceConnector:
    source_name: str
    source_type: str

    async def discover(self) -> list[DiscoveredItem]:
        ...

    async def fetch(self, item: DiscoveredItem) -> RawObservation:
        ...

    async def normalize(self, raw: RawObservation) -> Observation:
        ...
```

Pipeline:

`DISCOVER → FETCH → NORMALIZE → DEDUPLICATE → EXTRACT → ENTITY RESOLVE → INDICATOR EVALUATE → RISK SNAPSHOT → ALERT`

Every stage must be idempotent.

---

# 26. Evidence Immutability

Original evidence should be content-addressed.

For each stored artifact:
- SHA-256 hash;
- acquisition timestamp;
- source;
- MIME type;
- original URL;
- archive location;
- extraction version.

Subsequent analysis should reference the immutable evidence object.

---

# 27. Auditability

Maintain an audit log for:

- classification changes;
- risk-state changes;
- human reviews;
- deleted relationships;
- correction requests;
- entity merges;
- source edits;
- publication decisions.

A reviewer should be able to answer:

> “Why did Dawnwatch classify this entity as High Risk on 14 August?”

---

# 28. Legal & Governance Framework

## 28.1 Public Language

Prefer:

- “Regulator warning identified.”
- “No matching licence was found in the register searched on [date].”
- “Multiple users reported withdrawal delays.”
- “The platform advertises X return.”
- “The claimed founder history could not be independently verified.”

Avoid unsupported statements such as:

- “This person is a scammer.”
- “This company stole money.”
- “This is definitely fraud.”

unless supported by an authoritative legal finding and properly contextualized.

## 28.2 Right of Reply

Entities should be able to:
- submit correction;
- provide licence evidence;
- challenge identity match;
- provide response;
- request factual update.

Responses should not automatically remove risk indicators.

## 28.3 Correction Log

Maintain public version history for material corrections.

## 28.4 Privacy

Do not publish:
- victim phone numbers;
- victim IDs;
- private financial details;
- home addresses;
- unredacted private chats without lawful basis.

---

# 29. Trust & Safety

Potential attack:
> A legitimate competitor is mass-reported as fraudulent.

Mitigation:
- report-count alone never triggers critical warning;
- reporter independence weighting;
- evidence requirements;
- human review;
- source tiers;
- brigading detection.

Potential attack:
> A fraudulent operator floods the internet with positive testimonials.

Mitigation:
- duplicate-copy analysis;
- referral-link clustering;
- account-age analysis;
- coordinated-posting detection;
- distinguish promotional volume from independent evidence.

---

# 30. Language Support

Initial:
- English
- Kiswahili

Later:
- Sheng / common Kenyan colloquial patterns;
- French;
- Portuguese;
- Arabic;
- major regional languages where useful.

Language models should preserve original text and translated interpretation separately.

---

# 31. Example Case: QVSE Historical Reconstruction

Example only; final case must be source-complete.

### Case
QVSE / Quant Vest Stock Exchange

### Pattern Tags
- copy trading;
- crypto funding;
- referral recruitment;
- signal group;
- high/deterministic return;
- regulatory uncertainty;
- founder identity anomaly;
- withdrawal freeze;
- additional verification payment;
- successor platform.

### Historical Questions
- when did the domain first appear?
- when did recruitment begin in Kenya?
- when did social promotion accelerate?
- when was the first public skepticism?
- when was the first regulator warning?
- when were withdrawal complaints first visible?
- when did additional-payment requirements appear?
- when did successor-platform migration begin?

### Back-Test Objective
Determine the earliest date on which Dawnwatch would have reached:
- Watch;
- Elevated Caution;
- High Risk;
- Critical Warning.

---

# 32. Historical Dataset Roadmap

## Phase H0 — Taxonomy
Create fraud taxonomy and evidence schema.

## Phase H1 — 20 Kenya Cases
Deeply reconstruct 20 historically important cases.

## Phase H2 — 100 Kenya Cases
Expand archive with structured metadata.

## Phase H3 — East Africa
Uganda, Tanzania, Rwanda, Ethiopia where source availability allows.

## Phase H4 — Africa
Cross-border case library.

Quality is more important than raw case count.

---

# 33. Delivery Phases

## Phase 0 — Repository & Governance Foundation
Deliver:
- repo structure;
- coding standards;
- data dictionary;
- evidence model;
- risk-state definitions;
- source-quality policy;
- legal-language policy;
- CI/CD;
- test framework.

Exit criteria:
- schemas stable enough for case ingestion.

---

## Phase 1 — Historical Archive MVP
Deliver:
- case database;
- source/evidence store;
- timeline;
- fraud-pattern tags;
- public historical pages;
- first 20 cases;
- search.

Exit criteria:
- every public statement traceable to evidence.

---

## Phase 2 — Entity Graph
Deliver:
- people/company/domain/phone/wallet nodes;
- relationship UI;
- evidence-backed edge creation;
- alias resolution.

Exit criteria:
- predecessor/successor relationships can be represented.

---

## Phase 3 — Regulatory Watch
Deliver:
- regulator source ingestion;
- licence matching;
- regulator warning alerts;
- company-register checks.

Exit criteria:
- new official warnings appear automatically.

---

## Phase 4 — News Radar
Deliver:
- continuous news ingestion;
- new scheme/entity discovery;
- article clustering;
- candidate creation.

Exit criteria:
- unknown financial propositions can be surfaced without manual seeding.

---

## Phase 5 — Social Radar
Deliver:
- supported public social streams;
- recruitment language classifier;
- promotion/complaint phase detection;
- velocity metrics.

Exit criteria:
- emerging recruitment clusters appear automatically.

---

## Phase 6 — User Submission Intelligence
Deliver:
- screenshot submission;
- URL/phone/wallet submission;
- extraction;
- clustering;
- moderation.

Exit criteria:
- repeated WhatsApp-style reports can open an emerging candidate.

---

## Phase 7 — Risk Engine
Deliver:
- explainable indicators;
- evidence weighting;
- state transitions;
- snapshot history;
- alert rules.

Exit criteria:
- historical back-tests produce reproducible results.

---

## Phase 8 — Watchtower
Deliver:
- continuous rechecking;
- material-change detection;
- subscriptions;
- email/push/API alerts.

Exit criteria:
- monitored entity changes trigger automatic reassessment.

---

## Phase 9 — Historical Validation
Deliver:
- time-sliced replay;
- precision/recall;
- warning lead-time metrics;
- false-positive analysis;
- weight calibration.

Exit criteria:
- published methodology and benchmark.

---

## Phase 10 — Institutional Portal
Deliver:
- investigator dashboard;
- evidence exports;
- API;
- regulator / bank watchlists;
- research tools.

---

# 34. Repository Structure

```text
dawnwatch/
├── README.md
├── DAWNWATCH_SPEC.md
├── docs/
│   ├── architecture.md
│   ├── governance.md
│   ├── risk-methodology.md│   ├── source-policy.md
│   ├── taxonomy.md
│   ├── api.md
│   └── historical-backtesting.md
├── apps/
│   ├── web/
│   ├── api/
│   └── worker/
├── packages/
│   ├── ingestion/
│   ├── extraction/
│   ├── entity_resolution/
│   ├── graph/
│   ├── risk_engine/
│   ├── alerts/
│   └── shared/
├── data/
│   ├── taxonomy/
│   ├── seed_cases/
│   └── fixtures/
├── connectors/
│   ├── regulators/
│   ├── news/
│   ├── corporate/
│   └── social/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── historical/
│   └── regression/
└── infra/
    ├── docker/
    ├── migrations/
    └── deployment/
```

---

# 35. Minimum Viable Product

A meaningful MVP should not attempt to ingest the whole internet.

MVP should include:

- 20–30 historical Kenyan cases;
- structured case pages;
- regulator monitoring;
- selected news monitoring;
- entity graph;
- company/domain/licence verification;
- claimed-return analyzer;
- manual/user submissions;
- rule-based risk states;
- email alerts;
- public search;
- analyst review queue.

MVP success criterion:

> Dawnwatch autonomously identifies at least one previously unseeded, emerging high-risk mass-recruitment proposition from monitored public sources and creates an evidence-backed candidate record.

---

# 36. Phase-2 Intelligence Enhancements

After MVP:

- richer social discovery;
- graph-based anomaly detection;
- image reuse detection;
- logo similarity;
- language fingerprinting;
- wallet transaction analytics where lawful/public;
- coordinated-promotion detection;
- scam-family clustering;
- successor prediction;
- cross-jurisdiction alerts;
- institutional APIs.

---

# 37. Metrics

## Discovery
- new candidates/week;
- percent autonomously discovered;
- duplicate candidate rate;
- average discovery latency.

## Accuracy
- false-positive rate;
- reviewed high-risk precision;
- relationship precision;
- licence-verification accuracy.

## Early Warning
- days before regulator warning;
- days before withdrawal freeze;
- days before major media report;
- days before enforcement.

## Coverage
- sources monitored;
- historical cases;
- active entities;
- counties represented;
- scheme categories represented.

## User Value
- searches/month;
- alert subscribers;
- reports submitted;
- reports leading to new cases;
- regulator/journalist citations;
- successful corrections.

---

# 38. Testing Strategy

## Unit
- parsers;
- phone normalization;
- domain extraction;
- return calculations;
- scoring logic.

## Integration
- regulator connector;
- article ingest;
- entity resolution;
- alert pipeline.

## Historical Regression
Historical known cases should produce stable expected indicator sequences.

## Adversarial
Test:
- fake testimonials;
- brigading;
- duplicate complaints;
- impersonation;
- deliberately misleading licence claims;
- company-name collisions.

---

# 39. Security

- encryption at rest;
- TLS everywhere;
- role-based analyst access;
- evidence access controls;
- secret management;
- audit logs;
- malware scanning for uploads;
- image metadata stripping for public display;
- rate limiting;
- abuse detection;
- secure file handling.

---

# 40. Ethical Constraints

Dawnwatch should never become:
- an automated blacklist without appeal;
- a rumor amplifier;
- a private-dossier marketplace;
- a people-scoring system;
- a tool for harassment;
- a pay-to-remove reputation service.

Revenue, if commercialized, must never influence risk classification.

---

# 41. Potential Business / Public-Interest Models

Possible models:

- free public consumer search;
- institutional subscriptions;
- API access for banks/fintechs;
- newsroom research tools;
- regulator dashboards;
- corporate fraud-intelligence feeds;
- grant-supported public-interest archive;
- premium monitoring for organizations.

Public warnings and core evidence should remain broadly accessible.

---

# 42. Branding Architecture

Working name:

# **DAWNWATCH**

Suggested descriptor:

> **Mass Fraud Early Warning & Intelligence**

Potential modules:

- **Dawnwatch Archive** — historical record
- **Dawnwatch Radar** — autonomous discovery
- **Dawnwatch Graph** — relationships
- **Dawnwatch Watchtower** — continuous monitoring
- **Dawnwatch Alerts** — notifications
- **Dawnwatch Lens** — deep case investigation
- **Dawnwatch Atlas** — geographic spread

Possible tagline:

> **See the warning signs earlier.**

Alternative:

> **Detect. Verify. Warn.**

---

# 43. Definition of Done for a Public Case

A case may be publicly listed as `HIGH RISK` or above only if:

1. entity identity is sufficiently resolved;
2. evidence is attributable;
3. at least one strong indicator is supported by Tier A/B evidence, or multiple independent Tier C sources;
4. allegations are clearly labeled;
5. regulatory claims are verified from official sources where possible;
6. risk rationale is human-readable;
7. named-person relationships are reviewed;
8. corrections mechanism exists;
9. publication passes moderation policy.

---

# 44. Example Alert Logic

Pseudo-rule:

```python
if regulator_warning.confirmed:
    escalate("CRITICAL_WARNING")

elif withdrawal_freeze.confirmed and unlock_fee.confirmed:
    escalate("CRITICAL_WARNING")

elif predecessor_failed_scheme.confidence >= 0.9 and recruitment_velocity.high:
    escalate("HIGH_RISK")

elif (
    extreme_return.confirmed
    and no_verified_licence.confirmed
    and referral_recruitment.confirmed
):
    escalate("HIGH_RISK")

elif new_mass_recruitment_candidate and evidence_count >= 3:
    escalate("WATCH")
```

Machine-learning models may influence prioritization, but final state transitions should remain auditable.

---

# 45. Example Observation Schema

```json
{
  "id": "obs_123",
  "source_type": "public_social",
  "source_name": "example",
  "published_at": "2027-03-14T09:20:00+03:00",
  "observed_at": "2027-03-14T09:24:11+03:00",
  "content_hash": "sha256:...",
  "language": "en",
  "text": "Deposit KSh 20,000 and earn KSh 5,000 daily...",
  "entities": [],
  "claims": [],
  "privacy": "public"
}
```

---

# 46. Example Indicator Object

```json
{
  "indicator_type": "EXTREME_RETURN",
  "status": "confirmed",
  "severity": "high",
  "confidence": 0.98,
  "first_seen": "2027-03-14",
  "evidence_ids": ["ev_12", "ev_13"],
  "explanation": "Promotional material advertises KSh 5,000 daily return on KSh 20,000 principal."
}
```

---

# 47. Example Public Explanation

Instead of:

> “MaliMax is a scam.”

Dawnwatch should say:

> **High Risk**
>
> Dawnwatch identified six independently observable warning indicators:
>
> - advertised return of approximately 25% per day;
> - no matching investment licence located in the regulator register searched on 14 March 2027;
> - recruitment rewards tied to new participants;
> - company incorporated 27 days before recruitment began;
> - payment requested in cryptocurrency;
> - founder history could not be independently verified.
>
> Dawnwatch has not identified a court finding establishing fraud. Users should independently verify regulatory authorization and underlying assets before transferring funds.

---

# 48. Long-Term Intelligence Goal

Dawnwatch should evolve from a searchable fraud database into a **fraud observatory** capable of answering questions such as:

- Which new financial propositions are spreading fastest this week?
- Which counties are seeing rising recruitment?
- Which schemes share payment infrastructure?
- Which promoters have moved between schemes?
- Which current schemes most closely resemble historical collapses?
- Which platforms have recently changed withdrawal rules?
- Which foreign regulator warnings involve entities now recruiting in Kenya?
- Which apparently new platforms are successors to old schemes?
- What warning signals most often precede collapse?
- How much earlier could intervention realistically occur?

---

# 49. North-Star Outcome

The system is successful when a future mass-recruitment scheme can be detected like this:

**Day 1**  
First promotional posts appear.

**Day 4**  
Dawnwatch clusters the name, phone number, domain, and referral language.

**Day 5**  
Automated checks identify a recently created company and no verified licence.

**Day 7**  
Recruitment velocity accelerates.

**Day 8**  
Dawnwatch moves the entity to `ELEVATED CAUTION`.

**Day 12**  
A foreign regulator warning is found involving the same operator.

**Day 12**  
Dawnwatch issues `CRITICAL WARNING`.

**Day 45**  
Mainstream media begins reporting withdrawal failures.

The measure that matters is not whether Dawnwatch correctly describes the collapse afterward.

It is whether Dawnwatch provides **credible, evidence-backed warning while people still have time not to send the money.**

---

# 50. Immediate Build Sequence

Recommended implementation order:

1. Create repository and schema.
2. Define evidence, source-quality, and risk-state governance.
3. Build 20 deeply documented historical Kenya cases.
4. Implement universal entity model.
5. Implement entity graph.
6. Add licence/regulator verification.
7. Add return analyzer.
8. Add news ingestion.
9. Add autonomous candidate discovery.
10. Add user screenshot/URL/phone submissions.
11. Add risk snapshots.
12. Add public case pages.
13. Add alert subscriptions.
14. Add historical replay framework.
15. Calibrate against known historical outcomes.
16. Expand public-social discovery.
17. Add institutional API and analyst portal.

---

## Final Product Definition

> **Dawnwatch is a provenance-first, continuously operating fraud-intelligence system that combines historical cases, autonomous discovery, entity graphs, regulatory verification, social recruitment signals, economic anomaly detection, and human-reviewed alerts to identify mass-recruitment schemes as early as possible without making unsupported accusations.**

The historical archive teaches the system what came before.

The radar finds what is emerging now.

The graph reveals what is connected.

The watchtower makes sure important changes are not missed.

And every warning shows its evidence.