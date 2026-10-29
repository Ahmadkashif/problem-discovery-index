# Demand Planning That Sees Dealer Floor Models

**Niche:** [[niches/consumer-goods-wholesalers/consumer-electronics-appliance-wholesale/profile|Consumer Electronics, Appliance & Housewares Wholesale]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Planning tools forecast from shipments; a dealer's next order is driven by which floor models it displays, and the tools do not know.
**Tags:** #time-series-forecasting #exponential-smoothing #feature-engineering #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to have the exact model a dealer or regional retailer just sold sitting in a nearby warehouse when the order lands, and whoever fills the highest share of dealer order lines from stock takes the account.

## The Problem
Dealers sell what is on their floor. When a dealer puts a new range or refrigerator on display, orders for the boxed unit follow for months, and when it pulls the display, orders stop. The distributor ships the display units but forecasts as if all shipments were alike.

## What Already Exists
Mid-market demand and inventory planning tools such as Netstock and Inventory Planner, and enterprise suites such as Blue Yonder and o9, forecast by SKU and location from history.

## The Customization Gap
The planner needs display placements as a leading signal: which dealers took floor models of which SKUs and when, brand display programmes, and dealer cluster demand. It also needs model-succession mapping, so history carries across changeovers, and price-protection windows treated as a holding cost.

## Target Customer
Inventory planners at regional appliance and electronics distributors already running a generic planning tool.

## Impact If Solved
Using display placements as a demand signal could cut lost dealer lines by ~20% (estimate), ~$10M of kept orders on $500M of sales at a ~90% fill rate, without adding inventory dollars.
