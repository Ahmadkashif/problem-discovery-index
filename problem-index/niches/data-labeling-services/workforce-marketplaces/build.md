# Routing by Availability When Capability Is the Constraint

**Niche:** [[niches/data-labeling-services/workforce-marketplaces/profile|Workforce Marketplaces]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform records exactly which contributors do well on which task types and routes work by who is available, which is the one property that does not predict quality.
**Tags:** #gradient-boosting #bayesian-inference #k-nearest-neighbors #survival-analysis #evaluation-metrics #confidence-intervals #worker-facing #revenue-impact
**Contested on:** Every serious competitor here is fighting to put the right capable contributor on the right task within days of a contract being signed — and whoever does that takes the delivery, because sourcing and matching at speed is now the binding constraint rather than labour supply.

## The Problem
A batch of clinical reasoning assessments is distributed to whichever qualified contributors are online. Among them are people who have consistently produced assessments that reviewers accept and that agree with the strongest annotators, and people who passed the same qualification test and have not. The platform holds both records. The routing uses availability and a reputation score that aggregates across all task types, which means a contributor excellent at one kind of judgement and poor at another is routed identically for both. The quality variation that results is then addressed by reviewing more, which is the expensive remedy for a routing problem.

## Why Nobody Has Built This
Routing was built for volume work where contributors were interchangeable, which they largely were, and the design has carried into expert work where they are not. Per-task-type capability estimation requires modelling ability from noisy outcomes, which is the measurement problem the expert-quality niche describes and is not staffed for. Reputation is a single number because a single number is easy to display and to reason about. And the quality consequence is absorbed by review, which is a cost line rather than a visible routing failure.

## What to Build
Route on demonstrated capability per task type. Estimate contributor ability per task type from their outcome history — reviewer verdicts, agreement with reliable peers, customer acceptance — using the ability modelling the quality niche requires, which produces a capability profile rather than a score. Match tasks to contributors on that profile, which improves quality without reviewing more and is the direct return. Model capability as developing rather than fixed, since contributors improve with exposure and a system that routes on early performance will never let them, which is both unfair and wasteful. Route for learning deliberately on a fraction of work, since the platform needs capability estimates on contributors it has not yet observed at a task type and the exploration is cheap relative to the misrouting it prevents. Model retention, because the most capable contributors leaving is the largest cost in expert delivery and the signals — declining activity, longer gaps, rejection experiences — are observable well in advance. Account for the customer's own quality definition, since different contracts value different things and a contributor excellent by one standard may not be by another. And report capability coverage before accepting a contract, so a vendor knows whether they can actually staff it rather than discovering it in week two.

## Target Customer
Delivery organisations and workforce marketplaces, and the laboratories whose contracts depend on the vendor's staffing being real.

## Impact If Built
The platform records exactly what would improve routing and routes on availability, which is why quality variation is addressed with review instead. Per-task-type capability profiles improve quality without additional review, and retention modelling addresses the largest cost in expert delivery.
