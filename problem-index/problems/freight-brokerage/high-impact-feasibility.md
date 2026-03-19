# Feasibility — Dynamic Lane Pricing and Margin Optimization

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Problem:** [[problems/freight-brokerage/high-impact|Dynamic Lane Pricing and Margin Optimization]]
**Problem type:** High Impact

**Problem summary:** Freight brokers who price loads on a lane by gut feel — using last week's rate they saw plus a margin — get a model that prices each load based on current market conditions, carrier capacity in the lane, day-of-week demand patterns, and the shipper's service sensitivity to generate the price that maximizes expected margin without losing the load.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
