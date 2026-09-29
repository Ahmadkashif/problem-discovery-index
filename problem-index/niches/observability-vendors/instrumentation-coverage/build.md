# Discovering the Gap During the Incident

**Niche:** [[niches/observability-vendors/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every capability in the category depends on telemetry existing, nobody verifies that it does, and the gap is found by an engineer at three in the morning looking for data that was never collected.
**Tags:** #graph-theory #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to tell an organisation what it cannot see before an incident rather than during one — and whoever does that takes the platform account, because every capability in the category is worthless on a service that emits nothing.

## The Problem
An incident propagates through a service that was deployed four months ago by a team that did not add the agent. There are no traces, no custom metrics and unstructured logs. The engineer investigating loses twenty minutes establishing that the absence of data is not itself a signal, then works around the blind spot. In the post-incident review, an action item is created to instrument that service. Three other services in the same situation are not identified, because nobody knows which they are — and the organisation's deployment system has a complete list of what is running.

## Why Nobody Has Built This
Coverage is assumed at rollout and never revisited; the observability practice owner has a list of what is instrumented rather than a list of what should be. Reconciliation requires joining the platform's telemetry inventory to the organisation's service inventory, which lives in a deployment system or cloud account and is a different owner. Instrumentation health is particularly awkward because the failure is silent — an agent that stopped attaching after a library upgrade looks like a service that is not busy. And the vendor has a mild disincentive, since complete coverage increases the customer's bill and raises the cost conversation.

## What to Build
Reconcile expected against actual, continuously. Derive the expected service inventory from the deployment system, the cloud resource inventory and the service catalogue, which is where the truth about what is running lives. Compare against what is emitting telemetry, by signal type, and report the gaps — services with no telemetry at all, services with metrics and no traces, services whose logs are unstructured — which is the coverage picture no organisation currently has. Monitor instrumentation health rather than only presence: an agent version that has fallen behind, a library upgrade that detached automatic instrumentation, a sudden drop in span volume from a service that is still serving traffic. Verify trace propagation at each boundary and report where context is being dropped, since a single bad boundary truncates every trace that crosses it and the effect is felt far from the cause. Prioritise gaps by consequence, using the dependency graph — a blind spot on a service that many others depend on matters more than one on a leaf. And feed coverage into the incident view, so an engineer is told what they cannot see rather than inferring it.

## Target Customer
Platform engineering teams and observability practice owners, and the vendors for whom coverage gaps are the root cause of a large share of support volume and customer dissatisfaction.

## Impact If Built
Every other capability in the category is void where telemetry is absent, and absence is currently discovered at the worst possible moment. The reconciliation is a join between two inventories the organisation already has, and propagation verification catches a failure whose effect is felt far from its cause.
