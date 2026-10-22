# LTL History Re-Rated Under Density Classes

**Niche:** [[niches/logistics-consultants/parcel-ltl-contract-optimisation/profile|Parcel & LTL Contract Optimisation]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Since July 2025 an LTL shipper's own history no longer tells it what its freight will cost, because classes now depend on density and most shipment records hold no dimensions.
**Tags:** #gradient-boosting #word-embeddings #feature-engineering #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know — from contracts and invoices across many comparable shippers — what discount tiers, minimums and surcharge terms a carrier will concede to a shipper of this profile, and whoever holds the deepest comparable-contract record negotiates the best agreement.

## The Problem
NMFC Docket 2025-1, effective 19 July 2025, moved many items from commodity classes to density-based ones on a 13-subprovision scale. A shipper negotiating a new LTL agreement needs to know what last year's freight would cost under each carrier's proposal at the new classes. Its TMS holds weight, commodity text and the old class — rarely length, width and height. Carriers, which reweigh and measure at terminals, know the shipper's density better than the shipper does.

## Why Nobody Has Built This
Rating engines price a shipment once its class is known; classification tools return an item's rule; neither estimates the missing dimensions of a year of history. The problem is new, created by the docket, and consultants are handling it with assumptions. The re-rating harness is described in [[problems/logistics-consultants/low-impact-1|Re-Rating LTL Bids After Density Classification]].

## What to Build
A density estimator trained on the shipper's own carrier inspection and reweigh corrections, item master dimensions and handling-unit data, which assigns each historical shipment a density, a post-docket class and a confidence; then bulk re-rating under every proposal, with the share of each proposal's apparent saving that depends on estimated rather than measured density shown alongside.

## Target Customer
LTL shippers renegotiating after the docket, and the consultants and audit firms that negotiate for them.

## Impact If Built
The shipper negotiates with a density picture as good as the carrier's, rather than signing a class agreement priced on classes that no longer apply.
