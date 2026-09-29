# The Cliff Customers Discover by Falling Off It

**Niche:** [[niches/developer-tools-vendors/monorepo-scale-performance/profile|Monorepo & Scale Performance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every tool in the category degrades past a repository size, the customers who cross that line are the largest and least switchable, and none of them is warned before it happens.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to keep navigation, search and build responsive past the repository size where everything degrades — and whoever does that keeps the largest accounts, because the customers who cross that line are the most valuable and the least able to switch.

## The Problem
A repository grows steadily for three years. Nothing is wrong until, over the course of a quarter, everything becomes slow at once: the index rebuild that took twenty minutes takes four hours, language features start timing out, and a full build no longer fits in the interval a developer will wait. The engineering organisation loses a measurable fraction of its capacity and starts building internal workarounds. The vendor learns about it as an escalation from their largest customer, framed as a support issue, when the trajectory was visible in their own telemetry for eighteen months.

## Why Nobody Has Built This
Vendor performance telemetry is aggregated, and aggregates are dominated by the many small repositories, so the tail where the problem lives is statistically invisible in the vendor's own dashboards. The degradation is also gradual and per-customer, so nobody experiences it as a release regression and no alarm fires. Optimising for the largest customers is expensive engineering benefiting a small number of accounts, which loses roadmap arguments to features benefiting everybody — right up until one of those accounts is a material share of revenue. And the affected customers build their own infrastructure rather than complaining, which removes the signal entirely.

## What to Build
Predict the cliff and manage the approach. Model each customer's trajectory on the dimensions that drive degradation — repository size, file count, history depth, dependency graph width, concurrent developers — and project when they will reach the thresholds where specific capabilities degrade, which is ordinary forecasting over telemetry the vendor already collects. Warn the customer well before, with the specific capability that will degrade and the specific remediation — partial checkout, index sharding, build caching, dependency graph restructuring — since these remedies exist and are adopted only after the pain. Report per-customer performance rather than aggregates, so the account team sees a degrading experience before it becomes an escalation. Instrument the operations that actually degrade rather than the ones easiest to time. Detect the workarounds, since a customer who has built internal tooling around a vendor's limitation is a churn risk and a product requirement simultaneously, and the workaround is usually visible in their usage pattern. And publish the scale envelope honestly, because a customer who knows where the limits are will plan around them and one who does not will discover them at the worst moment.

## Target Customer
The largest engineering organisations, platform and developer experience teams, and the tool vendors for whom these accounts are concentrated revenue.

## Impact If Built
The affected customers are the most valuable and least switchable in the category, and the degradation is forecastable from telemetry that already exists. Warning before the cliff converts an escalation into a planned migration, and the remedies are already built.
