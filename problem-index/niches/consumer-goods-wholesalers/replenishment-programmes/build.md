# Ordering Ahead of the Retailer's Replenishment System

**Niche:** [[niches/consumer-goods-wholesalers/replenishment-programmes/profile|Replenishment Programmes]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Learn the retailer's ordering rules from its own store data and forecast its purchase orders, not its sales, so the importer's container lands before the order does.
**Tags:** #temporal-fusion-transformers #lstms-and-grus #time-series-forecasting #exponential-smoothing #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a retailer's everyday items in stock through its automatic replenishment orders, and whoever ships the fewest of the retailer's ordered units short takes the account.

## The Problem
A retailer's replenishment system turns store sales and on-hand into DC orders with its own safety stock and order-batching rules. Importers forecast sales, but what they have to fill is the orders, which are lumpier and lag sales in ways the importer never models.

## Why Nobody Has Built This
POS tools stop at sell-through, and retailers do not publish their ordering logic. Learning it needs the retailer's order history joined to its 852 product-activity data at SKU, store and DC level, which few importers have assembled.

## What to Build
A multi-horizon model that takes store sales, on-hand, on-order, promotions and modular changes from 852 or portal data and predicts each DC's purchase orders 4–12 weeks out, with quantiles. It feeds container bookings and US warehouse allocation.

## Target Customer
Demand planners at importers with replenishment programmes at two or more large retailers.

## Impact If Built
Cutting units shipped short from ~8% to ~3% of ordered units (estimate) on a $50M programme avoids ~$75K a year of fines at a 3% rate on missed cases (estimate) and protects the slot at the next line review.
