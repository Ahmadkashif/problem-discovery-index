# Near-Duplicate Detection Applied to a Clause Library

**Niche:** [[niches/esignature-document-workflow/template-and-clause-sprawl/profile|Template & Clause Sprawl]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Near-duplicate detection and semantic clustering are decades-old solved problems, and a four-hundred-template library has never been compared against itself.
**Tags:** #word-embeddings #bert #dbscan #k-means-clustering #dimensionality-reduction #evaluation-metrics #confidence-intervals #automation
**Contested on:** Every serious competitor in agreement content is fighting to guarantee that the clause in the document going out today is the one legal currently approves — and whoever can prove that across a whole library takes the legal operations account.

## The Problem
A library contains six templates that differ from one another in a single sentence, created by six people who each could not find the one that already existed. Finding them is near-duplicate detection, which search engines have done at web scale since the nineties and which runs on four hundred documents in seconds. Nobody has run it, so the library grows and the search problem that caused the duplication gets worse, which causes more duplication.

## What Already Exists
Shingling and minhash for near-duplicate detection; sentence and passage embedding models that judge semantic equivalence well; density-based and hierarchical clustering; and text diffing at every granularity. Legal-domain embedding models trained on contract text are available. All of it is free, fast at this scale, and thoroughly documented.

## The Customization Gap
The adaptation is to legal documents where small differences sometimes matter enormously. It requires: (1) clause-level rather than document-level comparison, since two templates are rarely duplicates as wholes and are frequently duplicates clause by clause, which is the granularity the library is maintained at; (2) legal-aware similarity that treats a changed number, a negation, or a swapped party as significant while treating formatting and defined-term substitution as noise — which is the opposite of what general semantic similarity does and is the whole adaptation; (3) a diff presentation aimed at a lawyer, showing what differs in substance rather than in characters, because the output is reviewed by someone whose time is the constraint; (4) merge proposals rather than automatic consolidation, since deciding that two clauses can be replaced by one is a legal judgement and the product's job is to make that judgement fast; and (5) usage evidence attached to every duplicate group, because the practical question is which of the six variants to keep and usage answers it.

## Target Customer
Legal operations teams, signature and contract lifecycle vendors, and the legal technology providers already selling clause analytics into the review side of the market.

## Impact If Solved
The technique is old, free and instant at this scale, and the analysis has never been pointed at the library it would help most. Legal-aware similarity is the one genuine adaptation and it is narrow: numbers, negations, parties and defined terms.
