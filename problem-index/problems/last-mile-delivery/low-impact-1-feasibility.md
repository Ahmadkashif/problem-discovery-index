# Feasibility — Dynamic Route Reoptimization During Delivery

**Industry:** [[last-mile-delivery|Last-Mile Delivery]]
**Problem:** [[problems/last-mile-delivery/low-impact-1|Dynamic Route Reoptimization During Delivery]]
**Problem type:** Low Impact

**Problem summary:** Generic route optimization tools plan the day's stops before departure but don't reoptimize the remaining route in real time as stop completion times deviate from plan, traffic conditions change, and failed deliveries require rerouting decisions.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
