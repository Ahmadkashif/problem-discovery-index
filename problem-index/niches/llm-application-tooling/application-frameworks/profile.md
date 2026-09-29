# Application Frameworks

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to be worth more than the hundred lines a developer would otherwise write themselves, all the way into production — and whoever does that takes the adoption, because the alternative is genuinely easy and the abstraction is what gets abandoned.

## Profile
**Market Size:** ~$320M US, most of the value captured indirectly
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** High
**Target Buyer:** Application developers, adopting before anybody pays for anything
**Automation Potential:** High

## What Makes This a Distinct Niche
A framework is adopted by a developer at the start of a project, for free, against a genuinely credible alternative: calling the model API directly in a hundred lines. It wins on ergonomics, documentation and the speed of getting something working. It loses — and it loses loudly, repeatedly and publicly in this category — when the abstraction that made the first day fast becomes the thing standing between the developer and the behaviour they need to change in month three. The persistent criticism of abstraction depth in this market is not a communications problem; it is the contest itself, and whoever resolves it holds the adoption that everything else in the category is built on.

## Current Tools & Gaps
Composition abstractions, integrations across models and stores, streaming, structured output, and a large surface of prebuilt components. The gaps: the assembled model call is frequently not inspectable; the escape hatch to the raw API is incomplete; upgrade paths break applications across minor versions; the abstraction is optimised for the first hour rather than the third month; and the framework's own overhead in latency and tokens is undocumented.

## Problems
- [[niches/llm-application-tooling/application-frameworks/build|🔨 Build: The Abstraction That Helps on Day One and Blocks in Month Three]]
- [[niches/llm-application-tooling/application-frameworks/buy|🛒 Buy: Library Design and Layered API Practice]]
- [[niches/llm-application-tooling/application-frameworks/fix|🔧 Fix: The Upgrade That Breaks the Application]]
