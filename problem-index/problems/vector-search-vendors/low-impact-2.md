# Index Maintenance Under Update Load

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Approximate nearest neighbour indexes were designed for corpora that mostly sit still, and every real application inserts, updates and deletes continuously — degrading recall in ways the operator cannot see.
**Tags:** #graph-theory #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #optimization-fundamentals #time-series-forecasting

## The Problem
HNSW builds a navigable graph over the vector space, and its search quality depends on the graph's connectivity. Insertions add nodes and edges incrementally. Deletions are the difficulty: removing a node properly means repairing the paths that routed through it, which is expensive, so implementations commonly mark deleted vectors as tombstones and filter them at query time.

Under sustained churn — a document corpus that is continuously edited, a product catalogue that turns over, a conversation memory that expires — tombstones accumulate, the graph's connectivity degrades relative to the live set, and recall falls. The query still returns ten results with plausible scores. Nothing errors. The operator sees latency and throughput dashboards that look fine.

The remedy is a periodic full rebuild, scheduled by intuition, requiring either downtime or double the memory for a shadow index.

Insertion order and distribution matter too, in ways that are poorly documented. A graph built by inserting a clustered corpus in cluster order has different properties from one built by inserting the same vectors randomly, and few operators know this.

## What Already Exists
HNSW, IVF and DiskANN implementations are mature and well studied. Managed vector services handle rebuilds operationally so the customer does not schedule them. Tombstone-based deletion is the standard approach and is documented. Some systems support incremental compaction. Recall against brute force can be measured on demand by sampling queries. Filtered search with metadata predicates is broadly supported and has its own well-known interaction with graph quality.

## The Customisation Gap
Nobody continuously measures the recall the customer is actually getting. Recall against brute force is measurable by sampling a few hundred queries and comparing to an exact scan, it costs very little, and it is run at benchmark time rather than as a standing health metric. The result is that degradation is invisible until someone complains about answer quality.

Rebuild scheduling is therefore unguided. It should be a function of measured recall degradation and the cost of the rebuild, and it is a fixed schedule or a manual decision.

Churn-aware index selection is a further gap. The right structure for a corpus with ten per cent monthly turnover differs from one for a static corpus, and the choice is made from documentation defaults rather than from the customer's own observed update pattern — which the vendor can measure directly.

Filtered search interaction is the sharpest under-documented failure. A highly selective metadata filter over a graph index can force a traversal that returns far fewer good candidates than the unfiltered query would, and the recall loss is severe, real, and not surfaced to the operator at all.

## Impact If Solved
Recall degradation under churn is a silent failure in a system whose entire purpose is finding the right documents. Continuous recall measurement is cheap, would make rebuild scheduling evidence-based, and would surface the filtered-search cliff that currently produces mysterious quality complaints.
