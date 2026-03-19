# Feasibility — Reefer Unit Pre-Cool Time Prediction for Load Planning

**Industry:** [[cold-chain-logistics|Cold Chain Logistics]]
**Problem:** [[problems/cold-chain-logistics/worker-life-2|Reefer Unit Pre-Cool Time Prediction for Load Planning]]
**Problem type:** Worker Life

**Problem summary:** Cold chain planners scheduling loads must know how long a reefer unit will take to reach setpoint temperature before loading — a number that varies with ambient temperature, unit age, unit model, and setpoint — but currently estimate from fixed tables that don't account for unit-specific performance degradation.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
