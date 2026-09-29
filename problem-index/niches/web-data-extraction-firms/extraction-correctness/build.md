# The Right Shape and the Wrong Field

**Niche:** [[niches/web-data-extraction-firms/extraction-correctness/profile|Extraction Correctness]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A scraper that returns nothing is obvious; a scraper that returns the wrong field with the right shape is invisible, and it feeds corrupted data into a customer's pricing or research pipeline for weeks.
**Tags:** #change-point-detection #hypothesis-testing #evaluation-metrics #probability-distributions #descriptive-statistics #confidence-intervals #large-language-models #automation
**Contested on:** Every serious competitor in this niche is fighting to detect when an extraction is returning plausible wrong values rather than no values — and whoever does that takes the account, because silent corruption is the failure customers cannot defend against.

## The Problem
A retailer redesigns a product page and the element the scraper reads now holds the subscription price rather than the one-off price. The extraction keeps succeeding. The values are numbers, in a plausible range, formatted correctly. A competitor's pricing engine consumes them for five weeks, adjusts its own prices downward against a number that was never the competitor's price, and the error is found when somebody manually checks a product. The firm's monitoring showed a hundred percent success rate throughout, because every check it ran was structural and nothing looked at what the values meant.

## Why Nobody Has Built This
Structural checks are easy and semantic ones require a model of what the field should look like, which nobody has built per field per source. The firms are measured on delivery success rate, which semantic validation would lower — a metric that goes down when you start measuring properly is a hard internal sell. Customers cannot detect it either, so there is no complaint to respond to until the damage is done. And the sheer number of sources makes per-source modelling feel intractable, even though the model is simple and the data is continuous.

## What to Build
Validate meaning, not structure. Monitor each field's distribution per source continuously and alert on a shift, since a field that changes what it points at almost always changes its distribution — this is the single highest-yield detector, it is cheap, and it needs only history the firm already has. Check internal consistency, because pages carry redundancy — a discounted price below a list price, a review count consistent with a rating distribution, a date within a plausible range — and violated relationships are strong evidence of a misread field. Cross-check against other sources collecting the same entity, which the firms uniquely can do and which is close to definitive when two independent extractions disagree. Use a model to verify a sample of extractions against the rendered page, asking whether the extracted value is what a person would say the field is — this is now cheap enough to run on a sample continuously and is the most direct check available. Detect page structure changes independently of extraction success, so a redesign triggers verification before anything looks wrong. Deliver a confidence score with every record, which the fix note develops. Report a semantic validity rate per source rather than a delivery success rate, because the second is the metric that allowed this to persist. And backfill corrections when a silent break is found, since the customer's downstream state is wrong and a fix going forward does not address it.

## Target Customer
Every customer running extracted data into a decision system, the firms whose reputations depend on silent failures not happening, and the data quality vendors who have never targeted this source type.

## Impact If Built
Delivery success rate is the metric that allowed silent corruption to persist. Per-field distribution monitoring is cheap and is the highest-yield detector available, and model-based sample verification against the rendered page is the most direct check and has only recently become affordable.
