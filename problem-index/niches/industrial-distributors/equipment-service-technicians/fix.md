# The Second Trip for the Part Nobody Loaded

**Niche:** [[niches/industrial-distributors/equipment-service-technicians/profile|Equipment Service Technicians at Pump, Compressor & Lift-Truck Dealers]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** The technician diagnoses the fault in twenty minutes, then drives back to the branch for a part that could have been on the truck.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to fix a down pump, compressor or lift truck on the first visit, and whoever sends the technician with the right diagnosis and the right parts already on the truck takes the account.

## The Problem
Truck stock is set by habit and replenished from what was used, not from what the next jobs will need. When the job needs a part outside that stock, the repair waits for a second visit, the customer waits longer, and the technician loses a slot.

## Why It's Still Broken
Dispatch assigns jobs by location and skill; parts planning happens separately in the warehouse. No one predicts parts per job at intake, because the intake note is a short complaint written by a customer service rep.

## What a Fix Looks Like
At intake, predict the likely parts for the job from the machine, its history and the complaint, and add the probable ones to the day's truck load. Track second-trip causes and adjust truck stock by technician territory and fleet mix.

## Who Feels the Pain
Field technicians losing hours to return trips, customers with machines down longer, and service managers missing contract response times.

## Impact If Fixed
Cutting second trips by ~30% (estimate) returns ~3–5 hours per technician a week and shortens customer downtime by ~1 day on every avoided trip (estimate).
