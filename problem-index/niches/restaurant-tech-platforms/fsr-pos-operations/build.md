# The Demand Forecast the Vendor Can Make and the Operator Cannot

**Niche:** [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|Full-Service Restaurant POS & Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Restaurants make two forecasts every week and have no forecasting tool, while the platform holding their transaction history holds the same history for every comparable restaurant in the country and uses it to draw a bar chart.
**Tags:** #time-series-forecasting #gradient-boosting #temporal-fusion-transformers #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #transfer-learning
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
Thursday afternoon. A manager decides how many servers, cooks and bussers to schedule for the weekend and how much of each prep item the kitchen should produce. He looks at last week, adjusts for a feeling about the weather and a vague sense that there is something happening downtown, and commits. Over-schedule and the labour percentage blows the week; under-schedule and service collapses and the reviews follow. Over-prep and the food is thrown away; under-prep and items are eighty-sixed at eight o'clock on the busiest night. Both errors happen constantly, both are expensive, and both are forecasting failures on a problem with abundant data.

## Why Nobody Has Built This
The single-location data problem is real: two years of one restaurant's history is a small sample for a question with strong weekly seasonality, holiday effects, weather sensitivity, menu changes and price changes, and forecasting products built on it produce estimates operators correctly distrust. Pooling across locations is the answer and requires the vendor to treat its corpus as an asset rather than as a per-customer database, which is an organisational change more than a technical one. There is also a trust dynamic that vendors have handled badly: a forecast that is wrong twice is never looked at again, so the first version has to be honest about uncertainty rather than confident, and product teams have consistently shipped the confident version.

## What to Build
A forecasting service trained on the pooled corpus and specialised to each location. Covers and item-level demand are forecast by daypart with intervals, conditioned on day of week, season, weather forecast, local events, holidays, price and promotion state, and the location's own recent trajectory. A new or thin-history location borrows from comparable locations — same service model, similar size, similar market — and the borrowing shrinks as its own history accumulates, which is what makes the product useful on day one rather than in year two. The output is expressed as the decisions being made: how many of each role to schedule, how much of each prep item to produce, with the interval visible so the manager can decide how much risk to carry on a given night. Accuracy is tracked and shown per location, because an operator will extend trust only in proportion to a track record they can see.

## Target Customer
Point of sale and restaurant operations platforms holding a large cross-location corpus, and the labour and inventory vendors who currently claim forecasting built on a single location's history.

## Impact If Built
Labour and food cost are the two largest controllable lines in a restaurant, and even modest forecast improvement moves both. For the vendor, a pooled forecast is the only capability in this category that a competitor cannot match by shipping another module — it requires a corpus — which is the defensible position every platform in this market has been trying to reach by acquisition.
