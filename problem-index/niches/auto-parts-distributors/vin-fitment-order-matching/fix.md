# The VIN Decode Stops Short of the Qualifier

**Niche:** [[niches/auto-parts-distributors/vin-fitment-order-matching/profile|VIN & Fitment Matching on Shop Orders]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** The VIN tells the counter the engine and trim; the catalog still shows two rotors split by a brake package the VIN doesn't encode, and the counter guesses.
**Tags:** #large-language-models #bayesian-inference #logistic-regression #feature-engineering #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a shop's call, text or e-catalog request into the one part that fits that VIN, and whoever has the lowest fitment-return rate on the shop orders it matches takes the account.

## The Problem
NHTSA's vPIC decoder returns make, model, year, displacement, engine model, trim and body class; catalog qualifiers often turn on options it doesn't return, such as a towing or heavy-duty brake package, a rear axle ratio or a mid-year production change. The counter either guesses, asks the shop to go look at the car, or sends both parts.

## Why It's Still Broken
Option-level build data is held by vehicle makers and licensed data vendors, not public; catalogs carry the qualifier text but not the probability that each applies; and nobody records which way past orders resolved.

## What a Fix Looks Like
For each ambiguous qualifier, estimate the probability from the decoded configuration, regional build mix and the store's past resolutions for the same configuration, and generate the one question that settles it ("Does it have the trailer hitch from the factory?", "Is the rotor 13.8 or 12.9 inches?"). Answers and outcomes feed back into the estimate.

## Who Feels the Pain
Counter staff, technicians asked to measure a part already on the lift, and drivers carrying two parts to return one.

## Impact If Fixed
If "send both" orders fell by ~half from ~5% of brake and suspension lines (estimate), a store would cut ~3–5 return pickups a week and the inventory tied up in round trips.
