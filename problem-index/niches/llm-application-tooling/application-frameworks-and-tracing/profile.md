# Application Frameworks & Tracing

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** High Market Share
**Contested on:** Not terminal — the contest differs by whether the buyer is starting the application or operating it, and the decomposition is recorded below.

## Profile
**Market Size:** ~$560M US
**Share of Parent Industry:** ~31% of category revenue
**Digital Adoption:** High
**Target Buyer:** App developers; separately, the teams operating them
**Automation Potential:** High

## What Makes This a Distinct Niche
This is the category's product surface: the libraries developers build with and the platforms that record what the resulting application did. Together they are the largest revenue line and the most visible competition.

It is **not terminal**, because the two halves are adopted at different moments by different people against different alternatives. A framework is chosen at the start of a project by a developer weighing its abstractions against writing the loop directly against a model API, and is won on ergonomics, documentation and whether the abstraction survives contact with production — a contest largely settled before any money changes hands. Tracing and prompt operations are bought after the application exists, by whoever operates it, to answer what happened in production and to change a prompt without breaking things; the competitor is generic observability plus a git repository. The adoption moment, the buyer, the competitor and the evidence that wins are all different. Filter Notes in the overview records the two rejected alternatives; the sub-niches below are the split.

## Current Tools & Gaps
Application frameworks with chains, agents and integrations; tracing compatible with open telemetry standards; prompt registries with versioning; evaluation harnesses; and gateways. The gaps are specific to each half and are stated in the sub-niches.

## Problems
- [[niches/llm-application-tooling/application-frameworks-and-tracing/build|🔨 Build: Chosen at the Start and Bought Afterwards]]
- [[niches/llm-application-tooling/application-frameworks-and-tracing/buy|🛒 Buy: Open Telemetry and Semantic Conventions]]
- [[niches/llm-application-tooling/application-frameworks-and-tracing/fix|🔧 Fix: Cost and Latency Visible Only in the Bill]]
