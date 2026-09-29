# The Solutions Architect

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to make the platform explain why a document was not returned — and whoever does that takes the support load, because that one question is most of the category's solutions engineering.

## Profile
**Market Size:** ~$150M US in loaded solutions and support cost
**Share of Parent Industry:** ~13% of category revenue equivalent
**Digital Adoption:** None — pipelines reconstructed by hand
**Target Buyer:** Vendor solutions organisations and support leadership
**Automation Potential:** Very High — every step is inspectable

## What Makes This a Distinct Niche
Solutions architects at these vendors spend their days on one question: why did my search not return this obviously relevant document. Answering it means reconstructing the pipeline by hand — embed the query, embed the document, check the similarity, check whether the document was in the index at all, check whether a filter excluded it, check whether the approximate traversal simply missed it, check whether chunking split the relevant passage. It takes an hour or more per case, it is the same seven checks every time, and the platform holds every artefact required to do it automatically. This is the category's largest support cost and its most mechanically automatable.

## Current Tools & Gaps
Query logs, manual similarity computation, ad hoc scripts, and the architect's experience. The gaps: no explain-this-result facility of any kind; no way to ask why a specific document ranked where it did; no comparison against exact search to separate approximation from representation; no chunk-level visibility, so a document present in three chunks appears as one object; and no accumulation of resolved cases, so the same diagnosis is repeated across customers.

## Problems
- [[niches/vector-search-vendors/the-solutions-architect/build|🔨 Build: Why Was This Document Not Returned]]
- [[niches/vector-search-vendors/the-solutions-architect/buy|🛒 Buy: Query Explanation From Search and Databases]]
- [[niches/vector-search-vendors/the-solutions-architect/fix|🔧 Fix: The Same Seven Checks, Every Time]]
