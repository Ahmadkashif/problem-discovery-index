# Platform Engineer Rationing GPUs

**Industry:** [[mlops-platforms|MLOps Platforms]]
**Type:** Worker Life Changing
**One-liner:** Platform engineers spend their days arbitrating between researchers who all need the cluster now, using a scheduler that knows nothing about how long anything will take or whether it will work.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #convex-optimization #confidence-intervals #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
GPU capacity is expensive, finite and contended. A platform engineer owns the cluster and spends the day allocating it: this team has a deadline, that experiment has been queued for two days, this job has been holding eight accelerators at eleven per cent utilisation for six hours, and someone has requested the entire pool for a run they cannot describe.

The scheduler helps with the mechanics and nothing else. It knows requested resources and priority class. It does not know how long a job will run, whether it will use what it reserved, whether it will fail in the first ten minutes, or whether the result will matter.

So the engineer negotiates. They read job configurations to guess at duration, chase people about idle allocations, and make judgement calls about whose deadline is more real. The cluster runs at utilisation everyone knows is poor, and the researchers experience it as scarcity while the engineer watches half of it sit idle inside reservations.

Every cost review asks why utilisation is low, and the honest answer — that allocation is made without any estimate of demand, duration or value — is not one the tooling helps with.

## Why It Matters to the Worker
This is a role where the job is to disappoint people. Every allocation decision is a refusal to someone else, made without a defensible basis, and repeated all day. Platform engineers describe the social load as the hard part, not the technical one.

It is also strategically important work being spent on arbitration. Capacity planning, scheduling design and cost architecture are genuinely valuable and get squeezed out by the daily queue.

The accountability is misaligned in a familiar way: the engineer owns a utilisation number driven by researchers' reservation behaviour, which they cannot control and can only cajole.

And the arithmetic is thankless. Reservations are sized defensively because a failed allocation costs a researcher a day, so everyone over-requests, and the engineer's job becomes reclaiming the difference from people who are individually behaving sensibly.

## What a Solution Looks Like
Duration and resource prediction from job characteristics. Model architecture, dataset size, batch size, hardware and the submitter's own history predict runtime and actual memory usage well, and the platform has seen enormous numbers of comparable jobs. A scheduler that knows expected duration can backfill, pack and pre-empt intelligently, which is where most of the recoverable utilisation is.

Early failure prediction. A meaningful share of jobs fail in the first few minutes, and identifying likely failures at submission — configuration errors, incompatible shapes, insufficient memory — returns capacity that is currently burned.

Idle reclamation with warning. Allocations running far below their reservation are detectable immediately, and a system that notifies and then reclaims removes the engineer from the conversation entirely.

Right-sizing recommendations to submitters, based on what their jobs actually used rather than what they requested, which addresses the defensive over-requesting at its source.

Queue transparency: honest wait time estimates so researchers can plan, which converts a great deal of the daily negotiation into information.

## Impact If Solved
GPU spend is among the largest line items in any machine learning organisation and utilisation is poor for reasons that are scheduling failures rather than physics. Predicting duration and reclaiming idle capacity is worth a substantial fraction of the fleet, and it removes the arbitration role that makes the job unpleasant.
