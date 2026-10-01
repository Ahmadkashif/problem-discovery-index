# Counterfactual Grading of Sizing and Selling

**Niche:** [[niches/asset-managers/investment-decision-analytics/profile|Investment Decision Analytics]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A PM's stock picks may be good and their sizing and selling may give the edge away, and attribution cannot tell which.
**Tags:** #causal-inference #monte-carlo-methods #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a portfolio manager's own trade history into a measured account of where their decisions add and lose value — sizing, timing, selling — that the PM accepts as fair, and whoever does that becomes the feedback loop active management never had.

## The Problem
Brinson attribution splits return into allocation and selection; it does not answer whether this PM tends to sell winners too early, hold losers too long, or size best ideas too small. Those are decision habits and they are measurable from trade history.

## Why Nobody Has Built This
The analysis requires daily holdings and trades over years, counterfactual baselines, and careful statistics; it threatens PMs; and the vendors that do it are small.

## What to Build
For each decision type, a counterfactual — hold instead of sell, equal-weight instead of conviction-weight, no add — simulated over the actual history, with bootstrap confidence intervals, presented privately to the PM first. Link to the research ledger so decisions that ignored a recommendation are visible.

## Target Customer
CIOs and PMs at active managers.

## Impact If Built
PMs gain a feedback loop on their own habits; CIOs gain an evidence base for capital allocation across teams.
