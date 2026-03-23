# Office Occupancy-Aware Demand Forecasting

**Niche:** [[niches/food-trucks/weekday-office-lunch-route/profile|Weekday Office Lunch Route Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool connects office building occupancy signals to food truck prep quantities — operators discover a dead stop only after they show up and sell 15 lunches instead of 80.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Route operators develop a feel for each stop's demand — "Tuesdays at Meridian Office Park are always strong, but Mondays are weak since they went hybrid." This intuition takes 6-12 months per location to develop and breaks whenever a major tenant changes work-from-home policy, a new competing truck appears, or seasonal patterns shift. Operators currently over-prep by 20-30% as insurance against demand uncertainty, generating chronic waste.

## Why Nobody Has Built This
The required signal — real-time or near-real-time office occupancy per building — has only recently become accessible through aggregated mobile location data providers (Placer.ai, SafeGraph) and commercial parking lot sensors. Connecting this signal to food truck POS data requires per-stop revenue history that most operators track only in their heads. The market is also fragmented: each city has different office districts, and a model trained on downtown Austin offers little to a truck serving suburban office parks in Charlotte.

## What to Build
A location intelligence layer for route trucks that ingests office-area foot traffic data (via Placer.ai or Google Popular Times API), combines it with the truck's own per-stop POS history, and produces a daily demand forecast per stop by 6 AM. When a stop's occupancy drops below a threshold (e.g., company holiday, building closure, WFH shift), the system alerts the operator and suggests reallocation to a backup stop. Over time, it learns day-of-week, weather, and seasonal patterns per location.

## Target Customer
Route operators with 3-8 regular stops who currently estimate demand by memory and absorb $3K-$8K in annual waste from inaccurate prep.

## Impact If Built
Reducing prep waste from 25% to 10% and avoiding 15-20 dead-stop days per year adds $6K-$12K in annual profit — plus the operator gains confidence to drop underperforming stops and trial new ones with data rather than gut feel.
