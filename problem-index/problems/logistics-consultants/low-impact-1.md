# Re-Rating LTL Bids After Density Classification

**Industry:** [[logistics-consultants|Logistics Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** LTL rating engines can price any shipment against any carrier's tariff, but a consultant comparing carrier bids has to re-rate a client's whole year of history under every proposal — and since July 2025 most of that history lacks the dimensions the new density-based classes need.
**Tags:** #gradient-boosting #feature-engineering #large-language-models #evaluation-metrics #data-integration #automation #quick-win

## The Problem
In a less-than-truckload bid, carriers do not quote lane rates the way truckload carriers do. Each proposes a discount off a base tariff — some off an industry base rate, some off their own — plus a freight-all-kinds class agreement, absolute minimum charges, fuel surcharge tables and a schedule of accessorials. The only honest way to compare five such proposals is to re-rate the client's last twelve months of LTL shipments under each one and total the result. The procurement analyst does this in Excel or a rating tool, one carrier at a time, then repeats it for every award scenario.

On 19 July 2025 NMFC Docket 2025-1 moved many LTL items from commodity-based classes to density-based ones on an expanded scale of 13 density subprovisions. Re-rating now needs each historical shipment's density, which needs its dimensions — and most shippers' TMS records hold weight, a commodity description and a class, but no length, width and height. The analyst either assumes the old class still applies, which makes every comparison wrong for exactly the freight whose class changed, or estimates dimensions by hand from the item master.

## What Already Exists
Base-rate and rating engines (SMC3's RateWare and CzarLite are the industry's standard references) price a shipment given origin, destination, class and weight; TMS platforms rate shipments in production against loaded contracts; NMFTA's ClassIT tools return the classification of an item. Freight sourcing platforms such as Keelvar run the bid event itself. Each does one step. None was built to take a messy year of client history, fill in what it lacks and rate it under many hypothetical contracts at once.

## The Customisation Gap
The consultant-specific logic is: a bulk re-rating harness that applies each carrier's full proposal — discount, base tariff, FAK ranges, minimums, fuel table, accessorial schedule — to every historical shipment; a density imputation step that estimates missing dimensions from the item master, handling-unit type, weight and commodity text, with a confidence flag per shipment; a re-classification step that maps each item to its post-Docket-2025-1 class and flags items whose class depends on handling or stowability rather than density; and side-by-side output by lane, customer and carrier that shows how much of each proposal's apparent saving comes from shipments whose density was estimated rather than measured.

## Impact If Solved
A re-rating that takes a procurement analyst two to three days per carrier for a large LTL shipper (estimate) becomes an overnight batch, so an award can be modelled under several scenarios before the bid deadline rather than one. And the shipper stops signing an LTL agreement priced on classes that no longer apply to a share of its freight.
