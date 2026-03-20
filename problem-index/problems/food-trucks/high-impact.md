# Location-Day Revenue Prediction for Food Trucks

**Industry:** [[food-trucks|Food Trucks]]
**Type:** High Impact
**One-liner:** Operators stop guessing which corner to park on and start knowing — turning the daily $200-or-$2,000 gamble into a data-driven decision.
**Tags:** #gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #tacit-knowledge-ml #revenue-impact

## The Problem
A food truck's daily revenue is almost entirely determined by where it parks and when. Experienced operators develop an intuitive model over years — they read weather forecasts, scan local event calendars, notice office-building occupancy patterns, track competitor locations, and weigh day-of-week effects — but this knowledge lives in their heads and takes 2-3 years of costly trial-and-error to build. New operators lose thousands in their first year parking in dead zones, and even veterans misjudge unfamiliar neighborhoods or miss emerging hotspots.

## Why It's Unsolved
The tacit knowledge problem is severe: the experienced operator's decision integrates at least six real-time signals (weather, events, foot traffic, competitor positions, day-of-week, time-of-year) into a single location pick, but they cannot articulate the weighting or the interaction effects. Collecting labeled training data requires pairing granular location-day revenue outcomes with the contextual features that drove the decision — most trucks lack GPS logging, event-calendar integration, or even consistent daily revenue records. The feature space is also highly local: a model trained on Austin data may be useless in Portland because zoning, permitted zones, and foot-traffic patterns differ city by city.

## What a Solution Looks Like
A mobile app ingests the truck's POS sales history (geotagged by shift), local weather forecasts, event-calendar APIs, Google Popular Times or SafeGraph foot-traffic data, and known competitor schedules. A gradient-boosted regression model predicts expected revenue for each candidate location on the upcoming day. The operator sees a ranked list of their permitted spots with predicted revenue ranges and confidence intervals, updated each morning by 6 AM.

## Impact If Solved
Operators who currently average $600/day could shift to $900+ by consistently choosing top-quartile locations — a 50% revenue lift with zero additional food cost. New operators compress 2-3 years of location intuition into their first week.
