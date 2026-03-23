# EV Charging Scheduling Conflicts at Shared Depot Chargers

**Niche:** [[niches/fleet-managers/mixed-fuel-ev-fleets/profile|Mixed Fuel & EV Transition Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Fleets with 10 EVs and 4 depot chargers have nightly scheduling conflicts — vehicles queue for chargers, some don't reach full charge by morning, and nobody optimizes the charging sequence.
**Tags:** #reinforcement-learning #workflow-orchestration #automation #worker-facing

## The Problem
A fleet depot has 10 EVs and 4 Level 2 chargers. All 10 vehicles return between 4-6 PM and need full charges by 6 AM. With 4 chargers doing 8-10 hours per full charge, only 4 vehicles charge overnight — the other 6 need someone to swap cables at 2 AM (which doesn't happen) or accept partial charges. The fleet manager tries to stagger departure times so some vehicles leave later and charge during the day, but this conflicts with route schedules. Nobody optimizes which vehicles charge first (vehicles with tomorrow's longest routes should charge first), when to swap cables, or how to use time-of-use electricity pricing to minimize costs.

## Why It's Still Broken
Charging station management platforms (ChargePoint, Blink) manage individual charging sessions but don't understand fleet operations — they don't know which vehicle has tomorrow's longest route or when each vehicle needs to depart. Fleet management platforms don't manage charging infrastructure. The overnight charging sequence is managed by whoever parks the vehicles (usually drivers), with no optimization and no accountability for the charging order.

## What a Fix Looks Like
A depot charging scheduler that takes tomorrow's route assignments (route length, departure time, required charge level), current battery states for each vehicle, and charger availability, then produces an optimal charging sequence: "Vehicle #3 plugs in first at Charger A (departure 5:30 AM, 150-mile route). Vehicle #7 plugs in at Charger B (departure 7:00 AM, 120-mile route). At 1:00 AM, swap Vehicle #3 to Charger C and plug in Vehicle #12." It also considers time-of-use electricity rates to minimize charging costs by shifting non-urgent charges to off-peak hours.

## Who Feels the Pain
Fleet managers whose EV drivers depart with insufficient charge 2-3 times per week, causing route disruptions, public charging stops ($0.40-$0.60/kWh vs. $0.12/kWh depot rate), and driver frustration.

## Impact If Fixed
Ensures 95%+ of EVs depart fully charged (up from 60-70%), eliminates 2-3 weekly partial-charge incidents, reduces electricity costs by 15-20% through time-of-use optimization, and prevents $400-$800/month in expensive public charging that drivers use when their depot charge is insufficient.
