# Seismic Permits Tracked Point by Point in Spreadsheets

**Industry:** [[geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Onshore seismic needs permission for every tract a source or receiver line crosses, and the permit, skid, no-permit zone and damage-claim record for tens of thousands of points runs on GIS layers and spreadsheets built for leases, not shot points.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #data-integration #workflow-orchestration #compliance #automation

## The Problem
Before a 3D survey records a single shot, a permit team must secure access across its footprint. A seismic operator cannot enter private property without the landowner's or occupant's permission; where land is leased for grazing or farming, both owner and tenant may need to agree; state and university lands have their own permits, surface damage rates and one-crew-one-client terms; and governmental permits do not always arrive when expected (Dawson Geophysical 10-K). A survey of a few hundred square miles touches thousands of tracts. Permit agents knock on doors, negotiate fees and conditions (no vibrators near the house, no access during calving, hand-carry only across the irrigated field), and record the outcome.

That record drives the survey. Refused tracts become no-permit zones; source points inside them are skidded or offset, which changes fold and image quality; conditional permits become crew instructions. After recording, damage claims — rutted fields, cut fences, cracked plaster blamed on vibrators — are settled tract by tract against the permit terms.

## What Already Exists
Oil and gas land management systems (Quorum Land and P2-family land software are typical) manage mineral leases, obligations and payments. GIS (ArcGIS) holds the survey design and tract layers. CRMs track contacts. Survey design software lays out source and receiver grids.

## The Customisation Gap
Land systems are built around leases that last years, not access permits that last a season and attach to individual shot points. The seismic-specific logic is: a permit status per tract joined to every planned source and receiver point it contains; conditions encoded as crew instructions (equipment type, timing, access route); automatic redesign triggers when no-permit polygons grow; a skid and offset log that the processor can trust; damage-claim records linked to the permit terms and to the crew's own GPS tracks and photos; and a status board that tells the client how much of the footprint is recordable today. Today these joins are made by a permit manager in Excel and an exported shapefile, re-done every evening.

## Impact If Solved
A permit system built for shot points cuts the days a crew of 40–100 technicians stands by waiting for access, lets the survey designer react to refusals before the crew reaches them, and settles damage claims from evidence rather than argument — on programs where crew standby can run to tens of thousands of dollars a day (estimate).
