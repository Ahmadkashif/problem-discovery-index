# The Scorecard That Arrives After the Month It Grades

**Niche:** [[niches/wireless-retail-agents/exclusive-postpaid-retail-chains/profile|Exclusive Postpaid Retail Chains]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Fix (Pain Point)
**One-liner:** District managers coach to last month's carrier scorecard because this month's can't be seen until it is too late to change.
**Tags:** #descriptive-statistics #time-series-forecasting #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche (iQmetrix, the chains' own BI teams and incentive-compensation vendors such as Xactly) is fighting to project each store's month-end carrier scorecard and net commission from live activation, attach and early-cancellation data, and whoever gives district managers a projection accurate enough to act on by mid-month takes the chain's analytics budget.

## The Problem
The carrier publishes the scorecard after month-end, sometimes weeks after. Managers spend the first half of each month explaining last month's miss and the second half chasing sales volume, which may not be the metric that's slipping.

## Why It's Still Broken
The chain has the raw data to compute most metrics itself, but definitions live in plan PDFs and change, and nobody owns a "shadow scorecard". Early-cancellation metrics need data the chain only gets from chargeback files later.

## What a Fix Looks Like
A shadow scorecard computed daily from the chain's own data, using the current definitions entered once a month by the finance team, with early cancellations estimated from historical rates per store. Not a forecasting project, just the same arithmetic done weeks earlier. Reconcile it against the carrier's scorecard each month to keep it honest.

## Who Feels the Pain
District and regional managers whose bonuses ride on tiers; store managers coached on the wrong metric; finance teams surprised by multipliers.

## Impact If Fixed
A spreadsheet-level change that moves coaching from autopsy to intervention, at the cost of a few hours of setup per plan change.
