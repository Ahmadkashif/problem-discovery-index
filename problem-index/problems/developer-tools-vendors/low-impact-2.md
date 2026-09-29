# Large Repository Performance

**Industry:** [[developer-tools-vendors|Developer Tools Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every tool in the category works well up to a repository size and degrades past it, and the customers who cross that line are the largest, most valuable and least able to switch.
**Tags:** #dimensionality-reduction #k-nearest-neighbors #graph-theory #feature-engineering #evaluation-metrics #automation #workflow-orchestration

## The Problem
Software tooling is largely built and benchmarked against repositories of ordinary size. Past a certain scale — a large monorepo, a decade-old codebase, a repository with deep history — everything degrades together. Indexing takes hours. Search becomes slow enough to break flow. The editor's language features time out. Cloning is a coffee break. Code review interfaces struggle on large changes. Assistants lose the thread because the relevant context is far larger than any window.

The organisations affected are the ones with the most developers and the most money, and they respond by building internal infrastructure: custom indexing, virtual file systems, sparse checkouts, bespoke code search. That work is duplicated at every large company, is expensive, and is a permanent tax on exactly the customers who pay the most.

The vendors know this and treat it as an enterprise scalability issue rather than as a product problem, which means each new capability ships working well at small scale and poorly at large.

## What Already Exists
Virtual file systems and partial clone are available in Git and are used by large organisations. Build systems like Bazel and Buck handle monorepo builds at scale. Sourcegraph and internal equivalents provide code search across large estates. Tree-sitter enables incremental parsing. Sparse checkout and shallow clone reduce local footprint. Several large companies have published their approaches.

## The Customisation Gap
Relevance is the missing abstraction. Tools attempt to index and analyse everything, when a developer works within a small, predictable neighbourhood of a large codebase. Predicting which parts of a repository this developer will touch — from their history, their team's ownership, the change they are currently making and the dependency graph — would let indexing, prefetching and context selection be prioritised rather than exhaustive.

Context selection is the same problem in its newest form. An assistant working in a large codebase must choose what to include, and the naive approaches — nearest files, recent files, embedding similarity — miss the semantically relevant code that a dependency graph would find immediately.

Incremental analysis at every layer is the third gap. Full re-indexing on change is common in tooling and unnecessary; the dependency graph determines what actually needs recomputation, and most tools do not use it.

Change impact prediction closes the loop: which tests, which reviewers, which downstream services are affected by this change is computable from the graph and is currently approximated by running everything.

## Impact If Solved
Large repositories are where the most valuable customers live and where every tool is worst, and each of those customers is independently rebuilding the same infrastructure. Relevance prediction and incremental analysis are the shared solution, and they are also exactly what makes assistants work at scale.
