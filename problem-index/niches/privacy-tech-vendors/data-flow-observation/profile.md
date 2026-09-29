# Data Flow Observation

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether where data actually goes can be derived from the systems that already record it, across the whole estate and past the organisational boundary.

## Profile

**Market Size:** ~$840M
**Share of Parent Industry:** ~12%
**Digital Adoption:** Very low — flows are described, not measured
**Target Buyer:** Privacy engineering, data governance, platform engineering
**Automation Potential:** Very high — every flow leaves a record somewhere

## What Makes This a Distinct Niche

This is the observable half of the map: what moves, from where, to where, how often, and across which boundaries.

It is separable from its sibling in discipline, testability and timeline. [[niches/privacy-tech-vendors/personal-data-classification/profile|🎯 Personal Data Classification]] asks what the data means — whether it is personal, whose, under what basis — which is a semantic and legal question no measurement settles. Flow observation is a systems engineering problem answerable entirely by instrumentation the organisation already has, producing results in weeks, and testable immediately: count the flows the observation found that the interview-based map did not.

The contest is over coverage and attribution. Every flow leaves a trace somewhere — egress logs, API gateways, database access records, warehouse lineage, OAuth grants, browser telemetry — and each source covers a different slice of the estate with different fidelity. Assembling them into one picture, and resolving destinations to named organisations rather than to addresses, is the whole problem. A vendor that did it would produce the first evidence-based account of where an organisation's data actually goes, and would almost certainly find third parties nobody registered.

## Current Tools & Gaps

Cloud flow logs and network telemetry, used for security and cost rather than privacy. API gateway logging. Warehouse and pipeline lineage within the analytics stack. SaaS discovery tooling enumerating OAuth grants and integrations. Tag scanners observing browser-side third-party calls. Service mesh and distributed tracing describing internal service flows.

The gaps are in assembly and attribution. No product joins these sources into one flow map. Destinations are recorded as addresses and domains rather than resolved to organisations, so a flow to a third-party processor looks like a flow to an IP range. Cross-border determination requires geolocation and infrastructure attribution that nothing performs for privacy purposes. Browser-side flows and server-side flows are observed by entirely different tools and never reconciled, though they are the same data leaving by different routes. And nothing compares observed flows against the declared record, which is the comparison that would make the observation matter.

## Problems

- [[niches/privacy-tech-vendors/data-flow-observation/build|🔨 Build: Every Flow, Attributed]]
- [[niches/privacy-tech-vendors/data-flow-observation/buy|🛒 Buy: Network and Cloud Telemetry, Read for Privacy]]
- [[niches/privacy-tech-vendors/data-flow-observation/fix|🔧 Fix: The Destination Is an IP Address]]
