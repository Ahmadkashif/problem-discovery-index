# Pricing One Unit at a Time, at Scale

**Niche:** [[niches/recommerce-platforms/unit-level-pricing/profile|Unit-Level Pricing]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every item is a single unit with its own condition, and pricing it correctly determines whether the platform makes money on an item that cost real labour to process and may sell for twenty dollars.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #k-nearest-neighbors #evaluation-metrics #revenue-impact #cnns #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to price a one-of-a-kind unit correctly in seconds at a cost the item can bear — and whoever does that takes the economics, because the price decision determines whether a processed item makes money and it is made hundreds of times a shift.

## The Problem
A jacket arrives. Its retail price four years ago was two hundred dollars. The rule says forty percent of retail for this grade, so it is listed at eighty. It does not sell. Four months later it is marked down twice and sells for thirty-one, having consumed storage and two markdown cycles and yielding less than the processing cost. Another jacket, from a brand with a strong resale following in a size that is in demand, is priced by the same rule at eighty and sells in three hours — it would have sold at a hundred and forty. Both prices were wrong in opposite directions and both were produced by a rule that ignores everything that determines resale value.

## Why Nobody Has Built This
Pricing was implemented as a rule because the decision must be instant and a rule is instant, and the modelling alternative was assumed to be slower. The condition grade — the largest value driver — is a coarse category that discards most of what the grader observed. The realised outcome is recorded in a different system from the intake decision, so the feedback loop was never closed. And the cost of a bad price is diffuse across thousands of items rather than visible on any one.

## What to Build
Predict the price from the item. Model expected realised price and time-to-sell jointly from the item's attributes, brand, condition detail, photographs, size, season and the platform's own sales history, which is a well-posed problem with enormous labelled data and is the whole build — every item the platform has ever sold is a training example with an outcome. Produce a price-to-speed curve rather than a single number, since the platform's real decision is how long it is willing to hold the item and the storage cost makes that trade explicit. Price the condition in detail rather than by grade band, since the grade is a lossy summary of observations the grader already made and recovering that detail materially improves the estimate. Use the photographs directly, since they contain condition and style information the attribute fields do not capture and the models to read them are available. Report confidence, since some items are well-comparable and some are genuinely singular, and a wide interval should trigger a different handling path rather than a confident guess. Incorporate seasonality at intake, since a coat received in April and the same coat in September have different optimal prices and the rule ignores the calendar. Feed realised outcomes back continuously, which is what makes the model improve where the rule cannot. And deliver it in the intake flow as a suggestion the processor accepts or adjusts, because the decision must stay fast.

## Target Customer
Managed recommerce platforms, resale-as-a-service providers, and the brands whose items are being priced by a percentage rule.

## Impact If Built
Every item the platform has ever sold is a labelled training example and the decision is made by a rule table. A price-to-speed curve makes the holding-cost trade explicit, and reading the photographs recovers the condition detail the grade band discards.
