# Every Declaration Is Presented as Equally Reliable

**Niche:** [[niches/electronics-contract-mfg/material-declaration-compliance-data/profile|Material Declaration & Product Compliance Data]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** A declaration obtained from the manufacturer this quarter and one inferred from a part family four years ago roll up into the same compliance percentage, and the customer ships against it.
**Tags:** #confidence-intervals #probability-distributions #descriptive-statistics #evaluation-metrics #survival-analysis #feature-engineering #compliance #data-integration #worker-facing #revenue-impact

## The Problem
Compliance status is reported as a rollup — this product is ninety-four percent declared — and the ninety-four percent is a mixture of very different things. Some declarations came directly from the manufacturer, recently, in a structured format. Some were inferred from a similar part or a family-level statement. Some are years old and predate a formulation change. Some came from a distributor rather than the manufacturer. The rollup treats them identically, so a customer looking at a high completeness figure cannot tell whether the remaining risk is in the six percent missing or in the ninety-four percent that is weakly evidenced. When a regulator or a customer challenges a specific part, the difference is the whole question.

## Why It's Still Broken
Completeness percentage is the metric the market buys on and is easy to compare between providers, which makes a quality-weighted figure commercially awkward to introduce alone. Provenance is captured internally for traceability in a form meaningful to analysts and not to customers. And the harder problem underneath is that nobody has quantified how declaration reliability actually decays — how often a four-year-old declaration turns out to be wrong after a formulation change — so there is no principled basis for weighting even if the will existed.

## What a Fix Looks Like
Provenance and confidence as first-class properties of every declaration: source type, date obtained, format, whether it is part-specific or inherited, and a staleness estimate grounded in the observed rate at which declarations of that type and age later proved wrong — which is measurable from the firm's own history of re-collection and correction. Rollups then report both completeness and evidential strength, and the customer sees where the weak evidence sits rather than a single number. Re-collection prioritization follows directly, targeting the declarations most likely to be stale and most consequential rather than working on a uniform refresh cycle. And when a customer is challenged on a specific part, the system produces the provenance record rather than requiring an analyst to reconstruct it.

## Who Feels the Pain
Compliance officers shipping against rollups whose composition they cannot see; analysts re-collecting declarations on a calendar rather than on risk; customers challenged on a part and unable to evidence reasonable care; and the provider, whose product is a claim about data quality that it reports as a count.

## Impact If Fixed
Turns the headline metric from a volume claim into a quality claim, using data already held. In a market where every provider reports completeness percentages, being the one that reports evidential strength is both the honest position and the defensible one — and it directs re-collection effort, the second largest cost in the business, at measured risk instead of at the calendar.
