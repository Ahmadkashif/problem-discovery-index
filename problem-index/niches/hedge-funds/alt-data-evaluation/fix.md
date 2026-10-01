# The Backtest Run on Revised History

**Niche:** [[niches/hedge-funds/alt-data-evaluation/profile|Alternative Data Evaluation & Onboarding]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Vendors deliver history as it looks today, not as it looked at the time, and backtests on it overstate what the data could have told anyone.
**Tags:** #time-series-forecasting #hypothesis-testing #evaluation-metrics #feature-engineering #quick-win
**Contested on:** Every serious competitor in this niche is fighting to prove or disprove, inside the trial window and on the fund's own universe, whether a dataset carries information not already in consensus — and whoever produces a defensible verdict before the trial expires decides which data gets bought.

## The Problem
Panels are re-weighted, merchants re-mapped, and late-arriving data backfilled. History delivered at trial reflects all of it. A backtest on that history uses information that was not available in real time and makes the dataset look better than it will perform.

## Why It's Still Broken
Many vendors do not store vintages, and funds under trial deadlines test what they are given.

## What a Fix Looks Like
Require vintage data where it exists; where it does not, estimate the revision effect by comparing successive deliveries during the trial and discount backtest results accordingly; record in the verdict which results are point-in-time and which are not.

## Who Feels the Pain
PMs who buy data on backtests that do not survive production; data teams blamed for the gap.

## Impact If Fixed
Fewer subscriptions bought on overstated evidence and more realistic expectations for those that are.
