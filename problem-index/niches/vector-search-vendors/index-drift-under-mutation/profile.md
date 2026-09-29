# Index Drift Under Mutation

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to keep an approximate index's recall stable while the corpus changes underneath it, and to show the operator that it is — and whoever does that takes the account, because the degradation is currently invisible until a user notices.

## Profile
**Market Size:** ~$210M US
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** Very Low — degradation the operator cannot see
**Target Buyer:** Platform and operations teams running mutating corpora
**Automation Potential:** High — measurement is mechanical, maintenance is schedulable

## What Makes This a Distinct Niche
Approximate nearest neighbour indexes were designed and benchmarked on corpora that mostly sit still. Every real application inserts, updates and deletes continuously. Deletions leave tombstones that still occupy graph structure; insertions attach to a graph whose connectivity assumptions were established at build time; updates are implemented as delete-plus-insert and compound both. Recall degrades gradually, the system reports no error, latency may even improve, and the operator's only signal is eventually a user saying search got worse. This is the largest gap between how these systems are evaluated and how they are run, and nothing in the category measures it.

## Current Tools & Gaps
Incremental insertion support, soft deletes with compaction, and periodic full rebuilds. The gaps: no continuous recall measurement, so degradation is unobserved; no rebuild trigger based on measured need; graph connectivity health is not reported despite being computable; the accumulated effect of deletion patterns is undocumented; and rebuild is the only remedy offered, which is expensive enough that it is deferred past the point of harm.

## Problems
- [[niches/vector-search-vendors/index-drift-under-mutation/build|🔨 Build: Degrading in Ways the Operator Cannot See]]
- [[niches/vector-search-vendors/index-drift-under-mutation/buy|🛒 Buy: Storage Engine Compaction and Maintenance]]
- [[niches/vector-search-vendors/index-drift-under-mutation/fix|🔧 Fix: Deletes That Never Actually Leave]]
