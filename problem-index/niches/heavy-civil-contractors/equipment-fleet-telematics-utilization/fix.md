# Machine Hours Typed by Foremen

**Niche:** [[niches/heavy-civil-contractors/equipment-fleet-telematics-utilization/profile|Equipment Fleet Telematics & Utilisation]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** The machine reports its own hours every few minutes, and the foreman still types them into the time card at the end of the shift, by memory.
**Tags:** #k-means-clustering #feature-engineering #data-integration #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn mixed-OEM telematics into equipment hours posted to job cost codes and hourly rates estimators bid with, and the vendor whose posted hours and rates match audited job cost most closely takes the account.

## The Problem
Typed hours are rounded, charged to the wrong code and include idle time. Job cost and the equipment record disagree with the telematics.

## Why It's Still Broken
Telematics knows the machine and location, not the cost code; the field app knows the code, not the hours.

## What a Fix Looks Like
Telematics hours pre-filled on the foreman's card, split by the codes active in that area that day, with idle shown separately; the foreman only confirms the split.

## Who Feels the Pain
Foremen doing paperwork after a shift, equipment managers reconciling meters, and estimators using the actuals.

## Impact If Fixed
If equipment entry drops to a confirmation (estimate: ~10–15 minutes saved per foreman per day), records match the machines and idle hours become visible.
