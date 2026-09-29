# Contract Modelling Against a Benchmark Nobody Has Fitted

**Niche:** [[niches/last-mile-delivery/parcel-audit-contract-negotiation/profile|Parcel Audit & Contract Negotiation Firms]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm holds the only real picture of what carriers charge and negotiates from the last deal it happened to do.
**Tags:** #tabular-ml #gradient-boosting #evaluation-metrics #causal-inference #revenue-impact

## The Problem
Parcel pricing is a confidential, heavily discounted, surcharge-laden system where two shippers of similar size and profile can pay materially different effective rates for the same service. The carrier knows what everyone pays. No individual shipper knows what anyone else pays.

The audit firm is the exception. It processes shipment-level invoice data for hundreds of shippers, across both national carriers, with the negotiated discount tiers, minimums, and surcharge waivers that produced each charge. That is the market's actual price distribution, conditioned on volume, mix, zone profile, and service level.

It is used to check invoices against contracts and, in negotiation, as a set of anecdotes — the analyst's recollection of what a comparable shipper achieved. There is no fitted model of achievable rate given a shipper's profile, no estimate of how much of a discount is explained by volume versus by negotiation, and no measure of which concessions the carriers actually give up.

## Why Nobody Has Built This
The core business is audit, and audit is a rules exercise: apply the contract to the invoice, find the discrepancy, claim the refund. It is measured on recovery and it scales with headcount, and analytics that do not produce a refund do not appear in the metric.

Confidentiality is the stated obstacle to using the cross-client data, and it is genuine at the level of an individual contract. It is not an obstacle to a fitted model — the useful output is what a shipper with this profile should expect to achieve, which discloses nothing about any particular client.

And negotiation is treated as relationship work. The people who do it are experienced, they trade on knowing the carriers, and the knowledge has never been asked to become a model.

## What to Build
Fit the price distribution and negotiate against it.

**Model effective rate given shipper profile.** Volume, weight and dimension distribution, zone mix, service mix, residential share, and accessorial exposure. What a comparable shipper achieves — as a distribution, not a point — is the single most valuable number in a negotiation and the firm alone can produce it.

**Decompose the discount.** How much of a rate is explained by volume and mix, and how much by how hard the shipper pushed? That difference is the value the firm adds, and it currently cannot be quantified or sold.

**Model the surcharge surface.** Effective cost is dominated by accessorials and dimensional pricing far more than headline discounts, and shippers negotiate the headline. Which waivers and caps are actually obtainable, and what each is worth for this shipper's profile, is computable from the corpus.

**Simulate the general rate increase.** Carriers announce an increase annually and its real impact depends entirely on where a shipper's volume sits in the surcharge and dimensional structure. Modelling that for a client before the increase lands is a product nobody currently sells.

**Score the recovery opportunity.** Which invoice lines are most likely to yield refunds, so audit capacity goes where it recovers most rather than through everything at uniform depth.

## Target Customer
Chief Analytics Officer or VP of Client Solutions at a parcel audit and consulting firm. The competitive context is that audit is commoditizing — carriers have reduced the refund surface, and firms competing on contingency percentages are converging — while contract optimization is where the value and the defensible data sit.

## Impact If Built
Parcel spend is one of the largest controllable costs for any shipper, and it is negotiated against anecdote on the shipper side and complete information on the carrier side. Fitting the distribution corrects an information asymmetry across a very large market, and it is computable today from data the firm already processes for a different purpose.
