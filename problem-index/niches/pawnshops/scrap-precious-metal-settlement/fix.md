# The Assay Shortfall Nobody Can Trace

**Niche:** [[niches/pawnshops/scrap-precious-metal-settlement/profile|Scrap Precious-Metal Lots & Refiner Settlement]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Fix (Pain Point)
**One-liner:** The refiner's statement says the lot was short, and the shop accepts it because it has no record to argue with.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to settle a pawnbroker's scrap gold and silver lots for the most metal at the best moment — accurate karat sorting before shipment, an assay the shop can check, and timing against spot — and whoever closes the gap between the shop's estimate and the refiner's settlement takes the account.

## The Problem
Lots are weighed and shipped with a total weight and a karat label; the assay comes back weeks later; the payment is whatever it is. Shortfalls are absorbed and the jewellery buyer is blamed.

## Why It's Still Broken
No expected fine weight is computed per lot before shipping, so there is nothing to compare the settlement against.

## What a Fix Looks Like
Before shipment, compute expected fine weight and value per lot from the piece log, store it, and compare against every settlement, flagging gaps beyond a tolerance for review or a re-assay request.

## Who Feels the Pain
Jewellery buyers blamed for shortfalls; owners losing margin silently.

## Impact If Fixed
Every lot has an expectation to test the settlement against, and the shop stops accepting short assays by default.
