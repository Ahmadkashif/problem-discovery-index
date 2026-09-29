# Scheduling and Admission Control

**Niche:** [[niches/ai-inference-providers/model-serving-platforms/profile|Model Serving Platforms]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Operating systems, networks and datacentres spent decades on scheduling mixed workloads with different service classes, and inference schedulers mostly batch whatever arrived.
**Tags:** #markov-chains #dynamic-programming #convex-optimization #markov-decision-processes #optimization-fundamentals #evaluation-metrics #automation #probability-distributions
**Contested on:** Not terminal — the contest differs by whether latency is constrained, and the decomposition is recorded in the profile.

## The Problem
Running latency-sensitive and throughput-oriented work on shared hardware without the second ruining the first is one of the oldest problems in systems, and the answers are well developed: priority classes, weighted fair queueing, admission control that rejects rather than degrades, deadline scheduling, and quality-of-service guarantees with published policies. Inference serving arrived with continuous batching and largely stopped there.

## What Already Exists
Weighted fair queueing and hierarchical schedulers; real-time and deadline scheduling with admission tests; network quality-of-service with traffic classes and policing; datacentre schedulers with priority preemption and resource guarantees; and load shedding and admission control patterns from large-scale serving.

## The Customization Gap
The adaptation is to a request whose duration is unknown and whose cost depends on its batch-mates. It requires: (1) scheduling under unknown output length, since a request's service time depends on how many tokens it generates and that is not known at admission — predicting it from the prompt is tractable and is the piece the classical schedulers assume away; (2) batch composition as the scheduling decision, because the unit of work is a batch whose members interact and the classical models schedule independent jobs; (3) preemption at token boundaries with state retention, which this workload uniquely allows and which most stacks do not exploit; (4) admission tests expressed against a latency objective given current batch state, which is computable and would let a provider reject rather than silently degrade — the honest behaviour the category avoids; and (5) fairness defined over accelerator time rather than request count, since requests differ in cost by orders of magnitude and per-request fairness is not fairness.

## Target Customer
Inference providers, serving engine projects, and the systems scheduling community for whom this is a large and technically rich unclaimed application.

## Impact If Solved
Mixed-class scheduling is decades mature and inference stacks batch whatever arrived. Predicting output length at admission is the missing piece the classical machinery assumes away, and token-boundary preemption is an advantage this workload has and does not use.
