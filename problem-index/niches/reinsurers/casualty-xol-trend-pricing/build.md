# A Severity Trend Monitor Built From Every Cedent's Large Losses

**Niche:** [[niches/reinsurers/casualty-xol-trend-pricing/profile|Casualty Excess-of-Loss Trend & Development Pricing]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reinsurer holds individual large-loss histories from hundreds of cedents and selects severity trend for each treaty from that cedent's few claims and a published benchmark.
**Tags:** #bayesian-inference #mcmc-sampling #change-point-detection #survival-analysis #time-series-forecasting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put trend and development selections on long-tail excess layers that survive the next several years of ceded development, and whoever's selections still hold when the adverse development arrives takes the account.

## The Problem
Each cedent supplies a listing of claims above a reporting threshold, with paid and incurred values over time. One cedent's listing is too thin to estimate trend by line and venue, so the actuary leans on benchmarks that lag the market by years.

## Why Nobody Has Built This
Listings arrive in different layouts and thresholds, claim attributes (venue, injury, attorney involvement) are inconsistent, and the data is held renewal by renewal rather than as one corpus.

## What to Build
A pooled large-loss store, normalised across cedents. It feeds a hierarchical severity-trend model by line, state and venue with change-point detection, and a time-to-settlement model that estimates how much of each open claim will develop past attachment. Every pricing selection is recorded against the model's view and graded at each later evaluation.

## Target Customer
Heads of casualty pricing at reinsurers writing US general liability, commercial auto, umbrella and professional lines excess.

## Impact If Built
Trend shifts seen across the book a renewal or two before any single cedent's data would show them, and a running record of which selections held.
