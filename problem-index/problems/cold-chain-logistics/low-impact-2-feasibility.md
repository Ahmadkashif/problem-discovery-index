# Feasibility — Reefer Unit Maintenance Prediction from Telematics Data

**Industry:** [[cold-chain-logistics|Cold Chain Logistics]]
**Problem:** [[problems/cold-chain-logistics/low-impact-2|Reefer Unit Maintenance Prediction from Telematics Data]]
**Problem type:** Low Impact

**Problem summary:** Generic predictive maintenance models exist for industrial equipment, but don't understand refrigeration unit operating cycles, the specific failure modes of Carrier Transicold and Thermo King units, or the relationship between reefer telemetry patterns and specific component failures — the domain translation that turns generic anomaly detection into actionable maintenance scheduling.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
