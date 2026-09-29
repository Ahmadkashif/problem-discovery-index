# Automated Bidding on a Broken Signal

**Niche:** [[niches/d2c-brand-operators/paid-acquisition/profile|Paid Acquisition]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform's automated bidding optimises toward whatever conversion signal the brand sends it, and most brands send an incomplete, delayed and unvalidated signal without knowing it.
**Tags:** #evaluation-metrics #data-integration #confidence-intervals #revenue-impact #logistic-regression #hypothesis-testing #automation #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to buy an incremental new customer for less than the next brand bidding on the same impression — and whoever does that survives, because the auction price rises structurally and the margin between cost and value is the whole business.

## The Problem
A brand hands bidding to the platform's optimisation, which is the only sensible choice, and the optimisation learns from the conversion events the brand sends back. Those events are sent by a tracking implementation nobody has audited: a proportion are lost, a proportion are duplicated, the value passed is revenue rather than margin, returns are never subtracted, and the events arrive late enough that the optimisation is learning from stale outcomes. The platform faithfully optimises toward the signal it receives. The brand's largest cost line is being steered by a feed nobody has checked, and the symptoms — inconsistent performance, drift, sudden degradation — are attributed to the platform or the market.

## Why Nobody Has Built This
Tracking implementation is treated as a setup task rather than as an ongoing operational dependency. There is no feedback telling a brand that their signal is degraded, because the platform reports on what it received. Agencies and internal teams are measured on the reported return, which is computed from the same broken signal. And the fix requires joining marketing infrastructure to order data, which is the join this whole category avoids.

## What to Build
Audit and improve the signal the optimisation learns from. Reconcile events sent against orders received continuously and report the match rate, loss rate and duplication rate, which is a straightforward comparison against the order database and immediately reveals a problem most brands do not know they have — this is the build's foundation. Send margin rather than revenue as the conversion value, since the optimisation will chase whatever value it is given and revenue-optimised bidding buys the discounted and returned orders enthusiastically. Subtract returns by sending a delayed correction, which the platforms support and few brands use, and which materially changes what the optimisation learns in categories with high return rates. Send the predicted lifetime value for high-signal customers rather than the first order value, so the optimisation buys the customers who come back rather than the ones who convert once. Reduce latency, since a conversion reported days late teaches the optimiser about a different auction. Monitor signal health continuously with alerts, because the degradation is silent and gradual. Test landing experiences against the creative that drove the visit, since the mismatch between them is a common and cheap loss. And report the signal quality alongside performance, so a drop is diagnosed rather than blamed.

## Target Customer
Performance marketing teams and their agencies, brands whose acquisition performance drifts unexplained, and the measurement vendors sitting between them and the platforms.

## Impact If Built
The largest cost line is steered by a feed nobody has audited, and its degradation is blamed on the market. Reconciling sent events against actual orders reveals it immediately, and sending margin with return corrections changes what the optimisation buys.
