# Feasibility — Carrier Reliability Scoring and Double-Broker Fraud Detection

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Problem:** [[problems/freight-brokerage/low-impact-1|Carrier Reliability Scoring and Double-Broker Fraud Detection]]
**Problem type:** Low Impact

**Problem summary:** Generic carrier vetting tools check FMCSA authority status and safety rating, but don't score carriers on the behavioral signals that predict service failure and double-brokering fraud — patterns in their load acceptance, communication behavior, and tracking compliance that experienced dispatchers recognize from prior incidents.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Ingest TMS/route/telematics feeds, surface exceptions, and add optimization that operators can override.

## Open Source Data
Maps/traffic and some GTFS feeds are open; telematics, carrier SLAs, and stop-level telemetry are private.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
