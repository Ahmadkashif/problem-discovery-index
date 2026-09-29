# Degrading in Ways the Operator Cannot See

**Niche:** [[niches/vector-search-vendors/index-drift-under-mutation/profile|Index Drift Under Mutation]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Approximate nearest neighbour indexes were designed for corpora that mostly sit still, and every real application inserts, updates and deletes continuously — degrading recall in ways the operator cannot see.
**Tags:** #graph-theory #evaluation-metrics #change-point-detection #k-nearest-neighbors #descriptive-statistics #time-series-forecasting #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to keep an approximate index's recall stable while the corpus changes underneath it, and to show the operator that it is — and whoever does that takes the account, because the degradation is currently invisible until a user notices.

## The Problem
A document management system indexes new files continuously and deletes on a seven-year retention policy. Eighteen months in, recall has fallen from 97 percent to the low 80s. No metric moved. Latency is fine — slightly better, because the traversal gives up earlier. No error was logged. The operator learns about it when a lawyer says a document they know exists cannot be found, and the investigation takes weeks because there is nothing to investigate: the system is behaving exactly as it was built to, and the degradation is a property of the structure that nobody instrumented.

## Why Nobody Has Built This
Measuring recall in production requires a ground truth, which means brute-force search, which is the expensive thing the index exists to avoid — so the measurement looks prohibitive until someone notices it can be sampled. Degradation is gradual and has no threshold event. Vendors benchmark on static corpora because that is the tradition, which means the degradation is not in any published result. And the remedy on offer is a rebuild, which is costly enough that measuring the need for it invites a conversation nobody wants.

## What to Build
Measure recall continuously and maintain on evidence. Sample a small number of queries per hour and compute exact nearest neighbours by brute force on a sample of the corpus, giving a continuous recall estimate at negligible cost — the measurement is affordable because it is sampled, and this reframing is the whole build. Report recall as a first-class service level with a trend, so degradation becomes a visible, alertable quantity rather than a user complaint. Report graph health directly: orphaned nodes, connectivity statistics, tombstone ratio, degree distribution against the build-time expectation — all computable from the structure without any queries and all currently unreported. Trigger maintenance from measured degradation rather than from a calendar, which is the difference between rebuilding when needed and rebuilding when remembered. Offer incremental repair — local graph repair around damaged regions — as an alternative to a full rebuild, since the damage is usually localised around deletion-heavy regions and full rebuild is a blunt instrument. Characterise and publish degradation under representative mutation patterns, so operators can anticipate it. Report the recall a given operation will cost before it runs, for bulk deletes and large ingests. And expose it all per shard, since degradation is rarely uniform and the aggregate hides the worst region.

## Target Customer
Platform and operations teams running mutating corpora, the vendors whose products degrade silently, and the application teams whose quality depends on it.

## Impact If Built
Recall degradation under mutation is invisible by construction and is the largest gap between how these systems are benchmarked and how they are run. Sampled brute-force measurement makes continuous recall affordable, and graph health statistics are computable today from structure nobody inspects.
