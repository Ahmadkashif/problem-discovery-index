# Daily Prep Quantity Optimizer

**Niche:** [[niches/coffee-shops-independent/perishable-food-menu-cafes/profile|Perishable Inventory & Food-Menu Cafes]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tells a cafe owner how many breakfast sandwiches to prep at 5am based on today's expected demand — every morning is a guess.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #automation #revenue-impact

## The Problem
Every morning, a cafe with a food menu makes 20-40 prep decisions: how many croissants to bake, how many sandwich builds to prep, how many salads to assemble. Each decision has a cost: over-prep wastes food (a $4 sandwich thrown away at 3pm), under-prep loses a sale (a customer who wanted the chicken wrap at noon sees an empty case and buys nothing). The owner or kitchen lead makes these decisions from memory — "Tuesdays are usually slow" — without accounting for weather (rainy days increase food sales by 15-20%), local events, or the display-case effect (a half-empty case depresses purchases even when stock exists).

## Why Nobody Has Built This
Restaurant prep optimization tools (Winnow, Leanpath) are designed for large kitchens with 100+ menu items and dedicated prep teams. A cafe's food operation is simpler (10-25 items) but runs on the same person who's also pulling espresso shots — the tool must be zero-input (no manual demand forecasting) and deliver a recommendation in a 30-second morning check. The market size (cafes with meaningful food menus, ~8,000-12,000 locations) is below the threshold for restaurant-tech vendors but above the threshold for a focused vertical product.

## What to Build
A daily prep recommendation engine that ingests POS sales history by item, day-of-week patterns, weather forecast, and any flagged local events, then outputs a morning prep sheet: "Today prep 18 croissants (not 24 — it's sunny and warm, which historically drops pastry sales 12%), 12 turkey sandwiches, 8 salads." The model accounts for display-case fill targets (never below 60% full at any point during service) and item-level shelf life. Inputs are automatic (POS API + weather API); output is a printed or phone-displayed prep sheet at 5am.

## Target Customer
Cafe owners or kitchen leads who make daily prep quantity decisions for 10-25 perishable menu items, currently averaging 18-25% waste rate.

## Impact If Built
Reduces food waste by 30-50% ($500-$2,000/month for a cafe doing $5K-$15K/month in food sales) while reducing stockouts during peak lunch hours by 40-60%.
