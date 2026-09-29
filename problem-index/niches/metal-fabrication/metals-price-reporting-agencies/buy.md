# Submission Quality From Contributors Who Are Positioned

**Niche:** [[niches/metal-fabrication/metals-price-reporting-agencies/profile|Metals Price Reporting Agencies]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every price submission comes from a company with a position in the market the price will settle.
**Tags:** #anomaly-detection #ml-time-series #data-integration #evaluation-metrics #compliance

## The Problem
Assessments are built from data submitted by market participants — mills, service centres, traders, and buyers — who are voluntary contributors and who hold positions the published price affects. A contributor who is long inventory benefits from a higher assessment. A buyer with an index-linked contract benefits from a lower one.

Most submissions are honest. Some are selectively reported: the trades that support a direction are submitted and the ones that do not are omitted, which is invisible in any individual record. Some are late, some are misclassified by grade or delivery terms, and some come from a company whose reporting conventions quietly changed.

Reporters catch a great deal of it — they know their contributors, they know when a submission does not fit — and that knowledge is entirely in people, in a role with meaningful turnover.

## What Already Exists
Data quality and anomaly detection platforms are mature. Market surveillance tooling exists in exchange-traded markets and is well developed for detecting manipulation patterns in order and trade data.

## The Customization Gap
Exchange surveillance assumes complete order books. Here the data is voluntary, partial, and submitted by interested parties.

**Selective omission is the central problem and is invisible per record.** Every submitted trade can be genuine while the set is biased by what was withheld. Detecting it requires reasoning about expected submission volume from a contributor given their known market activity — which is a model of the contributor, not a check on the record.

**Contributor-relative baselines with position awareness.** A submission's plausibility depends on this contributor's own history and on which side of the market they sit. That combination is specific to this domain and no generic tool models it.

**Influence-weighted triage.** In a thin grade one contributor can be most of the assessment, so an error there moves a published price that settles contracts. Prioritization must follow effect on the assessment, not size of the anomaly.

**The relationship constraint.** Contributors are volunteers whose participation is the whole business, so querying them has a cost. The system must weigh the value of asking against the relationship, which is the same constraint that appears in every reciprocity-based data business and that no off-the-shelf stewardship queue expresses.

**Full auditability under regulatory review.** Benchmark oversight requires every assessment to be reconstructable with every input, exclusion, and reason, years later.

## Target Customer
Head of price assessment operations or chief data officer, where a fixed reporter team covers an expanding set of grades and geographies under a daily publication clock.

## Impact If Solved
The assessment is only as good as what goes into it, and the failure mode that matters most — selective submission by positioned contributors — is undetectable by any per-record check. Modelling contributor behaviour and expected submission volume catches the bias that methodology alone cannot, and concentrates limited reporter goodwill on the queries that actually move a published price.
