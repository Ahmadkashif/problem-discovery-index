# Perishable Demand Forecasting and Inventory Optimization

**Industry:** [[food-distributors|Food Distributors]]
**Type:** High Impact
**One-liner:** Distributors stop throwing away 2-5% of revenue in spoiled perishables because purchase quantities finally match actual demand at the SKU-customer-day level.
**Tags:** #gradient-boosting #lstm #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
A mid-size food distributor carrying 5,000 perishable SKUs must decide daily how much of each product to purchase from suppliers, knowing that over-buying creates spoilage write-offs and under-buying creates stockouts that push customers to competitors. Current forecasting relies on buyer intuition and trailing 4-week averages inside the ERP, which cannot account for weather shifts (a heat wave doubles beverage demand), local event calendars (a stadium concert spikes bar supply orders), menu cycle changes at institutional accounts (schools rotating to a new monthly menu), or complex substitution patterns (when Roma tomatoes stock out, 40% of customers accept grape tomatoes but 60% cancel the line). Spoilage waste runs $7M-$17M annually for a $350M distributor, and stockout-driven customer defection compounds the loss over time.

## Why It's Unsolved
Three factors keep this hard. First, the feature space is enormous: each SKU's demand depends on day-of-week, weather, customer segment, promotional status, supplier lead time variability, and the availability of 10-50 substitute SKUs — and these interactions differ by geography. Second, the target variable is censored: when a product stocks out, you observe zero sales but not the demand that existed, so naive models train on biased data. Third, the optimization layer on top of forecasting must jointly decide purchase quantities across SKUs subject to supplier minimum order quantities, truck capacity constraints, and shelf-life-aware FIFO rotation — a constrained optimization problem that changes daily.

## What a Solution Looks Like
An ML pipeline ingests historical order data (3+ years), weather forecasts, local event calendars, supplier lead time distributions, and current inventory positions. A gradient-boosted ensemble or LSTM generates SKU-level demand distributions (not point forecasts) for each of the next 7 days. A downstream optimization layer converts these distributions into purchase orders that minimize expected spoilage + stockout cost subject to supplier MOQs and warehouse capacity. The buyer reviews and approves the recommended PO, with the system highlighting high-uncertainty items for manual override.

## Impact If Solved
A 40-60% reduction in spoilage waste translates to $3M-$10M in recovered margin annually for a $350M distributor. Stockout rates dropping from 5-8% to 2-3% reduce customer churn by an estimated 15-20%, worth another $2M-$5M in retained revenue. Combined, this shifts net margin by 1-2 percentage points — transformative in an industry where 3% net is considered strong.
