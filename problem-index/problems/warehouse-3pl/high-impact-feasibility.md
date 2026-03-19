# Feasibility — Dynamic SKU Slotting Optimization

**Industry:** [[warehouse-3pl|Warehouse / 3PL]]
**Problem:** [[problems/warehouse-3pl/high-impact|Dynamic SKU Slotting Optimization]]
**Problem type:** High Impact

**Problem summary:** Warehouse operations managers who slot SKUs manually based on gut feel and experience — placing fast-moving items near the pick face but without continuously optimizing the slot assignments as velocity and order patterns change — get a slotting optimization model that continuously recommends slot reassignments to minimize total picker travel distance as demand patterns evolve.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
