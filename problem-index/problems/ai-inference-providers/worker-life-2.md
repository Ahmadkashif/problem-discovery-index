# Performance Engineer Chasing Regressions

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Type:** Worker Life Changing
**One-liner:** Performance engineers spend their time bisecting latency regressions across a stack where the serving engine, the driver, the kernel library, the model and the hardware all change independently and none of it is version-locked.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #descriptive-statistics #gradient-boosting #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
Latency for a model rises fifteen per cent. The engineer must find out why.

The candidates are numerous and independent. The serving engine was upgraded — vLLM moves quickly. The CUDA driver changed. A kernel library was updated. The model weights were reloaded, possibly with a different quantisation. The traffic mix shifted toward longer prompts. Batch composition changed because a co-tenant's pattern changed. The workload landed on a different hardware generation. Thermal throttling in a specific rack.

Bisecting means reproducing, which means holding all the other variables still — and the stack is not version-locked, the traffic is live, and the hardware is shared. Reproduction in a controlled environment is possible and does not reproduce production conditions, which is frequently where the regression actually lives.

The measurement itself is noisy. Latency at high percentiles is genuinely variable, so a fifteen per cent move may be a real regression or may be a shift in the request mix, and establishing which comes first.

## Why It Matters to the Worker
These are among the most specialised engineers in the industry, capable of writing kernels and reasoning about memory hierarchies, and they spend a large share of their time on attribution rather than optimisation.

The dependency churn is relentless. The open serving engines release frequently and the improvements are real, so staying current is necessary and each upgrade is a potential regression the engineer will be asked to explain.

The unfalsifiability is demoralising. Many investigations end without a definitive cause — the regression is real, several things changed, and reproduction was not possible. Closing an investigation with a hypothesis rather than an answer is professionally uncomfortable and happens often.

And the work is invisible. A regression found and fixed restores the previous state, which nobody notices.

## What a Solution Looks Like
Continuous benchmarking on production hardware with every stack component version-tracked. A fixed workload run continuously across the fleet, with results attributed to serving engine version, driver, kernel library, model build and hardware generation, converts bisection into a query.

Statistical change point detection on latency series that accounts for request mix. Separating a genuine regression from a shift in prompt length distribution is the first question in every investigation and is answerable automatically by conditioning on the mix.

Attribution against the change log. When a change point is detected, listing what changed in the same window across every component — with the fleet as a natural control group, since not every node upgrades simultaneously — narrows the candidate list immediately.

Canary deployment as the default for stack changes, so a regression is caught on a small fraction of traffic with a clean comparison rather than discovered globally.

Cross-fleet comparison. Nodes running different versions at the same time are a natural experiment, and the provider has thousands of them.

## Impact If Solved
Performance engineering capacity is the scarcest resource in this category and most of it goes to attribution rather than optimisation. Continuous benchmarking with version attribution turns a multi-day bisection into a lookup, and canary deployment prevents the regressions from reaching the fleet at all.
