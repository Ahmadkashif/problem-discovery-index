# One Platform for Two Opposite Failure Modes

**Niche:** [[niches/subscription-commerce/subscription-lifecycle-platforms/profile|Subscription Lifecycle Platforms]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same platform serves a business whose customers cancel because deliveries arrive at the wrong time and one whose customers cancel because the contents disappointed, and it offers both the same cadence dropdown and the same skip button.
**Tags:** #workflow-orchestration #data-integration #evaluation-metrics #automation #revenue-impact #confidence-intervals #descriptive-statistics #gradient-boosting
**Contested on:** Not terminal — the contest differs by whether the customer chose the contents, and the decomposition is recorded in the profile.

## The Problem
A replenishment operator needs to know when each customer will run out and to move the next delivery accordingly. A curation operator needs to know what each customer will like and to select accordingly. The platform they both use offers a cadence dropdown with four options, a skip button, and a swap catalogue. Neither operator gets the capability their business turns on, so both build it themselves or do without — and the platform competes on billing reliability and integration breadth, which is the commodity layer.

## Why Nobody Has Built This
Platforms were built around the recurring order as the object, which is genuinely common, and the differentiation above it looked like customer-specific configuration. The vendor's customers span both models, so building for one looks like narrowing. And the capabilities required — consumption prediction and taste modelling — are data science functions in a product category built by commerce engineers.

## What to Build
Build the substrate both need and the capabilities separately. The genuinely shared requirement is a subscriber state model richer than a plan and a next-delivery date: what has been received, what was skipped, swapped, returned or complained about, what was consumed where that is observable, and how each delivery was rated — which almost no platform maintains and which both models' capabilities depend on. Make the next delivery a decision rather than a schedule, so an operator can influence timing and contents per subscriber through an interface rather than by rebuilding the order. Expose the decision point as an extension surface, so a replenishment operator's consumption model and a curation operator's selection model can both plug in rather than being reimplemented outside the platform. Record every intervention and outcome, which is what makes either model learnable and which the corpus niche depends on. Treat flexibility actions as first-class signals rather than as billing events, since a skip is the most informative thing a subscriber does and is currently recorded as a skipped charge. Support per-subscriber cadence rather than per-plan, since a plan-level cadence is the source of the replenishment failure. And be explicit about which model a platform serves well, because the capability gap is where operators leave.

## Target Customer
Subscription platform vendors, operators of both models, and the merchandising and data functions building around the platform's limits.

## Impact If Built
Both models need a subscriber state model richer than a plan and a date, and almost no platform maintains one. Making the next delivery a decision with an extension surface lets each model's real capability live in the platform rather than around it.
