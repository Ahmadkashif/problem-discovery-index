# Short-Dated Inventory Markdown Timing

**Niche:** [[niches/food-distributors/perishable-inventory-management/profile|Perishable Inventory Management]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** Perishable product approaching its sell-by date sits at full price in the warehouse until it is too late to sell at any price — distributors recover only 10-20% of value on short-dated inventory because markdowns happen reactively (someone notices the date) rather than proactively (a system triggers the markdown 48 hours before expiration).
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #automation

## The Problem
A food distributor's buyer purchases product expecting to sell it before expiration. When demand falls short of forecast, product approaches its sell-by date while sitting at full price in the warehouse. The recovery window is narrow: at 48-72 hours before expiration, the product can be marked down 30-50% and sold to price-sensitive customers (casual dining, caterers, food banks). At 24 hours, it is worth 10-20% at best. At expiration, it is waste. Currently, the markdown decision is triggered when a warehouse worker notices a date code during picking ("hey, this expires tomorrow"), which may be too late for meaningful recovery. No systematic process identifies markdown candidates 48-72 hours before expiration and routes them to price-sensitive customers.

## Why It's Still Broken
The markdown process has three broken links: (1) identification — the WMS does not proactively surface product approaching expiration; it relies on workers noticing dates during picking, (2) pricing — there is no model for what price will clear the product quickly without training customers to wait for markdowns, and (3) distribution — the sales team does not have a systematic way to offer markdown product to the right customers (price-sensitive accounts that would buy short-dated product) without cannibalizing full-price sales to quality-sensitive accounts. Each link requires a different intervention: data for identification, analytics for pricing, and workflow for distribution.

## What a Fix Looks Like
An automated markdown workflow: (1) the WMS flags all product within 72 hours of expiration every morning, (2) a pricing model calculates the recommended markdown price based on remaining shelf life, product category, historical markdown sell-through rates, and current full-price demand, (3) the system identifies customers most likely to purchase short-dated product (based on historical markdown purchase behavior and price sensitivity) and routes markdown offers to their sales reps, (4) the sales rep receives a mobile notification: "50 cases of yogurt expiring in 72 hours — offer to [5 specific customers] at $2.50/case (vs. $4.00 full price)." The system tracks markdown sell-through rates to refine pricing and customer targeting over time.

## Who Feels the Pain
Buyers who watch product they purchased spoil because nobody caught the approaching expiration in time. Sales reps who could have placed markdown product with their price-sensitive accounts but were never informed. Finance teams that write off $500K-$2M annually in spoilage that was partially recoverable.

## Impact If Fixed
Markdown revenue recovery improves from 10-20% to 40-60% of full-price value. On $2M in annual spoilage, recovering an additional 30% at 50% of full price saves $300K. Waste volume reduced by 30-40% as more product moves through markdown channels before expiration. Customer relationships with price-sensitive accounts strengthen through consistent markdown access, increasing their total spend 5-10%.
