# The Bill Grows Faster Than the Value

**Niche:** [[niches/observability-vendors/observability-platforms/profile|Observability Platforms]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Observability spend has become a board-level line item that frequently rivals the infrastructure being observed, and the pricing model rewards collecting data nobody ever reads.
**Tags:** #gradient-boosting #k-means-clustering #logistic-regression #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to be the place an organisation's telemetry lands and is queried — and that contest is fought twice, for engineering and for security, which is why this niche is not terminal and is decomposed below.

## The Problem
A company's monitoring bill exceeds the cost of the infrastructure it monitors. Someone is asked to reduce it. The only attribute they can see is volume, so they cut by volume: drop the noisiest service's logs, shorten retention globally, sample traces uniformly. Some of what they cut was never read; some of it was the thing that would have explained the next incident. Nobody can tell which, because no platform reports whether a signal has ever been queried, appeared in an investigation, or underpinned an alert that fired usefully.

## Why Nobody Has Built This
The commercial conflict is unavoidable and explains the whole gap: telling customers what to stop paying for reduces revenue, and every incumbent's pricing is volume-based. Value measurement is entirely feasible — query logs, alert definitions and investigation traces all exist inside the platform — and building it is against the builder's interest, which is why the capability's absence is a product choice rather than a technical limitation. Investigation traces, which record what an engineer actually looked at, are collected by some platforms and surfaced by none.

## What to Build
Value scoring per telemetry stream, and the retention policy that follows from it. Score every stream by how often it is queried, by whom and in what context, whether it has appeared in an incident investigation, whether an alert built on it has ever fired usefully, and how recently — then join that to its cost to produce a value-per-dollar ranking across the estate. Drive retention and sampling from the score rather than from a global policy: queried signals stay hot, rare-but-interesting traces are preserved while ordinary ones are dropped, and streams never read in a year are surfaced for deletion with the evidence attached. Track regret honestly, since the only convincing test is retrospective — of the streams dropped, how many were subsequently needed — and that number is directly measurable and is what a customer will ask for. Attribute cost anomalies to the specific service, metric and label rather than to a team. Warn on cardinality before ingestion rather than after billing. And accept that the natural home for this is a collector layer or a third party rather than an incumbent, which is what the open instrumentation standard has made possible.

## Target Customer
Engineering and platform teams under observability cost pressure, which is most of them; the open collector ecosystem; and whoever was asked why the monitoring bill exceeds the infrastructure bill.

## Impact If Built
Customers are cutting by volume because volume is all they can see, which means they are discarding the wrong things. Value scoring is computable from data every platform holds, and regret tracking is the measurement that makes the recommendation trustworthy.
