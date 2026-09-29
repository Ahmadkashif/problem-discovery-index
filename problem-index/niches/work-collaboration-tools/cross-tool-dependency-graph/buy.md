# Entity Resolution and Critical Path, Applied Across Tools

**Niche:** [[niches/work-collaboration-tools/cross-tool-dependency-graph/profile|Cross-Tool Dependency Graph]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution, relation extraction and critical path analysis are all mature with free implementations, and the work tool estate applies none of them.
**Tags:** #graph-theory #bert #large-language-models #transfer-learning #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in integration is fighting to turn pairwise field syncing into a single graph of what blocks what across the whole tool estate — and whoever holds that graph owns the question every executive asks and no integration answers.

## The Problem
Deciding that two records in different systems describe the same thing is entity resolution, solved for decades in customer data and master data management. Pulling a stated relationship out of a sentence is relation extraction, which language models do well. Finding the longest chain through a dependency graph is critical path, which predates all of this by half a century. The work tool estate needs exactly these three and uses none of them, connecting its tools with field-mapping rules instead.

## What Already Exists
Entity resolution frameworks, blocking and matching libraries, and probabilistic record linkage are mature and free. Sentence embedding models handle semantic similarity between differently-worded titles. Language models extract stated relationships from prose reliably enough for a confirm-before-acting workflow. Graph libraries provide critical path, cycle detection and reachability. Project management's scheduling literature is extensive. Every component is available.

## The Customization Gap
The adaptation is to work items across heterogeneous tools. It requires: (1) matching features suited to work rather than to people — title similarity, shared participants, temporal proximity, explicit links and reference patterns, since the customer-matching features that make record linkage tractable do not exist here; (2) a precision-weighted threshold, because a false merge of two distinct pieces of work produces a graph people stop trusting after one instance, and the correct default is to leave things unmerged and offer the match; (3) relation extraction tuned to the vocabulary teams actually use — "waiting on", "after the API lands", "once legal signs off" — which is narrow enough to work well and varied enough that a rule set will not cover it; (4) confidence and provenance on every edge, with the source sentence shown, since a dependency a user cannot trace is a dependency they will not act on; and (5) incremental maintenance, because the graph changes continuously and a nightly rebuild is both wasteful and too slow for the notification that matters.

## Target Customer
Integration platform vendors, work management vendors extending beyond their own data, and internal platform teams at companies large enough to have a dedicated tooling function.

## Impact If Solved
Every technical component is mature and the assembly has not been done for this domain, which is an unusually favourable position. The binding constraint is precision on entity resolution rather than anything about the graph analysis, and that constraint is manageable with a confirm-before-merge design.
