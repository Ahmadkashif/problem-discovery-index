# A Fill-and-Replace Planner for an Ageing Fleet

**Niche:** [[niches/satellite-operators/geo-meo-capacity-services/profile|GEO & MEO Capacity and Managed Services]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A GEO operator decides which contracts go on which satellite and when to order a replacement using slide decks, while the inputs — remaining fuel and component health, contracted backlog, renewal risk and the demand pipeline — sit in four systems.
**Tags:** #survival-analysis #monte-carlo-methods #gradient-boosting #time-series-forecasting #revenue-impact #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to keep a fleet of fifteen-year satellites full while capacity prices fall, but writing it out produced two contests with different winners. In video, operators fight to keep broadcasters and pay-TV platforms on established orbital neighbourhoods as channels move to IP, and the incumbent with the most dishes pointed at its slot wins. In enterprise, backhaul and government data, they fight to sell guaranteed throughput across orbits at a price that survives comparison with LEO, and whoever can quote and prove a multi-orbit SLA wins. Decomposed into contested sub-niches below.

## The Problem
Every GEO satellite is a fixed inventory with an end date. Fuel, battery and wheel health set how long it can stay; contracts set how much of it earns. When a satellite approaches end of life, the operator must decide whether to extend it (inclined-orbit operations, life-extension servicing), replace it with a new satellite ordered years ahead, or move customers to another slot or orbit. A wrong call either strands customers or orders a satellite a shrinking market can't fill.

## Why Nobody Has Built This
The data sits in separate organisations: flight dynamics owns fuel estimates, engineering owns component health, sales owns the pipeline, finance owns the backlog. Each operator does this a few times a decade per slot, so it is treated as a strategy project with consultants rather than a standing system. Vendors sell mission control and billing, not fleet economics.

## What to Build
A planner that joins, for every satellite and slot: remaining-life distributions from fuel and component-health models, contracted revenue by customer and renewal date, renewal probabilities learned from past renewals, and demand forecasts by region and service. It simulates fill and revenue under each option — extend, replace, relocate, migrate to MEO or partner LEO — with uncertainty bands, and updates as telemetry and contracts change.

## Target Customer
VP Fleet Planning and the Chief Financial Officer at GEO and MEO operators, especially those integrating acquired fleets, such as SES after Intelsat.

## Impact If Built
Replacement and extension decisions, each worth hundreds of millions of dollars (estimate), are made on a shared quantitative view rather than competing departmental slides, and customer migrations are planned before a satellite's last year rather than during it.
