# The Semantic Cache That Answers the Wrong Question

**Niche:** [[niches/llm-application-tooling/model-routing-and-cost/profile|Model Routing & Cost]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** Semantic caching returns a stored answer when a new question is similar enough, and similar enough is a threshold somebody picked, so the cache confidently answers a question nobody asked.
**Tags:** #k-nearest-neighbors #norms-and-inner-products #evaluation-metrics #hypothesis-testing #confidence-intervals #revenue-impact #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to send each request to the cheapest model that will answer it well enough — and whoever does that takes the account, because the spread across models is an order of magnitude and the current rule is to ignore it.

## The Problem
Semantic caching stores answers and reuses them for similar questions, which saves real money. The similarity threshold was set by trying a few values. Two questions can be highly similar in embedding space and have opposite correct answers — can I cancel after thirty days and can I cancel within thirty days, or the same question about two different accounts. The cache returns the stored answer confidently, no error occurs, the user gets a wrong answer, and the saving is reported as a success. Nobody measures the cache's error rate because the cache hit is counted and the correctness is not.

## Why It's Still Broken
Cache hit rate is easy to measure and cache correctness is not, so the reported metric is the one that always looks good. Embedding similarity is a poor proxy for answer equivalence in exactly the cases that matter — negation, quantities, entity identity — and this is known and not designed around. The threshold is a single global number for a property that varies by question type. And the error is silent.

## What a Fix Looks Like
Measure the cache's error rate and make the threshold earn its value. Sample cache hits and verify against a fresh model call, which measures the error rate directly, costs a small share of the saving, and is the only honest way to know what the cache is doing — most deployments have never done it. Set the threshold from that measurement rather than by trial, and set it per question type, since the safe threshold for a factual lookup and for a policy question are different. Detect the known failure patterns explicitly — negation, differing quantities, different entities, changed dates — since these are where similarity misleads and all are cheaply checkable before serving a cached answer. Include the parameters that change the answer in the cache key: user, account, locale, permissions, time sensitivity, which is where a surprising share of the errors originate. Expire by content volatility rather than by a fixed period, since a policy answer and a balance enquiry have different lifetimes. Report cache error rate alongside hit rate, so the saving is stated net of its cost. Exclude classes of question from caching entirely where the risk is high, which is a configuration most teams would want and few products offer. And make the cache hit visible in the trace, so a wrong answer can be traced to a cache rather than blamed on the model.

## Who Feels the Pain
Users given a confident answer to a question they did not ask; teams reporting a saving that is partly a quality cost; and engineers debugging a wrong response that no model produced.

## Impact If Fixed
Hit rate is measured and correctness is not, which makes the reported saving gross rather than net. Sampling cache hits against a fresh call measures the error rate directly for a small share of the saving, and most deployments have never tried it.
