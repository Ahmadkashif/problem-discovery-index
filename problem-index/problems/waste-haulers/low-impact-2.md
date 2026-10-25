# Franchise Reports Rebuilt Every Month

**Industry:** [[waste-haulers|Waste Haulers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every franchise contract asks for its own monthly or quarterly report of tonnage, diversion, complaints and service failures, plus SB 1383 records in California, and haulers assemble each one by hand from scale tickets and route data that were never tagged by jurisdiction.
**Tags:** #large-language-models #descriptive-statistics #data-integration #compliance #automation #workflow-orchestration

## The Problem
A regional hauler may hold 20–40 franchise or municipal contracts, each with a reporting exhibit. One city wants monthly tons by stream (trash, recycling, organics), customer counts by service level, diversion rate, missed-pickup complaints and their resolution times, and a count of liquidated-damage events. Another wants quarterly reports in its own spreadsheet template plus the fee remittance calculation, because the franchise fee is a percentage of gross receipts. In California, jurisdictions that delegate SB 1383 contamination monitoring to the hauler also need route-review records: who reviewed which route on what date, which addresses had prohibited contaminants, and which notices went out. CalRecycle requires every hauler route to be reviewed every year, and the counts flow into the jurisdiction's Electronic Annual Report.

The data exists but not in the shape the reports need. Trucks cross city lines in a day, so a load of mixed residential trash weighed at the transfer station must be split across the jurisdictions whose stops it collected. Scale tickets live in the scale-house system, customer counts in billing, complaints in the CRM, and route reviews on auditors' tablets or paper. A contract manager or analyst rebuilds each report by exporting, allocating tonnage by stop counts or estimated set-out weights, reconciling, and pasting into the city's template. Errors surface as audit findings, disputed franchise fees and, at renewal, as a record the city's consultant uses against the incumbent.

## What Already Exists
Business intelligence tools (Power BI, Tableau) on top of the billing and scale systems; hauler platforms' standard reports (Routeware, AMCS, Soft-Pak); Re-TRAC Connect and state portals where jurisdictions submit recycling data; and SB 1383 implementation record tools published by CalRecycle.

## The Customisation Gap
Generic BI answers questions about the hauler's own business; franchise reporting answers each city's questions in each city's definitions. The industry-specific layer is: tagging every stop and therefore every lift to a jurisdiction and service level; allocating shared-load tonnage to jurisdictions by a documented method a city auditor will accept; mapping the hauler's material streams to each contract's diversion definition (whether organics delivered to an anaerobic digester counts, whether residue from the recycling facility is deducted); computing franchise fees on the contract's definition of gross receipts; keeping SB 1383 route-review evidence in the record structure 14 CCR 18984.6 expects; and filling each city's template, including the free-text explanations of service failures. Today that layer is a contract manager's spreadsheet, rebuilt every reporting period.

## Impact If Solved
A regional hauler spending ~2–3 analyst-days per contract per month on 25 contracts uses ~400–600 hours a month (estimate); generating reports from jurisdiction-tagged stop data cuts most of that and turns the franchise-renewal record from a liability into evidence of performance.
