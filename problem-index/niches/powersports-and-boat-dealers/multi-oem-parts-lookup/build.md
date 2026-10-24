# Photo to Part Number Across Every Line the Store Carries

**Niche:** [[niches/powersports-and-boat-dealers/multi-oem-parts-lookup/profile|Parts Lookup & Special Orders Across OEM Catalogs]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The parts counter matches a dirty part to a line drawing by eye, in one catalog at a time.
**Tags:** #cnns #contrastive-learning #k-nearest-neighbors #transformers #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a customer's description, photo or old part into the right current part number across several OEM and aftermarket catalogs, and whoever has the lowest wrong-part return rate takes the account.

## The Problem
Lookups that need more than one catalog, a supersession or a serial break are slow and error-prone, especially in spring when new counter staff are thrown in.

## Why Nobody Has Built This
Catalog content is licensed by each OEM; catalog publishers sell lookup within the catalogs they license, not identification; and matching photos of worn parts to line art is a hard vision problem.

## What to Build
A counter tool that takes a photo, a model-plate image or a description and returns ranked part numbers across the store's catalogs, constrained by model and serial range, resolved to current numbers through supersession tables, with stock and distributor availability. It abstains and asks for the serial number when unsure, and logs every lookup against later returns to retrain.

## Target Customer
Parts managers at multi-line powersports and marine stores; catalog publishers and DMS vendors as channel.

## Impact If Built
Halving wrong-part orders at a counter handling 40 lookups a day in season (estimate) avoids hundreds of returns a year and saves an hour or more of counter time a day.
