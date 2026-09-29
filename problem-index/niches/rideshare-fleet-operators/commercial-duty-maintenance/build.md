# Build: Duty-Cycle Maintenance Intervals and Failure Prediction

**Niche:** [[niches/rideshare-fleet-operators/commercial-duty-maintenance/profile|Maintenance for Commercial-Duty Vehicles]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Schedule maintenance against actual duty cycle from telematics rather than odometer readings, and predict the failures that idle a vehicle from the fleet's own repair history.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #feature-engineering #automation #revenue-impact
**Contested on:** Whether a fleet's own repair history is large enough to predict the failures that matter.

## The Problem

Maintenance scheduling by odometer treats all miles as equivalent. They are not. A rideshare vehicle accumulates engine hours far out of proportion to distance because of idling, cycles its brakes an order of magnitude more often than a commuter car per mile, runs its transmission through constant low-speed shifting, and frequently never reaches full operating temperature on short urban trips.

The result is predictable and expensive: brakes, transmissions, suspension components and batteries fail earlier than the schedule anticipates, and they fail while the vehicle is out with a driver, which turns a planned service into a roadside event, a tow, a driver with no income and a week of idle days.

Meanwhile some services are performed early because the odometer says so, on a vehicle whose actual duty has been light.

## Why Nobody Has Built This

Fleet operators are small and maintenance is a cost to be minimised rather than a system to be optimised. The prevailing approach is a reasonable one for a small operation: follow the manufacturer's schedule, shorten it somewhat because everyone knows these vehicles work hard, and deal with failures as they come.

The data that would improve it is present but unjoined. Telematics holds the duty-cycle signal — engine hours, idle fraction, braking events, trip lengths, temperature cycles — and is consumed as a location and safety product. Repair history sits in invoices from a garage, often on paper or in a different system, with no structured record of what failed and at what mileage and duty.

And a single fleet's failure history feels too small to model, which is a real concern for rare failures and a poor excuse for the common ones. A two-hundred-vehicle fleet over three years generates hundreds of brake jobs and dozens of transmission events — enough for the failures that actually drive the cost.

## What to Build

A duty-cycle model driving intervals, and a failure model driving interventions.

**Build the duty-cycle index.** Per vehicle, from telematics: engine hours against distance, idle fraction, braking events per mile and their severity, average trip length, cold-start frequency, ambient and coolant temperature cycles, and load proxies. This converts an odometer reading into an effective wear measure, and the conversion factor differs by component — brakes care about stop events, the engine cares about hours and cold starts, the transmission about shift cycles.

**Set intervals against effective wear** rather than distance, per component. The manufacturer's schedule becomes a baseline scaled by the duty index, which typically shortens brake and fluid intervals substantially while leaving some others alone. Validate against the fleet's own failure record: if brakes are failing at 70% of the scheduled interval, the schedule is wrong and the data says by how much.

**Structure the repair history.** Every invoice becomes a record: vehicle, date, mileage, duty index at the time, component, failure or scheduled, parts, labour, and — crucially — idle days caused. Most fleets have three years of this in paper form and it is the dataset the whole exercise depends on. Digitising it is the unglamorous first step and it is worth doing before any modelling.

**Predict the failures that idle vehicles.** Survival modelling per component with duty-cycle covariates, plus diagnostic trouble code patterns, which are strongly predictive and currently triaged by whoever notices them. The target is not all failures but roadside failures — the ones that strand a driver and cost days rather than hours.

**Optimise the timing against the idle cost.** The decision is not merely when a component will fail but when servicing it is cheapest, which depends on the predicted turnover gap. Pulling a brake job into a vehicle's already-idle handover window costs nothing in downtime; doing it while a driver is earning costs a day. Joining the failure forecast to the churn forecast is what makes this operationally valuable.

## Target Customer

Fleet operators above the scale where maintenance is a meaningful cost centre, and the independent garages and mobile mechanics serving them, for whom duty-aware scheduling is a service differentiator. Also telematics and fleet software vendors, for whom commercial-duty interval modelling is an obvious extension of data they already collect.

## Impact If Built

Failures move from the roadside to the workshop, which is where the idle-day cost is made or lost. Intervals reflect how the vehicle is actually used rather than how a private owner would use it. And the fleet stops relearning each model's weak points by experiencing them, because the repair history becomes a dataset instead of a drawer of invoices.
