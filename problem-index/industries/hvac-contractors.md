# HVAC Contractors

**Category:** Trades & Home Services
**Tags:** #tacit-knowledge-ml #signal-processing #tabular-ml #computer-vision #revenue-impact

## Industry Overview

The US HVAC (heating, ventilation, and air conditioning) contractor industry generates approximately $115 billion annually. Residential and light commercial HVAC is a highly fragmented market dominated by independently owned service companies, with major national brands (Service Experts, ARS/Rescue Rooter) holding a small share. The industry covers system installation, repair, and maintenance — with maintenance agreements (service plans) being the recurring revenue anchor that stabilizes cash flow for well-run firms.

HVAC work spans two major seasonal peaks: air conditioning season (April-September) and heating season (October-March), with overlap in mild climates. Emergency service — the system fails on the hottest or coldest day of the year — drives significant high-margin revenue.

## Dominant Platforms

- **ServiceTitan** — the leading field service management platform for HVAC, same platform dominance as plumbing
- **FieldEdge / Coolfront / Housecall Pro** — secondary platforms with HVAC-specific pricing books
- **Carrier / Trane / Lennox dealer portals** — OEM equipment diagnostic interfaces with some remote monitoring capability
- **Predictive maintenance IoT platforms** — Emerson Sensi, Carrier Côr, ecobee — smart thermostat platforms that collect runtime and temperature data but do minimal diagnostic processing

## Workforce and Knowledge Structure

Experienced HVAC technicians develop multi-sensory diagnostic knowledge that takes 5-10 years to fully develop: interpreting system pressures (suction and discharge side refrigerant pressures on gauges) to diagnose refrigerant charge, compressor health, and metering device performance; reading electrical measurements (amperage draw, voltage, resistance) across components to identify failing capacitors, contactors, and motor windings; listening to compressor and blower motor sounds to identify bearing wear, valve noise, and refrigerant flood-back.

The most financially significant tacit knowledge is refrigerant system diagnosis: an experienced technician reading a set of manifold gauge pressures can diagnose compressor valve failure, low refrigerant charge, TXV restriction, or airflow problems within minutes — a diagnostic skill that requires understanding the interplay of 4-5 simultaneous pressure and temperature measurements. Translating this reasoning into an ML model would enable junior technicians to diagnose the full refrigerant circuit correctly on their first service call.

## Key Economic Pressures

- Labor shortage — experienced HVAC technicians are scarce; the industry trains apprentices for 3-5 years before they can diagnose independently
- Refrigerant regulatory transition (R-22 to R-410A, now R-454B/R-32 for new equipment) creates diagnostic complexity as technicians work across multiple refrigerant types simultaneously
- Maintenance agreement retention — losing a maintenance customer costs 5× as much as retaining one; predictive outreach to at-risk customers is a top priority for most firms
- Equipment efficiency upgrades — homeowners replacing working units for efficiency/comfort rarely have the information to evaluate whether the upgrade economics make sense; firms that present data-driven upgrade recommendations close more sales

## Adjacencies

[[problems/hvac-contractors/high-impact|High Impact]] · [[problems/hvac-contractors/low-impact-1|Low Impact 1]] · [[problems/hvac-contractors/low-impact-2|Low Impact 2]] · [[problems/hvac-contractors/worker-life-1|Worker Life 1]] · [[problems/hvac-contractors/worker-life-2|Worker Life 2]] · [[problems/hvac-contractors/ml-opportunity|ML Opportunities]] · [[problems/hvac-contractors/ai-agents-platforms|AI Agents & Platforms]]
