# Change Attribution and Continuous Benchmarking

**Niche:** [[niches/llm-application-tooling/the-applied-ai-engineer/profile|The Applied AI Engineer]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Performance engineering runs continuous benchmarks with deployment markers and automated bisection, and quality engineering in this category runs nothing between incidents.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #automation #workflow-orchestration #descriptive-statistics #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to tell an engineer which of five simultaneously-moving things caused a quality change — and whoever does that takes the account, because that attribution is most of the job and nothing supports it.

## The Problem
Detecting that a metric regressed, attributing it to a change, and confirming the fix is standard practice wherever performance matters: a benchmark suite runs continuously, deployment markers annotate the timeline, statistical change detection flags a shift, and bisection narrows it to a cause. The tooling is public and the discipline is ordinary. This category has the harder version of the problem — several of the moving parts belong to other companies — and runs no continuous measurement at all.

## What Already Exists
Continuous benchmarking with historical tracking and dedicated runners; statistical change detection on noisy series; automated bisection over a change history; deployment and configuration markers on metric timelines; and experiment tracking joining a result to the configuration that produced it.

## The Customization Gap
The adaptation is to a benchmark whose grading is itself a model and whose dependencies are third parties. It requires: (1) external dependencies as first-class events on the timeline, since a provider's undisclosed update is the change most likely to be responsible and appears in no changelog — synthesising that event from a canary probe is the key addition; (2) grading noise accounted for separately from model noise, because the judge is stochastic too and conflating the two sources inflates the apparent variance; (3) repetition sized to the noise, since a single run per configuration cannot support the comparisons teams are making; (4) bisection over a configuration space rather than a commit history, which is a modest generalisation nobody has built for this domain; and (5) cost-aware scheduling, since each benchmark run costs model calls and the suite should be small and frequent with a larger one on change.

## Target Customer
Applied AI teams, tooling vendors, and the continuous benchmarking community for whom a third-party-dependent quality metric is a new shape.

## Impact If Solved
The practice is ordinary wherever performance matters and absent here, on a harder version of the problem. Synthesising a provider-change event from a canary probe puts the most likely cause on the timeline, where no changelog will ever put it.
