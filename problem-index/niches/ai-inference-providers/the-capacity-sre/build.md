# Deciding in Real Time Who Gets Degraded

**Niche:** [[niches/ai-inference-providers/the-capacity-sre/profile|The Capacity SRE]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Site reliability engineers manage capacity crises by hand — deciding in real time which customer gets degraded so that another does not — because the system has no way to anticipate a spike or to arbitrate between guarantees.
**Tags:** #time-series-forecasting #change-point-detection #markov-decision-processes #convex-optimization #worker-facing #evaluation-metrics #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make contention a policy the system executes rather than a decision a person makes at three in the morning — and whoever does that takes the account, because the arbitration is currently a human bottleneck with commercial consequences.

## The Problem
At 03:40 the fleet saturates. An engineer has a dashboard showing utilisation, a chat channel, and the ability to change rate limits per customer. They do not have, in that moment, a list of which customers hold contractual latency commitments, which are in a renewal cycle, which are running a launch, or what the company's policy is when two commitments cannot both be met. They make a call based on what they can remember about the account names, throttle someone, and write it up afterwards. The same situation recurs weekly and the decision is improvised every time.

## Why Nobody Has Built This
The policy has never been written down, because writing it means deciding explicitly which customers matter more, which is a conversation the commercial side prefers to leave implicit. Contractual terms live in a sales system that operations tooling does not reach. Each event feels unique in the moment even though the shape repeats. And the improvisation mostly works, in that the business survives, which removes the pressure to formalise.

## What to Build
Encode the policy and let the system execute it. Write the priority policy explicitly — commitment tier, contractual latency terms, service class, current consumption against entitlement — and make it machine-readable, which is the hard organisational step and the one everything else depends on. Join contractual state into the operational surface, so the decision is made with the facts rather than from memory. Execute degradation automatically according to that policy when contention occurs, since the policy is better applied consistently by a system than inconsistently by a tired person, and the engineer's role becomes exception handling. Anticipate contention from demand forecasting and the early shape of a spike, so action is taken minutes before saturation rather than during it — which is the difference between shaping and firefighting. Present the engineer with options and consequences when a genuine exception arises: throttle here and this commitment breaks, add on-demand capacity and this costs this much. Record every decision with its rationale, which builds the policy empirically and is currently lost. Notify affected customers automatically, since the worst part of these events for a customer is silence. And report page volume and overnight incident counts for this team, because the human cost is the thing that makes the automation fundable.

## Target Customer
Site reliability leadership at the providers, the commercial functions whose commitments are being arbitrated, and the customers on the wrong side of an improvised decision.

## Impact If Built
A commercial decision is being made hourly by an operations engineer from memory. Writing the priority policy down is the hard organisational step and the precondition for everything; anticipating contention turns firefighting into shaping.
