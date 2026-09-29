# Platform Usage Telemetry

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to give a platform team the usage instrumentation any product team would consider essential — and whoever ships it by default takes the category, because the signals all exist and nobody collects them.

## Profile
**Market Size:** ~$230M US attributable to platform instrumentation and developer experience measurement
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** None — the instrumentation is absent by default everywhere
**Target Buyer:** Platform engineering teams themselves
**Automation Potential:** Very High — every signal is produced by systems the platform already runs

## What Makes This a Distinct Niche
Every signal a consumer product company would consider essential — activation, funnel drop-off, feature usage, retention, support contact rate — is available from the platform's own systems and is almost never collected. This is the mechanical counterpart to the first niche's framing problem: the platform-as-product niche is about a team behaving like a product team, and this one is about the instrumentation that would let them, which does not exist in any of the tooling by default. That is the distinguishing fact: a platform team wanting these numbers must build the collection themselves, which is work competing against everything else, and the tooling vendors — who could ship it as a default and would differentiate enormously by doing so — have not. The result is a category whose products cannot tell their customers whether they are working.

## Current Tools & Gaps
Portal page analytics where anybody enabled them, pipeline execution records, provisioning logs, and catalogue registration counts. The gaps: nothing is joined, so the funnel spanning portal, scaffold, pipeline and deployment cannot be constructed; the tooling ships without instrumentation, so every platform team builds it or does without; feature-level usage within the platform is unrecorded, so a capability nobody uses is indistinguishable from one everybody does; the developer's elapsed time through each step is not measured, although it is the experience; and the vendors do not instrument their own products' usage either, so they cannot tell which of their features their customers use.

## Problems
- [[niches/internal-developer-platforms/platform-usage-telemetry/build|🔨 Build: Every Signal Available, None Collected]]
- [[niches/internal-developer-platforms/platform-usage-telemetry/buy|🛒 Buy: Instrumentation Shipped by Default]]
- [[niches/internal-developer-platforms/platform-usage-telemetry/fix|🔧 Fix: The Feature Nobody Uses and Nobody Knows]]
