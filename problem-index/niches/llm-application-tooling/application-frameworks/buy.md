# Library Design and Layered API Practice

**Niche:** [[niches/llm-application-tooling/application-frameworks/profile|Application Frameworks]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Decades of library design produced clear principles about layering, escape hatches and versioning, and this category is relearning them in public at speed.
**Tags:** #workflow-orchestration #automation #compliance #evaluation-metrics #data-integration #worker-facing #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to be worth more than the hundred lines a developer would otherwise write themselves, all the way into production — and whoever does that takes the adoption, because the alternative is genuinely easy and the abstraction is what gets abandoned.

## The Problem
How to build a library that is easy to start with and does not trap its users is well-understood craft. The principles are established: layer the API so every convenience is built on a public primitive, provide escape hatches at each level, keep the abstraction shallow enough to see through, version so that upgrades are boring, and treat the public surface as a commitment. Web frameworks, cloud clients and data libraries have all learned this, some painfully. This category is repeating the same lessons at the speed of a hype cycle.

## What Already Exists
Layered API design principles with convenience built on primitives; semantic versioning with clear compatibility guarantees; deprecation policies with published timelines; plugin architectures that avoid a monolithic surface; and the accumulated library design literature on abstraction depth and escape hatches.

## The Customization Gap
The adaptation is to a domain where the underlying capability changes every few months. It requires: (1) versioning that separates the framework's own compatibility from the model providers' changes, since a provider adding a parameter should not be a breaking change in the framework and currently often is — this separation is the specific discipline this domain needs; (2) a narrow core with integrations as separate packages, because a monolithic surface covering every provider and store guarantees churn from other people's releases; (3) escape hatches that reach the wire, since debugging here frequently requires seeing the exact request and no other library domain makes that as necessary; (4) explicit stability tiers, so a developer knows which parts are committed and which are experimental — this category's surface contains both, undifferentiated; and (5) deprecation timelines measured against how long applications live rather than how fast the ecosystem moves, which is the tension at the heart of the complaints.

## Target Customer
Framework maintainers, developers choosing a framework, and the vendors whose products depend on a healthy framework ecosystem.

## Impact If Solved
The library design craft is decades old and this category is relearning it publicly. Separating framework compatibility from provider churn, and publishing explicit stability tiers, address the two complaints that drive developers back to writing it themselves.
