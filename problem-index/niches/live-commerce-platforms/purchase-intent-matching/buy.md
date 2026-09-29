# Conversion Optimisation Practice

**Niche:** [[niches/live-commerce-platforms/purchase-intent-matching/profile|Purchase-Intent Matching]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Ecommerce has twenty years of conversion modelling with well-understood sparse-label technique, and live commerce ranks with a video team's objective.
**Tags:** #logistic-regression #gradient-boosting #loss-functions #evaluation-metrics #hypothesis-testing #confidence-intervals #causal-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rank streams for what a viewer will buy rather than for how long they will watch — and whoever changes the objective successfully converts an entertainment feed into a commerce channel.

## The Problem
Predicting and optimising conversion is one of the most thoroughly worked applied problems there is. Ecommerce ranking, search and advertising have all developed the technique for rare delayed labels, multi-objective ranking, position bias correction and incrementality measurement, and the practice is documented in detail. Live commerce, which is commerce, mostly does not use it, because the teams building it came from video and the infrastructure they inherited was built for a different objective.

## What Already Exists
Conversion prediction with delayed-feedback handling; multi-objective ranking with explicit trade-off weights; position and presentation bias correction; incrementality and uplift measurement; and value-aware ranking that accounts for price and margin.

## The Customization Gap
The adaptation is from a browsable catalogue to a live, expiring, one-shot offer. It requires: (1) the purchasable item being available for minutes rather than indefinitely, which collapses the delayed-feedback window and means a conversion missed is not deferred but lost — the standard delayed-label machinery assumes the opposite; (2) intent that must be met now rather than retargeted later, removing the fallback every ecommerce conversion stack relies on; (3) attribution to a moment inside a stream rather than to a page view, which no ecommerce measurement framework is instrumented for; (4) the entertainment objective remaining genuinely valid, so this is multi-objective by nature rather than a conversion system with a retention guardrail; and (5) the seller side entering the objective, which ecommerce ranking never has to consider because a catalogue item does not churn.

## Target Customer
Live commerce platforms, marketplaces with live formats, and ranking teams staffed from video backgrounds.

## Impact If Solved
The delayed-feedback machinery every conversion stack uses assumes the item is still there tomorrow, and here it is not. Removing retargeting as a fallback makes meeting intent in the moment the entire game.
