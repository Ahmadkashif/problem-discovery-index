# Non-Cloud-Native Estates

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to bring modern observability to systems that are not ephemeral, not containerised and frequently not connected — and whoever does that takes the industrial and enterprise estate, because the current tooling assumes a world these systems do not live in.

## Profile
**Market Size:** ~$1.4B US attributable to on-premise, edge and industrial observability
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Very Low — the tooling's assumptions do not hold here
**Target Buyer:** Enterprise operations, manufacturing and utility technology functions
**Automation Potential:** High — the systems are stable and their normal behaviour is highly learnable

## What Makes This a Distinct Niche
Modern observability is built around a specific set of assumptions: workloads are ephemeral and identified by labels, everything has network access to a collector, telemetry volume is elastic and cheap to ship, and the systems are recent enough to instrument. A very large share of the systems that run the physical economy violate every one of those. A programmable controller on a factory floor, a point-of-sale estate across nine hundred stores, a fleet of devices on intermittent cellular links, a mainframe, an on-premise application server that has run since 2011 — these are stable rather than ephemeral, frequently bandwidth-constrained, sometimes air-gapped, and often cannot be instrumented at all. They are also the systems where failure has physical consequences. The contest is observability under constraints the category's architecture does not contemplate.

## Current Tools & Gaps
Agents for traditional servers, industrial historians and supervisory systems in operational technology, device management platforms for edge fleets, and network monitoring. The gaps: telemetry volume and continuous connectivity are assumed, which makes the standard architecture unusable over constrained links; operational technology and information technology monitoring are separate worlds with separate teams and no shared view, so a failure spanning both has no owner; systems that cannot be instrumented are observed only from outside, and nothing makes good use of the external signals available; and the stability of these systems — a genuine advantage for anomaly detection — is exploited by nobody.

## Problems
- [[niches/observability-vendors/non-cloud-native-estates/build|🔨 Build: The Assumptions Do Not Hold Here]]
- [[niches/observability-vendors/non-cloud-native-estates/buy|🛒 Buy: Edge Analytics and Constrained Telemetry]]
- [[niches/observability-vendors/non-cloud-native-estates/fix|🔧 Fix: Two Monitoring Worlds With No Shared View]]
