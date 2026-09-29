# Continuous Benchmarking and Bisection

**Niche:** [[niches/ai-inference-providers/the-performance-engineer/profile|The Performance Engineer]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compilers, browsers and database engines all run continuous performance benchmarking with automated regression detection and bisection, and inference stacks benchmark when somebody complains.
**Tags:** #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #descriptive-statistics #automation #workflow-orchestration #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to attribute a latency regression to the layer that caused it without a person bisecting five independently-moving components — and whoever does that takes the account, because that bisect is most of a performance engineer's week.

## The Problem
Projects where performance is the product — compilers, browsers, storage engines, numerical libraries — all converged on the same practice: a benchmark suite run continuously on dedicated hardware, statistical change detection on the results, automatic bisection to the responsible commit, and a dashboard with history. The tooling is public and the methodology is well documented. Inference providers, whose entire product is performance, run benchmarks reactively.

## What Already Exists
Continuous benchmarking infrastructure with dedicated runners and historical tracking; statistical change detection on noisy benchmark series; automated bisection triggered by detected regressions; performance dashboards with per-commit attribution; and benchmark stability practice including pinning, isolation and repetition.

## The Customization Gap
The adaptation is to a stack whose components are not all in one repository. It requires: (1) bisection across a multi-dimensional version space rather than a linear commit history, since the layers move independently and the search is over combinations — which is a modest generalisation nobody has implemented; (2) external dependencies treated as versioned inputs, where a vendor driver or library release is an event in the history even though it lives in nobody's repository; (3) the workload mix as a tracked dimension, since a production regression can be caused by customer behaviour rather than by code and conflating the two wastes days; (4) noise handling calibrated to accelerator measurements, which are noisier than CPU benchmarks and where the repetition requirements are higher than the standard tooling assumes; and (5) the benchmark defined at the serving level under realistic concurrency rather than at the kernel level, since kernel benchmarks miss most of what regresses in production.

## Target Customer
Performance engineering teams, serving engine projects, and the continuous benchmarking tooling community for whom a multi-repository stack is an unserved shape.

## Impact If Solved
The practice is standard in every project where performance is the product, and this industry benchmarks reactively. Treating vendor driver and library releases as events in the version history is what makes bisection possible across a stack nobody fully owns.
