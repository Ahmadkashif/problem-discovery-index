# The Customer Who Wants One Different Chart

**Niche:** [[niches/bi-analytics-platforms/embedded-analytics/profile|Embedded Analytics]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A software company's largest customer wants one metric added to the embedded dashboard, and the options are a code change, a fork, or no.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #revenue-impact
**Contested on:** Every serious competitor in embedded analytics is fighting to serve thousands of a software vendor's customers their own data, fast, inside a product that is not theirs — and whoever holds latency and isolation at that scale takes the deal, because the buyer is an engineering team that will otherwise build it.

## The Problem
The embedded analytics page ships with twelve charts. A major customer asks for a thirteenth, specific to how they operate. The account team says yes. Engineering adds a feature flag. Six months later there are nineteen flags, four customer-specific charts, a conditional layout nobody fully understands, and the next request is harder than the last. The alternative — refusing — costs renewals, since the request is usually reasonable and the customer can see that the data is right there.

## Why It's Still Broken
Embedded analytics is shipped as a fixed set of views authored by the host's product team, because that is what the tooling makes easy and because exposing authoring to customers raises immediate concerns about performance, isolation and support. So customisation arrives through the code path, which is the most expensive one available. The requests are also individually small, so each one is approved on its own merits and the accumulation is never a decision anybody made.

## What a Fix Looks Like
Make customisation a tenant-level capability rather than a code change. A constrained authoring surface for tenants — add a chart from a defined set of metrics and dimensions, rearrange, filter, set a threshold — which covers the large majority of requests and cannot generate an unbounded query, since the constraint is what makes it safe to offer. Per-tenant configuration stored as data rather than as flags, so the host's codebase stays single-tenant in shape no matter how many customers customise. A governed metric set the host controls, which keeps the definitions consistent and prevents a customer inventing a metric the host will then be asked to explain. Cost and latency guardrails on anything a tenant authors, so a customer cannot construct something that degrades their own experience or the host's bill. And measurement of what tenants actually add, which is the most valuable output: the chart that forty customers add themselves is the next thing the product should ship, and the host currently learns that from account managers rather than from data.

## Who Feels the Pain
Engineering teams maintaining an accumulation of customer-specific flags; account teams choosing between a roadmap fight and a renewal risk; and customers who can see their data and cannot arrange it the way they need.

## Impact If Fixed
Constrained tenant authoring converts a recurring engineering cost into a product capability, and the constraint set is what makes it safe. The what-tenants-add measurement turns customisation requests into a prioritised roadmap signal, which is the part that compounds.
