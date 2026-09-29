# Hybrid Search Tuning

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to set the balance between lexical and dense retrieval from the customer's own evidence rather than from a documentation default — and whoever does that takes the account, because the setting is free to change and nobody knows what theirs should be.

## Profile
**Market Size:** ~$190M US
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** Very Low — weights copied from an example
**Target Buyer:** Retrieval and search engineering teams
**Automation Potential:** Very High — this is parameter fitting against available signal

## What Makes This a Distinct Niche
Combining lexical matching with dense vector similarity reliably outperforms either alone, which is why every vendor supports it. The weighting between them determines how much, and it is almost universally set to whatever the documentation example used. The right value depends on the corpus, the query distribution and the embedding model: a corpus full of part numbers, drug names and error codes needs lexical weight because embeddings represent rare exact tokens poorly, while a corpus of prose answering conversational questions needs the opposite. The signal to fit this exists in every deployment. The contest is turning a copied constant into a fitted parameter, and possibly into a per-query decision.

## Current Tools & Gaps
Support for combining scores by weighted sum or reciprocal rank fusion, configurable weights, and reranking as a second stage. The gaps: no fitting procedure, so the weight is a guess; no per-query adaptation, though query type is the strongest predictor of which mode should dominate; no diagnostic showing what each mode contributed; and no re-fitting when the corpus or the embedding model changes.

## Problems
- [[niches/vector-search-vendors/hybrid-search-tuning/build|🔨 Build: The Weight From the Documentation Example]]
- [[niches/vector-search-vendors/hybrid-search-tuning/buy|🛒 Buy: Learning to Rank]]
- [[niches/vector-search-vendors/hybrid-search-tuning/fix|🔧 Fix: Scores That Are Not on the Same Scale]]
