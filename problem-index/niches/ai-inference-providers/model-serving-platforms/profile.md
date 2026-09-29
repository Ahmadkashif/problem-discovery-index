# Model Serving Platforms

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** High Market Share
**Contested on:** Not terminal — the contest differs by whether latency is constrained, and the decomposition is recorded below.

## Profile
**Market Size:** ~$1.9B US
**Share of Parent Industry:** ~32% of category revenue
**Digital Adoption:** High
**Target Buyer:** Product teams; separately, data teams
**Automation Potential:** High

## What Makes This a Distinct Niche
This is the product: an endpoint that takes a request and returns tokens, backed by a serving engine, a scheduler and a fleet. It is the category's largest revenue line and where the visible competition happens.

It is **not terminal**, because serving names the mechanism rather than the contest, and the two workloads running through it are operated on opposite principles. Interactive serving is won on time-to-first-token and inter-token latency while concurrency climbs, bought by product teams whose users are watching a cursor, and priced with a guarantee attached. Batch inference has no latency requirement worth speaking of, is won purely on cost per million tokens, is bought by data teams running offline scoring and embedding jobs, and derives its entire advantage from exploiting interruptible and off-peak capacity that an interactive guarantee forbids anyone from touching. The scheduling policy, the hardware strategy, the pricing model and the buyer all differ. Filter Notes in the overview records the two rejected alternatives; the sub-niches below are the split.

## Current Tools & Gaps
Open serving engines with continuous batching and paged attention, vendor-optimised runtimes, prefix caching, speculative decoding, and autoscaling endpoints. The gaps are specific to each workload and are stated in the sub-niches.

## Problems
- [[niches/ai-inference-providers/model-serving-platforms/build|🔨 Build: One Endpoint, Two Opposite Operating Principles]]
- [[niches/ai-inference-providers/model-serving-platforms/buy|🛒 Buy: Scheduling and Admission Control]]
- [[niches/ai-inference-providers/model-serving-platforms/fix|🔧 Fix: Benchmarks Published at Concurrency One]]
