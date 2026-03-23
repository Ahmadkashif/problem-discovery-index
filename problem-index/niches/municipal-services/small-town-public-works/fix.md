# Equipment Maintenance Tracking Across Shared Fleets

**Niche:** [[niches/municipal-services/small-town-public-works/profile|Small-Town Public Works]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Fix (Pain Point)
**One-liner:** Small-town public works equipment — dump trucks, loaders, mowers — breaks down mid-season because nobody tracked that the oil change was 200 hours overdue.
**Tags:** #time-series-forecasting #tabular-ml #worker-facing #automation

## The Problem
A typical small-town public works department operates 8–20 pieces of equipment: dump trucks, plow trucks, backhoes, wheel loaders, riding mowers, chainsaws, and generators. Maintenance is tracked by stickers on dashboards, notes in binders, or the superintendent's memory. Equipment is shared across crews and seasons — the dump truck that hauls gravel in summer becomes the plow truck in winter. When a piece fails mid-snowstorm because the hydraulic filter wasn't changed, the town is stranded. Parts for municipal equipment (often 15–30 years old) can take weeks to arrive, so a preventable breakdown becomes a 3-week outage.

## Why It's Still Broken
Fleet management software (Fleetio, RTA Fleet) is designed for trucking companies with full-time mechanics and hundreds of vehicles. These platforms are overkill for a department where the operator is also the mechanic. The setup requires entering detailed vehicle specs, creating maintenance schedules, and configuring alerts — a 4-hour setup process that the superintendent doesn't have time for. Meanwhile, the equipment is too diverse (trucks, heavy equipment, small engines) for any single maintenance interval to apply. Each piece has different hour/mile/calendar-based service needs.

## What a Fix Looks Like
A dead-simple mobile app where operators log hours/miles at the end of each shift by selecting the equipment from a list and entering the reading. The system auto-calculates when each piece is due for service based on manufacturer intervals (pre-loaded for common municipal equipment models). Push notifications go to the superintendent 1 week before service is due. A one-page dashboard shows fleet status: green (current), yellow (service due this week), red (overdue). Parts ordering links for common service items. No IT setup — scan the equipment's model plate to auto-populate specs.

## Who Feels the Pain
The superintendent who gets blamed when equipment fails during critical operations, and the operators who work with unreliable machines.

## Impact If Fixed
Reducing unplanned equipment failures by 50% prevents an estimated $15K–$40K annually in emergency repair costs and rental equipment. Equipment lifespan extends 20–30% with proper preventive maintenance, deferring $50K–$200K in capital replacement costs per decade.
