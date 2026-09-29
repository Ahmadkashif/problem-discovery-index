# On-Call During Peak Traffic

**Industry:** [[headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Worker Life Changing
**One-liner:** An on-call engineer owns an incident spanning six vendors' systems on the highest-revenue day of the year, with visibility into their own integration code and nothing else.
**Tags:** #change-point-detection #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #graph-theory #workflow-orchestration #worker-facing

## The Problem
Peak trading — Black Friday, a product drop, a campaign — puts a composed stack under load it does not otherwise see. Something degrades.

The engineer on call sees elevated errors or latency at the front end. Beneath that are six services owned by six vendors. Their own monitoring covers the integration layer; each vendor's covers their component; nothing covers the composition.

They open a bridge call and start contacting vendors. Each vendor's support has its own process, its own severity definitions and its own hours, and each reports their component healthy — which is frequently true, because the failure is an interaction. Service A is slower than usual, which causes Service B's timeouts to retry, which amplifies load on Service C, which was already near capacity.

This takes hours, during which the retailer is losing revenue at the highest rate of the year, and the engineer is on a call with a dozen people including their own executives.

Meanwhile they cannot easily roll back, because a composed stack has no single deployment and the change that triggered this may have been made by a vendor.

## Why It Matters to the Worker
This is the highest-stakes and lowest-visibility incident work in commerce engineering. The engineer is accountable for a system they can observe only at the edges, at the moment when the cost per minute is highest.

The vendor coordination is the specific difficulty. Technical diagnosis is secondary to getting six organisations to respond, and the engineer becomes an incident coordinator rather than a diagnostician, which is not the skill they were hired for and not the one that resolves the problem.

Peak scheduling is punishing by construction. The busiest trading periods are holidays, so on-call coverage falls on people who are missing family occasions to sit on a bridge call.

And the post-incident outcome is frequently unsatisfying. When the cause is an interaction between two vendors' components, neither accepts it, no fix is committed, and the same failure is available next year.

## What a Solution Looks Like
Composition-level observability that survives vendor boundaries. Outcome-level synthetic journeys running continuously, plus latency and error decomposition by service contribution, tell the engineer which component's behaviour changed without depending on that vendor's own monitoring.

Automatic change correlation. Every vendor releases independently and each maintains a status page and a change log, and correlating a degradation against everything that changed in the window is the diagnostic that most often identifies the cause, and it is assembled by hand today.

Interaction failure detection. Retry amplification, timeout cascades and capacity coupling are recognisable patterns with recognisable signatures, and identifying them explicitly is what converts "everyone says they are healthy" into a diagnosis.

Load testing of the composition rather than of components. Each vendor tests their own service; nobody tests the assembly under realistic peak traffic with realistic data, which is why these failures are discovered in production.

Pre-negotiated vendor escalation with agreed severity definitions and response times, so the engineer is not negotiating support processes during an incident.

## Impact If Solved
Peak incidents in composed stacks are slow because diagnosis spans organisations, and the cost per minute is the highest a retailer experiences. Composition-level observability with change correlation turns hours of coordination into a routed ticket, and interaction failure detection addresses the class of problem that no individual vendor will ever own.
