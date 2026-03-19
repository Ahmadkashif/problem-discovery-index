# Feasibility — Pick Path Optimization for Batch and Zone Picking

**Industry:** [[warehouse-3pl|Warehouse / 3PL]]
**Problem:** [[problems/warehouse-3pl/worker-life-1|Pick Path Optimization for Batch and Zone Picking]]
**Problem type:** Worker Life

**Problem summary:** Pickers who follow WMS-generated pick lists in a sequence that's not optimized for their current aisle position — resulting in unnecessary backtracking — get a real-time path that minimizes their travel distance for the current pick batch given their location in the warehouse.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
