# Distributed Systems Observability

**Niche:** [[niches/mlops-platforms/large-scale-training-runs/profile|Large-Scale Training Runs]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A distributed training job is a distributed system, and the observability industry has spent fifteen years on exactly the problems these teams are solving with custom dashboards.
**Tags:** #time-series-forecasting #change-point-detection #data-integration #evaluation-metrics #automation #graph-theory #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to tell an infrastructure team, while a sixty-day distributed run is still going, whether it is healthy and what to do about it — and whoever does that takes the account, because the run costs more than every tool in the stack combined.

## The Problem
Tail latency analysis, straggler detection, high-cardinality metric storage, distributed tracing across processes, and telemetry pipelines that handle millions of points per second are mature, well-understood capabilities with several strong products behind them. A training job with a thousand ranks has all of those problems and the teams running them build dashboards from first principles, because the observability industry and the ML infrastructure world do not talk to each other.

## What Already Exists
High-cardinality time series databases built for per-instance metrics at scale; distributed tracing with context propagation across process boundaries; straggler and tail latency analysis methods; telemetry collection standards with high-throughput collectors; profiling infrastructure with continuous production profiling; and alerting on multi-dimensional aggregates.

## The Customization Gap
The adaptation is to a workload whose health metric is a learning curve rather than a request. It requires: (1) the step as the unit of time rather than the wall clock, since every meaningful comparison in training is per-step and every observability tool assumes wall-clock windows; (2) collective communication as a first-class traced operation, because the synchronisation barrier is where a single slow rank becomes everyone's problem and generic tracing has no concept of it; (3) gradient and numerical statistics as monitored signals, which is the domain-specific part with no analogue in the observability world and is where the training-specific failures show; (4) cardinality shaped by rank rather than by service, which is a large but bounded and highly regular dimension the storage engines handle well once modelled correctly; and (5) retention tuned to a job's lifetime rather than a rolling window, since the useful comparison is against this run's own first hour and against previous runs, not against yesterday.

## Target Customer
ML infrastructure teams, observability vendors for whom training is an unserved workload, and the accelerator cloud providers whose customers are debugging these jobs blind.

## Impact If Solved
Straggler detection and high-cardinality telemetry are solved problems being re-solved with custom dashboards. Treating the step as the time unit and collective communication as a traced operation is what makes the mature tooling fit.
