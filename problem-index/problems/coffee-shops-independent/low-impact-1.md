# Perishable Inventory Ordering for Coffee Shops

**Industry:** [[coffee-shops-independent|Independent Coffee Shops]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic inventory tools count shelf-stable goods fine but cannot tell you whether to order 4 or 6 gallons of whole milk for Wednesday when it's supposed to rain.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #automation

## The Problem
Independent coffee shops carry 15-30 perishable SKUs — milk varieties (whole, oat, almond, coconut), baked goods (croissants, muffins, scones), fresh fruit, sandwich ingredients — each with a 2-5 day shelf life. Ordering happens daily or every-other-day through Sysco, US Foods, or local bakery partners, and the decision is almost always made by the owner or shift lead from gut feel. Over-order and you dump $50-$150 of expired product per day; under-order and you 86 the oat milk latte at 10am, losing a $6 ticket and annoying a loyal customer.

## What Already Exists
Restaurant inventory tools (MarketMan, BlueCart, Lightspeed Restaurant) handle purchase orders and track theoretical vs. actual usage, but they are designed for full-service restaurants with prep recipes, not coffee shops where a "recipe" is 2oz espresso + 10oz milk and waste happens at the ingredient level, not the plate level. These tools do not forecast perishable demand by SKU at the daily level — they track what you used, not what you will need.

## The Customisation Gap
Coffee shop perishable ordering requires a model that links POS drink-mix data (what percentage of lattes used oat milk today) to ingredient-level demand forecasts, adjusted for day-of-week, weather, and seasonal menu changes. The model must handle substitution behavior (when oat milk runs out, some customers switch to almond, others leave) and minimum-order quantities from suppliers. It also must account for the bakery display case problem: customers buy more pastries when the case looks full, so you need to bake/order slightly more than you sell to maintain visual appeal, but not so much that you waste 30% at close.

## Impact If Solved
Reduces daily perishable waste by 25-40% ($30-$60/day for a typical shop) while cutting stockout events from 3-5 per week to fewer than 1, protecting an estimated $200-$400/week in otherwise-lost sales.
