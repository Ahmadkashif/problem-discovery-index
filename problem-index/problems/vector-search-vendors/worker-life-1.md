# Solutions Architect Explaining a Missing Document

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Type:** Worker Life Changing
**One-liner:** Solutions architects spend their days on the same question — why did my search not return this obviously relevant document — and answer it by manually reconstructing a pipeline the platform could explain itself.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #word-embeddings #bert #dimensionality-reduction #workflow-orchestration #worker-facing

## The Problem
A customer opens a ticket. They searched for something, a document they know is relevant was not in the results, and they want to know why.

The architect works backwards through a chain. Is the document in the index at all, or did ingestion fail silently. How was it chunked, and did the chunking split the relevant passage across a boundary so that neither half looks relevant. What is the embedding of the relevant chunk, and what is its actual similarity to the query embedding. Was it retrieved but ranked below the cut-off. Was a metadata filter excluding it. Was the query embedded with a different model version than the corpus.

Each step requires manual investigation with ad-hoc scripts. The answer is usually one of six things, the architect has diagnosed each of them many times, and there is no tool that runs the diagnosis.

Frequently the answer is unwelcome: the chunking strategy is wrong for this corpus, or the embedding model does not represent this domain well. Both are the customer's decisions, sit outside the database, and are difficult conversations because the vendor's product is technically working correctly.

## Why It Matters to the Worker
Solutions architects in this category are strong engineers doing the same forensic exercise repeatedly. The genuinely interesting work — helping a customer design retrieval for an unusual corpus — is crowded out by explaining individual misses.

The structural frustration is owning an outcome without owning the components. Retrieval quality depends on the embedding model, the chunking and the query, none of which the vendor controls, and the customer holds the vendor responsible because the vendor is who they are paying.

There is a commercial edge to it as well. Every one of these tickets is a moment where the customer wonders whether a different vector database would have found the document. The honest answer is usually no, and the architect has to establish that from scratch each time.

The pattern across tickets is also lost. An architect who has seen forty customers make the same chunking mistake has knowledge that would prevent the forty-first, and nothing captures it.

## What a Solution Looks Like
A retrieval explain function, in the product. Given a query and a document the customer expected, return the diagnosis: is the document indexed, how was it chunked, what is the similarity of each chunk to the query, where did it rank, which filters applied, and which embedding model version was used for each side.

Chunk boundary analysis specifically. A relevant passage split across a boundary is one of the most common causes and one of the least obvious, and it is directly detectable by checking whether a passage spanning two chunks would have scored higher.

Corpus-level diagnostics rather than per-query firefighting. Chunk length distribution, embedding space coverage, duplicate and near-duplicate density, and orphaned documents that are never retrieved by any query are all computable from the index and none are surfaced.

Configuration recommendations from the corpus itself. Optimal chunk size depends on document structure and length distribution, which the vendor can see, and is currently chosen from a blog post.

## Impact If Solved
Retrieval explanation is the single most common support interaction in this category and is performed by hand by expensive engineers. Making it a product feature converts a forensic exercise into a query, and the corpus-level diagnostics would prevent most of the tickets before they are opened.
