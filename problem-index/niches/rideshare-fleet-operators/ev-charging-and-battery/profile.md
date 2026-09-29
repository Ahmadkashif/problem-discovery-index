# EV Transition, Charging & Battery

**Parent Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Category:** Highly Automatable
**Contested on:** Whether an electric vehicle's economics in commercial rideshare duty can be projected accurately enough to price a rental against.

## Profile
**Market Size:** ~$420M — 7% of US rideshare fleet services, growing fastest of the eight
**Share of Parent Industry:** ~7%
**Digital Adoption:** Moderate — telemetry is abundant, the economics are unmodelled
**Target Buyer:** Fleet owners, charging partners, vehicle financiers
**Automation Potential:** Very high — battery and charging data is dense and continuous

## What Makes This a Distinct Niche

Electrification has introduced charging access and battery degradation as first-order economic variables that the industry is still learning to model. An EV in rideshare service changes every term in the fleet's calculation at once: fuel cost drops substantially, maintenance drops, acquisition cost rises, residual value is uncertain, and two entirely new variables appear — charging time, which is unpaid driver time, and battery degradation, which is the asset's depreciation in a form nobody has historical data for at this duty cycle.

The niche is distinct because the uncertainty is genuine rather than neglected. Nobody knows what a 60,000-mile-per-year rideshare EV's battery looks like at year three, because that vehicle has not existed for three years in enough numbers. Fleets are making capital commitments against it anyway.

## Current Tools & Gaps

EV telematics gives state of charge, charging sessions, energy consumed, battery temperature and, in many vehicles, state-of-health estimates. Charging networks provide session data and pricing. Some fleets have negotiated depot charging or network agreements. Vehicle manufacturers provide warranty terms on battery capacity.

The gaps are projection and allocation. Degradation under commercial duty with frequent DC fast charging is not well characterised, and manufacturer warranty thresholds are a floor rather than a forecast. Charging cost and time are borne inconsistently between operator and driver, with the time almost always falling on the driver unpaid. And residual value at high mileage with a degraded battery is the largest single number in the fleet's capital model and is essentially guessed.

## Problems
- [[niches/rideshare-fleet-operators/ev-charging-and-battery/build|🔨 Build: Degradation and Residual Modelling for Commercial-Duty EVs]]
- [[niches/rideshare-fleet-operators/ev-charging-and-battery/buy|🛒 Buy: EV Fleet and Charging Platforms Adapted to Rented Vehicles]]
- [[niches/rideshare-fleet-operators/ev-charging-and-battery/fix|🔧 Fix: Charging Time Is the Driver's, Charging Cost Is Whoever's]]
