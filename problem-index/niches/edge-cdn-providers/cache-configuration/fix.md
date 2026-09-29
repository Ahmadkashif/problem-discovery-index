# One Hit Ratio for the Whole Property

**Niche:** [[niches/edge-cdn-providers/cache-configuration/profile|Cache Configuration]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Cache performance is reported as a single hit ratio, which averages the assets that always hit with the endpoints that never do and tells nobody what to change.
**Tags:** #descriptive-statistics #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to derive what is genuinely cacheable from the traffic rather than from a rule somebody wrote in 2019 — and whoever does that takes the account, because caching decisions determine both performance and origin cost and are the category's oldest unsolved problem.

## The Problem
The dashboard reports a cache hit ratio of sixty-one percent. It is the number reviewed monthly and it has never moved. Underneath, the static assets hit at ninety-eight percent, one API path hits at three percent and accounts for a large share of origin traffic, a document type is never cached because of a header, and one cache key is fragmenting a popular page into thousands of single-use entries. Every one of those is a specific fixable problem and all of them are averaged into a number that has looked the same for two years.

## Why It's Still Broken
Hit ratio was defined as a property-level metric because that is the billing and reporting unit, and it has become the operational metric by default. Decomposing it requires grouping requests by path pattern, content type and cache key structure, which is straightforward and has not been surfaced. And the single number is comfortable: it never looks alarming, which is precisely why it never prompts anything.

## What a Fix Looks Like
Decompose the metric into the units where action is possible. Hit ratio by path pattern, content type and cache status reason, which immediately separates the assets that are fine from the endpoints that are not and is a grouping of data the provider already has. Report misses by reason rather than as a count: no cache directive, explicitly private, key miss, expired, too large, purged — since each reason has a different remedy and the distribution is usually dominated by two of them. Rank by origin requests caused rather than by miss rate, because a path with a low hit rate and little traffic does not matter and one with a moderate hit rate and enormous traffic does. Report cache key cardinality per path, which exposes fragmentation directly and is a one-line query that regularly finds a parameter nobody meant to include. Show the origin cost attributable to each group, which converts a performance metric into a financial one and changes who pays attention. And track the decomposition over time, so a regression introduced by a change is attributable rather than appearing as a slight movement in an average.

## Who Feels the Pain
Configuration owners with a metric that never moves and no indication of what to change; platform teams paying for origin capacity serving cacheable content; and providers whose customers cannot see the improvements available to them.

## Impact If Fixed
The decomposition is a grouping of data every provider already holds and turns a static average into a short ranked list of specific problems. Miss-by-reason and cache key cardinality are the two views that most reliably find the largest opportunity.
