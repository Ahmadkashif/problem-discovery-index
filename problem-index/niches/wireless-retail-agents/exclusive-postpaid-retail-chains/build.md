# Mid-Month Scorecard Projection by Store

**Niche:** [[niches/wireless-retail-agents/exclusive-postpaid-retail-chains/profile|Exclusive Postpaid Retail Chains]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A chain's income is set by a carrier scorecard tier it sees only after the month closes, when nothing can be done about it.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche (iQmetrix, the chains' own BI teams and incentive-compensation vendors such as Xactly) is fighting to project each store's month-end carrier scorecard and net commission from live activation, attach and early-cancellation data, and whoever gives district managers a projection accurate enough to act on by mid-month takes the chain's analytics budget.

## The Problem
Carrier scorecards weight a handful of metrics (activation mix, protection and accessory attach, early deactivations, survey scores, audit results) into tiers that set bonus multipliers and influence which new doors the carrier approves (estimate; no carrier publishes its dealer scorecard). A district manager with twelve stores sees today's sales, but not what they will score after early cancellations are netted and the carrier's definitions are applied. By the time the scorecard arrives, the month is over.

## Why Nobody Has Built This
Scorecard definitions are confidential to each dealer–carrier relationship and change with the comp plan, so vendors can't productise them. Chargeback-adjusted numbers need the chargeback history joined to activations, which few chains have done. In-house BI teams are small and spend their time building last month's reports.

## What to Build
A projection engine that ingests the current scorecard definition, computes each metric daily from POS and traffic data, projects early deactivations from the chain's own chargeback survival curves, and forecasts each store's month-end tier with an interval. It then ranks the actions with the largest expected tier impact (which metric, which store, which rep) and estimates the dollar value of moving up a tier.

## Target Customer
VPs of retail operations and finance at exclusive chains of 100+ doors; roughly a dozen per national carrier (estimate).

## Impact If Built
Managers act in week two instead of reading results in week five. One store moved up a tier is worth more than a district's worth of reports, and the same engine produces the door-level economics a chain needs when it buys or closes stores.
