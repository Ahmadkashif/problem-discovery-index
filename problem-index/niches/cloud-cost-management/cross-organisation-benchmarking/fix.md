# Nobody Can Tell Whether Their Rate Is Good

**Niche:** [[niches/cloud-cost-management/cross-organisation-benchmarking/profile|Cross-Organisation Benchmarking]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** An organisation negotiating a cloud agreement has no way to know whether the discount offered is good, because the only party with comparable data is the counterparty.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #quick-win #compliance
**Contested on:** Every serious competitor that gets here is fighting to tell a customer what a workload of this shape should cost and what comparable organisations actually pay — and whoever does that holds the only asset in this category a competitor cannot obtain from the same billing export.

## The Problem
A company negotiates a multi-year cloud agreement worth a substantial sum. The provider offers a discount schedule. The company's procurement team has no basis for evaluating it: they do not know what organisations of similar size and commitment receive, whether the structure is standard, or which terms are negotiable. The only party in the room with comparative data is the one across the table. The company accepts something in the middle of what feels reasonable, and will not learn whether it was good until a consultant tells them at the next renewal, if then.

## Why It's Still Broken
Discount terms are confidential by contract, which makes informal sharing difficult and formal aggregation delicate. The cost management vendors hold the effective rates of their whole customer base and have not published anything, partly from the same confidentiality and partly because the hyperscalers are their partners. Advisory firms hold fragments from their own engagements and sell it per engagement rather than as data. And the asymmetry favours the provider, who has no reason to change it.

## What a Fix Looks Like
Publish what can be published, carefully. Effective rate distributions by commitment size and term, aggregated with cohort thresholds large enough that no individual agreement is identifiable, which is the core deliverable and is achievable within confidentiality constraints if the aggregation is genuine. Structural benchmarks rather than only rates — which terms are commonly obtained, what flexibility is typical, what non-price concessions organisations receive — since much of the value in these negotiations is structural and none of it is confidential in the same way. A position rather than a verdict: this offer sits in this part of the distribution for organisations of this commitment size, which is informative without asserting anything about any specific agreement. Contribution-based access, so that participating organisations receive the benchmark and the corpus grows. Time series, since discount norms shift and a benchmark from two years ago is misleading. And absolute clarity about the methodology and the thresholds, because the participants are contractually bound and will only contribute to something whose disclosure properties they can verify.

## Who Feels the Pain
Procurement teams negotiating against the only party with the data; organisations paying more than comparable companies for identical capacity; and cloud economics functions asked whether the rate is good and unable to answer.

## Impact If Fixed
The asymmetry is structural and one-sided, and genuine aggregation with large cohorts can address it within the confidentiality constraints. The structural benchmarks are the least constrained part and are immediately useful on their own.
