# The Serial Break Discovered When the Part Doesn't Fit

**Niche:** [[niches/powersports-and-boat-dealers/multi-oem-parts-lookup/profile|Parts Lookup & Special Orders Across OEM Catalogs]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** The OEM changed the part partway through the model year, the catalog shows both, and the customer didn't know their serial number.
**Tags:** #k-nearest-neighbors #workflow-orchestration #quick-win #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a customer's description, photo or old part into the right current part number across several OEM and aftermarket catalogs, and whoever has the lowest wrong-part return rate takes the account.

## The Problem
Phone and web orders are taken by model and year. When a serial break splits the part, the counter guesses, the special order arrives a week later, and it doesn't fit.

## Why It's Still Broken
Catalogs show the break but don't stop the order; the customer's serial number isn't asked for or isn't on file.

## What a Fix Looks Like
Block any order on a part with a serial break until a serial number or model-plate photo is captured; look it up from the DMS if the store sold or serviced the unit; and keep it on the customer record for next time.

## Who Feels the Pain
Parts associates handling returns; customers waiting twice; technicians whose jobs stall.

## Impact If Fixed
Stopping serial-break mis-orders (~2–4 a week in season at a busy counter, ~50–80 a season, estimate) saves ~7 days of customer wait on each and the return shipping and restocking behind them.
