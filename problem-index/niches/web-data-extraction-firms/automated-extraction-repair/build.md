# The Repair a Model Can Now Do

**Niche:** [[niches/web-data-extraction-firms/automated-extraction-repair/profile|Automated Extraction Repair]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Fixing a broken extractor means finding where the field moved on the page, which is now a mechanical task, and it is still the largest consumer of engineering time in the industry.
**Tags:** #large-language-models #automation #evaluation-metrics #transfer-learning #confidence-intervals #hypothesis-testing #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to repair a broken extractor without a person, verified, at fleet scale — and whoever does that takes the account, because repair is now mechanically feasible and is still being done by hand.

## The Problem
An extraction breaks because a site moved the price into a different element. The repair is: open the page, find the price, update the selector, check that the values look right, deploy. An engineer does this in ten minutes, several times a day, across a fleet of thousands of extractors maintained by a team that is permanently behind. A model can read the page, identify the price and produce a new selector, and most firms use models to extract rather than to repair — which spends model cost on every page forever instead of once per breakage.

## Why Nobody Has Built This
Trusting an automatic repair requires verification the firms have not built, and an unverified automatic fix is worse than a break because it turns a loud failure into a silent one. The repair loop spans monitoring, page rendering, rule generation, validation and deployment, which is more integration than any single team owns. The capability became feasible recently and the assumption that repair needs a person has not updated. And the engineers who would build it are in the queue.

## What to Build
Close the loop with a verification gate. Trigger repair automatically on detected breakage, rendering the page and asking a model to locate the requested fields — which is the mechanical core and is now reliable enough for the common cases. Generate a new extraction rule rather than extracting directly, so the repair is a one-time cost and the steady state remains cheap, which is the economic point and is what distinguishes repair from simply switching to model-based extraction. Verify before deploying: run the candidate against a sample, compare the value distribution against the pre-breakage distribution, check the internal consistency relationships, and require agreement before the fix goes live — this gate is what makes automation safe and its absence is why it should not ship without one. Route by confidence, sending low-confidence repairs to an engineer with the candidate attached, which makes even the failures faster. Learn from human repairs, since every fix an engineer makes is a labelled example of exactly this task and firms have years of them. Repair the whole group when one site changes, since the fix usually generalises across that site's extractions. Report an automatic repair rate and a verified-correct rate, so trust is built on evidence. And keep a human review of a sample of automatic repairs indefinitely, because the failure mode is silent and the sampling is cheap.

## Target Customer
Firms operating scraper fleets, the engineers in the repair queue, and the customers whose extractions would be restored in minutes rather than days.

## Impact If Built
Using a model to repair once rather than to extract forever is the economic difference, and it is the one most firms have not made. The verification gate — distribution comparison against the pre-breakage baseline — is what makes unattended repair safe rather than a way to convert loud failures into silent ones.
