# Six Dashboards With Almost the Same Name

**Niche:** [[niches/bi-analytics-platforms/dashboard-estate-lifecycle/profile|Dashboard Estate Lifecycle]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A search for sales performance returns six dashboards with nearly identical names and contents, the user cannot tell which is authoritative, and nothing in the platform compares them.
**Tags:** #word-embeddings #dbscan #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation
**Contested on:** Every serious competitor in analytics governance is fighting to make retiring an asset safe enough that an organisation will actually do it — and whoever does that takes the governance account, because every estate grows monotonically and every governance programme has failed to stop it.

## The Problem
A regional manager searches for sales performance. Six results: "Sales Performance", "Sales Performance (New)", "Sales Performance v2", "Regional Sales Performance", "Sales Perf - Q3", and "Copy of Sales Performance". Three were built by people who have left. Two show the same numbers. One is right for this manager's question and there is no way to tell which. They ask an analyst — which is the ad hoc queue — or they pick one and are possibly wrong, which is worse. Every asset's definition, query, usage and creation history is in the platform.

## Why It's Still Broken
Duplication accumulates because copying a dashboard is the standard way to make a variant, and nothing ever compares the results. Search ranks by title match and recency rather than by authority or usage, so the six appear in arbitrary order. Certification would help and covers a small fraction of most estates, leaving the confusing majority untouched. And nobody owns the experience of a person searching, because the platform's users of record are the builders rather than the readers.

## What a Fix Looks Like
Compare assets to each other, which nothing currently does. Group near-duplicates by comparing the underlying queries and the rendered content rather than the titles, which is ordinary similarity work at this scale and immediately collapses six results into one group. Within a group, rank by evidence — usage, audience, recency of maintenance, whether the owner is still at the company, whether it matches the governed definitions — and present one recommended asset with the alternatives collapsed beneath it, which is the single highest-value change to the reading experience. Surface authority signals in search results rather than requiring a click: how many people use this, when it last refreshed, whether its pipeline is healthy, who owns it. Flag ownerless assets explicitly, since an asset whose owner has left is a specific and common risk that no platform reports. And feed the duplicate groups into the retirement process, since a group of six with one clear winner is the easiest and safest retirement decision an organisation will ever make.

## Who Feels the Pain
Everyone who searches an analytics estate and cannot tell which result to trust; analysts fielding the resulting questions; and governance teams who know the duplication exists and have no way to enumerate it.

## Impact If Fixed
Content-based duplicate grouping is straightforward at estate scale and has never been applied, and it improves the reading experience and the retirement backlog with one analysis. The ownerless-asset flag is a one-line query that most organisations would find alarming.
