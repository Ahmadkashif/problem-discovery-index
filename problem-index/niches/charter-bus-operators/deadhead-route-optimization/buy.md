# Proximity-Based Trip Assignment for Dispatch

**Niche:** [[niches/charter-bus-operators/deadhead-route-optimization/profile|Deadhead Route Optimization]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fleet dispatch tools assign trips by availability, not by bus proximity to the pickup location — adding thousands of unnecessary deadhead miles per month.
**Tags:** #automation #data-integration #workflow-orchestration #revenue-impact

## The Problem
When a dispatcher assigns a trip in BusHive or a spreadsheet, they see which buses are available at the requested time — but not where each bus will physically be at that moment. A bus might be "available" at 2pm but currently assigned to a trip ending at 1pm, 40 miles from the 2pm pickup. Another bus is available at 2pm and will be 3 miles from the pickup, but the dispatcher does not have the spatial awareness to see this without manually cross-referencing the prior trip's dropoff location with the new trip's pickup. The result: trip assignment defaults to calendar order (first available bus wins) rather than proximity order (closest bus wins).

## What Already Exists
Fleet management platforms (Samsara, Geotab, Verizon Connect) provide real-time GPS tracking of all vehicles. Dispatch tools (BusHive, Tribus) manage trip assignments and driver schedules. Delivery route optimization tools (Route4Me, OptimoRoute) optimize multi-stop routes within a single day. None of these combine GPS-based future bus positions (where will each bus be when it finishes its current assignment?) with trip assignment logic to suggest proximity-based assignments.

## The Customization Gap
Charter dispatch needs a proximity prediction layer that calculates each bus's expected location at any future time based on its current assignment schedule, then ranks bus-trip assignments by projected deadhead distance. The system must account for bus-type compatibility (you cannot assign a 20-seat minibus to a 50-person trip), driver qualifications, and schedule flexibility (can a trip start 15 minutes later to allow the closer bus to finish its current assignment?). A simple heat map showing bus positions over time against upcoming trip pickups would transform dispatch decision-making.

## Target Customer
Dispatchers at operators with 6+ buses who currently make 10-30 trip assignment decisions per day using availability-first, not proximity-first, logic.

## Impact If Solved
Reduces daily deadhead miles by 15-25% per fleet through proximity-aware assignments, saving $30K-$80K annually for a 10-15 bus operator — achievable with a relatively simple GPS data integration into the dispatch workflow.
