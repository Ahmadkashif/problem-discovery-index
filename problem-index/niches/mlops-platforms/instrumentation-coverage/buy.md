# Auto-Instrumentation From the Observability World

**Niche:** [[niches/mlops-platforms/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Application monitoring solved zero-code instrumentation years ago with runtime agents and bytecode injection, and ML tracking still asks people to edit their training scripts.
**Tags:** #data-integration #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #quick-win #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make tracking work on the training code an organisation actually runs rather than on the frameworks the vendor supports — and whoever does that takes the account, because the unsupported code is where the important models live.

## The Problem
Application performance monitoring faced precisely this problem — get telemetry out of code nobody will modify — and solved it with runtime agents that attach to a process and instrument it without a source change. That capability is mature, widely deployed, and covers arbitrary application code. ML tracking asks a researcher to import a client, call an initialisation function, and log each metric explicitly, which is why coverage stops where enthusiasm stops.

## What Already Exists
Runtime auto-instrumentation agents that attach without code changes; open telemetry standards with automatic library instrumentation; continuous profilers that attach to running processes; orchestrator event streams carrying task metadata; container and process introspection; and storage access logging that reveals what a job read and wrote.

## The Customization Gap
The adaptation is to a workload whose interesting events are semantic rather than structural. It requires: (1) recognising training-shaped operations — an epoch, a metric computation, a checkpoint write, a model save — from generic runtime signals, which is the domain knowledge the observability agents lack and is the substance of the work; (2) treating the orchestrator task as the primary run identity, since it is present for every pipeline regardless of language and is the most reliable anchor available; (3) capturing hyperparameters from configuration and command-line arguments rather than from an explicit call, which covers a surprising share of real pipelines because the parameters are already externalised; (4) operating with degraded fidelity gracefully and labelling it, since a derived run is not equivalent to an instrumented one and pretending otherwise poisons the data; and (5) language coverage beyond the obvious, since the untracked estate is disproportionately in languages the ML tooling ecosystem has ignored, which is exactly why it is untracked.

## Target Customer
Platform engineering teams, tracking vendors seeking coverage beyond their adapter set, and the observability vendors for whom training jobs are an unserved workload.

## Impact If Solved
Zero-code instrumentation is a solved discipline and unapplied here. Anchoring run identity to the orchestrator task works for every pipeline regardless of language, which is precisely the estate the adapter model cannot reach.
