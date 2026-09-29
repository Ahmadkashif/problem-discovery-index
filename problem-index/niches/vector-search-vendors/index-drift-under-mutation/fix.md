# Deletes That Never Actually Leave

**Niche:** [[niches/vector-search-vendors/index-drift-under-mutation/profile|Index Drift Under Mutation]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Deleted vectors are marked rather than removed, they keep occupying graph structure and memory, and in several deployments the deleted content is still reachable — which is a compliance problem nobody has framed as one.
**Tags:** #graph-theory #compliance #evaluation-metrics #descriptive-statistics #automation #data-integration #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to keep an approximate index's recall stable while the corpus changes underneath it, and to show the operator that it is — and whoever does that takes the account, because the degradation is currently invisible until a user notices.

## The Problem
Deletion in a graph index is a soft mark. The vector stays in memory, stays in the graph, is traversed during search and filtered from results. A corpus with a high churn rate accumulates a large fraction of tombstones, paying memory and traversal cost for content that is gone. Worse, in several implementations the underlying vector remains readable through the raw storage layer, and a customer who deleted a document to satisfy a legal erasure request has not actually erased it. The operator was never told that delete means mark, and the compliance implication has not been drawn.

## Why It's Still Broken
Hard deletion from a graph index is genuinely hard — removing a node damages connectivity and repairing it properly costs work — so soft deletion is the pragmatic implementation. It is documented as an implementation detail rather than as a data lifecycle property, which is where the compliance question gets lost. Nobody has asked the vendors to certify erasure. And the memory cost of tombstones is absorbed as normal usage because no metric separates it.

## What a Fix Looks Like
Make deletion mean deletion, and say what it currently means. Report the tombstone ratio and the memory and traversal cost it carries, which is trivially computable and immediately reframes a hidden cost as a visible one. Offer verifiable hard deletion — vector data actually overwritten, with a certificate — since that is what an erasure obligation requires and no vendor currently provides it, which makes it both a compliance fix and a differentiator. Document the current semantics plainly, because a customer relying on delete to satisfy a legal obligation is relying on something the product does not do and has not been told. Repair connectivity locally when a node is hard deleted rather than rebuilding, which is what makes hard deletion affordable. Schedule compaction on the tombstone ratio automatically, rather than leaving it to an operator who has no metric. Support bulk retention-policy deletion as a first-class operation, since retention sweeps are the dominant deletion pattern and doing them one at a time is what creates the worst damage. And report the recall impact of a deletion batch before it runs, so an operator can plan maintenance around it.

## Who Feels the Pain
Compliance functions who believe deleted data is gone; operators paying memory for content that no longer exists; and the individuals whose erasure request was satisfied on paper.

## Impact If Fixed
Delete means mark, and a customer satisfying an erasure obligation has not been told. Verifiable hard deletion with a certificate is both the compliance answer and an unclaimed differentiator, and the tombstone ratio is a one-line metric that makes a hidden cost visible.
