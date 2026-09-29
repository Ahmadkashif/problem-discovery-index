# The Same Harness Every Quarter

**Niche:** [[niches/data-marketplace-brokers/the-sourcing-analyst/profile|The Sourcing Analyst]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Data sourcing analysts spend their quarters running bespoke evaluations of sample files against internal benchmarks, building the same comparison harness repeatedly because the market provides no basis for comparison.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #k-nearest-neighbors #hypothesis-testing #automation #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to give the analyst a reusable evaluation harness instead of a quarter spent rebuilding one — and whoever does that takes the account, because the same comparison is being constructed from scratch in every firm in the market.

## The Problem
An analyst evaluating five candidate providers writes five loaders for five schemas, maps each to their internal entity model, computes overlap against a reference file, measures field completeness, estimates freshness from timestamp distributions, and assembles a comparison table. Three weeks. Next quarter, a different category, five different providers, the same three weeks. The measurements are identical every time; only the schemas differ. Every firm in the market has an analyst doing exactly this, privately, and none of the work is reusable even inside one company.

## Why Nobody Has Built This
The harness looks bespoke because each dataset's schema differs, which hides that the measurements are constant. Marketplaces will not build it because it would surface comparative quality among their own suppliers. Providers will not build it for obvious reasons. Buyers build it internally and treat it as proprietary, which prevents it becoming a product. And the analyst is too busy running evaluations to build the thing that would stop them.

## What to Build
Build the harness once and make it schema-agnostic. Separate the measurements — overlap against a reference, field completeness, freshness distribution, accuracy on the matched subset, distributional comparison — from the schema mapping, so the analyst supplies a mapping and gets the full evaluation, which turns three weeks into a day and is the entire build. Infer the schema mapping automatically where possible, since providers model the same entities in recognisably similar ways and a proposed mapping the analyst corrects is far faster than one they write. Produce a standard comparison report, so evaluations are comparable across categories, analysts and time. Keep a durable evaluation history, so a provider re-encountered in two years arrives with their previous assessment attached rather than being re-evaluated from nothing. Record rejection reasons in structured form, which the fix note develops. Support the buyer's own reference data as the accuracy benchmark, since that is the only reference they trust. Let the analyst define category-specific criteria on top of the generic ones, because the generic measurements are most of the work and never all of it. And make the harness runnable inside the buyer's environment, since the reference data cannot leave.

## Target Customer
Data sourcing teams at enterprises and investment firms, the analysts doing this work, and the marketplaces whose buyers are currently building the quality layer themselves.

## Impact If Built
The measurements are identical every quarter and only the schemas differ, which is exactly the shape that generalises. A schema-agnostic harness with inferred mapping turns three weeks into a day, and a durable evaluation history stops the same provider being reassessed from nothing.
