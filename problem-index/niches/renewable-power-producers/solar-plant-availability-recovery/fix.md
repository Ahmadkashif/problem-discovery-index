# Trackers Stuck Flat That Nobody Sees

**Niche:** [[niches/renewable-power-producers/solar-plant-availability-recovery/profile|Solar Plant Availability & Underperformance Recovery]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Fix (Pain Point)
**One-liner:** A tracker row that stops following the sun loses output every morning and evening without tripping anything, and is found weeks later in a monthly performance review or by a technician driving past.
**Tags:** #change-point-detection #descriptive-statistics #feature-engineering #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to find and fix the inverters, trackers and strings that drag a plant below its expected output, and whoever has the smallest energy-based availability loss across a fleet takes the account.

## The Problem
Single-axis trackers can stall, lose communications or sit in stow after wind events. The inverter keeps producing, just less, so no alarm fires. Tracker angle data sit in the tracker vendor's portal, apart from the production data.

## Why It's Still Broken
Tracker controllers report to their own systems, monitoring platforms rarely ingest commanded versus actual angle, and losses spread across shoulders of the day look like weather.

## What a Fix Looks Like
Pull actual and commanded tracker angles into the same store as inverter output, flag any row whose angle departs from the sun-tracking schedule or from its neighbours, estimate the lost energy, and send a ranked list to the crew each morning.

## Who Feels the Pain
Performance engineers explaining shortfalls; O&M crews finding stalled rows by chance; owners losing output with no alarm.

## Impact If Fixed
At a 300 MW site where ~2% of rows misbehave at any time and lose ~10% of their output (estimate), catching them within a day recovers ~0.2% of plant output, ~1,300 MWh or ~$60K a year at a ~25% capacity factor and $45/MWh.
