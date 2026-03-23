# Prep Quantity Forecasting for Mobile Kitchens

**Niche:** [[niches/food-trucks/prep-waste-optimization/profile|Prep Waste & Inventory Optimization]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tells a food truck operator how many pounds of brisket to prep at 5 AM for a location they will serve at 11 AM — they guess, and guess wrong 40% of the time in either direction.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Prep happens 3-6 hours before service, at a commissary kitchen where the operator has no visibility into today's actual demand. An experienced operator develops intuition: "Wednesday at the downtown spot with good weather needs 30 pounds of pulled pork, but if it's raining cut to 18." This tacit knowledge integrates day-of-week, location, weather, event proximity, and menu mix — but it takes 1-2 years to calibrate per location and breaks whenever conditions change. New operators over-prep by 25-40% as insurance, destroying their margins.

## Why Nobody Has Built This
The model requires per-item sales data linked to location, weather, and day-of-week — most food trucks track only total daily revenue, not per-item POS data. Even trucks with itemized POS data do not tag transactions with enough context (location, weather at time of sale) to build a training set. The prep-to-sales feedback loop (how much was prepped vs. how much sold vs. how much wasted) is never recorded — operators would need to weigh prep quantities and waste quantities, which adds labor to an already overloaded workflow.

## What to Build
A prep planning assistant that ingests POS data (itemized sales by day), location schedule, and weather forecast to produce a prep sheet each morning: "For today's downtown Wednesday shift, prep 28 lbs pulled pork, 15 lbs coleslaw, 200 buns." The system learns from outcome data — operators log end-of-day waste by item (simplified: "ran out of pork at 1 PM" or "threw out 5 lbs coleslaw") to refine the model. Initial calibration uses the operator's own 60-90 days of POS history; accuracy improves over 6 months.

## Target Customer
Owner-operators who prep at a commissary 3-6 hours before service and currently lose 12-20% of food cost to over-prep waste or 10-15% of revenue to premature sellouts.

## Impact If Built
Reducing waste from 18% to 8% of food cost saves $4K-$9K annually. Reducing sellouts from 25% to 10% of service days captures $5K-$12K in revenue that currently walks away. Combined impact: $9K-$21K in annual margin improvement.
