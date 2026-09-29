# The Page That Did Not Need a Person

**Niche:** [[niches/mlops-platforms/the-on-call-ml-engineer/profile|The On-Call ML Engineer]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of overnight ML pages resolve to waiting for a late upstream table or rerunning a job, and both are automatable, and both wake somebody up.
**Tags:** #automation #workflow-orchestration #change-point-detection #descriptive-statistics #evaluation-metrics #worker-facing #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to make the page arrive with a diagnosis instead of a log file — and whoever does that takes the account, because the platform already recorded everything needed to produce one.

## The Problem
The pipeline starts at 02:00 and reads a table that a source system usually lands by 01:30. Twice a month it lands at 02:40. The task fails, the page fires, the engineer wakes up, looks, sees the table is not there yet, waits, reruns, and goes back to bed. Nothing was learned, nothing was decided, and nothing required a human — the job needed to wait forty minutes. The same pattern covers transient resource contention, a spot instance reclaimed, and a flaky network call. These pages are a substantial fraction of the total and every one of them is a person woken up to perform an action a scheduler could take.

## Why It's Still Broken
Retry policies are configured once at pipeline creation, usually as a fixed count with a fixed delay, and nobody revisits them because they are not anybody's job. Distinguishing a transient failure from a real one requires knowing the failure's history, which nothing tracks. Waiting on data readiness requires a readiness signal that upstream teams do not publish. And the cost is borne by whoever is on call, who is not the person who would have to fix it and is usually too tired to raise it.

## What a Fix Looks Like
Stop paging for things a scheduler can handle. Wait on data readiness rather than starting on a clock, which removes the single largest category outright and requires only that upstream freshness be checkable — which it usually is, even without a formal signal. Classify failures by their own history and retry the ones that have always been transient, escalating only when the pattern breaks, since the history is recorded and nobody reads it. Set retry policy from observed behaviour rather than from a default chosen at creation time, because a policy that has never been revisited is calibrated to nothing. Suppress the page when an automatic recovery succeeded and report it in the morning instead, which is the correct severity for something that fixed itself. Hold non-urgent failures until working hours, since a nightly retraining job that fails is frequently not urgent and paging for it is a convention rather than a decision — making that explicit per pipeline is a short exercise with a large return. Report the share of pages that required no human action, which is the metric that exposes the problem and is currently computed nowhere. And feed every automatic recovery back into the policy, so the system gets quieter rather than noisier over time.

## Who Feels the Pain
ML engineers woken for nothing, repeatedly, and the ones who leave over it; teams whose alert response degrades because most pages are noise; and the organisations paying for an on-call rota that is largely automatable.

## Impact If Fixed
Waiting on data readiness instead of a clock removes the largest category outright. Reporting the share of pages that needed no human action is computed nowhere and is the number that would make the problem fundable.
