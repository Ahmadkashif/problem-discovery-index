# Seasonal Protocol Drift

**Niche:** [[niches/pest-control/residential-recurring/profile|General Residential Pest Programs]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians are supposed to adjust treatment protocols seasonally, but without system-enforced protocol changes, they apply the same products year-round.
**Tags:** #automation #compliance #worker-facing

## The Problem
Residential pest control requires seasonal protocol adjustments: spring treatment emphasizes ant and spider control, summer focuses on mosquitoes and stinging insects, fall shifts to rodent exclusion, winter addresses overwintering pests. Treatment protocols should specify different products, application areas, and techniques for each season. In practice, technicians develop habits and apply the same products the same way regardless of season. A tech who's been doing "spray the perimeter with Demand CS" since March is still doing it in October when the protocol calls for rodent bait station servicing and exclusion work.

## Why It's Still Broken
Protocol changes are communicated in team meetings or memos that technicians forget by afternoon. The scheduling system shows "Quarterly Service — Smith Residence" with no protocol details. Product selection is at the technician's discretion (they grab what's on the truck), and supervisors only catch protocol drift during occasional ride-alongs. There's no system that changes the work order template based on the date/season and enforces product/technique selection at the point of service.

## What a Fix Looks Like
Seasonal protocol enforcement in the mobile work order: when a technician opens a job, the system displays the current seasonal protocol (products, application areas, techniques, inspection focus areas) and requires the tech to confirm or document deviations. Product selection auto-populates from the seasonal protocol. Supervisors see a dashboard showing protocol adherence rates by technician, flagging those who deviate from seasonal standards.

## Who Feels the Pain
Service managers who discover during October ride-alongs that technicians have been applying spring protocols for 6 months, and customers who experience breakthrough pest activity because treatments weren't adjusted for seasonal pest pressure changes.

## Impact If Fixed
Proper seasonal protocols reduce callback rates by 15-25% (because treatments target the actual seasonal pest pressure), improving customer satisfaction and reducing the cost of free re-service visits.
