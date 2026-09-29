# Experiment Tracking Platforms

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** High Market Share
**Contested on:** Not terminal — the contest differs by workload scale, and the decomposition is recorded below.

## Profile
**Market Size:** ~$820M US
**Share of Parent Industry:** ~27% of category revenue
**Digital Adoption:** High
**Target Buyer:** Research teams; separately, ML infrastructure teams
**Automation Potential:** High

## What Makes This a Distinct Niche
This is the product every vendor in the category actually sells: capture what a training run was, what it produced, and how it compared to the runs before it. It is the largest revenue line and the one with the most direct competition.

It is **not terminal**, and the reason is that "experiment tracking" describes an interface rather than a contest. A data science organisation running ten thousand cheap sweeps a month is fighting over comparability across a large population — reproducing a result from four months ago, finding which of four hundred configurations actually differed, spending its search budget well. An ML infrastructure team running one distributed job for sixty days across a thousand accelerators is fighting to notice a loss curve diverging at hour forty, to distinguish a genuine instability from a straggling node, and to recover from a checkpoint without losing a week. The telemetry volumes differ by orders of magnitude, the failure modes have nothing in common, the buyers sit in different organisations, and the alternatives they compare against are a spreadsheet in one case and a bespoke telemetry stack in the other. Filter Notes in the overview records the two rejected alternatives; the sub-niches below are the split by scale.

## Current Tools & Gaps
Run logging clients, metric dashboards, artefact and model registries, hyperparameter sweep orchestration, and report generation. The gaps are scale-specific and are stated in the sub-niches.

## Problems
- [[niches/mlops-platforms/experiment-tracking-platforms/build|🔨 Build: An Interface That Spans Two Unrelated Contests]]
- [[niches/mlops-platforms/experiment-tracking-platforms/buy|🛒 Buy: Versioning and Provenance Infrastructure]]
- [[niches/mlops-platforms/experiment-tracking-platforms/fix|🔧 Fix: Recorded Faithfully, Not Reproducible]]

### Contested sub-niches
- [[niches/mlops-platforms/classical-ml-experimentation/profile|🎯 Classical ML Experimentation]]
- [[niches/mlops-platforms/large-scale-training-runs/profile|🎯 Large-Scale Training Runs]]
