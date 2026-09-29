# Developer Experience for Regulated Builds

**Niche:** [[niches/embedded-finance-platforms/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Developer experience is a mature discipline optimised for time-to-first-call, and a regulated product's hard part starts long after the first call succeeds.
**Tags:** #workflow-orchestration #large-language-models #automation #worker-facing #compliance #evaluation-metrics #tacit-knowledge-ml #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get the regulated-product knowledge a solutions engineer carries in their head into a form a first-time developer team can use without them — and whoever extracts it turns the category's scarcest people into leverage instead of a bottleneck.

## The Problem
Developer experience as practised — quickstarts, sandboxes, SDKs, interactive references, time-to-first-successful-request as the headline metric — is well understood and embedded finance platforms have adopted all of it. It optimises the first hour. The problem in this category is months three through eight, where the decisions are compliance decisions, the constraints are a bank's, and the failure mode is a design that works perfectly and cannot be launched.

## What Already Exists
API documentation platforms; sandboxes and test environments; SDK generation; interactive references; developer onboarding funnels and activation metrics.

## The Customization Gap
The adaptation is to a build whose hard part is regulatory rather than technical. It requires: (1) guidance about decisions rather than about endpoints, since the API is the easy part and no documentation platform has a shape for design consequence — this is the substantive gap; (2) an approval gate outside the developer's control, which means correctness cannot be verified by a successful response; (3) constraints specific to a counterparty rather than universal to the API, so guidance must be scoped per bank; (4) a success metric of launched-and-approved rather than first-call-latency, which reframes the whole funnel; and (5) a sandbox that can simulate review outcomes rather than only transaction responses.

## Target Customer
Platform developer experience and solutions teams, fintech engineering leads on a first regulated build, and developer platform vendors whose model of the developer journey ends at activation.

## Impact If Solved
Developer experience optimises the first hour and this category's failure happens in month six. Guidance scoped to decisions and to a specific bank's constraints is a shape the mature discipline has no template for.
