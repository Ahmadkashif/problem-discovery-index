# Ingredient Ordering with Demand-Adjusted Par Levels

**Niche:** [[niches/food-trucks/prep-waste-optimization/profile|Prep Waste & Inventory Optimization]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Restaurant par-level systems assume you reorder the same quantities weekly — food trucks need ordering that flexes with next week's location schedule, event bookings, and weather forecast.
**Tags:** #time-series-forecasting #regression #tabular-ml #automation

## The Problem
Food truck operators order ingredients 1-2 times per week from Sysco, US Foods, Restaurant Depot, or local suppliers. They order based on habit and rough mental estimates: "I usually go through 40 lbs of chicken per week." But demand varies 50-100% week over week depending on the location schedule (a festival week vs. a slow route week), weather, and events. Ordering the same quantity every week guarantees either waste (buying 40 lbs for a 25-lb week) or emergency mid-week purchases at retail prices (running out Wednesday and buying from Costco at 2x the wholesale cost).

## What Already Exists
Restaurant inventory and ordering platforms (MarketMan, BlueCart, Orderly) calculate par levels based on historical usage and generate purchase orders. These tools work well for restaurants with stable daily covers and predictable menu mix. They assume demand variance of 10-20% week-over-week, not 50-100%.

## The Customization Gap
The system needs to adjust par levels based on next week's schedule: "You have 2 event days + 3 route days next week, expected covers are 40% above your normal week, increase chicken order to 56 lbs." It must integrate with the operator's location calendar, weight event types differently (festival day = 3x normal, slow route day = 0.7x normal), and factor in perishable vs. shelf-stable categories (over-ordering rice is fine, over-ordering fresh avocado is waste). Supplier integration should enable one-tap ordering from the demand-adjusted par list.

## Target Customer
Operators who order ingredients 1-2x/week and currently estimate quantities manually, resulting in 15-20% waste on perishables and 2-3 emergency retail purchases per month at 40-60% cost premium.

## Impact If Solved
Right-sizing orders to demand reduces perishable waste by $2K-$5K annually and eliminates $1K-$3K in emergency retail markups. Total annual savings of $3K-$8K for a typical operator.
