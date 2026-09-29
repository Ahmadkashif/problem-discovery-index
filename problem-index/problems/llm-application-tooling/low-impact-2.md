# Cost and Latency Routing Across Models

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Gateways that route across providers are widely available and the routing rule is almost always the same one: use the model we picked at the start, for everything.
**Tags:** #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #optimization-fundamentals #hypothesis-testing #revenue-impact

## The Problem
Model capability and price span more than an order of magnitude. Within any application, task difficulty spans a similar range: a simple classification, a routine extraction and a complex multi-step reasoning problem all flow through the same code path.

Most applications use one model for everything, chosen during development against the hardest case, and pay that price on every request. The economics are obvious and the reason is equally obvious: routing requires knowing which requests are easy, and getting it wrong means a bad answer at a moment nobody is watching.

Caching has the same shape. Exact-match caching is safe and rarely hits. Semantic caching hits far more often and can return a stale or subtly inappropriate response, and the conditions under which it is safe are application-specific and rarely characterised.

Fallback is the third case. When a provider degrades or rate-limits, falling back to another model keeps the application up and changes its behaviour, sometimes materially, and teams configure fallback without measuring what the fallback path actually produces.

## What Already Exists
Gateways and routers (OpenRouter, LiteLLM, Portkey, Martian and the framework-native routers) support multi-provider routing, fallback and load balancing. Cost tracking per request is standard in every observability tool. Semantic caching is available in several products. Batch APIs offer substantial discounts for latency-tolerant work. Provider pricing is public and comparable.

## The Customisation Gap
Routing infrastructure exists and the routing policy does not. Deciding which requests can be served by a cheaper model requires predicting difficulty, and no tool offers it — so the policy is static and conservative.

Difficulty prediction is tractable and unexploited. The application's own history contains requests served by an expensive model where a cheaper one would have produced an equivalent answer, and that comparison can be run offline at leisure to build a router with measured quality impact rather than a guess.

Quality-cost frontier measurement is the missing artefact. For a given application, the achievable combinations of cost and quality across routing policies form a curve, and the team is currently sitting at an arbitrary point on it without knowing the shape.

Cache safety characterisation is the fourth gap. Whether semantic caching degrades quality is measurable by serving cached and fresh responses to comparable requests and comparing, and it is set by a similarity threshold someone picked.

## Impact If Solved
Model spend is a large and growing line item and most applications pay premium prices for their easiest requests. Difficulty-based routing with measured quality impact is a direct cost reduction the tooling is already positioned to deliver, and the quality-cost frontier is a number teams currently have no way to see.
