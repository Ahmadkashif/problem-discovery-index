# Flaky Tests and the Collapse of Trust in the Signal

**Industry:** [[ci-cd-platforms|CI/CD Platforms]]
**Type:** High Impact
**One-liner:** A test that fails intermittently teaches engineers to re-run rather than investigate, and once that habit forms every failure is re-run — which means the pipeline stops being a signal at exactly the moment it matters.
**Tags:** #logistic-regression #gradient-boosting #hypothesis-testing #change-point-detection #confidence-intervals #feature-engineering #evaluation-metrics #causal-inference

## The Problem
A test fails. The engineer looks at it, does not believe it relates to their change, presses re-run, and it passes. They merge.

That interaction is the most consequential in continuous integration and it is corrosive. Once an engineer has learned that failures are often meaningless, they apply the same response to all failures. A genuine regression gets re-run, passes on a retry because of some other nondeterminism, and ships. The pipeline has become theatre.

Flakiness has many sources and they are well understood: timing assumptions, test order dependencies, shared state, unmocked network calls, resource contention on the runner, clock and timezone assumptions, and race conditions in the code being tested — which is the interesting case, because a flaky test sometimes indicates a real bug that only manifests under specific interleaving.

Every organisation of scale has a quarantine list and it grows. Tests are added to it during releases and never removed, which means coverage silently erodes in exactly the areas that were hardest to test reliably.

The platform sees every execution. It knows which tests pass and fail on identical code, on which runners, in what order, at what time, and it presents a red or green result.

## Why It's Unsolved
Detection looks easy and is not. The simple definition — different results on the same commit — requires re-running, which is expensive, and misses tests that fail intermittently across different commits without ever being re-run on the same one. Distinguishing a flaky test from a test that correctly catches a nondeterministic bug is genuinely hard and matters enormously, since the two demand opposite responses.

Ownership is the structural problem. A flaky test belongs to whoever wrote it, who may have left, and fixing it is unrewarded work that competes with feature delivery. Quarantine is the path of least resistance and it is a one-way door in practice.

The cost is diffuse. Re-runs consume compute and, more importantly, engineer attention in fragments that never appear anywhere. Nobody can state what flakiness costs the organisation, so nobody funds fixing it.

And the platforms' incentives are mildly adverse: re-runs are billed minutes.

## What a Solution Looks Like
Flakiness inferred statistically across the whole execution history rather than by re-running. A test whose failures show no relationship to the changes that preceded them is flaky, and that is a testable proposition on data the platform already has, without a single extra execution.

Cause classification, because the remedy differs. Timing, order dependence, shared state, resource contention and genuine nondeterminism in the system under test have different signatures — correlation with runner load, with execution order, with parallelism level, with time of day — and separating them turns a flaky test list into a work queue.

The distinction between a lying test and a test detecting a real race is the highest-value output and the hardest, and it deserves to be flagged for human judgement rather than automated away, because quarantining a test that was correctly catching a race is how a serious bug reaches production.

Cost quantification: engineer-hours and compute lost to re-runs, attributed to specific tests, which converts an invisible drag into a ranked list with a number attached.

And quarantine with an expiry, because a quarantine list without one is a coverage decision nobody made.

## Impact If Solved
Flakiness destroys the trust that makes continuous integration worth having, and the response it trains — re-run everything — silently allows real regressions through. Statistical detection with cause classification requires no extra executions, and quantifying the cost is what finally makes fixing it competitive with feature work.
