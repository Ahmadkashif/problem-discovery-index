# Build: Cure Prediction and Expected-Value Collections

**Niche:** [[niches/rideshare-fleet-operators/collections-and-recovery/profile|Collections & Vehicle Recovery]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict which arrears will cure on their own, and choose between forbearance, disablement and recovery on expected value rather than on the day of the month.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #monte-carlo-methods #revenue-impact #automation
**Contested on:** Whether the probability an arrears cures can be estimated well enough to decide against recovering the vehicle.

## The Problem

An operator's collections decision is between three actions with very different economics. Forbearance costs the arrears if the driver never recovers and costs nothing if they do. Disablement stops the driver earning, which guarantees they cannot pay this week and pressures them to find money elsewhere. Recovery ends the relationship, costs a recovery fee, produces idle days and a vehicle that may be damaged, and writes off the balance.

The right choice depends almost entirely on the probability that the driver recovers, which varies enormously — a driver with eighteen months of perfect payments who missed one week after an illness is a different proposition from a driver three months in whose hours have been declining. The operator treats them identically because the sequence is a calendar.

## Why Nobody Has Built This

Collections in a small fleet is triage under pressure, done by someone with forty other things to do, and a rule of thumb that escalates at fixed intervals is a defensible way to handle that. It also feels safer: the cost of forbearance that fails is visible and attributable, while the cost of recovering someone who would have recovered is invisible.

The data has never been assembled. Arrears episodes with their outcomes — cured, partially cured, written off, recovered — sit in payment records and nobody has structured them into an episode-level dataset. Without that there is nothing to learn from, and the sequence persists because there is no evidence against it.

And the disablement decision in particular has never been evaluated. Starter interrupt is deployed widely on the theory that it improves payment behaviour, and almost no operator has measured whether it does — including the obvious mechanism by which it cannot, since a disabled driver cannot earn the money.

## What to Build

An arrears model and a decision rule, both fitted on the fleet's own history.

**Structure the arrears episodes.** Each one: driver, tenure, payment history before the episode, arrears amount and age, telematics before and during (hours, utilisation trend), any communication, the interventions applied and when, and the outcome with the amount ultimately recovered and the vehicle's condition and idle days. A fleet with a few years of operation has hundreds of these and they are the dataset.

**Predict cure.** Probability the arrears is fully paid within a horizon, as a function of the covariates. Survival framing is natural since the timing matters as much as the outcome. The strongest signals are likely to be pre-episode payment consistency, tenure, and the telematics trend during the episode — a driver still working full hours is in a different position from one whose vehicle has not moved in four days, and the second is nearly always the more serious sign.

**Attach values to the actions.** Forbearance: expected recovery given cure probability, minus the carrying cost of continued exposure. Disablement: the effect on cure probability, which must be estimated honestly and may well be negative, plus the pressure effect on drivers with other resources. Recovery: recovery fee, expected idle days, vehicle condition, remaining balance recoverable, and the replacement renter's expected value. Choose the action with the highest expected value, with the model's uncertainty carried through.

**Separate the market case.** When many arrears open at once, the cure model's driver-level features are misleading — the driver has not changed, the market has. The decision rule needs a market-state input, and in a market-wide event the right action is almost always repricing the cohort rather than recovering vehicles into a soft market where the next renter will face the same conditions.

**Measure what the interventions do.** Where practice varies naturally — different staff, different periods, different thresholds — there is enough variation to estimate intervention effects. The disablement question in particular is worth answering properly, because the answer determines whether a widely-deployed and legally fraught tool is doing anything.

## Target Customer

Fleet operators above the scale where collections is a role rather than a task, and the lenders financing them, who bear the loss given default and currently have no view of how their operators make these decisions. Also fleet management software vendors, for whom an arrears module with cure prediction is a clear differentiator.

## Impact If Built

Vehicles stop being recovered from drivers who would have recovered, which is the largest avoidable loss in the collections function. Forbearance becomes a priced decision rather than an act of optimism. The market-wide case gets recognised as such and answered with pricing. And the operator finally learns whether starter interrupt does anything, which is worth knowing given what it does to the person on the other end.
