# Forecasting a Scent That Has Never Sold

**Niche:** [[niches/consumer-products-makers/seasonal-pos-demand-planning/profile|Seasonal Demand Planning From Retailer POS]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every holiday programme is mostly new items, and the planner forecasts them by picking a past item that "feels similar".
**Tags:** #time-series-forecasting #temporal-fusion-transformers #k-nearest-neighbors #word-embeddings #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set seasonal and new-item quantities from retailer point-of-sale data before the last re-order date, and whoever leaves a maker with the least unsold seasonal stock at season's end takes the account.

## The Problem
A new scent, colour or set has no sales history. The planner chooses analogues from memory, and the first two weeks of sell-through, which would correct the guess, arrive too late for the plant.

## Why Nobody Has Built This
General planning tools need history; makers rarely structure item attributes well enough for similarity models.

## What to Build
Item embeddings from attributes, descriptions and images; analogue selection learned from past launches; probabilistic forecasts by retailer and store cluster; and in-season updating from the first weeks of POS, with a recommended re-order before each retailer's cut-off.

## Target Customer
Demand planners at makers with heavy seasonal and new-item mixes.

## Impact If Built
Unsold seasonal stock falls from ~15% to ~10% of seasonal units (estimate); on ~$15M of seasonal sales that is ~$350K–$750K a year of returns and markdowns avoided (estimate).
