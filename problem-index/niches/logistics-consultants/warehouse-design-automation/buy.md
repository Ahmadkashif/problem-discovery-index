# Discrete-Event Simulation Adapted to Vendor-Neutral Automation Selection

**Niche:** [[niches/logistics-consultants/warehouse-design-automation/profile|Warehouse Design & Automation Advisory]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Simulation software can model any warehouse system; selecting between five vendors' proposals needs the same client order profile replayed through each, with ramp-up and bid terms normalised.
**Tags:** #monte-carlo-methods #probability-distributions #feature-engineering #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to predict the throughput a redesigned or automated building will actually reach on the client's own order profile, and whoever's projections hold at go-live wins the next site.

## The Problem
Each automation vendor returns a proposal with its own simulation, run on a design-day profile it selected, with its own assumptions about order release, replenishment and operator rates. Comparing them means rebuilding each concept in a common simulation, which takes weeks per vendor, so most selections compare vendor numbers that were never produced on the same basis.

## What Already Exists
FlexSim, AnyLogic and Simio — general discrete-event simulation platforms with warehouse object libraries, used by consultants and vendors alike.

## The Customization Gap
The adaptation needs: a standard client order-profile package (peak day, peak hour, growth years, SKU and cube distributions) that every model consumes identically; parameterised templates for common system types so a vendor concept is configured rather than built; ramp-up curves applied consistently; a bid normalisation layer that aligns scope, software, spares, service and throughput guarantees across proposals; and side-by-side output a steering committee can read.

## Target Customer
Automation consultancies running vendor selections, and owners' engineering teams buying their first or second automated system.

## Impact If Solved
Vendor proposals are compared on the client's operation rather than the vendor's demonstration, and a selection that took ~8–12 weeks of modelling (estimate) takes a fraction of that.
