# Admitted Anyway and Degraded Silently

**Niche:** [[niches/ai-inference-providers/interactive-token-serving/profile|Interactive Token Serving]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** When a provider cannot serve a request well it serves it badly instead of refusing, so the customer's product degrades invisibly rather than receiving an error they could handle.
**Tags:** #evaluation-metrics #markov-chains #descriptive-statistics #confidence-intervals #automation #worker-facing #quick-win #change-point-detection
**Contested on:** Every serious competitor in this sub-niche is fighting to hold time-to-first-token and inter-token latency steady while concurrency climbs — and whoever does that takes the account, because a product whose cursor stalls loses its users regardless of what the model can do.

## The Problem
At peak the fleet is saturated. Every request is still accepted, batched with fifty others, and served with a first token after four seconds and gaps a user notices. The customer's application has no signal — the response has a 200 status and the tokens arrive. Their users experience a product that is slow and occasionally abandoned. Had the provider returned a rate limit, the application could have queued, retried elsewhere, degraded to a smaller model or shown a wait state. Instead every party is worse off, because refusing looks like failing and degrading looks like working.

## Why It's Still Broken
An error is visible and a slow response is not, which makes silent degradation the choice that protects the provider's error rate dashboard. Every accepted request is billable and every rejected one is not. There is no latency objective in the request, so the system has no definition of serving badly. And customers do not ask for rejections, because nobody has offered the trade.

## What a Fix Looks Like
Refuse honestly and give the caller something to act on. Implement admission control against a stated latency objective and return a retryable rejection when it cannot be met, which is the fix and requires the objective to be expressible — this is why it pairs with the build note. Include a retry-after estimate derived from current queue state, so the caller's backoff is informed rather than guessed. Expose current expected latency in the response headers even on success, since a caller who can see degradation approaching can act before it bites. Offer a degrade-rather-than-refuse option the caller chooses explicitly — a smaller model, a shorter output, a lower quantisation — because many applications would take it and none are asked. Report service level achievement per customer as a published number, which makes silent degradation visible and is the accountability that changes behaviour. Distinguish rejection from failure in the status semantics and in the billing, so refusing is not punished. Shed load by class rather than uniformly, protecting the customers who bought a guarantee. And publish the degradation policy, because a customer who knows what happens at peak can build for it.

## Who Feels the Pain
Product teams whose applications degrade with no signal to act on; end users abandoning a slow interface; and the providers whose reputation absorbs a failure mode they chose in order to protect an error rate.

## Impact If Fixed
Serving a request badly instead of refusing leaves every party worse off, because a rejection is actionable and a slow stream is not. A retryable rejection with a retry-after estimate, plus expected latency in the headers, gives the caller something to build against.
