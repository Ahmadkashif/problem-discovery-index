# Launch-Slot Risk From Subsystem and Test Data

**Niche:** [[niches/defense-systems-manufacturers/space-vehicle-manufacturing/profile|Space Vehicle & Satellite Bus Manufacturing]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A constellation contractor learns a vehicle will miss its launch slot when integration stalls, though the signals were in supplier deliveries and early test data months before.
**Tags:** #survival-analysis #gradient-boosting #monte-carlo-methods #autoencoders #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver space vehicles to their contracted launch slots, and whoever ships the highest share of vehicles to their slot takes the account.

## The Problem
Each vehicle in a tranche moves through subsystem delivery, bus integration, payload integration and environmental test (vibration, acoustic, thermal vacuum) before shipping to the launch site. A late optical terminal or a thermal-vacuum anomaly cascades through every vehicle behind it. Programme managers track readiness in spreadsheets and learn of slips late, when the only recovery is reshuffling vehicles between launches.

## Why Nobody Has Built This
Proliferated production is new; most space factories were built for one-off satellites where schedule risk was managed by experienced integrators. The data sit in supplier portals, MES and test systems, and launch manifests belong to the customer and launch provider.

## What to Build
A per-tranche model that scores every open subsystem order by the supplier's delivery record and ramp status, simulates vehicle flow through integration and test stations with demonstrated durations and anomaly rates, and ranks each vehicle's probability of making its slot. Test anomalies are matched against past vehicles to estimate rework time.

## Target Customer
Programme directors and production VPs at constellation bus makers and primes on fixed-price space contracts.

## Impact If Built
Seeing a slot miss two months earlier lets a programme reorder vehicles, expedite a subsystem or negotiate a manifest swap instead of paying for a missed launch. On fixed-price work, avoided rework and slip penalties go straight to margin.
