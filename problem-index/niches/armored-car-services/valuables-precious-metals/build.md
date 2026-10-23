# Declared-Value Checks at Booking

**Niche:** [[niches/armored-car-services/valuables-precious-metals/profile|High-Value Valuables & Precious Metals Transport]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier accepts whatever value a jeweller writes on the manifest, prices and insures on it, and learns the real value only when something is stolen.
**Tags:** #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to move a declared-value consignment of bullion, jewellery or banknotes door to door, across borders where needed, with the declaration, customs entry and insurance cover right first time, and whoever delivers with no customs hold and no gap between declared and insured value takes the account.

## The Problem
Declared value drives three things: the fee, the carrier's liability cap and the carrier's own aggregate exposure on a vehicle or in a vault, which its specie insurers limit. If shippers under-declare, the carrier carries far more value than it priced or insured, and the loss, when it comes, becomes a lawsuit about what was really in the bags, as the 2022 Lebec theft did.

## Why Nobody Has Built This
Booking desks are service functions that want to keep shippers happy, and challenging a valued customer's declaration is commercially awkward. Values vary enormously by item, and precious metal prices move daily. Nobody has assembled the data to say what a given shipper's consignment of a given weight and description is likely worth.

## What to Build
A booking-time check that estimates the plausible value range of each consignment from the shipper's history, item descriptions and counts, weights, metal content and current metal prices, customs values declared on the same goods, and the shipper's insured values elsewhere where shared. Consignments far below the range prompt a confirmation and an explicit liability acknowledgement; aggregate exposure per vehicle and vault is recomputed on estimated, not declared, values.

## Target Customer
Heads of global services and valuables logistics at national carriers and specialist valuables carriers, and their specie underwriters.

## Impact If Built
Exposure that matches reality protects the carrier's insurance programme and pricing, and a recorded acknowledgement at booking turns the post-loss dispute into a document rather than a lawsuit.
