# Retrieval Quality Measurement

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to tell a customer whether the documents they retrieved would actually answer the question asked — and whoever does that takes the account, because it is the only question the buyer has and the category answers a different one.

## Profile
**Market Size:** ~$340M US attributable to quality rather than to the index
**Share of Parent Industry:** ~28% of category revenue
**Digital Adoption:** None — unmeasured in production
**Target Buyer:** Application teams whose product depends on retrieval
**Automation Potential:** High — the signals are present and mostly unused

## What Makes This a Distinct Niche
The category reports recall against brute-force search: how many of the true nearest neighbours the approximate index returned. That measures the index and says nothing about whether those documents answer the question, which depends on the embedding model, the chunking strategy, the query distribution and the corpus — all of which the vendor can see and none of which they measure. A customer whose retrieval is failing cannot tell whether the index is at fault, the chunking split a fact across two pieces, the embedding model does not represent their domain vocabulary, or the query is phrased unlike anything in the corpus. The contest is production retrieval quality on the real query distribution, and it is the move from infrastructure competing on cost per vector to a quality layer competing on outcomes.

## Current Tools & Gaps
Recall against brute force, latency percentiles, offline evaluation on public retrieval benchmarks, and whatever the customer builds themselves. The gaps: no measurement on the customer's actual queries; no attribution of a failure to embedding, chunking, index or query; no use of the downstream signal where the application is instrumented; and no notion of whether a corpus even contains the answer, which is a distinct and common failure.

## Problems
- [[niches/vector-search-vendors/retrieval-quality-measurement/build|🔨 Build: Recall Against Brute Force Measures the Index]]
- [[niches/vector-search-vendors/retrieval-quality-measurement/buy|🛒 Buy: Information Retrieval Evaluation Methodology]]
- [[niches/vector-search-vendors/retrieval-quality-measurement/fix|🔧 Fix: The Answer Was Never in the Corpus]]
