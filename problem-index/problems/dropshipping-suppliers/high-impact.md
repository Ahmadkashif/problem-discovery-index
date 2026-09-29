# Supplier Reliability Is Unmeasured

**Industry:** [[dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** High Impact
**One-liner:** A merchant commits their storefront and their customer relationship to a supplier they have never met, on the basis of a star rating that measures volume more than performance.
**Tags:** #gradient-boosting #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #change-point-detection #revenue-impact

## The Problem
Dropshipping asks a merchant to list a product they have never handled, from a supplier they cannot visit, and to be the party the customer holds responsible when it arrives late, wrong or broken.

The supplier's reliability is therefore the entire product. Everything else — the integration, the catalogue import, the order routing — is plumbing around that one question.

The platforms answer it with a rating. Ratings on these platforms are weak in well-understood ways: they are dominated by volume, since a supplier with thousands of orders accumulates reviews and a new one cannot; they are aggregated across a supplier's whole catalogue when performance varies enormously by product and by destination; they lag, so a supplier whose quality has just declined still shows a strong historical average; and they are gameable.

What the merchant actually needs is narrower and answerable: for this product, to my customers' destinations, at my volume, what is the distribution of fulfilment time, the defect rate, and the probability of a stock failure. The platform has every order it has ever routed to that supplier and does not compute it.

The failure lands entirely on the merchant. Their storefront takes the review, their customer service handles the complaint, their marketplace account bears the metric penalty.

## Why It's Unsolved
The platform's revenue comes from transactions and subscriptions, not from merchant outcomes, so a supplier that performs badly and ships volume is still revenue. Publishing rigorous supplier performance would make part of the catalogue unsaleable and would antagonise the suppliers whose participation the platform depends on.

Attribution is genuinely muddy. A late delivery may be the supplier, the carrier, customs, or a merchant who set an unrealistic expectation, and the platform's data does not cleanly separate them without effort.

Outcome data lives downstream. Whether the customer was satisfied is known by the merchant, not by the platform, and most platforms do not collect it — so the signal that matters most is outside the system.

Small samples are the honest statistical difficulty. Most supplier-product-destination combinations have few orders, and a rating computed on eight orders is close to meaningless, which pushes toward the aggregation that destroys the useful granularity.

## What a Solution Looks Like
Performance measured where it matters: by supplier, by product category, by destination region, with honest uncertainty on thin samples. A supplier who is reliable to one region and poor to another is common, and an aggregate hides exactly that.

Hierarchical estimation to handle small samples properly. Pooling across a supplier's products, and across similar suppliers, produces usable estimates on thin data with intervals that widen appropriately — which is the correct statistical answer and is better than either a naive average or silence.

Decline detection rather than a lagging average. A supplier whose fulfilment times have shifted this month is the thing a merchant needs to know now, and it is a change point in a series the platform already holds.

Downstream outcome collection. Merchant-side signals — customer complaints, returns, marketplace metric impacts — are the real quality measure and are obtainable if the platform asks for them.

Merchant-facing risk at the moment of decision. The useful place for this is when a merchant is deciding whether to list a product, not in a rating on a supplier profile page.

## Impact If Solved
Supplier reliability is the whole model and is currently conveyed by a rating that measures volume. Measuring it properly at the granularity merchants actually need would let them commit with evidence — and it is computable from data these platforms have been collecting since they started.
