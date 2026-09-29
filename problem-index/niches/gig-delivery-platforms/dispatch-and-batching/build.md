# Build: Courier-Realised Outcome in the Dispatch Objective

**Niche:** [[niches/gig-delivery-platforms/dispatch-and-batching/profile|Dispatch, Routing & Batching]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Put predicted courier net earnings per engaged hour into the assignment objective as a constraint, so an optimisation that improves throughput cannot silently degrade the work.
**Tags:** #convex-optimization #dynamic-programming #gradient-boosting #evaluation-metrics #confidence-intervals #markov-decision-processes #revenue-impact #worker-facing
**Contested on:** Whether courier-realised earnings can be modelled well enough to enter the assignment objective without degrading service.

## The Problem

The dispatch objective is composed of delivery time, throughput, cancellation rate and cost per delivery. Each is well instrumented and continuously improved. Courier realised earnings per engaged hour is not in it.

The result is systematic rather than occasional. An assignment that sends a courier six minutes out of their way to a merchant that runs late, for an order whose pay was set by distance to the customer rather than total distance travelled, is an excellent assignment by every metric in the objective and a poor hour for the courier. Batching amplifies it: two orders assigned together raise utilisation and throughput and frequently reduce the per-order pay while adding wait, walking and route complexity that the pay model does not capture.

Because the quantity is not in the objective it is also not in the reporting, so the degradation accumulates without anyone observing it — until it surfaces as supply shortfall in a market, which is attributed to competition or seasonality.

## Why Nobody Has Built This

The immediate reason is that supply has been elastic. When couriers leave, more arrive, so the cost of degrading courier outcomes has been diffuse and delayed while the benefit of throughput improvements is immediate and measured. Any objective term that trades measured throughput against unmeasured retention loses that argument.

The technical obstacle is real but secondary: putting realised earnings into the objective requires predicting it at assignment time, which requires the merchant-wait and engaged-time modelling that the offer prediction work supplies. Without that prediction there is nothing to optimise against. The two pieces of work are sequential, and the first has not been done.

And there is a legal shadow over it. An assignment system that manages courier earnings deliberately is exercising a kind of control that weighs in classification analysis, and platforms have been cautious about building anything that looks like managing a workforce's pay outcomes.

## What to Build

Add a courier-outcome term to the assignment objective and instrument it as a first-class metric.

Predict, for each candidate assignment, the courier's net earnings per engaged hour — total engaged time including drive to merchant, predicted wait, drive to customer and handoff, against the offer amount net of route cost. This is the offer outcome model, consumed at assignment time rather than at offer time.

Enter it as a constraint rather than as a weighted term, because a weight gets traded away. A floor — no assignment whose predicted courier outcome falls below a threshold, with the threshold set per market — bounds the harm without requiring the optimiser to price courier welfare against delivery speed, which is an exchange rate nobody can defend. Where an assignment would breach the floor, the correct response is to reprice the offer upward rather than to withhold it, which puts the cost of a difficult delivery on the platform and the merchant rather than the courier.

Model batching honestly. The current batching decision compares combined delivery time against separate delivery times. It should also compare the courier's predicted outcome batched against unbatched, including the added walking, the second merchant wait and the route complexity, and it should account for the pay model's treatment of the second order. Batches that improve platform metrics and degrade courier outcome should be visible as a category with a count, which today they are not.

Measure the distribution, not the mean. Assignment quality per courier, per hour, aggregated by cohort — tenure, market, vehicle type, acceptance rate. If assignment quality is systematically worse for some cohorts, that is either a modelling artefact or a policy, and either way somebody should know which. This measurement is available today with no modelling at all, from realised outcomes, and no platform reports it.

## Target Customer

Dispatch and marketplace engineering leadership, where the internal case is supply retention in tight markets and the external case is the minimum earnings standards now arriving in several jurisdictions — which convert the constraint from optional to mandatory and make the engineering necessary rather than virtuous.

## Impact If Built

The optimisation stops being able to improve itself at the courier's expense without anyone noticing, because the term is in the objective and the metric is on the dashboard. Difficult deliveries get priced rather than absorbed. And a platform entering a minimum-earnings jurisdiction has the constraint where it belongs — in the assignment — rather than discovering shortfalls at period-end reconciliation.
