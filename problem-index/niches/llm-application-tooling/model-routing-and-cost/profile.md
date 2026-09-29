# Model Routing & Cost

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to send each request to the cheapest model that will answer it well enough — and whoever does that takes the account, because the spread across models is an order of magnitude and the current rule is to ignore it.

## Profile
**Market Size:** ~$230M US
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Low — one model, chosen once, for everything
**Target Buyer:** Engineering and finance jointly
**Automation Potential:** Very High — routing is a classification problem with abundant labels

## What Makes This a Distinct Niche
Gateways that route across providers are widely available and the routing rule is almost always the same one: use the model we picked at the start, for everything. Cost and latency vary across models by an order of magnitude, and the share of requests that genuinely require the most capable model is usually small. Nothing in the tooling estimates which requests those are, so the expensive model handles the trivial ones too. The contest is per-request routing on predicted difficulty with a measured quality floor — which is a well-posed classification problem with abundant labelled data sitting in every deployment's own trace history, and which almost nobody has built.

## Current Tools & Gaps
Gateways with provider abstraction, fallback on failure, manual per-feature model selection, and caching. The gaps: no difficulty prediction, so routing is static; no measured quality floor, so nobody knows what downgrading costs; fallback is configured for outages rather than for economics; no re-evaluation when a new model is released; and cache correctness trade-offs are inconsistently understood.

## Problems
- [[niches/llm-application-tooling/model-routing-and-cost/build|🔨 Build: One Model, Chosen Once, for Everything]]
- [[niches/llm-application-tooling/model-routing-and-cost/buy|🛒 Buy: Cascade and Cost-Sensitive Classification]]
- [[niches/llm-application-tooling/model-routing-and-cost/fix|🔧 Fix: The Semantic Cache That Answers the Wrong Question]]
