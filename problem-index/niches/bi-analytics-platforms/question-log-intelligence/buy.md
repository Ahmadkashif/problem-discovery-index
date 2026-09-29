# Query Log Mining as Search Analytics

**Niche:** [[niches/bi-analytics-platforms/question-log-intelligence/profile|Question Log Intelligence]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Search engines built an entire discipline on query log mining — intent clustering, reformulation detection, unanswered-query identification — and the analytics estate has never had any of it applied.
**Tags:** #word-embeddings #bert #k-means-clustering #dbscan #mutual-information #evaluation-metrics #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor that gets here is fighting to turn the record of how an organisation questions itself into a product — and whoever does that takes a position no competitor can copy, because the query log is the one asset each platform holds exclusively.

## The Problem
Working out what users want from a log of what they asked, spotting when they reformulated because the first attempt failed, and identifying the demand nothing in the index satisfies is search query log mining, a discipline with two decades of published method behind it. A BI platform's log is a query log with far richer structure — the queries are explicit, the schema is known, the user is identified, the session is bounded — and it has never been mined.

## What Already Exists
Query intent clustering, session segmentation, reformulation and abandonment detection, unanswered-query identification, and query-to-result satisfaction inference all have an extensive literature and open implementations. Embedding models cluster semantically similar queries well. Sequence analysis over sessions is standard. Change-point detection handles the temporal side. Everything required is published and free.

## The Customization Gap
The adaptation is from keyword search to structured analytical queries. It requires: (1) a query representation that is semantic rather than textual, since two SQL queries that differ entirely in text may ask the same business question and the clustering must work on what is being asked — the normalised plan from the definition-drift niche is the right input here; (2) session and intent segmentation adapted to analytical behaviour, where a single intent spans a dashboard open, four filter changes, two drill-downs and an export, which looks nothing like a search session; (3) a satisfaction signal built for this domain, where the honest indicators are negative — reformulation, abandonment, export followed by a human request — since there is no click-through to measure; (4) a business-concept vocabulary so that clusters are reported as concerns rather than as query groups, which is what makes the output usable by a data leader; and (5) privacy-preserving aggregation as a design constraint rather than a setting, because the same log supports understanding organisational demand and monitoring individuals, and the product must be constructed so it cannot easily do the second.

## Target Customer
BI platform vendors, warehouse vendors who hold query logs without the asking context, and data catalogue vendors for whom demand signal is the missing half of their inventory.

## Impact If Solved
Two decades of search log mining transfers onto a richer and cleaner log that nobody has touched. Semantic query representation and analytical session segmentation are the real adaptations, and the privacy posture is what determines whether organisations will permit it at all.
