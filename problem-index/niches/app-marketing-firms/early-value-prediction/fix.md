# The Model Nobody Backtested

**Niche:** [[niches/app-marketing-firms/early-value-prediction/profile|Early Value Prediction]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The predicted lifetime value figure has driven every budget decision for two years and has never been compared to what those users actually turned out to be worth.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #quick-win #revenue-impact #survival-analysis #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to predict six-month value from a delayed, coarsened and partly suppressed early signal — and whoever does that accurately bids on better information than everyone else in the auction.

## The Problem
Every dashboard in the team shows predicted lifetime value. Campaigns are scaled and killed on it. Bids are set from it. Payback periods are calculated with it and presented to finance. The actual six-month value of those cohorts is knowable now for everything acquired more than six months ago, and the comparison has never been run. When someone eventually runs it, the common finding is a systematic bias that differs by network — which means budget has been misallocated in a consistent direction for a long time, correctably, on data the team already had.

## Why It's Still Broken
Nobody is tasked with looking back, and a model that is retrained regularly feels maintained — retraining is mistaken for validation, which is the specific confusion at the centre of this. The predictions were not stored in a way that makes comparison easy. The team is busy with this month's campaigns. And a systematic bias, once found, implies past decisions were wrong, which nobody is eager to establish.

## What a Fix Looks Like
Run the comparison. Backtest the predictions against realised value for every cohort old enough to have one, which is the fix, needs only data the team already has, and is typically a day's work with a finding that changes allocation. Report bias by network, since networks differ systematically and a single overall error figure conceals the actionable part. Store predictions prospectively from now on, so the exercise becomes a standing report rather than an archaeology project. Report calibration rather than only error, since a model that is unbiased on average and wrong at the extremes is dangerous in a tail-dominated business. Check the payback calculations finance has been given, because a biased prediction has been feeding a number the company's planning rests on. Distinguish model error from schema ceiling, so the team fixes the half that is fixable. Correct the bias in the bidding rather than only reporting it, which is where the money is. Re-run after every model change, since a change made without a backtest is a change of unknown sign. Publish the accuracy internally, because the model's credibility with finance and leadership depends on it having one. And measure the allocation shift the correction produces, since that figure is what justifies making backtesting permanent.

## Who Feels the Pain
Teams allocating budget on a biased prediction; finance receiving payback numbers built on it; and analysts who suspect the model is off and have never had time to check.

## Impact If Fixed
Retraining is mistaken for validation, which is why a two-year-old model has never been scored. A day's backtest on data already held typically reveals a systematic per-network bias that has been misallocating budget in a consistent and correctable direction.
