# Paged at Three to Read Logs

**Niche:** [[niches/mlops-platforms/the-on-call-ml-engineer/profile|The On-Call ML Engineer]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Machine learning engineers are paged at three in the morning for training pipelines that failed for reasons the platform recorded and did not diagnose, and most of what they do on that page is read logs.
**Tags:** #large-language-models #change-point-detection #graph-theory #evaluation-metrics #gradient-boosting #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to make the page arrive with a diagnosis instead of a log file — and whoever does that takes the account, because the platform already recorded everything needed to produce one.

## The Problem
The page fires at 03:12: nightly retraining pipeline, task failed. The engineer opens a laptop, finds the log, scrolls past a stack trace to an out-of-memory error, checks whether the input grew, finds that an upstream backfill tripled the partition size, allocates more memory, reruns, and goes back to bed at 04:40. Every fact in that sequence was in the platform at the moment the page fired: the exception, the input size against its history, the upstream backfill event, the memory allocation, and the fact that the same pipeline with the same signature was fixed the same way in March.

## Why Nobody Has Built This
Vendors are organised around the training experience rather than the operations experience, and the on-call engineer is not the buyer nor the evaluator. Orchestration is a separate product from tracking in most stacks, so the failure context and the run context sit in different systems owned by different vendors. Diagnosis requires being confidently right, and a wrong diagnosis at three in the morning is worse than none — which is a real risk that has been treated as a reason not to try rather than as a design constraint. And nobody measures on-call load for ML teams, so the cost is not visible where budgets are set.

## What to Build
Put the diagnosis in the page. Assemble the context automatically at failure time — exception and its classification, input data statistics against their own history, upstream task outcomes and data readiness, resource utilisation against allocation, recent code and configuration changes, and the last successful run's differences — because that assembly is the bulk of the engineer's work and is entirely mechanical. Match the failure signature against the organisation's own history and surface what resolved it last time, since ML pipeline failures repeat heavily and the resolution is usually already known to somebody. Rank candidate causes with confidence and evidence rather than asserting one, which makes a wrong suggestion cheap to dismiss and is the design answer to the confidently-wrong risk. Classify by urgency, so that a transient resource failure, a late upstream dependency and a genuine data corruption produce different responses — the first two frequently need no person at all, which the fix note develops. Estimate the blast radius: which models, which downstream consumers, whether tomorrow's predictions are affected, because that is the second question always asked and it is answerable from lineage. Assemble the timeline for the morning review automatically. And measure time-to-diagnosis and page volume per engineer, since that is how the improvement gets funded.

## Target Customer
ML engineering organisations with a real on-call rota, the leaders losing people to it, and the tracking and orchestration vendors on either side of the context gap.

## Impact If Built
Everything the engineer reconstructs at three in the morning was already recorded. Matching against the organisation's own resolved history is the part that compounds, and ranking candidates with evidence is what makes a wrong suggestion cheap rather than dangerous.
