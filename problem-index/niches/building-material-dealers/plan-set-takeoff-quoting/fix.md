# Waste Factors Set by Habit

**Niche:** [[niches/building-material-dealers/plan-set-takeoff-quoting/profile|Plan-Set Takeoff & Lumber Package Quoting]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** Every estimator applies a waste factor to every package, and nobody has ever checked it against what the job actually used.
**Tags:** #linear-regression #gradient-boosting #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a builder's or remodeler's plan set into a complete, priced lumber package before the builder picks a supplier, and whoever wins the highest share of the plan sets it quotes takes the account.

## The Problem
Waste factors of ~5–15% (estimate) are set by estimator habit, builder reputation and how hard the bid is fought. Too high loses the bid; too low brings the add-on truck.

## Why It's Still Broken
Job consumption is spread across tickets, and returns are not always booked, so the realised waste of a job is never computed.

## What a Fix Looks Like
Compute realised net consumption by category for closed jobs without plan changes, compare it with the quoted waste, and publish a waste table by builder, framer, house type and season that the estimator sees when quoting. Update it quarterly.

## Who Feels the Pain
Estimators guessing under bid pressure, drivers running add-ons, and the dealer losing bids to an over-padded number.

## Impact If Fixed
If waste factors move two points closer to realised consumption (estimate), a ~$60,000 package (estimate) is ~$1,200 sharper in a bid war or one add-on truck lighter, from ERP history the dealer already has.
