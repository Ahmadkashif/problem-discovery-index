# Averages That Hide the Customers Who Matter

**Niche:** [[niches/developer-tools-vendors/monorepo-scale-performance/profile|Monorepo & Scale Performance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Vendor performance dashboards report means across all repositories, which are dominated by the small ones, so the degradation at the top of the distribution is invisible in the vendor's own data.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #time-series-forecasting #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to keep navigation, search and build responsive past the repository size where everything degrades — and whoever does that keeps the largest accounts, because the customers who cross that line are the most valuable and the least able to switch.

## The Problem
The vendor's performance dashboard shows median index time of eleven seconds and a healthy trend. Ninety percent of repositories are small and they dominate the statistic. The forty largest customers, who account for a large share of revenue, are experiencing index times measured in hours and a steadily worsening one. Nothing in the vendor's reporting shows this, so engineering effort goes to improvements that move the median, and the escalations from the large accounts are handled as individual support cases with no connection to any metric.

## Why It's Still Broken
Aggregate metrics were established early and are what leadership reviews, and nobody has argued for changing them because the argument requires already knowing the thing the metrics conceal. Segmenting by customer size is a small piece of work that nobody has been asked for. And the largest customers frequently stop reporting problems and build workarounds instead, which removes the qualitative signal at the same time the quantitative one is hiding it.

## What a Fix Looks Like
Report by segment and by percentile. Performance by repository size band rather than pooled, which immediately separates the population that is fine from the population that is not and is a grouping change rather than new instrumentation. Percentiles rather than means throughout, since the experience that causes churn is the slow operation and not the typical one. Per-account performance visible to the account team, so a degrading large customer is noticed before they escalate. Trend by account, because the trajectory matters more than the level and is what enables a warning. Explicit scale bands in the product's own performance objectives, so that acceptable behaviour at each size is defined rather than emergent. And correlate performance with usage and renewal, which usually establishes that the degradation is a commercial risk rather than an engineering nicety, and is what gets the work prioritised.

## Who Feels the Pain
The largest customers, whose experience is worst and least visible; account teams surprised by escalations; and engineering organisations optimising a median that describes nobody they are worried about.

## Impact If Fixed
Segmenting by size band and reporting percentiles is a reporting change over existing telemetry and immediately reveals a population the vendor cannot currently see. Correlating with renewal is what converts an engineering concern into a funded one.
