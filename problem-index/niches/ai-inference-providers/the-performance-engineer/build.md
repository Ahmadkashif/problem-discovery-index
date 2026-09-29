# Five Layers Moving Independently

**Niche:** [[niches/ai-inference-providers/the-performance-engineer/profile|The Performance Engineer]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Performance engineers spend their time bisecting latency regressions across a stack where the serving engine, the driver, the kernel library, the model and the hardware all change independently and none of it is version-locked.
**Tags:** #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #descriptive-statistics #automation #worker-facing #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to attribute a latency regression to the layer that caused it without a person bisecting five independently-moving components — and whoever does that takes the account, because that bisect is most of a performance engineer's week.

## The Problem
Tail latency on a heavily-served model rose nine percent over a fortnight. In that window the serving engine took two minor releases, the driver was updated on part of the fleet, the kernel library shipped a patch, the quantised weights were regenerated, and the customer mix shifted toward longer prompts. The engineer re-runs benchmarks holding one variable at a time, on hardware shared with production, where run-to-run variance is comparable to the regression being chased. Four days later they identify the kernel library patch. Every version was recorded somewhere; nothing recorded them together.

## Why Nobody Has Built This
Several layers belong to vendors and open projects with their own release cadences, so pinning everything conflicts with taking security and performance fixes. Continuous benchmarking requires dedicated hardware, which competes directly with revenue-serving capacity and loses that argument every time. Performance engineers build for the current fire. And the cost is diffuse — days here and there — so it never becomes a project.

## What to Build
Record the stack and attribute automatically. Capture a full manifest with every performance measurement — serving engine, driver, kernel library, model artefact hash, hardware model and firmware, workload mix — which is mechanical, cheap, and the precondition for attribution that nothing currently does. Diff manifests between any two measurements and report what changed, which converts the first day of every investigation into a query. Run a continuous benchmark suite on reserved, uncontended hardware, since a clean baseline is what makes a regression detectable at all and the capacity argument against it is won by comparing a few accelerators against days of engineer time repeatedly. Treat measurement statistically: repeat, report intervals, and require a regression to clear the noise before it is chased, because a large share of investigations are of movements that were never real. Attribute by replaying the benchmark across historical manifests, which is a designed experiment rather than a manual bisect and parallelises. Alert on regressions at detection rather than at customer complaint. Extend the manifest to production measurements, so the mixed fleet's heterogeneity is an analysable variable rather than a confound. And track which layers historically cause regressions, which is a prior that would shorten every future investigation.

## Target Customer
Performance engineering teams at the providers, the serving engine projects, and the accelerator and library vendors whose releases are the unattributed cause.

## Impact If Built
Every version is recorded and nothing records them together. A manifest diff turns the first day of each investigation into a query, and a continuous benchmark on uncontended hardware is what makes a nine-percent regression detectable rather than debatable.
