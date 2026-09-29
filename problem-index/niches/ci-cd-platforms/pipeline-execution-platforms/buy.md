# Scheduling and Caching Are Solved Somewhere Else

**Niche:** [[niches/ci-cd-platforms/pipeline-execution-platforms/profile|Pipeline Execution Platforms]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cluster scheduling, content-addressed caching and dependency-graph execution are mature disciplines with open implementations, and most pipelines are a sequence of shell commands run in order.
**Tags:** #graph-theory #dynamic-programming #optimization-fundamentals #convex-optimization #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to be where an organisation's pipelines actually run — and that contest is fought on economics in one market and on control in another, which is why this niche is not terminal and is decomposed below.

## The Problem
Placing work on machines to minimise completion time subject to resource constraints is cluster scheduling, with decades of research and mature open implementations. Executing only the parts of a dependency graph whose inputs changed is what modern build systems do. Content-addressed caching with remote execution is proven at very large scale. A typical pipeline runs steps in the order they were written, on a fresh machine, with a cache key somebody guessed.

## What Already Exists
Cluster schedulers with resource-aware placement; dependency-graph build systems with remote caching and execution; content-addressed storage; critical path analysis; bin packing and job shop scheduling literature; and workflow engines with dependency semantics. All mature, most open.

## The Customization Gap
The adaptation is to pipelines defined as scripts by people who are not build engineers. It requires: (1) dependency inference rather than declaration, since the value of the graph is available only if the customer does not have to write it — observing file access and environment use during execution is the practical route and is what distinguishes this from asking everyone to adopt a build system; (2) correctness guarantees for skipping, because an incorrect skip produces a build that passes and should not have, which is a far worse failure than a slow build and will end adoption immediately; (3) cache key derivation that is automatic and conservative, since hand-written cache keys are the most common source of both cache misses and stale results; (4) scheduling that optimises the critical path of the pipeline rather than machine utilisation, because the objective is developer waiting time and a scheduler tuned for throughput will make it worse; and (5) incremental adoption, so that a pipeline can be partially modelled and partially imperative, which is the only realistic migration path.

## Target Customer
CI platform vendors, build system vendors, platform engineering teams, and the remote execution service providers.

## Impact If Solved
The scheduling and caching disciplines are mature and the category executes shell scripts in order, which leaves a large and well-understood gap. Dependency inference without declaration is the adaptation that makes it adoptable, and correctness of skipping is the property everything depends on.
