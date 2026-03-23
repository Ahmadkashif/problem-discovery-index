# Water and Supply Capacity Planning

**Niche:** [[niches/pet-services/mobile-grooming/profile|Mobile Pet Grooming]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Fix (Pain Point)
**One-liner:** Mobile groomers carry limited water (40-65 gallons per tank) and supplies, but have no tool to estimate daily consumption based on the day's appointment mix — leading to mid-day refill trips or skipped appointments.
**Tags:** #regression #tabular-ml #automation #worker-facing

## The Problem
A mobile grooming van carries 40-65 gallons of fresh water and 40-65 gallons of grey water tank capacity. A bath for a small dog uses 5-8 gallons; a large, thick-coated dog uses 15-25 gallons. A groomer with 6 appointments doesn't calculate total water needs in advance — they discover they're running low after the 4th appointment, forcing either a 20-30 minute refill detour or a conversation with the 5th client about rescheduling. Shampoo, conditioner, and other supplies run out unpredictably for the same reason: no consumption forecasting based on the day's specific appointment mix.

## Why It's Still Broken
Groomers mentally estimate water usage ("I can do about 6 dogs on a tank") without accounting for the breed mix. A day with 3 Golden Retrievers uses dramatically more water than a day with 3 Chihuahuas. The mental model fails on atypical days. Supply ordering is similarly reactive — groomers order when they run out, not when they project they'll run out. No scheduling tool accounts for resource constraints because resource tracking isn't connected to the appointment calendar.

## What a Fix Looks Like
A capacity planning layer integrated with the grooming scheduler that estimates water and supply consumption per appointment (based on breed, size, coat condition, and groom type), projects daily totals, and warns when the day's appointments will exceed tank capacity. The system suggests which appointment to move (the one that's geographically closest to a refill point, or the one that could shift to the next day) when capacity is tight. Over time, actual consumption data (logged at end of day) refines the estimates.

## Who Feels the Pain
Mobile groomers who make 1-2 unplanned refill trips per week (wasting 30-60 minutes each), or who turn away a same-day booking request because they're not sure they have enough water to add another dog.

## Impact If Fixed
Eliminates 1-2 wasted refill trips per week (saving 30-60 minutes and $10-20 in water/fuel), enables confident same-day booking for dogs that fit within remaining capacity, and reduces the stress of guessing whether supplies will last the day.
