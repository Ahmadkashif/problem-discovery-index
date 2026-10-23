# One Fuel Record Behind Every Emissions Report

**Niche:** [[niches/ocean-shipping-carriers/emissions-monitoring-reporting/profile|Emissions Monitoring, Reporting & Verification]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same fuel figures feed four regulatory regimes and three commercial parties, and each copy is reconciled by hand before the verifier sees it.
**Tags:** #gaussian-processes #large-language-models #feature-engineering #evaluation-metrics #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a fleet's noon reports and fuel records into emissions figures a verifier accepts before 31 March, and whoever gets the most ships' reports verified with no corrections takes the account.

## The Problem
A ship's fuel consumption per voyage drives the EU MRV report, the ETS allowance bill, the FuelEU compliance balance and the IMO DCS figure. It also drives the charterer's performance claim and the owner's bunker accounts. Each is compiled from noon reports, bunker delivery notes and tank soundings, and each compiler fixes discrepancies their own way. Verifiers then find voyages split wrongly between EU and non-EU legs, fuel figures that do not reconcile with deliveries, and emission factors applied to the wrong fuel batch.

## Why Nobody Has Built This
Emissions platforms grew out of performance monitoring, where approximate figures were fine. The regulated figure needs a fuel ledger by batch and voyage leg that survives audit, and building it means reconciling messy shipboard data rather than drawing dashboards.

## What to Build
A per-ship fuel ledger built from bunker deliveries, tank movements and daily consumption, with every figure traced to a source document. Voyage legs are classified automatically under EU ETS and FuelEU rules from port calls, and a weather-corrected consumption model flags implausible days. Every regime's report and every commercial format is generated from the one ledger. A verifier-ready pack is assembled before the 31 March deadline.

## Target Customer
Fleet performance and decarbonisation managers at owners, operators and third-party ship managers trading to EU ports.

## Impact If Built
Take a ship with ~20,000 tonnes of in-scope CO2 a year (estimate). A 2% fuel-reporting error there is ~400 allowances, ~€28,000 at ~€70 each (estimate), before verifier corrections and rework. Compliance cost becomes a forecast per voyage rather than a year-end surprise.
