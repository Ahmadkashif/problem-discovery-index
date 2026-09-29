# Niche Analysis — Vector Search Vendors

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Retrieval Quality Measurement | 🔵 High Market Share | $340M | None — measured by nobody in production | Application teams whose product depends on retrieval |
| 2 | Vector Index Infrastructure | 🔵 High Market Share | $420M | High | Platform teams; separately, application developers |
| 3 | Hybrid Search Tuning | 🟠 Low Digitized | $190M | Very Low — weights set to the documentation default | Retrieval and search engineering teams |
| 4 | Index Drift Under Mutation | 🟠 Low Digitized | $210M | Very Low — degradation the operator cannot see | Platform and operations teams |
| 5 | The Solutions Architect | 🟣 Underserved Audience | $150M | None — pipelines reconstructed by hand | Vendor solutions organisations |
| 6 | The Index Rebuild Operator | 🟣 Underserved Audience | $130M | None — rebuilds scheduled on a hunch | Site reliability and platform operations |
| 7 | Embedding Dependency Management | ⚡ Highly Automatable | $180M | Low — the model changes underneath the corpus | Anyone whose vectors came from a third party |
| 8 | Query & Corpus Intelligence | ⚡ Highly Automatable | $160M | None — every query seen, nothing concluded | The vendors themselves |

## Why These Niches

This is a category that engineered the wrong question extremely well. Recall against brute-force search measures the index and says nothing about whether the retrieved documents answer the question, which is the only thing the customer wants to know. Nobody measures that on the real query distribution, and the vendors sit at the exact point where it is determined. Quality measurement is therefore the largest contested surface and the one that would move the category off cost per vector.

Vector index infrastructure **failed the filter as one niche**. A platform team running a billion-vector retrieval workload is fighting over cost per vector per month and the recall-latency frontier at a fixed budget, and its alternative is self-hosting an open index. An application developer adding retrieval to an existing product is fighting to avoid operating another system at all, and its alternative is the vector extension in the database they already run — which has commoditised that end of the market substantially. Different buyers, different unit economics, different competitors, different definition of winning. Decomposed below.

The two underdigitised areas are both settings nobody adjusts. Combining lexical and dense retrieval reliably beats either alone and the weighting between them is whatever the documentation example used. Approximate indexes were designed for corpora that mostly sit still, every real application mutates continuously, and the resulting recall degradation is invisible to the operator.

The two underserved constituencies are the solutions architect answering the same question every day — why was this obviously relevant document not returned — by reconstructing a pipeline the platform could explain itself, and the reliability engineer babysitting index rebuilds that consume double the memory and hours of wall clock with no measurement saying whether they were needed.

The automation niches are the third-party embedding model that changes underneath a corpus nobody re-embedded, and the accumulated record of queries, returned sets and corpora that would answer empirically what the field currently settles with defaults.

## Niches
- [[niches/vector-search-vendors/retrieval-quality-measurement/profile|🔵 Retrieval Quality Measurement]]
- [[niches/vector-search-vendors/vector-index-infrastructure/profile|🔵 Vector Index Infrastructure]]
  - [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/profile|🎯 Dedicated Retrieval Infrastructure]]
  - [[niches/vector-search-vendors/in-database-and-embedded-vectors/profile|🎯 In-Database & Embedded Vectors]]
- [[niches/vector-search-vendors/hybrid-search-tuning/profile|🟠 Hybrid Search Tuning]]
- [[niches/vector-search-vendors/index-drift-under-mutation/profile|🟠 Index Drift Under Mutation]]
- [[niches/vector-search-vendors/the-solutions-architect/profile|🟣 The Solutions Architect]]
- [[niches/vector-search-vendors/the-index-rebuild-operator/profile|🟣 The Index Rebuild Operator]]
- [[niches/vector-search-vendors/embedding-dependency-management/profile|⚡ Embedding Dependency Management]]
- [[niches/vector-search-vendors/query-corpus-intelligence/profile|⚡ Query & Corpus Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Vector Index Infrastructure** is not: it names the component rather than the contest, and the two markets buying that component are competing on different axes against different alternatives. Dedicated retrieval infrastructure is won on cost per vector and the recall-latency frontier at scale, bought by platform teams whose alternative is running an open index themselves. In-database and embedded vectors are won on being adequate without operating a second system, bought by application developers whose alternative is the extension already installed in their Postgres. The first is a capacity purchase and the second is an avoidance purchase. Decomposed into two contested sub-niches.

Two candidates were rejected. *Embedding model training and provision* was rejected because it belongs to the model providers rather than to the retrieval infrastructure market, and the vendors here are its customers rather than its competitors. *Retrieval-augmented application frameworks* was rejected because its contest belongs to LLM application tooling, covered separately in this vault, and treating it here would restate it.
