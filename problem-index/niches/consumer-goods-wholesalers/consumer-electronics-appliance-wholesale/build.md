# Stock Positioned Through Model Changeovers

**Niche:** [[niches/consumer-goods-wholesalers/consumer-electronics-appliance-wholesale/profile|Consumer Electronics, Appliance & Housewares Wholesale]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forecast each model's demand by dealer cluster through the yearly changeover, so the distributor holds the right boxes near the right dealers and is not left with last year's model.
**Tags:** #time-series-forecasting #gradient-boosting #transfer-learning #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to have the exact model a dealer or regional retailer just sold sitting in a nearby warehouse when the order lands, and whoever fills the highest share of dealer order lines from stock takes the account.

## The Problem
A distributor serving a few thousand dealers carries thousands of active models across brands, each with a life of about a year (estimate). Demand for a new model has no history, the outgoing model's demand collapses at a date the brand sets, and dealers order one or two units at a time. Buyers position stock across regional warehouses by feel and by last year's totals, so fill rates drop exactly when models change.

## Why Nobody Has Built This
Brands forecast their own models and do not see across brands. Generic planning tools need history per SKU, and these SKUs are new every year. Distributors have the cross-brand order history, but not the data science to use it.

## What to Build
A model that maps each new model to its predecessor and close substitutes by attributes (size, capacity, finish, price band), transfers their demand curves by dealer cluster, and adjusts for brand launch dates, promotions and dealer floor-model placements. It recommends regional stock levels for the incoming model and run-down levels for the outgoing one.

## Target Customer
COO and inventory planning leads at independent appliance and electronics distributors with several regional warehouses.

## Impact If Built
Raising first-pass fill on dealer lines from ~90% to ~94% (estimate) on ~$500M of sales keeps ~$20M of orders that would go to a competitor (estimate), and cuts stranded end-of-life stock.
