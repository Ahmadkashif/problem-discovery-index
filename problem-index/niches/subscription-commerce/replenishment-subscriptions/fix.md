# The Cupboard Full of Product

**Niche:** [[niches/subscription-commerce/replenishment-subscriptions/profile|Replenishment Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** A customer who has accumulated four months of unused product cancels, and the company's system recorded every one of those deliveries as a successful order and a satisfied customer.
**Tags:** #evaluation-metrics #descriptive-statistics #gradient-boosting #confidence-intervals #revenue-impact #survival-analysis #quick-win #causal-inference
**Contested on:** Every serious competitor in this sub-niche is fighting to have the next delivery arrive as the last one runs out — and whoever does that keeps the subscriber, because the alternative is a customer who simply buys it when they need it and does not need a subscription at all.

## The Problem
A subscriber has received eleven deliveries and used the contents of seven. The remaining four sit unopened. Every delivery charged successfully, arrived on time and generated no complaint, so every operational and commercial metric is green. From the company's point of view this is a model subscriber. From the customer's, they are paying monthly for a growing pile of product they will never get through, and at some point they look at the pile and cancel. The over-supply was visible in their skip pattern and their declining engagement, and the system was measuring successful charges.

## Why It's Still Broken
Successful delivery and successful charge are the metrics the operational systems produce, and over-supply generates neither an error nor a complaint. Reducing frequency for a customer who is paying happily is revenue the company would rather keep, which is a short-run calculation nobody has tested against retention. The signals — skips, unopened packages where observable, engagement decline — are present and are not read as over-supply. And the cancellation is attributed to price.

## What a Fix Looks Like
Detect over-supply and act against short-run revenue. Build an over-supply score per subscriber from the available signals — skip frequency, delivery acceptance, engagement decline, support contacts about pausing, quantity change requests — which is a straightforward classification and is the detection this whole fix depends on. Intervene before the pile becomes visible, offering a reduced cadence or quantity proactively, which feels counter-commercial and is the correct decision if lifetime value is the objective rather than next month's charge. Test it properly with a holdout, since the revenue objection is empirical and the category has the cohort structure to settle it — and the answer is almost certainly that the reduced cadence subscriber is worth more over a year. Read the skip as the signal it is, since a customer skipping is telling you they have too much and the system treats it as a deferred charge. Ask about stock levels periodically, which customers answer readily and which resolves the estimate directly. Report over-supply prevalence as a metric, because it is currently invisible and is likely a large share of the base. Offer a pause that is genuinely easy, which the flexibility niche develops. And frame the reduction to the customer as the service working, since a company that notices they have too much is demonstrating the value the subscription promised.

## Who Feels the Pain
Subscribers paying for a growing pile; operators losing them and recording price as the reason; and retention teams offering discounts to people whose problem is that they already have too much.

## Impact If Fixed
Every metric is green while the customer accumulates product they will never use, because successful charges are what the systems measure. A holdout settles the revenue objection empirically, and the category's cohort structure makes that test unusually easy to run.
