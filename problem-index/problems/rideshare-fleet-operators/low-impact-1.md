# Maintenance Scheduling for Commercial-Intensity Use

**Industry:** [[rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Vehicles doing forty thousand miles a year in stop-start city service are maintained on schedules designed for private owners doing ten.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #change-point-detection #confidence-intervals #evaluation-metrics #feature-engineering #automation

## The Problem
A rideshare vehicle accumulates mileage at three or four times the rate of a private car, in the duty cycle that wears components fastest — constant stopping, idling, short trips, heavy urban use, frequently with a driver who is not the owner and has no incentive to report a developing noise.

Manufacturer service intervals assume private use. Following them in commercial service means components fail between services; ignoring them means over-maintaining a fleet on a cost line that is already thin. Operators mostly land on a rule of thumb — a fixed mileage interval — that is wrong in both directions for different components.

Downtime is the real cost. A vehicle off the road earns nothing, still depreciates, still carries insurance, and the driver renting it either gets a substitute or loses their income and possibly leaves. A breakdown mid-shift is worse than a scheduled service by a large multiple, so the entire point of maintenance planning is converting unplanned failures into planned ones.

Electric vehicles have changed the failure profile rather than removed it. Fewer mechanical components and more dependence on battery condition, charging behaviour and thermal management, with degradation that is the vehicle's main depreciation driver and is affected by how it is charged and driven.

## What Already Exists
Telematics platforms — Samsara, Motive, Geotab — provide diagnostic trouble codes, mileage, engine hours and driving behaviour, with maintenance scheduling modules. Manufacturer connected-car data is available in some programmes. Predictive maintenance is a mature field in heavy trucking and commercial fleets with substantial vendor offerings. Independent repair networks and fleet service agreements handle execution. Battery state-of-health monitoring is available on most electric vehicles and is inconsistently exposed to fleet operators.

## The Customisation Gap
The available tooling is built for larger commercial fleets with uniform vehicles and controlled drivers, and rideshare fleets are the opposite — mixed vehicles, many drivers per vehicle over time, uncontrolled duty cycles and no in-house workshop. Failure models transferred from trucking do not describe this population.

Duty cycle is the informative variable nobody uses. Two vehicles at the same mileage have very different remaining component life depending on stop frequency, idle proportion, acceleration profile, terrain and load, and telematics captures all of it. Component-level survival models conditioned on actual duty cycle rather than on odometer reading are the right formulation and are not what maintenance modules implement.

Scheduling against earnings is the second gap. The cost of downtime differs by day and hour — taking a vehicle off the road on a slow Tuesday morning is far cheaper than on a Friday night — and scheduling maintenance into predicted low-demand windows is a straightforward optimisation nobody performs.

And driver-reported symptoms need capturing. The person in the vehicle every day notices developing problems first, has no structured way to report them, and often no incentive to. A simple reporting path with an incentive attached is the cheapest diagnostic input available.

## Impact If Solved
Unplanned downtime is the largest controllable cost in a fleet business and directly removes a driver's income for its duration. Duty-cycle-conditioned survival models convert failures into scheduled services, demand-aware scheduling puts those services in the cheapest windows, and structured driver reporting adds the earliest available signal — all from telematics data operators already pay for and use as a map.
