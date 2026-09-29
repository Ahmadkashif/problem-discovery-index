# Recommending for Retention

**Niche:** [[niches/streaming-video-platforms/discovery-and-personalisation/profile|Discovery & Personalisation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The recommender optimises what the subscriber watches tonight and the business is paid on whether they are still here next month.
**Tags:** #matrix-decompositions #markov-decision-processes #causal-inference #evaluation-metrics #confidence-intervals #survival-analysis #gradient-boosting #policy-gradient-methods
**Contested on:** Every serious competitor in this niche is fighting to get each subscriber to the title that will keep them subscribed rather than the one they will watch tonight — and whoever optimises recommendation for retention rather than for engagement changes what the catalogue is worth.

## The Problem
The recommender is trained and evaluated on immediate engagement — did they click, did they watch, did they finish. That objective is a proxy for retention and diverges from it in specific ways: it favours the familiar over the new, the comfortable over the distinctive, and the title the subscriber would have found anyway over the one that would have given them a reason to stay. Meanwhile the recommender's own allocation determines which titles perform, which entangles it with the content valuation problem.

## Why Nobody Has Built This
Engagement is immediate and measurable and retention is delayed and confounded, so the objective followed the available signal — a system evaluated on what it can see optimises what it can see. Long-horizon optimisation requires methods that are harder to deploy and evaluate safely. The recommender's effect on title performance is inconvenient for content valuation and is left unmodelled. And engagement metrics are deeply embedded in how the team is measured.

## What to Build
Optimise the long horizon and account for the recommender's own influence. Define the objective as subscriber retention over the renewal horizon rather than session engagement, which is the core and is what aligns the system with the business. Model the sequence of recommendations as a policy over a subscriber's tenure, since retention is the outcome of many decisions rather than one. Estimate the recommender's causal effect on each title's performance, because content valuation is otherwise measuring the recommender rather than the title and this connects the two contests. Explore the catalogue deliberately, as a system that only exploits leaves most of an expensive catalogue unseen and undervalues it permanently. Handle the new and narrow title, which suffers a cold start that becomes self-fulfilling. Balance breadth against comfort, since a subscriber who has seen everything they like is a churn risk. Personalise artwork and presentation with the same objective rather than for click-through alone. Measure the whole thing with long-horizon experiments, which are slower and are the only honest evaluation. Report the recommender's contribution to retention as the team's metric. And separate recommendation quality from catalogue quality in reporting, because they are currently conflated and both decisions suffer.

## Target Customer
Product and data leadership, content leadership whose titles are exposed by it, subscription leadership accountable for churn, and recommendation platform vendors.

## Impact If Built
A system evaluated on what it can see optimises what it can see, so engagement became the objective by default. Optimising for the renewal horizon aligns the strongest capability in the business with the outcome it is paid on.
