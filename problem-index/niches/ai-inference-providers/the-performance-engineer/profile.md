# The Performance Engineer

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to attribute a latency regression to the layer that caused it without a person bisecting five independently-moving components — and whoever does that takes the account, because that bisect is most of a performance engineer's week.

## Profile
**Market Size:** ~$220M US in loaded engineering cost
**Share of Parent Industry:** ~4% of category revenue equivalent
**Digital Adoption:** None — bisecting an unversioned stack
**Target Buyer:** Performance engineering teams and their leads
**Automation Potential:** Very High — every layer's version is knowable

## What Makes This a Distinct Niche
A latency regression appears. The serving engine has moved, the driver has moved, the kernel library has moved, the model weights may have been re-quantised, the hardware may be a different generation in a mixed fleet, and the workload mix has changed. None of it is version-locked, several layers are outside the provider's control, and the engineer bisects by hand across a combinatorial space, re-running benchmarks on contended hardware with enough noise that a single measurement settles nothing. It takes days per regression and it is the recurring core of the role — and it is the same problem the evaluation engineers face, in a domain with more layers and noisier measurements.

## Current Tools & Gaps
Profilers, benchmark scripts, changelogs, and the engineer's memory of what moved. The gaps: no pinned manifest of the full stack per measurement; no automated attribution of a change to a layer; no continuous benchmark on stable hardware to give a clean baseline; no statistical treatment, so noise is mistaken for signal and back again; and no regression alerting, so changes are found late.

## Problems
- [[niches/ai-inference-providers/the-performance-engineer/build|🔨 Build: Five Layers Moving Independently]]
- [[niches/ai-inference-providers/the-performance-engineer/buy|🛒 Buy: Continuous Benchmarking and Bisection]]
- [[niches/ai-inference-providers/the-performance-engineer/fix|🔧 Fix: Benchmarks Run on Contended Hardware]]
