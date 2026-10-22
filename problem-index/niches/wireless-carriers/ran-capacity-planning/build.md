# Sector Exhaustion Forecasts With Ranked Relief Options

**Niche:** [[niches/wireless-carriers/ran-capacity-planning/profile|RAN Capacity Planning & Spectrum Deployment]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers forecast sector traffic as a trend line and pick fixes by rule of thumb, when what they need is a probability of exhaustion by date and the cheapest fix that prevents it.
**Tags:** #temporal-fusion-transformers #time-series-forecasting #survival-analysis #confidence-intervals #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict, sector by sector, when mobile and fixed wireless demand will exhaust capacity and which fix — a new carrier, a sector split, a small cell or a cap on fixed wireless sales — buys the most relief per dollar, and whoever forecasts exhaustion earliest and most accurately takes the planning budget.

## The Problem
Capacity planners project each sector's busy-hour PRB utilisation forward and flag sectors that will cross a threshold within the planning horizon. Every flagged sector then competes for a limited budget of carrier adds, sector splits and small cells, each with a different cost, lead time and effect. Point forecasts hide uncertainty, so planners either over-build to be safe or get caught by sectors that exhaust early, and those sectors show up as throughput complaints and churn.

## Why Nobody Has Built This
Vendors sell planning tools and radios, not forecasts; carriers build forecasts in-house with small teams. Relief options depend on site constraints (spare spectrum, tower loading, permitting lead time) that live in other systems, and FWA demand is forecast by the marketing team, not engineering.

## What to Build
A probabilistic forecast of busy-hour load per sector, combining mobile traffic, FWA subscriber growth on that sector, events and seasonality, with a date-to-exhaustion distribution. On top sits an optimiser that ranks relief options by expected avoided congestion per dollar, respecting lead times, spectrum availability and site loading, and that re-plans as forecasts update.

## Target Customer
Directors of capacity planning and RAN engineering VPs at national and regional carriers.

## Impact If Built
Fewer sectors exhaust unplanned and less capex goes to sectors that never needed it; a few percent of a $30B capex envelope moved to better sectors is a large number (estimate).
