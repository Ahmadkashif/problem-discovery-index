# Feasibility — Check-Call Automation and Shipment Status Monitoring

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Problem:** [[problems/freight-brokerage/worker-life-2|Check-Call Automation and Shipment Status Monitoring]]
**Problem type:** Worker Life

**Problem summary:** Freight brokers who call drivers once or twice during transit to confirm location and ETA — a task that takes 1-2 minutes per load per check-call, adding up to 45-90 minutes daily for a broker managing 20-30 active loads — get automated check-calls via carrier app or ELD integration with exceptions surfaced when a shipment is behind schedule.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
