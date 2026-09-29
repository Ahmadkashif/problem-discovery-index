# The Function Nobody Measures

**Niche:** [[niches/customer-data-platforms/identity-resolution-accuracy/profile|Identity Resolution Accuracy]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every downstream use of customer data depends on deciding which records are the same person, that decision is probabilistic, and essentially no organisation has measured how often it is wrong or in which direction.
**Tags:** #bayesian-inference #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #gradient-boosting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to measure how often the identity graph merges two people or splits one — and whoever makes that measurable turns the category's central function from a threshold into an engineering discipline.

## The Problem
The profile for a customer contains an email, three device identifiers, a loyalty number, two phone numbers and forty orders. Some of that belongs to their partner, who shares a household and a device. Somewhere else in the graph, the same person exists twice because they ordered once as a guest with a different email. Neither situation is flagged, neither is counted, and the organisation has no estimate of how common either is. A piece of infrastructure that determines personalisation, suppression, lifetime value and privacy compliance operates with no accuracy metric at all — which no database, no classifier and no measurement system would be permitted to do.

## Why Nobody Has Built This
There is no ground truth, so measurement looks impossible and the absence has been accepted as inherent — that assumption is the obstacle and it is wrong, because ground truth can be constructed on a sample. Vendors report match rates, which reward merging aggressively and measure the wrong thing. An error rate would be an uncomfortable number to publish. And neither error is visible downstream, so nobody has been forced to ask.

## What to Build
Make the graph measurable. Construct ground truth on a sample through deliberate verification — authenticated sessions, confirmed customer service interactions, seeded records, survey confirmation — which is the foundation and is entirely achievable at sample scale even though it is impossible at population scale. Report over-merge and under-merge rates separately with intervals, since they are different errors with different consequences and a single accuracy figure conceals the trade-off that matters. Expose the threshold as a deliberate choice with its consequences shown, so an organisation can decide whether it prefers splitting to merging rather than inheriting a default. Vary the threshold by use case, because suppression and privacy demand caution about merging while marketing reach tolerates it, and one graph serving both at one threshold serves neither well. Model household versus individual explicitly, since shared devices and addresses are the largest source of over-merge and the distinction is frequently knowable. Trace the downstream consequences of a merge decision, connecting to the impact tracing work, so the cost of an error is visible rather than theoretical. Detect suspect profiles proactively — conflicting attributes, implausible behaviour, duplicate signatures — which surfaces errors without any ground truth. Support review and correction, since some errors are worth a human decision and there is currently no route for one. Publish the methodology, because an identity vendor that can state its error rates competes on something no competitor currently offers. And validate continuously, since the graph degrades as data sources and identifier availability change.

## Target Customer
Customer data platform vendors, enterprise data and privacy leadership, and the organisations whose personalisation and suppression rest on an unmeasured graph.

## Impact If Built
The absence of ground truth was accepted as inherent, and it can be constructed on a sample. Reporting over-merge and under-merge separately exposes a trade-off every organisation is making by default and none has chosen.
