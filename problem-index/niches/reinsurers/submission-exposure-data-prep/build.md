# A Data-Quality Score That Prices

**Niche:** [[niches/reinsurers/submission-exposure-data-prep/profile|Submission & Exposure Data Preparation]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Exposure analysts fix a submission's defects and throw away the record of what was wrong, which is exactly what the underwriter needs to load for.
**Tags:** #gradient-boosting #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a cedent's exposure submission into a model-ready file with a data-quality score within hours of arrival, and whoever's cleaned files need the fewest manual fixes in December takes the account.

## The Problem
Analysts fill missing roof ages, recode construction, re-geocode postcode centroids and question values that look low. The cleaned file goes to the model, and the defects become an anecdote in an email to the underwriter.

## Why Nobody Has Built This
Data preparation is treated as a cost to minimise, not a measurement. Vendors stop at import validation, and brokers clean data to present it well, not to measure it.

## What to Build
A score per submission that combines geocoding resolution, completeness of secondary modifiers, value plausibility against rebuild-cost benchmarks and coding confidence. It is paired with a sensitivity run showing how far the modelled loss moves when defects are filled with expected values, and both feed the underwriter's data-quality load and the own-view-of-risk ledger.

## Target Customer
Heads of exposure management and cat modelling at reinsurers that lead property programmes.

## Impact If Built
A defensible, repeatable data-quality load in place of a feeling, and cedents told precisely which fixes would lower their price.
