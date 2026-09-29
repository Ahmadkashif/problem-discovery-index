# Usage Metering and Pricing Design

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Metering and usage billing are solved plumbing available from several vendors, and choosing what to charge for, at what tier, with what overage behaviour, is a commercial decision every API business makes by guessing and revisits painfully.
**Tags:** #gradient-boosting #k-means-clustering #logistic-regression #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
API businesses charge for usage, and the pricing design determines everything: whether customers adopt, whether they scale, whether they resent the bill, and whether the revenue tracks the cost of serving them.

The decisions are hard and consequential. What is the billable unit — a request, a resource, a compute-second, a record processed, a seat? Where do the tier boundaries sit? What happens on overage: a bill, a throttle, a hard stop? Should there be a free tier and how generous? How is a burst treated?

These are chosen early, usually by intuition and by copying a competitor, and they are extremely difficult to change later because every existing customer has planned around them. Getting them wrong shows up as customers whose bills are unpredictable enough that they cap usage defensively, which suppresses exactly the growth the model was meant to capture.

Meanwhile the provider has complete usage data for every customer, and it is used to render an invoice.

## What Already Exists
Metering and usage-based billing platforms (Metronome, Orb, Lago, Stripe Billing) handle event ingestion, aggregation, rating and invoicing well. Gateways emit usage events natively. Revenue recognition tooling handles the accounting. Pricing consultancies exist. Competitor pricing is public and widely copied.

## The Customisation Gap
Nothing analyses the usage data for pricing design. Clustering customers by usage shape — steady, spiky, seasonal, growing, dormant-then-bursting — reveals the segments that a tier structure should reflect, and tiers are instead set at round numbers.

Bill shock prediction is the most immediately valuable gap. A customer whose usage trajectory will produce a bill far above their expectation is identifiable well in advance, and telling them is both good service and better than a support escalation and a credit. The data is in the metering stream and nobody watches it for this.

Cost-to-serve alignment is the third gap. The billable unit should correlate with what serving the customer actually costs, and providers rarely check whether it does — with the result that some customers are structurally unprofitable and are discovered during a margin review rather than at pricing design.

Elasticity is the fourth and hardest: how usage responds to a price change is estimable where any variation exists, including across grandfathered cohorts, and is otherwise guessed at entirely.

## Impact If Solved
Pricing design determines the economics of an API business and is set by intuition against complete usage data that is used only to compute invoices. Segment analysis, bill shock prediction and cost-to-serve alignment are all straightforward analytics on data every provider already has.
