# Range-Aware Route Assignment for Mixed ICE/EV Fleets

**Niche:** [[niches/fleet-managers/mixed-fuel-ev-fleets/profile|Mixed Fuel & EV Transition Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No routing tool assigns vehicles to routes based on whether the route is EV-feasible (range, charging availability, payload weight) or requires an ICE vehicle.
**Tags:** #reinforcement-learning #regression #tabular-ml #automation #revenue-impact

## The Problem
A delivery fleet with 40 ICE vans and 10 EVs needs to assign vehicles to routes daily. Some routes are EV-feasible (under 80 miles, flat terrain, return-to-depot midday for charging). Others require ICE (150-mile rural route, no public charging, cold weather reducing EV range by 30%). The dispatcher currently assigns EVs to "easy" urban routes by gut feel, but doesn't account for payload weight (heavy loads reduce EV range), temperature forecasts (extreme heat/cold reduces range 20-40%), or the specific EV's current battery health (a 3-year-old EV has 85% of its original range). The result: EVs run out of charge on routes, requiring ICE backup retrieval, or EVs are underutilized on short routes while ICE vehicles burn fuel on routes the EVs could handle.

## Why Nobody Has Built This
Route optimization tools (OptimoRoute, Routific) treat vehicles as interchangeable. EV range estimation requires real-time inputs (temperature, payload, battery SOH, elevation profile) that routing tools don't have. Fleet management platforms track EV battery status but don't feed it into routing decisions. The cross-domain integration between routing, telematics, weather, and battery management systems doesn't exist.

## What to Build
A vehicle-to-route assignment optimizer that evaluates each route against each available vehicle (ICE and EV), considering: route distance and elevation profile, forecasted temperature, estimated payload weight, EV battery state-of-health and current charge level, and en-route charging availability. The system assigns EVs to routes they can complete with 15%+ charge margin, assigns ICE to routes beyond EV capability, and maximizes EV utilization to reduce fuel costs.

## Target Customer
Fleet managers with 10-40% EV penetration who want to maximize EV utilization without risking stranded vehicles.

## Impact If Built
Increases EV route utilization from 60-70% to 85-95% of available EV capacity, reducing fleet fuel costs by 15-25%. Eliminates stranded-EV incidents (currently 1-3 per month per fleet) that each cost $200-$500 in retrieval and missed deliveries.
