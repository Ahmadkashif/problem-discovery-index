# Application Corpus Intelligence

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn the complete record of how these applications behave into empirical answers about what actually works — and whoever does that stops selling a trace viewer and starts defining the practice.

## Profile
**Market Size:** ~$160M US
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** None — exceptional recording, no inference
**Target Buyer:** The tooling vendors themselves, and their customers as beneficiaries
**Automation Potential:** Very High — the corpus is structured and continuous

## What Makes This a Distinct Niche
These tools sit on the complete record of how LLM applications behave: every prompt version, every input, every output, every model, every configuration change and — where instrumented — every user reaction. That corpus answers what the field guesses at: which prompt patterns actually work, what a model upgrade costs in quality on real traffic, how much of a reported improvement is measurement noise, and what a well-performing application looks like compared to a poor one. The category built exceptional recording infrastructure and stopped short of inference, which is precisely the failure the machine learning operations category made a decade earlier — and the second occurrence is harder to excuse than the first.

## Current Tools & Gaps
Per-customer traces and dashboards, evaluation runs, and documentation examples. The gaps: no cross-deployment analysis of what works; no empirical account of prompt patterns; no measurement of what model upgrades cost in practice; no reference for what normal looks like, so no customer knows whether their application is good; and no feedback from the corpus into product defaults.

## Problems
- [[niches/llm-application-tooling/application-corpus-intelligence/build|🔨 Build: Exceptional Recording, No Inference]]
- [[niches/llm-application-tooling/application-corpus-intelligence/buy|🛒 Buy: Benchmarking Cohorts and Observational Study Design]]
- [[niches/llm-application-tooling/application-corpus-intelligence/fix|🔧 Fix: Nobody Knows What Normal Looks Like]]
