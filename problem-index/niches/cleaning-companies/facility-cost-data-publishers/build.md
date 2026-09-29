# Awarded Bids as a Validation Signal on Published Unit Costs

**Niche:** [[niches/cleaning-companies/facility-cost-data-publishers/profile|Facility & Construction Cost Data Publishers]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Subscribers build estimates against the published line items and then find out what the work actually cost, and none of that comes back — so a database of unit costs is validated by nothing except the collection method that produced it.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #causal-inference #time-series-forecasting #confidence-intervals #hypothesis-testing #data-integration #revenue-impact

## The Problem
A line item asserts that a task takes a crew of this composition this many hours, at this material cost, in this city. Subscribers estimate against it, submit bids, win or lose, and then execute the work — generating, collectively, an enormous volume of evidence about whether the assertion was right. The publisher sees none of it. Costs are maintained by researchers who collect quotes, conduct time studies, and apply escalation factors, and validated against the same collection process that produced them. So the database is internally consistent and externally unverified, and its weakest entries — infrequent tasks, unusual crew configurations, smaller markets — are exactly the ones where no researcher has looked recently and no feedback exists.

## Why Nobody Has Built This
Actual cost data is commercially sensitive and belongs to subscribers, who compete with each other and have no obvious reason to share what a job really cost. Bid outcomes are similarly private. There is also a legitimate methodological objection: an actual cost reflects one contractor's productivity, negotiating position, and site conditions, so a naive comparison to a published national line item confounds four different things — which is why the publisher's researchers have preferred controlled collection to observed outcomes. And a database that adjusted toward observed costs could drift toward whatever its most active contributors experience, which is a real quality risk rather than a hypothetical one.

## What to Build
A voluntary outcome contribution programme with the analysis designed around the confounders rather than despite them. Subscribers contribute actual costs and bid outcomes in exchange for something they cannot get otherwise — their own performance benchmarked against the contributed population, which is a genuine reason to participate and the only structure that makes contribution rational. Contributions carry site, scope, and condition metadata so that contractor productivity, market conditions, and scope variance can be modelled separately from the line item's own accuracy. The publisher's output is not an adjusted price but a validation report per line item: how much observed cost disperses around the published figure, whether there is systematic bias, and where dispersion is wide enough that the line item should carry a range rather than a point. Research effort then concentrates where the evidence says the database is weak, rather than on a rotation. And the most commercially interesting product falls out of the same data — published figures gaining an empirical confidence band, which is what an estimator most wants and no cost publisher currently offers.

## Target Customer
VPs of data and directors of cost research at cost data publishers running 100-400 cost engineers, and the estimating leaders at facility services and construction firms who bid against these figures with no measure of their reliability.

## Impact If Built
Converts a database validated by its own method into one validated by outcomes, which is the difference between an authoritative reference and a defensible one. Confidence bands change what the product is worth to a bidder, because knowing which line items are shaky is directly worth money on a tight bid. And the contribution programme creates a data asset that compounds with subscriber base — the one moat a competitor entering with better collection technology cannot replicate.
