# Latency That Degrades as Concurrency Climbs

**Niche:** [[niches/ai-inference-providers/interactive-token-serving/profile|Interactive Token Serving]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Continuous batching buys throughput by making each individual request wait for its batch-mates, and no provider lets a customer state the latency they need or tells them when it is not being met.
**Tags:** #convex-optimization #markov-chains #dynamic-programming #time-series-forecasting #evaluation-metrics #confidence-intervals #gradient-boosting #optimization-fundamentals
**Contested on:** Every serious competitor in this sub-niche is fighting to hold time-to-first-token and inter-token latency steady while concurrency climbs — and whoever does that takes the account, because a product whose cursor stalls loses its users regardless of what the model can do.

## The Problem
A chat product is comfortable at two hundred concurrent sessions and unusable at eight hundred. The tokens still arrive; they arrive in uneven bursts with pauses, because each decoding step now processes a larger batch and each individual stream waits for the slowest member. The provider's dashboard shows healthy throughput and rising utilisation, which is the metric they optimise. The customer sees a product that feels broken at peak. There is no parameter the customer can set, no signal that the objective is being missed, and no pricing option that would buy the behaviour they need.

## Why Nobody Has Built This
Serving engines optimise throughput because throughput is what determines the provider's cost per token, and the incentive points the wrong way at exactly this decision. Latency objectives are not modelled in the request path, so there is nothing to optimise against even if someone wanted to. Exposing a latency parameter means committing to it, which means refusing work. And the customer's degradation is gradual and attributed to the model rather than to the scheduler.

## What to Build
Let the caller state the objective and schedule against it. Accept a latency objective per request — first token by this time, inter-token gaps under this bound — and make it the scheduler's constraint rather than an aspiration, which is the product change and the thing no provider offers. Compose batches to satisfy objectives rather than to maximise size, since batch composition is the controllable variable and grouping by similar prompt and expected output length materially improves both latency and throughput. Predict output length from the prompt, because a long generation batched with short ones penalises all of them, and the prediction is tractable and unused. Surface prefix cache hit rates to the customer, since for chat workloads with shared system prompts the cache dominates time-to-first-token and a customer who knows their hit rate can restructure their prompts to improve it dramatically. Price the objective, so a customer needing tight latency pays for the headroom it requires and one who does not is not charged for it. Report achieved objectives per customer continuously rather than fleet percentiles. Reject rather than degrade when the objective cannot be met, which the fix note develops. And publish the concurrency-latency curve per model, so a customer can plan capacity rather than discover it.

## Target Customer
Product engineering teams shipping user-facing applications, and the providers competing for them against frontier model APIs.

## Impact If Built
Throughput is what the provider optimises and latency is what the customer buys, and nothing connects them. A per-request latency objective makes it the scheduler's constraint, and surfacing prefix cache hit rates hands the customer a lever that dominates their first-token time.
