# Feasibility — Perishable Demand Forecasting and Inventory Optimization

**Industry:** [[food-distributors|Food Distributors]]
**Problem:** [[problems/food-distributors/high-impact|Perishable Demand Forecasting and Inventory Optimization]]
**Problem type:** High Impact

**Problem summary:** Distributors stop throwing away 2-5% of revenue in spoiled perishables because purchase quantities finally match actual demand at the SKU-customer-day level.

## Solution Approach
Stand up a focused pilot that integrates ERP/WMS order history, promotions, seasonality, and spoilage signals to forecast SKU-customer-day demand, then tie the model to purchasing and minimum-on-hand rules. Start with the top perishables, measure shrink and service levels weekly, and keep a human override path for buyers.

## Open Source Data
Open data is limited; general weather feeds and commodity indices can help, but accurate models need the distributor's own sales history, promo calendar, supplier lead times, and spoilage write-offs.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
