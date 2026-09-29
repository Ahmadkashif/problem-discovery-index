# Inference Cost Corpus

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn request-level history into an empirical account of what inference actually costs — and whoever does that prices, provisions and optimises against evidence while everyone else guesses.

## Profile
**Market Size:** ~$300M US
**Share of Parent Industry:** ~5% of category revenue
**Digital Adoption:** None — used to generate invoices
**Target Buyer:** The providers themselves, and their customers as beneficiaries
**Automation Potential:** Very High — the corpus is complete and structured

## What Makes This a Distinct Niche
These providers hold the most detailed record anywhere of what inference costs: request-level latency, token counts, batch composition, memory pressure and hardware utilisation across millions of requests, thousands of models and every accelerator generation. That corpus answers what the whole industry currently guesses at — what a given quantisation costs in quality and saves in cost, which architectures serve efficiently at which batch sizes, how much of the fleet is genuinely necessary, what the marginal cost of a request actually is. It is used to generate invoices. Every other niche in this industry — capacity, optimisation, isolation, quantisation — depends on measurements that live in this corpus and are not extracted.

## Current Tools & Gaps
Billing pipelines, utilisation dashboards, and per-incident analysis. The gaps: no marginal cost model, so pricing is set by competition rather than by cost; no empirical account of which architectures serve efficiently; no analysis of which fleet capacity was genuinely necessary; and no feedback from the corpus into scheduling, placement or procurement decisions.

## Problems
- [[niches/ai-inference-providers/inference-cost-corpus/build|🔨 Build: The Cost Record Used to Generate Invoices]]
- [[niches/ai-inference-providers/inference-cost-corpus/buy|🛒 Buy: Cost Accounting and Operations Research]]
- [[niches/ai-inference-providers/inference-cost-corpus/fix|🔧 Fix: Pricing Set by Competitors, Not by Cost]]
