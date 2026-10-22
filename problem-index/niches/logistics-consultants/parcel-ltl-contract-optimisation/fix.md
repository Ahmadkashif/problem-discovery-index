# Incentive Tiers That Pay Nothing After Volume Shifts

**Niche:** [[niches/logistics-consultants/parcel-ltl-contract-optimisation/profile|Parcel & LTL Contract Optimisation]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Parcel discounts are tied to weekly spend tiers, and when a shipper moves volume to a regional carrier its tier drops and the remaining freight gets more expensive.
**Tags:** #monte-carlo-methods #time-series-forecasting #descriptive-statistics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to know — from contracts and invoices across many comparable shippers — what discount tiers, minimums and surcharge terms a carrier will concede to a shipper of this profile, and whoever holds the deepest comparable-contract record negotiates the best agreement.

## The Problem
An agreement is modelled at last year's volume. During the year the shipper diversifies to a regional carrier, loses a large customer or grows faster than planned. Earned incentive tiers are recalculated on rolling spend, so diverting volume shrinks the discount on everything left — sometimes erasing the saving that motivated the diversion.

## Why It's Still Broken
Tier mechanics are buried in contract language, and the model that negotiated them used one volume scenario. Nobody re-runs the agreement when the volume plan changes.

## What a Fix Looks Like
Model every agreement across a range of weekly spend paths, show the spend at which each tier is lost, and evaluate diversion decisions — moving zones to a regional carrier, shifting heavy parcels to LTL — against tier effects before freight moves. Negotiate tier thresholds with the volume plan, not last year's history.

## Who Feels the Pain
Transportation directors whose diversification costs more than expected; finance teams surprised by rising cost per package.

## Impact If Fixed
Volume decisions made with their tier consequences visible, preventing a saving on one carrier from becoming a loss on another.
