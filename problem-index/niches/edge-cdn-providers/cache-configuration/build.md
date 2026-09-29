# Rules Written Once While the Answer Flows Past

**Niche:** [[niches/edge-cdn-providers/cache-configuration/profile|Cache Configuration]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** What to cache, for how long, keyed on what — the decisions that determine both performance and origin cost — are made once in a rule set that then accumulates for years, while the traffic that would answer them flows past every second.
**Tags:** #descriptive-statistics #k-means-clustering #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to derive what is genuinely cacheable from the traffic rather than from a rule somebody wrote in 2019 — and whoever does that takes the account, because caching decisions determine both performance and origin cost and are the category's oldest unsolved problem.

## The Problem
A property's cache hit ratio is sixty-one percent and has been for two years. Behind that number: an API endpoint returning identical responses to every user is marked private by a framework default and is never cached; a static asset path has a five-minute time-to-live set during an incident in 2019 when content was changing rapidly, and the content has not changed since; a cache key includes a session parameter, so every user gets their own copy of an identical page; and a purge rule invalidates an entire directory whenever anything in it changes. Each of these is visible in the traffic — the responses are identical, the content is unchanged, the key varies with a parameter that does not affect the response — and nothing looks.

## Why Nobody Has Built This
The category's product is a rule engine, and the expressiveness of the language has been the axis of competition rather than the quality of the rules. Analysing response bodies to establish identity is more expensive than routing them, and has been treated as prohibitive rather than as something to sample. The customer's origin sets headers that the CDN obeys, which lets the provider treat suboptimal caching as the customer's doing — which is technically true and is why the largest available improvement in the product is nobody's responsibility. And hit ratio is reported as a single number, which makes the specific opportunities invisible even to a customer who wants to look.

## What to Build
Derive the configuration from what the traffic shows. Sample responses and establish which are genuinely identical across requests, which vary only by headers not in the cache key, and which vary per user in ways that matter — which is the foundational analysis and distinguishes what is cacheable from what is currently cached. Measure actual content stability rather than accepting the declared time-to-live: how long does this resource genuinely remain unchanged, observed directly, which usually shows that conservative values are costing hit rate for no benefit and that a few aggressive ones are serving stale content. Detect cache key fragmentation by identifying keys whose variation does not correspond to response variation, which is a common and entirely invisible cause of poor hit rates. Identify responses marked uncacheable by an origin default rather than by intent, which is where the largest single gains usually are and is visible from the header pattern. Quantify each opportunity in origin requests and cost, so the recommendation is a number rather than a suggestion. And apply changes in a measured, reversible way, since the fear of serving stale content is what keeps every conservative rule in place.

## Target Customer
Platform engineering teams and CDN configuration owners, and the providers themselves, for whom origin offload is the value they sell and cannot currently maximise for their customers.

## Impact If Built
The traffic contains the answer to every caching question and no product computes it, which makes this the clearest unexploited position in the category. Fragmented cache keys and default-uncacheable responses are usually the two largest opportunities and are invisible in every current report.
