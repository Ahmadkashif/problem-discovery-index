# Rotation Planning That Books the Unit-Day, Not the Slot

**Niche:** [[niches/diagnostic-imaging-centers/mobile-imaging-operators/profile|Mobile Imaging Operators & Rural Shared Units]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mobile MRI's route is fixed months ahead by contract, while each host's demand varies week to week, so some unit-days run half empty and others turn patients away.
**Tags:** #time-series-forecasting #optimization-fundamentals #dynamic-programming #gradient-boosting #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep each mobile MRI, CT or PET unit scanning on the days it is parked at a host site, and whoever fills the highest share of booked unit-days with completed, paid scans takes the account.

## The Problem
An operator runs a dozen trailers on weekly rotations across 30 hosts. Host A has a three-week backlog; host B booked six patients for an eight-hour day. The rotation does not change, because nobody sees both hosts' schedules and the contract specifies days.

## Why Nobody Has Built This
Mobile imaging is a small segment, and host bookings sit in each hospital's own system, out of the operator's reach. Fleet tools route vehicles, not scanners with demand.

## What to Build
A demand forecast per host and modality from referral and booking feeds. A rotation optimiser proposes day swaps and extra days within contract terms, accounting for drive time, set-up, staff licences and maintenance windows. A shared booking view lets hosts fill unit-days against authorization windows.

## Target Customer
Mobile imaging operators running 5–50 units, and rural hospital networks sharing units.

## Impact If Built
Lifting average unit-day fill from ~70% to ~85% (estimate) adds a day or more of scanning per unit per week without buying a trailer.
