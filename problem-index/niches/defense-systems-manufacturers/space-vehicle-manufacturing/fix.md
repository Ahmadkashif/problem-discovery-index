# The Subsystem Late to Integration

**Niche:** [[niches/defense-systems-manufacturers/space-vehicle-manufacturing/profile|Space Vehicle & Satellite Bus Manufacturing]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** Subsystem suppliers report "on track" until the week a unit is due, and the integration team finds out at the dock.
**Tags:** #survival-analysis #large-language-models #evaluation-metrics #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver space vehicles to their contracted launch slots, and whoever ships the highest share of vehicles to their slot takes the account.

## The Problem
Optical terminals, encryption devices, propulsion units and payload electronics come from specialist suppliers who are scaling at the same time as the bus makers. Their status reports are self-assessed and optimistic, which is how a whole tranche slipped six months in 2024.

## Why It's Still Broken
The bus maker sees only the supplier's promised date and a colour on a status chart. The leading indicators (the supplier's own test yields, sub-tier shortages, staffing) are in the supplier's systems, and contracts rarely require sharing them.

## What a Fix Looks Like
Require a short, structured weekly feed from critical suppliers (units in test, test yield, open shortages) and score each delivery against that feed and the supplier's own record of slips. Let a language model read the free-text status notes for hedging language that has preceded past slips. Show integration managers predicted dock dates, not promised ones.

## Who Feels the Pain
Integration and test leads with idle teams and fixtures, programme managers explaining slipped launches, and customers re-planning manifests.

## Impact If Fixed
A one-to-two-month warning on a late subsystem (estimate) is enough to resequence vehicles or reserve a later slot instead of flying a launch with fewer satellites than planned.
