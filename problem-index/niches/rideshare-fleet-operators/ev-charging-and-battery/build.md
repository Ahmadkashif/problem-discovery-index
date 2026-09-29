# Build: Degradation and Residual Modelling for Commercial-Duty EVs

**Niche:** [[niches/rideshare-fleet-operators/ev-charging-and-battery/profile|EV Transition, Charging & Battery]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model battery degradation under rideshare duty from charging and thermal telemetry, and turn it into the residual value assumption the fleet's capital model depends on.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #feature-engineering
**Contested on:** Whether degradation under high-mileage commercial duty can be projected from a few years of data on vehicles that have not aged yet.

## The Problem

A fleet buying EVs is making a five-year capital commitment against a residual value nobody can estimate. The vehicle will do 50,000 to 70,000 miles a year, largely on DC fast charging, in a thermal and cycling regime quite unlike the private ownership from which all the degradation data comes.

Every term in the fleet's model depends on where the battery ends up. Residual value at resale is dominated by remaining capacity. Whether the vehicle can complete a driver's shift without a mid-day charge depends on retained range, and the day it cannot is the day the rental rate has to fall. Warranty coverage has a capacity threshold, and whether the fleet crosses it before the term expires is a material financial question.

Fleets are guessing all of this, and the guesses sit underneath the rate card, the financing and the purchase decision.

## Why Nobody Has Built This

The data is young. High-mileage commercial EV duty at scale is recent, so there is no five-year record at this cycling intensity to fit against, and the manufacturer literature reflects consumer patterns.

The telemetry is also fragmented and partly closed. Battery management systems compute state-of-health internally; what they expose varies by manufacturer, and the exposed value is itself a model output with unknown properties rather than a measurement. Getting at the underlying signals — charge and discharge curves, cell balance behaviour, temperature under fast charge — requires manufacturer cooperation or careful inference.

And fleets are small buyers individually. The party with the data volume to model this is either a large fleet, a charging network, or a consortium, and none has taken it on.

## What to Build

A degradation and residual model fitted on operational telemetry, with honest uncertainty.

**Instrument the duty cycle.** Per vehicle: charge sessions with rate, start and end state of charge, duration and temperature; depth of discharge distribution; energy throughput cumulatively; ambient and pack temperature; fast-charge fraction; and time spent at high or low state of charge. These are the variables the degradation literature identifies and they are all available from EV telematics.

**Model capacity as a trajectory, not a point.** Fit capacity fade against cumulative energy throughput and the stress covariates, with a hierarchical structure so each vehicle's trajectory borrows strength from the fleet while retaining its own level. Bayesian estimation is the right approach here specifically because the data is short and the extrapolation is long — the honest output is a widening band, and a point estimate would be dishonest.

**Validate against what can be measured.** Periodic controlled capacity checks — a full charge under known conditions — give a cleaner capacity measure than the BMS estimate and are cheap to run during turnover gaps. A few per vehicle per year anchors the model properly.

**Project residual value.** Resale price as a function of mileage, age and retained capacity, fitted against actual disposals plus market listing data. This is the number the capital model needs and it is currently a manufacturer's assumption applied to a duty cycle it does not describe.

**Turn it into operational decisions.** When a vehicle's range no longer supports a full shift, it should move to a shorter-shift renter or a different class, and the rate should change — knowing that date in advance rather than discovering it through driver complaints is worth real money. Likewise, identifying which charging behaviours accelerate degradation lets the operator price or steer them, since a driver who fast-charges to 100% daily is depleting the operator's asset.

**Watch the warranty threshold.** Whether each vehicle will cross the capacity floor within the warranty term is directly computable from the trajectory model and is a claim worth several thousand dollars per vehicle if made in time.

## Target Customer

Fleet operators and the lessors and lenders financing EV fleets, who are currently underwriting residual values they cannot defend. Also charging networks with fleet relationships, who hold much of the session data, and insurers pricing EV fleet risk.

## Impact If Built

The largest uncertain number in an EV fleet's capital model acquires an evidence base and an honest error band. Vehicles get moved to appropriate duty before drivers discover the range problem. Charging behaviour that destroys the asset becomes visible and priceable. And warranty claims get made while they are still claimable.
