# Query & Corpus Intelligence

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn what they see across every deployment — queries, returned sets, corpora, outcomes — into empirical answers about chunking, embedding and configuration, and whoever does that stops competing on cost per vector.

## Profile
**Market Size:** ~$160M US
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** None — every query seen, nothing concluded
**Target Buyer:** The vendors themselves, and their customers as beneficiaries
**Automation Potential:** Very High — the data is structured and continuous

## What Makes This a Distinct Niche
These vendors see every query, every returned set, every corpus and — where the application is instrumented — every downstream outcome. That is the empirical basis for the decisions the whole field currently makes from blog posts: which chunking strategy works for which document type, which embedding model suits which domain vocabulary, what hybrid weighting fits which query mix, how configuration maps to quality at which scale. The category has defined its product boundary just short of all of it, deliberately, to avoid having opinions about embeddings and chunking. That boundary is the reason the category competes on cost per vector, and crossing it is the move from infrastructure to a quality layer.

## Current Tools & Gaps
Per-customer dashboards showing latency and volume, and documentation examples. The gaps: no cross-deployment analysis of what configurations work; no empirical guidance on chunking despite being the most common cause of retrieval failure; no benchmark of embedding models on domain-specific rather than general corpora; and no feedback from the aggregate into any customer's configuration.

## Problems
- [[niches/vector-search-vendors/query-corpus-intelligence/build|🔨 Build: Every Query Seen, Nothing Concluded]]
- [[niches/vector-search-vendors/query-corpus-intelligence/buy|🛒 Buy: Meta-Learning and Configuration Transfer]]
- [[niches/vector-search-vendors/query-corpus-intelligence/fix|🔧 Fix: Chunking Advice From a Blog Post]]
