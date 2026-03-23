# Maintenance Scheduling Disconnected from Route Assignment

**Niche:** [[niches/fleet-managers/last-mile-delivery-fleets/profile|Last-Mile Delivery Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Fix (Pain Point)
**One-liner:** The maintenance scheduler doesn't know which vehicles are assigned to tomorrow's routes, and the route planner doesn't know which vehicles are due for service — so vehicles get scheduled for routes and maintenance on the same day.
**Tags:** #workflow-orchestration #data-integration #automation #worker-facing

## The Problem
A delivery fleet manager uses Fleetio to schedule preventive maintenance and OptimoRoute to assign vehicles to delivery routes. Neither system talks to the other. Result: Vehicle #47 is due for an oil change on Tuesday, but it's also assigned to a 120-stop delivery route on Tuesday because the dispatcher didn't check Fleetio. The maintenance gets deferred (again), the oil change interval is exceeded, and the engine warranty is jeopardized. Alternatively, the vehicle goes to the shop and 120 packages go undelivered because a replacement vehicle wasn't pre-assigned to the route.

## Why It's Still Broken
Fleet management tools and routing tools are built by different vendors for different buyers (fleet manager vs. dispatch/logistics). They share no data, no API integrations, and no common vehicle identifier beyond the VIN. The fleet manager maintains a mental or spreadsheet-based "availability calendar" that bridges the two systems — a manual process that breaks down at scale (50+ vehicles) and during peak seasons when every vehicle is needed.

## What a Fix Looks Like
A bidirectional integration between the maintenance management system and the route planning system. When Fleetio schedules Vehicle #47 for service on Tuesday, OptimoRoute automatically marks it unavailable and re-assigns its route to a spare vehicle. When OptimoRoute assigns a vehicle to a critical route, Fleetio defers non-urgent maintenance to the next available day. Conflicts are surfaced to the fleet manager with recommendations rather than discovered at 6 AM when the vehicle is needed.

## Who Feels the Pain
Fleet managers who spend 30-60 minutes every morning cross-referencing maintenance schedules against route assignments, and dispatchers who discover vehicle unavailability after routes are already assigned.

## Impact If Fixed
Eliminates 30-60 minutes of daily manual cross-referencing, prevents 3-5 missed maintenance events per month (protecting warranty coverage and reducing breakdown risk), and avoids 1-2 route disruptions per month caused by vehicles unexpectedly going to the shop.
