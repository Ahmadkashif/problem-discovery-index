# Compiler Autotuning and Search

**Niche:** [[niches/ai-inference-providers/model-optimisation-per-target/profile|Model Optimisation Per Target]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Autotuning compilers, superoptimisation and library generators solved searching a huge implementation space against a measured objective, and inference optimisation still ends in a person trying things.
**Tags:** #bayesian-optimization #gaussian-processes #convex-optimization #transfer-learning #gradient-boosting #evaluation-metrics #optimization-fundamentals #numerical-methods
**Contested on:** Every serious competitor in this niche is fighting to serve a new architecture at near-peak hardware efficiency on the day it is released rather than six weeks later — and whoever does that takes the account, because the window between a model's release and its commoditisation is where the margin is.

## The Problem
Searching an enormous space of implementation choices against measured performance is what autotuning has done since the numerical library generators of the nineties, and deep learning compilers extended it with learned cost models and transfer across kernels. The methodology is public, implemented and effective. The architecture-level decisions in inference serving — which the kernel autotuners do not reach — are still made by an engineer trying configurations.

## What Already Exists
Autotuning compilers with learned cost models and search over schedules; automatically tuned numerical library generators; superoptimisation for instruction sequences; Bayesian and multi-fidelity optimisation for expensive objectives; and performance modelling with roofline analysis for bounding achievable throughput.

## The Customization Gap
The adaptation is to the level above the kernel, where the decisions are architectural. It requires: (1) the search space spanning serving-level choices — batching policy, cache configuration, parallelism strategy, quantisation placement — rather than only loop schedules, which is where the remaining gains are and where no autotuner operates; (2) an objective that is throughput at a latency constraint rather than raw kernel speed, since the fastest kernel does not always produce the best served throughput and optimising the wrong objective is a real and common error here; (3) transfer across architectures rather than across input shapes, which is a different and more valuable form of transfer than the compiler work targets; (4) quality as a constraint, since quantisation and approximation choices enter the same search and a configuration that is fast and degraded is not a solution — this coupling is unique to this setting; and (5) evaluation under realistic batch composition, because measuring at concurrency one selects configurations that do not win in production.

## Target Customer
Inference providers, serving engine projects, compiler teams, and the autotuning research community for whom the serving level is an unclaimed layer.

## Impact If Solved
Autotuning solved the kernel level and the remaining gains are a level above it. Optimising throughput at a latency constraint rather than raw kernel speed, with quality as a search constraint, is what makes the machinery fit this setting.
