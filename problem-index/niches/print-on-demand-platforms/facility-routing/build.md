# Routing on Distance, Not on Who Prints It Well

**Niche:** [[niches/print-on-demand-platforms/facility-routing/profile|Facility Routing]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Routing engines that assign orders to facilities by distance and capacity are standard, and the variable that determines whether the customer is happy — which facility prints this kind of work well — is not in the routing decision.
**Tags:** #convex-optimization #gradient-boosting #evaluation-metrics #confidence-intervals #optimization-fundamentals #revenue-impact #hypothesis-testing #dynamic-programming
**Contested on:** Every serious competitor in this niche is fighting to send each order to the facility that will produce it well rather than the one that is nearest — and whoever does that takes the quality, because quality is the variable the routing decision currently omits.

## The Problem
An order for a detailed design on a dark garment is routed to the facility three hundred miles from the customer, because it is closer than the one four hundred miles away and both have capacity and both are flagged as capable of direct-to-garment. The nearer facility's reprint rate on dark-substrate detail work is four times the further one's. The order is printed, is unacceptable, is reprinted at the same facility, and finally ships eleven days later from a distance advantage of a hundred miles. Every number needed to make the better decision is in the platform's own order history and none of it is in the routing engine.

## Why Nobody Has Built This
Routing was built as a logistics optimisation, where distance and capacity are the classical variables, and quality was assumed to be a property of the network rather than of a facility-and-work-type pair. Capability is represented as a flag because that is how the partner onboarding recorded it. Outcome data lives in the support system and routing runs in operations. And the shipping distance is visible on every order while the reprint probability is not.

## What to Build
Put quality in the objective. Estimate expected outcome quality per facility per work type from the order history — decoration method, substrate colour, detail density, colour complexity, product family — which is a straightforward model on abundant labelled data and is the missing routing input. Optimise against total expected cost including the probability and cost of a reprint and the delay it causes, rather than against shipping distance, which is the objective change and frequently reverses the decision on exactly the orders that matter. Replace capability flags with measured competence scores, which the fix note develops. Route deliberately to build the evidence, sending a small share of work to facilities whose record on that type is thin, since otherwise the estimate never improves for anything but the incumbent. Feed outcomes back continuously so competence scores track reality rather than onboarding claims. Give facilities their scores and the volume consequences, which is the mechanism by which network quality improves rather than merely being measured. Detect degradation per facility and reroute before the reprints accumulate. Balance the load so quality routing does not simply overload the best facility, which is a capacity constraint the optimisation must carry. And report the reprint cost avoided, since that is what funds the build.

## Target Customer
Network operations, platform finance, partner facilities, and the merchants whose orders are currently routed on the wrong variable.

## Impact If Built
Every number needed for a better decision is in the order history and none is in the routing engine. Optimising against expected total cost including reprint probability reverses the decision on exactly the orders where it matters, and deliberate exploratory routing is what keeps the estimates alive.
