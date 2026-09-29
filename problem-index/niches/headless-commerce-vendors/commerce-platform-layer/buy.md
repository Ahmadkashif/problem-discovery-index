# API Product Management Practice

**Niche:** [[niches/headless-commerce-vendors/commerce-platform-layer/profile|Commerce Platform Layer]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The API economy produced real practice on versioning, deprecation, developer experience and backwards compatibility, and commerce APIs frequently break their consumers.
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #quick-win #graph-theory
**Contested on:** Not terminal — the contest differs by whether the buyer is an architecture committee or a developer, and the decomposition is recorded in the profile.

## The Problem
Running an interface that other people build businesses on is a discipline: versioning with explicit compatibility guarantees, deprecation with long timelines and usage-driven communication, developer experience treated as a product, sandbox environments, and change management that assumes consumers cannot redeploy on your schedule. The API-first platforms in every other category learned this. Commerce platforms whose entire proposition is an interface routinely handle it worse than the payment and messaging providers their customers also integrate.

## What Already Exists
API versioning and compatibility conventions; deprecation policies driven by measured consumer usage; developer portals with reference implementations and sandboxes; change communication tied to actual consumers of an endpoint; and rate limiting, idempotency and error semantics conventions.

## The Customization Gap
The adaptation is to an interface behind a storefront that cannot go down. It requires: (1) deprecation timelines measured against enterprise replatform cycles, since a consumer here may take eighteen months to change and a twelve-month deprecation is not a deprecation — matching the timeline to the customer's actual change capability is the specific adaptation; (2) idempotency and consistency semantics documented precisely, because commerce operations are financial and the failure modes are double charges and lost orders rather than a retry; (3) behavioural compatibility as well as interface compatibility, since a change in how promotions stack breaks a consumer with no interface change; (4) usage-driven change communication, so a deprecation notice reaches the specific customers calling that endpoint rather than a mailing list; and (5) sandbox fidelity, since a composed system cannot be tested against a sandbox that behaves differently from production and the enterprise buyer needs to.

## Target Customer
Platform vendors, the retailers and developers building on them, and the API product management community.

## Impact If Solved
The API discipline is mature and this category, whose entire product is an interface, frequently handles it worse than the payment providers its customers also use. Deprecation timelines matched to enterprise replatform cycles, and behavioural compatibility treated as compatibility, are the two adaptations.
