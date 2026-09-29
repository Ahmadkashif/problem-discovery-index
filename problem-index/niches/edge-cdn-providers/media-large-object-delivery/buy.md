# Prefetching and Demand Forecasting

**Niche:** [[niches/edge-cdn-providers/media-large-object-delivery/profile|Media & Large Object Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Forecasting demand and pre-positioning inventory is what supply chains have done for a century, and a new release reaches the edge when the first viewer requests it.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #monte-carlo-methods #confidence-intervals #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to deliver a byte more cheaply while holding playback quality — and whoever does that takes the media account, because egress is a dominant cost line and quality of experience is the product.

## The Problem
A title is released at nine o'clock. For the first minutes, every edge node misses and fetches from origin, which is exactly the moment of highest concurrent demand and the point at which origin capacity is most stressed. The release schedule was known for weeks. Pre-positioning content at the edge before demand arrives is inventory placement with a known demand event, which is a solved logistics problem, and the content is fetched reactively because caching is demand-driven by default.

## What Already Exists
Demand forecasting with seasonality and event effects; inventory placement and pre-positioning optimisation from logistics; prefetch and cache warming interfaces offered by most providers; content popularity prediction research from the content delivery literature; and the release schedule, which the customer has.

## The Customization Gap
The adaptation is to content with extremely skewed and short-lived popularity. It requires: (1) forecasting at the region and node level rather than globally, since the placement decision is per location and global popularity does not determine where a title will be watched — this is the core modelling requirement; (2) cold-start prediction for new titles with no history, using metadata, cast, genre and pre-release engagement signals, since the highest-value pre-positioning is for content with no traffic history at all; (3) a cost model that weighs storage and transfer for pre-positioning against the origin load and latency it avoids, because pre-positioning everything everywhere is possible and wasteful; (4) partial pre-positioning, since the first segments of a video are what determine the startup experience and placing those is far cheaper than placing the whole title; and (5) handling of the extremely heavy-tailed distribution, where a small number of titles dominate demand and the long tail should never be pre-positioned at all.

## Target Customer
Streaming platforms and media operations teams, delivery providers offering prefetch capabilities, and the multi-CDN steering vendors.

## Impact If Solved
Demand is known in advance and content is fetched reactively, which concentrates origin load at the worst possible moment. Partial pre-positioning of opening segments captures most of the startup benefit at a fraction of the cost and is rarely done.
