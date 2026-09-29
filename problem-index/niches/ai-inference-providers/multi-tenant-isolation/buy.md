# Resource Isolation From Operating Systems and Clouds

**Niche:** [[niches/ai-inference-providers/multi-tenant-isolation/profile|Multi-Tenant Isolation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cloud providers spent fifteen years on noisy neighbour isolation with cgroups, cache partitioning and interference-aware placement, and accelerator sharing started from nothing.
**Tags:** #markov-chains #evaluation-metrics #descriptive-statistics #change-point-detection #convex-optimization #automation #causal-inference #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to share an accelerator between tenants without one of them being able to affect another's latency — and whoever does that takes the account, because sharing is the only route to acceptable utilisation and the hardware was not built for it.

## The Problem
The noisy neighbour problem is the defining operational challenge of multi-tenant infrastructure and the cloud industry has an extensive answer: control groups for CPU, memory and I/O; last-level cache and memory bandwidth partitioning in modern processors; interference-aware placement informed by workload profiling; and published isolation guarantees per instance type. Accelerator sharing has coarse memory partitioning and placement by heuristic.

## What Already Exists
Control group resource limits with hierarchical enforcement; cache allocation and memory bandwidth allocation technologies in server processors; interference-aware scheduling research with workload profiling and co-location prediction; performance isolation benchmarking methodology; and cloud instance families with documented isolation properties.

## The Customization Gap
The adaptation is to hardware without the enforcement primitives. It requires: (1) software-level enforcement standing in for hardware partitioning, shaping the batch and the admission rate to bound a tenant's bandwidth consumption, which is indirect but is the only lever available and is currently unexploited; (2) workload profiling in accelerator terms — bandwidth intensity, cache footprint, kernel mix — since the co-location prediction literature depends on profiles and none exist for this hardware; (3) interference measured on a streaming workload, where the effect appears as inter-token variance rather than as a completion time, which requires a different metric than the co-location research uses; (4) placement across a fleet where migration means reloading model weights, so the cost of correcting a bad placement is much higher than moving a container; and (5) published isolation properties per tier, which the cloud industry treats as table stakes and this category does not offer at all.

## Target Customer
Inference providers, their platform teams, accelerator vendors, and the systems research community working on interference-aware placement.

## Impact If Solved
Fifteen years of noisy neighbour practice exists and accelerator sharing started from nothing. Software-level shaping of batch and admission rate is the only enforcement lever available on this hardware and it is unused; published isolation properties per tier are table stakes elsewhere.
