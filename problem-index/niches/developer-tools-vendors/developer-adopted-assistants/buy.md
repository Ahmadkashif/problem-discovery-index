# Retrieval and Latency Engineering, Applied to the Editor

**Niche:** [[niches/developer-tools-vendors/developer-adopted-assistants/profile|Developer-Adopted Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retrieval quality and tail latency are both well-developed engineering disciplines, and the assistant that wins the developer is decided on exactly those two properties rather than on model capability.
**Tags:** #word-embeddings #bert #large-language-models #graph-theory #evaluation-metrics #confidence-intervals #cross-validation #transfer-learning
**Contested on:** Every serious competitor here is fighting to be the assistant a developer keeps switched on after week three — and whoever wins that takes the account regardless of what was procured, because an unused licence is a cancelled one.

## The Problem
The properties that decide this market are which context is retrieved and how fast the suggestion arrives. Both are ordinary engineering problems with substantial literatures — information retrieval for the first, tail latency engineering for the second — and both are frequently treated as secondary to model selection, which is the visible and less decisive variable.

## What Already Exists
Dense and sparse retrieval with hybrid ranking; reranking models; code-specific embedding models; abstract syntax tree and call graph analysis for structural retrieval; speculative decoding and caching for latency; and the whole tail-latency engineering literature from serving systems. Language Server Protocol implementations already compute much of the structural information required.

## The Customization Gap
The adaptation is to code context under a hard latency budget. It requires: (1) structural rather than purely semantic retrieval, since the relevant context for a function is its callers, its type definitions and its tests, which a call graph identifies precisely and an embedding search approximates badly; (2) a latency budget treated as a hard constraint on the retrieval itself, because a better context that arrives two hundred milliseconds later loses to a worse one that is already on screen — the trade-off is real and is usually resolved in the wrong direction; (3) incremental index maintenance, since the repository changes under the developer continuously and a stale index produces confidently wrong context; (4) tail latency rather than mean, because the occasional two-second suggestion is what causes a developer to disable a feature, and means conceal exactly that; and (5) evaluation on the retrieval separately from the generation, since a bad suggestion from good context and a good model given nothing are different failures with different fixes and vendors routinely conflate them.

## Target Customer
Assistant and editor vendors, code search vendors whose indexing is directly applicable, and the infrastructure teams serving these models.

## Impact If Solved
The market is decided on retrieval and latency while attention goes to model choice, which is the visible variable rather than the decisive one. Structural retrieval and a hard latency budget are the two adaptations, and separating retrieval evaluation from generation evaluation is what makes improvement possible at all.
