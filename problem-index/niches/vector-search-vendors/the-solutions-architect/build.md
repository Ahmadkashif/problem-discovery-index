# Why Was This Document Not Returned

**Niche:** [[niches/vector-search-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Solutions architects spend their days on the same question — why did my search not return this obviously relevant document — and answer it by manually reconstructing a pipeline the platform could explain itself.
**Tags:** #k-nearest-neighbors #norms-and-inner-products #evaluation-metrics #graph-theory #worker-facing #automation #descriptive-statistics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make the platform explain why a document was not returned — and whoever does that takes the support load, because that one question is most of the category's solutions engineering.

## The Problem
A customer sends a query and a document and says this should have come back. The architect embeds the query, pulls the document's stored vector, computes the similarity, finds it ranks fortieth, checks the metadata filter, re-runs with exact search to see whether the approximation missed it, finds the document was chunked such that the relevant paragraph sits in a chunk dominated by boilerplate, and explains that the chunking strategy is the cause. An hour, sometimes three. The next ticket is the same shape with a different cause, and the check sequence is identical.

## Why Nobody Has Built This
Explanation requires the vendor to have a position on chunking and embedding, which is the same neutrality choice that blocks quality measurement. The evidence spans the index, the embedding service and the application's chunking code, and the vendor owns only the middle. Support cost is a line item that grows quietly and never gets its own roadmap slot. And the architects are the ones who would build it, and they are fully occupied answering the tickets.

## What to Build
Turn the seven checks into one command. Build an explain facility that takes a query and a document identifier and reports the full trace: was it indexed, did a filter exclude it, what is its exact similarity and rank under brute force, what rank did the approximate traversal give it, which chunk of it matched and how well, and what the top returned documents scored — which is the entire diagnosis, is assembled from artefacts the platform holds, and takes seconds. Classify the cause automatically, since the seven outcomes are distinct and mechanically distinguishable: not indexed, filtered out, approximation miss, chunking, embedding representation, or genuinely less relevant than the returned set. Show the chunk-level detail, because a document is not one object and treating it as one hides the most common cause. Compare against exact search as a standard part of the trace, which separates approximation loss from representation loss definitively. Put it in the customer's hands rather than in an internal tool, since the ticket is the cost and self-service removes it. Aggregate the diagnoses into a pattern report per deployment, which turns individual tickets into a systemic finding — this deployment's failures are eighty percent chunking — that no architect can produce today. And accumulate resolutions across customers so the classification improves.

## Target Customer
Vendor solutions and support organisations, the customers currently filing these tickets, and the application teams debugging retrieval without instruments.

## Impact If Built
The same seven checks are run by hand on every ticket and every artefact required is already held. Chunk-level explanation exposes the most common cause, and the aggregated diagnosis report turns individual tickets into a systemic finding nobody currently produces.
