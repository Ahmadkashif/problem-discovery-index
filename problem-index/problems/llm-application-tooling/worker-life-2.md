# Maintaining a Prompt Library

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Type:** Worker Life Changing
**One-liner:** Prompt libraries grow into hundreds of overlapping templates that nobody can safely delete, because no one knows which are in use, which duplicate each other, or what any of them do that matters.
**Tags:** #bert #word-embeddings #k-means-clustering #large-language-models #evaluation-metrics #hypothesis-testing #workflow-orchestration #worker-facing

## The Problem
An application starts with a few prompts. Two years later there are hundreds, spread across a prompt registry, application code, configuration files and a notebook someone used for an experiment that reached production.

They overlap heavily. Six variants of a summarisation prompt exist because six engineers needed one and none found the others. Several are dead — the code path was removed and the prompt was not. Many contain accumulated instructions added to fix specific cases, some of which contradict each other and none of which are documented.

Nobody deletes anything, because determining whether a prompt is used requires tracing call sites through dynamic construction and configuration lookups, and the cost of being wrong is a production failure.

The person maintaining this is usually the engineer who has been on the project longest, and their knowledge of which prompt does what is the only documentation.

New engineers write new prompts rather than reusing existing ones, because finding an existing prompt requires knowing it exists, which makes the sprawl self-reinforcing.

## Why It Matters to the Worker
The maintainer becomes a bottleneck and a single point of failure. Every change touching prompts routes through them because they are the only person who knows what will break.

The work has no end and produces nothing visible. Nobody notices a well-organised prompt library; everybody notices a production incident caused by deleting the wrong one.

The accumulated instructions are the specific frustration. A prompt with forty lines of case-specific guidance added over two years is unreadable, cannot be reasoned about, and is nearly impossible to improve — any edit risks breaking a case that some instruction was added to handle, and the engineer does not know which instruction handles which case.

And the fear of deletion means the library only grows, which makes every subsequent change harder.

## What a Solution Looks Like
Usage tracking from production traces. Which prompts actually execute, how often and in which code paths is directly observable from the traces the application already emits, and it makes deletion safe rather than a gamble.

Duplicate and near-duplicate detection. Semantic similarity over prompt text identifies the six summarisation variants immediately and is trivially available.

Instruction-level attribution through ablation. Replaying historical inputs with individual instructions removed shows which lines actually change behaviour, which are dead, and which conflict — turning an unreadable forty-line prompt into a set of measured components.

Provenance capture. Recording why an instruction was added, ideally linked to the failure that prompted it, converts institutional memory into documentation and is a small workflow change with a large effect.

Consolidation proposals rather than manual reconciliation, with the behavioural equivalence of merged variants tested against production replay before anyone commits.

## Impact If Solved
Prompt sprawl is the technical debt of LLM applications and it compounds because deletion is unsafe and duplication is easier than discovery. Usage tracking makes pruning possible, ablation makes long prompts legible, and both use trace data the tooling already collects.
