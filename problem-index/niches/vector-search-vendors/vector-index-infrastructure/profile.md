# Vector Index Infrastructure

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** High Market Share
**Contested on:** Not terminal — the contest differs by whether the buyer is acquiring capacity or avoiding a system, and the decomposition is recorded below.

## Profile
**Market Size:** ~$420M US
**Share of Parent Industry:** ~35% of category revenue
**Digital Adoption:** High
**Target Buyer:** Platform teams; separately, application developers
**Automation Potential:** High

## What Makes This a Distinct Niche
This is the product itself: the index structures, the storage layer, the query engine and the operational surface that make approximate nearest neighbour search fast and cheap. The engineering here is genuinely excellent and it is the category's largest revenue line.

It is **not terminal**, because "vector index" names a component and the two markets buying it are competing on different axes. A platform team with a billion vectors and a serving budget is making a capacity purchase: cost per vector per month, the recall-latency frontier at a fixed spend, memory footprint, and how the system behaves at the ninety-ninth percentile under load. Their alternative is running an open index themselves, and they will if the economics say so. An application developer adding retrieval to a product with two hundred thousand documents is making an avoidance purchase: they are trying not to operate a second system, and the vector extension in the database they already run is frequently adequate — which has commoditised that end of the market substantially and is a competitive dynamic with nothing in common with the first. Filter Notes in the overview records the two rejected alternatives; the sub-niches below are the split.

## Current Tools & Gaps
Graph-based indexes with well-understood build and query trade-offs, inverted-file and quantisation variants for memory-constrained deployments, disk-resident approaches for larger-than-memory corpora, and managed operational surfaces. The gaps are specific to each side and are stated in the sub-niches.

## Problems
- [[niches/vector-search-vendors/vector-index-infrastructure/build|🔨 Build: A Capacity Purchase and an Avoidance Purchase]]
- [[niches/vector-search-vendors/vector-index-infrastructure/buy|🛒 Buy: Database Engineering Practice]]
- [[niches/vector-search-vendors/vector-index-infrastructure/fix|🔧 Fix: Benchmarks Run on Corpora Nobody Has]]
