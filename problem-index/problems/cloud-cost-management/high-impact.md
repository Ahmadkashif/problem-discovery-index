# Attribution to Decisions Engineers Can Make

**Industry:** [[cloud-cost-management|Cloud Cost Management]]
**Type:** High Impact
**One-liner:** The bill is organised by resource and the decisions are organised by team, service and feature, and bridging the two depends on tagging discipline that does not exist — so cost reporting reaches finance and never reaches the person who could change it.
**Tags:** #graph-neural-networks #gradient-boosting #k-means-clustering #dbscan #feature-engineering #confidence-intervals #evaluation-metrics #data-integration

## The Problem
A cloud bill is a list of resources and their charges. What an organisation needs to know is which team, which product, which service and — increasingly — which customer generated the spend, because those are the units in which decisions are made.

The bridge is tagging. Every cost tool depends on it, every organisation attempts it, and it is always incomplete. Resources created before the policy exists are untagged. Shared infrastructure belongs to everyone. Managed services emit costs that do not map to anything a team created. Data transfer charges appear without an owner. Kubernetes runs many teams' workloads on shared nodes, and the node is what gets billed.

The unallocated remainder is typically large, and it is not random — the shared, cross-cutting, hardest-to-attribute components are exactly the ones that concentrate cost.

So cost reporting lands with finance and platform teams, who cannot act, rather than with the engineers who could. The eventual mechanism is a top-down instruction to reduce spend, applied without information about where reduction is safe.

Unit economics — what it costs to serve one customer, one transaction, one tenant — is the version of this question that businesses most want answered, and it requires attribution the tooling cannot produce.

## Why It's Unsolved
Tagging is a governance problem that has resisted governance for a decade. Enforcement policies help for new resources and do nothing for the estate that exists, and the estate is where the spend is.

Shared cost allocation has no correct answer, only defensible conventions, and every convention makes someone's numbers look worse. That politics has stalled many implementations.

Kubernetes broke the model that the tooling was built for. Costs are billed at node level and consumed at pod level by workloads that move, scale and share, so allocation requires joining billing data to cluster telemetry — a different system entirely, sampled differently, with its own attribution ambiguities.

And the category's incentives are mild. Vendors are paid for reporting and reporting is easy; attribution is hard, contested and difficult to demonstrate in a sales cycle.

## What a Solution Looks Like
Inferred ownership where tags are absent. A resource's creator, the account and project it sits in, its naming convention, its network position, what it talks to and what deployed it are all observable, and together they identify the owning team with high confidence for most untagged resources. That is entity resolution over infrastructure metadata and it is entirely tractable.

Dependency-based allocation for shared services. A shared database's cost should follow the services that query it, and the query telemetry to apportion it exists.

Kubernetes allocation from actual consumption, joining node billing to pod-level resource usage over time, with idle capacity attributed to the platform rather than silently spread.

Unit economics as the output that matters. Once attribution reaches services, joining to request and tenant telemetry gives cost per customer and per transaction, which is the number product and finance actually want and no tool produces.

And confidence stated per allocation, because a number presented as certain when it was inferred will be disputed and then ignored.

## Impact If Solved
Cloud cost is the second largest line in most technology organisations and the reporting reaches everyone except the people who could change it. Inferred attribution converts a governance project that has failed for a decade into a data problem with a solution, and unit economics is the capability every business asks for and no vendor delivers.
