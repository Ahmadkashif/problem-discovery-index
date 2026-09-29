# The Same Expensive Query, Run by Four People

**Niche:** [[niches/database-platform-vendors/analytical-warehouse-lakehouse/profile|Analytical Warehouse & Lakehouse]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Four analysts run semantically identical queries within an hour, each scanning the same terabytes, and nothing recognises that it is the same question.
**Tags:** #graph-theory #word-embeddings #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #revenue-impact
**Contested on:** Every serious competitor here is fighting to make a large query cheap and a hundred concurrent users fast without locking the customer's data into a format they cannot leave — and whoever does that takes the data platform account, because cost at scale and openness are the two things that decide it.

## The Problem
On the morning of a board meeting, four analysts each compute last quarter's revenue by segment. The queries differ in whitespace, alias names, the order of predicates and whether a filter is in the join or the where clause. They are the same question. The warehouse scans the same data four times and charges four times. Result caching, where it exists, requires textual identity and matches none of them. Multiply by a dashboard refreshed by two hundred viewers and the pattern is a substantial share of many organisations' analytical spend.

## Why It's Still Broken
Result caching was implemented on query text because that is the cheap and safe comparison, and semantic equivalence requires comparing normalised plans rather than strings — which the engine could do, since it produces the plan anyway. Consumption pricing again provides no incentive to reduce scans. And nobody reports the duplication, so the customer cannot see the pattern to complain about it.

## What a Fix Looks Like
Recognise the same question. Cache on the normalised plan rather than the query text, which matches semantically equivalent queries regardless of formatting and is the direct fix — the engine already computes the plan and the comparison is ordinary. Extend to subsumption, where a cached result covers a narrower query, which is standard view-matching technology and multiplies the hit rate. Report duplication explicitly: how much of the month's scan volume went to answering questions already answered, by query group and by team, which is the number that would make an organisation act. Identify the repeated expensive questions and propose materialisation, since a question asked forty times a day should be a table rather than a query, and the selection is the physical design problem above. Group semantically similar queries across users and surface them to the analytics team, which reveals the metrics everyone is computing independently — the definition drift problem the analytics industry describes, visible here from the cost side. And make caching transparent, since an analyst needs to know whether they received a fresh or a cached result before they act on it.

## Who Feels the Pain
Data platform teams paying repeatedly for the same computation; analysts whose queries are slower and more expensive than they need to be; and organisations whose warehouse bill contains a large redundant fraction nobody has measured.

## Impact If Fixed
Plan-normalised caching uses a representation the engine already computes and matches the equivalent queries that text caching misses entirely. The duplication report is a grouping over query history and typically reveals a share of spend large enough to force the change.
