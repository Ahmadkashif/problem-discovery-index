# The Route Supervisor's 5 a.m. Rebuild

**Industry:** [[armored-car-services|Armored Car Services]]
**Type:** Worker Life Changing
**One-liner:** Every morning a branch route supervisor rebuilds the day's routes around crew call-outs, broken trucks and emergency ATM orders by phone and whiteboard, and a planner that knew the rules would give back the first two hours of the shift and the evenings spent on the phone.
**Tags:** #optimization-fundamentals #dynamic-programming #monte-carlo-methods #gradient-boosting #worker-facing #workflow-orchestration #automation

## The Problem
An armored branch opens before dawn. Crews check in at the vault from about 6 a.m., draw weapons and load trucks with the day's deliveries. Before that, the route supervisor has already found out who is not coming. A messenger called in sick, a driver's firearm permit lapsed, one truck failed its pre-trip check, a bank phoned in an emergency order for a branch that ran out of $20s, and two ATMs went offline overnight with "cash low" alerts.

Rebuilding the day is not just moving stops between routes. A replacement messenger must hold a weapons licence valid in every state the route crosses. A truck cannot take on more value than its limit. Customer windows are fixed: a bank branch wants its delivery before opening, a store wants pickup after the lunch rush, an ATM's service window depends on the host site's hours. Stops must not drift into a predictable pattern, and the vault needs the trucks back before the bank deposit cut-off. The supervisor holds all of this in their head, makes a dozen phone calls and starts the day already behind.

## Why It Matters to the Worker
The supervisor is usually a former messenger promoted for reliability and paid little more for it. The job is the pressure point of the branch: drivers blame them for impossible routes, customers blame them for late deliveries, and management judges them on overtime and missed windows. The phone rings in the evening and on weekends with tomorrow's problems. Many go back to driving because it is easier.

Crews feel it too. A badly rebuilt route means skipped breaks, a late return and pressure to rush stops — the moment a messenger is most likely to skip the look around that keeps them safe.

## What a Solution Looks Like
A planner that knows the branch's real rules: crew licences by state, truck value limits, customer windows and penalties, vault and Fed cut-offs, and a requirement to vary sequences and timing. At 4:30 a.m. it ingests call-outs, vehicle status, emergency orders and ATM alerts, and proposes a rebuilt plan with the reasons for each change and the customers who will be late. The supervisor adjusts and confirms; customers get updated windows automatically. Over time it learns real service times per stop from the route record, so plans stop assuming every supermarket takes ten minutes.

## Impact If Solved
Reclaiming ~1–2 hours each morning (estimate) and most of the evening calls turns the supervisor's job from firefighting into running the branch, and plans that respect real stop times and break rules take time pressure off the crews at the curb.
