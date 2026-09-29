# Pricing Set by Competitors, Not by Cost

**Niche:** [[niches/ai-inference-providers/inference-cost-corpus/profile|Inference Cost Corpus]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Per-token prices are set by looking at what everyone else charges, in an industry where nobody has computed their own marginal cost, so the whole market is anchored to a number with no floor under it.
**Tags:** #revenue-impact #descriptive-statistics #confidence-intervals #evaluation-metrics #gradient-boosting #hypothesis-testing #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to turn request-level history into an empirical account of what inference actually costs — and whoever does that prices, provisions and optimises against evidence while everyone else guesses.

## The Problem
A provider sets a price by checking three competitors and going slightly under. Those competitors did the same. None of them has computed the marginal cost of the request they are pricing, so the entire market's price level rests on an anchor nobody established and everyone references. When a well-funded entrant prices below cost to gain share, the others follow, because following is what the method requires and nobody has a floor to stop at. Margins compress across the industry and no participant can say whether a given price is profitable for them, which is a remarkable state for a capital-intensive business to be in.

## Why It's Still Broken
Competitive pricing is fast, requires no analysis and is defensible in any meeting. Computing marginal cost requires the corpus work nobody has assigned. In a growth market, share is rewarded more visibly than margin, so the discipline is deferred. And knowing your floor is only useful if you are willing to decline business at it, which is a harder conversation than matching a competitor.

## What a Fix Looks Like
Establish the floor and price from it. Compute marginal cost per request by model, hardware generation and concurrency regime, which is the prerequisite and is a tractable regression on data already held. Set a floor and hold it, declining business below cost rather than taking share that loses money — which is the discipline, and it is worth almost nothing without the number to justify it. Price differentiated products differently, since batch, interactive, dedicated and guaranteed-latency service have genuinely different costs and charging one price for all of them is a set of cross-subsidies nobody has quantified. Report contribution margin per customer, so unprofitable relationships are visible and can be repriced or restructured rather than silently funded. Distinguish strategic loss-leading from accidental loss-making, since the first is a decision and the second is what currently happens. Use the cost model to evaluate hardware procurement, since the right accelerator depends on the served mix and that is computable. Report price against cost as a standing metric to leadership, which is ordinary practice in every capital-intensive industry and absent here. And be willing to publish cost-based reasoning to customers, since a price a customer understands is more defensible than one that merely matches the market.

## Who Feels the Pain
Providers competing on price without a floor; investors funding growth whose unit economics nobody has established; and customers whose supplier may not survive the price it quoted them.

## Impact If Fixed
An entire capital-intensive market is anchored to a price nobody established. A computed floor is what makes declining unprofitable business possible, and per-product pricing exposes the cross-subsidies a single per-token rate currently hides.
