# Multi-Signal Location Scoring Engine

**Niche:** [[niches/food-trucks/location-revenue-intelligence/profile|Location Revenue Intelligence]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product scores food truck locations by predicted revenue using the same signals an experienced operator weighs mentally — weather, events, foot traffic, competitors, and day-of-week — but with data instead of gut feel.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced operator's daily location decision integrates 6+ real-time signals: weather forecast (rain kills foot traffic), local events (concerts boost demand, road closures kill it), day-of-week patterns (Friday downtown beats Monday), competitor positions (two taco trucks on the same block split revenue), foot traffic density, and seasonal trends. This mental model is the operator's most valuable asset — but it is built through expensive trial-and-error, cannot be taught to a new operator, and fails in unfamiliar territory. The $200-vs-$2,000 daily revenue spread is primarily a location intelligence problem.

## Why Nobody Has Built This
Building this requires three hard-to-assemble data sets: (1) per-location daily revenue from multiple operators (private, competitive data that operators will not share), (2) real-time feature data (weather, events, foot traffic, competitors) matched to those revenue outcomes, and (3) city-specific permitted zones (not all locations are legal). The chicken-and-egg problem is severe: operators will not share data until the model provides value, and the model cannot provide value without operator data. Additionally, the feature space is hyperlocal — a model trained on Houston data may be useless in Chicago.

## What to Build
A location scoring engine that starts with publicly available signals (weather API, event calendar scraping, Google Popular Times, social media competitor tracking) and overlays the individual operator's own POS data geotagged to locations. For each candidate location in the operator's permitted zone list, the system produces a daily revenue prediction with confidence interval. Initial models use the operator's own 60-90 day history plus public features; network effects improve accuracy as more operators in the same city contribute anonymized data.

## Target Customer
Operators in their first 2 years who have not yet built location intuition, and veteran operators entering new markets where their existing mental model does not apply.

## Impact If Built
Shifting daily location choices from 50th-percentile (random) to 75th-percentile (data-informed) adds $150-$400/day in revenue for a typical truck — $40K-$100K annually. For new operators, it compresses 2-3 years of location learning into week one.
