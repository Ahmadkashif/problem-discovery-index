# Checkout and Inventory Under Burst

**Industry:** [[live-commerce-platforms|Live Commerce Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Queuing, reservation and oversell protection are solved patterns from ticketing, and live commerce needs them applied to thousands of independent micro-drops a day rather than to one scheduled event.
**Tags:** #optimization-fundamentals #time-series-forecasting #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #workflow-orchestration

## The Problem
A host holds up a limited item and says there are three. Hundreds of viewers attempt to buy within seconds.

This is a burst concurrency problem with an absolute inventory constraint, and the standard failure modes are all present. Overselling, where the same unit is sold twice because reservation was not atomic under contention. Race conditions in the payment path where the fastest network connection wins rather than the fastest tap. Queue behaviour that is opaque to the viewer, who does not know whether they got it. Payment authorisation latency deciding the outcome.

Ticketing solved this for scheduled events with known demand, and the solution assumes a single high-value event with dedicated preparation. Live commerce has thousands of unscheduled micro-drops a day across thousands of streams, each unpredictable, each small.

The consequences are disproportionate to the transaction size. A viewer who believes they were unfairly denied an item tells the chat, and the perception of unfairness in a live audience is corrosive in a way a failed checkout on a normal storefront is not.

## What Already Exists
Queuing and virtual waiting room systems are mature. Atomic inventory reservation is a well-understood distributed systems problem with established solutions. Payment authorisation is fast and getting faster with modern rails. Ticketing platforms have decades of experience with exactly this pattern. Rate limiting and bot detection are standard.

## The Customisation Gap
Ticketing patterns assume preparation for a known event, and live commerce bursts are unannounced. Capacity cannot be provisioned per drop because nobody knows which moment in which stream will produce one — which points at prediction rather than at provisioning.

Burst prediction is the unexploited opportunity. Signals precede the moment: the host's introduction, chat volume rising, the item's characteristics, the host's own history with similar items. A few seconds of warning is enough to pre-warm capacity and pre-authorise, and nothing does it.

Fairness is undefined. Whether allocation should favour speed, randomise among those who acted within a window, or weight by viewer loyalty is a policy question with real consequences for the audience's perception, and it is currently decided implicitly by whoever's request arrives first.

Bot resistance matters more here than in ordinary commerce, since automated purchasing on limited drops is both feasible and lucrative, and the fairness perception depends on the audience believing they competed with people.

## Impact If Solved
The drop moment is where live commerce converts and where its fairness is judged by a watching audience. Predicting bursts to pre-warm capacity, and defining allocation fairness explicitly rather than implicitly, addresses both the technical failure and the perception problem that follows it.
