# Rulemaking Impact Routing Across a Dependent Content Corpus

**Niche:** [[niches/charter-bus-operators/transport-compliance-publishers/profile|Transportation Regulatory Compliance Publishers]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A single rule change can invalidate wording in four hundred places across manuals, forms, training modules, and audit checklists, and finding them is a full-text search followed by editorial memory.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #evaluation-metrics #transfer-learning #compliance #data-integration #workflow-orchestration

## The Problem
The corpus is a dependency structure presented as a library. A requirement — a retention period, a qualification threshold, an inspection interval — appears in a regulation, then propagates into an interpretive manual, a training module, a wall chart, a recordkeeping form, an audit checklist, and a managed service procedure, written by different editors across many years. When the underlying rule changes, every one of those has to move. The current method is to search for the regulatory citation, which finds the places that cite it explicitly and misses everything that inherited the requirement without citing the source — a checklist that adopted a threshold from a sibling document, a training script that paraphrased a manual paragraph. Editors close the gap from memory, which works while the people who wrote the content are still there and degrades quietly when they are not. For a publisher whose customers face five-figure fines for following outdated guidance, that is the wrong failure mode to be exposed to.

## Why Nobody Has Built This
The content grew document by document over decades across print, digital, training, and service delivery, in different systems with different structures, and nothing captured the semantic relationships between them. Regulatory citation is also an unreliable index: much of the interpretive value the publisher adds is precisely in stating a requirement operationally without quoting the regulation, so the most useful content is the least citation-linked. Reconstructing the dependency graph therefore means mining meaning rather than references, which has been out of reach until recently and remains a substantial undertaking.

## What to Build
An engine that indexes the corpus at the requirement level rather than the document level. Each operative requirement becomes an addressable object — the retention period, the interval, the threshold — with its regulatory basis, its interpretation, and every place it is expressed across manuals, training, forms, and service procedures, whether by citation or by inheritance. Building that graph is the substantive work and is done once by mining the existing content, then maintained as editors write. Incoming rulemakings, guidance documents, and enforcement actions are then resolved against requirements rather than against documents, so a proposed rule arrives as a scoped work order: these eleven requirements are affected, expressed in these forty-three places, here is each one's current wording and its regulatory basis. The queue sorts by exposure — how many customers rely on the affected content and what the penalty for following it wrongly would be — rather than by arrival order. State-level rules attach to the same requirements, which is what makes the multi-jurisdiction picture tractable at all.

## Target Customer
VPs of editorial and directors of regulatory content at compliance publishers running 50-200 editors, and the managed-service leaders whose delivered procedures inherit the same requirements and currently update on a separate track.

## Impact If Built
Turns rulemaking response from a search-and-remember exercise into a bounded task, which is the difference between a corpus that is defensibly current and one that is merely recently reviewed. It also removes the dependency on editorial memory that is the publisher's real continuity risk, and it produces a provenance trail — why this sentence says what it says — that is directly useful the first time a customer's reliance on the guidance is questioned.
