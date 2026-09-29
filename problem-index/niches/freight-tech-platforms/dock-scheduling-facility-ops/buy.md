# Appointment Scheduling Against Real Capacity

**Niche:** [[niches/freight-tech-platforms/dock-scheduling-facility-ops/profile|Dock Scheduling & Facility Operations]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Appointment scheduling against constrained resources is a solved problem in healthcare and in every service industry, and distribution centres allocate dock slots from a fixed grid that has no relationship to the labour actually on shift.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor in dock scheduling is fighting to let a carrier book an appointment at any facility without learning that facility's system — and whoever makes booking work across an incompatible estate takes the network.

## The Problem
A facility publishes appointment slots in a grid: eight doors, hourly slots, six in the morning to six in the evening. The grid does not know that Tuesday afternoon has two fewer forklift operators, that a floor-loaded container takes three hours while a palletised trailer takes forty minutes, or that four of the eight doors are occupied by a cross-dock operation until eleven. So the calendar fills, the floor is overwhelmed at ten and idle at three, trucks wait, and the facility concludes it needs more doors.

## What Already Exists
Capacity-aware appointment scheduling is mature in healthcare — clinic and operating theatre scheduling against staff and room constraints is a well-developed discipline with published methods and commercial systems — and in field service. Constraint solvers handle this problem size instantly. Warehouse labour management systems already hold shift schedules and productivity standards. Service time estimation from historical data is ordinary. Every component is purchasable and most are already inside the building.

## The Customization Gap
The adaptation is to the dock's actual constraints. It requires: (1) service time predicted per appointment from the freight's characteristics — floor-loaded versus palletised, case count, whether it needs sorting or inspection — rather than a uniform slot, since service time variance is the dominant factor and the grid ignores it entirely; (2) labour capacity by shift as a hard constraint, connected to the labour management system the facility already runs; (3) door compatibility and equipment constraints, because not every door serves every freight type and the grid pretends otherwise; (4) arrival uncertainty modelled explicitly, since a truck's arrival is a distribution and a schedule built on point arrivals fails at the first delay — this is where the visibility data belongs and is the most valuable available integration; and (5) an overbooking policy derived from measured no-show rates, which is exactly what airlines and clinics do and which facilities currently approximate by frustration.

## Target Customer
Distribution centres, manufacturing plants and warehouses running appointment systems, and the dock scheduling vendors whose products are grids.

## Impact If Solved
Capacity-aware scheduling smooths the floor's workload without adding doors or labour, which is the facility's own strongest incentive and the one that gets this bought. It also reduces the detention that carriers are currently charging for, so the improvement lands on both sides — which is the argument that makes the interoperability in the build note reachable.
