# One Product Configured Two Ways

**Niche:** [[niches/api-infrastructure-providers/api-gateways-and-management/profile|API Gateways & Management]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Internal service traffic and external partner consumption have almost nothing in common, and the category serves both with the same product and a different set of checkboxes.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor here is fighting to be the layer every API call passes through — and that contest is fought twice, for internal traffic and for external consumers, which is why this niche is not terminal and is decomposed below.

## The Problem
A platform team deploys the gateway for internal traffic and finds it carrying features they will never use — a developer portal, monetisation, self-service key issuance — while lacking the latency headroom and deployment ergonomics they need. The API product team deploys the same gateway for the partner programme and finds strong policy features and a portal that is an afterthought, no usable sandbox, and analytics that describe traffic rather than adoption. Both configure around the mismatch. Neither is well served, and the vendor's roadmap oscillates between them.

## Why It's Still Broken
The product grew from one origin — usually the enterprise management case — and the other was added as a configuration rather than as a product. Selling one thing to two buyers is commercially attractive and the seams only show after deployment. And the two constituencies rarely talk to each other inside the customer, so the mismatch is experienced twice and reported as two unrelated sets of feature requests.

## What a Fix Looks Like
Separate the two concerns explicitly rather than through configuration. Establish distinct defaults, deployment models and metrics for each: internal deployments optimised for latency, footprint and self-service onboarding of internal teams; external deployments optimised for consumer onboarding time, documentation, sandbox fidelity and monetisation. Report the metrics each buyer actually has — internal platform teams are measured on reliability and on how little friction they impose, external programmes on adoption and revenue per consumer — and no current product reports the second at all. Let the two share the traffic layer, since that is genuinely common and is where the leverage is, while diverging above it. Price them differently, because per-call pricing suits an external programme and is actively hostile to internal traffic, and the mismatch drives platform teams to the free alternatives. And stop reporting a single set of gateway statistics, since traffic volume means something completely different in the two cases.

## Who Feels the Pain
Platform teams carrying a product built for somebody else's use case; API product managers with a portal that was an afterthought; and vendors whose roadmap is pulled in two directions by one product.

## Impact If Fixed
The shared traffic layer is genuinely common and everything above it is not, and recognising that in the product rather than in a configuration page is what lets each half be good. Reporting the metrics each buyer is measured on is the smallest change and the most immediately useful.
