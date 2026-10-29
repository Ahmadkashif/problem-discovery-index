# The Container That Decides the Scorecard

**Niche:** [[niches/consumer-goods-wholesalers/replenishment-programmes/profile|Replenishment Programmes]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Fix (Pain Point)
**One-liner:** When a container rolls at the port, nobody knows until the shipping day which retailer purchase orders will now ship short.
**Tags:** #gradient-boosting #survival-analysis #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a retailer's everyday items in stock through its automatic replenishment orders, and whoever ships the fewest of the retailer's ordered units short takes the account.

## The Problem
Container status sits with the forwarder, purchase orders with the ERP and allocation with the warehouse. A delay at origin or a port hold becomes visible as a short shipment only when the warehouse picks.

## Why It's Still Broken
Forwarder milestones are not linked to SKUs or to the retailer orders they will fill, and nobody owns the join between import logistics and customer service.

## What a Fix Looks Like
Predict each inbound container's arrival from forwarder milestones and lane history, map its SKUs to open retailer orders, and alert the account team early enough to reallocate stock, split shipments or ask the retailer for a date change before a fine is earned.

## Who Feels the Pain
Account managers facing scorecard reviews, warehouse leads blamed for short ships, and import coordinators chasing forwarders.

## Impact If Fixed
Seeing delays two to three weeks earlier could save a third of the units shipped short because of inbound delays (estimate), ~$20–40K a year in fines on a $50M programme (estimate).
