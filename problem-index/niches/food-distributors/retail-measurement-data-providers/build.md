# Projection Accuracy Measured Against Known Totals

**Niche:** [[niches/food-distributors/retail-measurement-data-providers/profile|Retail Measurement Data Providers]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every number sold is a projection from a sample of retailers to a market total, and the projections are checked against manufacturer shipment data only when a client complains loudly enough.
**Tags:** #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #cross-validation #probability-distributions #feature-engineering #data-integration #revenue-impact

## The Problem
Retail measurement is a sampling and projection exercise. Cooperating retailers supply point-of-sale data; non-cooperating channels — hard discount, club, and a long tail of independents — are estimated. The published market total is a modelled quantity, and its accuracy varies enormously by category, channel mix, and geography. Manufacturers hold a partial check in their own shipment data and raise it when the numbers disagree with what they know they sold, which is how projection error is usually discovered: as a client dispute rather than as a measurement. The provider has the components to do better — cooperating-retailer coverage by category, historical revisions, and in many cases manufacturer-supplied shipment data — and does not maintain projection accuracy as a standing metric.

## Why Nobody Has Built This
Projection methodology is the most guarded part of the business and disclosing accuracy invites the discussion the industry has spent decades avoiding, particularly as unmeasured channels have grown. Shipment data is also an imperfect check — it leads consumption and includes trade inventory movement — so a naive comparison misleads, and constructing a valid one requires modelling the pipeline. And no competitor publishes accuracy either, so nobody has been forced to.

## What to Build
A standing projection validation function. Published estimates are versioned and compared against independent references where they exist — manufacturer shipments with pipeline effects modelled, retailer-reported totals where cooperation permits, and category totals from external sources — with error decomposed by category, channel mix, geography, and coverage level. The most valuable output is not a headline accuracy figure but a per-cell reliability signal: which categories and geographies are well-measured and which rest on thin cooperation, published alongside the data so a client planning against a number knows how much to trust it. That is more honest than the current position and, in a market where clients increasingly suspect the unmeasured channels are distorting the picture, more credible than confident silence. Internally the same measurement directs retailer cooperation investment — the largest data acquisition cost — at the categories where coverage most degrades the estimate.

## Target Customer
Chief analytics officers and heads of methodology at retail measurement providers running 1,000-5,000 staff, and the manufacturer insight leaders who plan against these totals and reconcile them against their own shipments by hand.

## Impact If Built
Converts the industry's most persistent client complaint into a managed, disclosed property. It also directs the dominant acquisition cost at measured gaps, and pre-empts the argument that the panel no longer represents a channel-shifting market — which is the existential question for this category.
