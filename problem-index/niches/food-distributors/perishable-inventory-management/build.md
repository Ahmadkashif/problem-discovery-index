# ML-Driven Perishable Purchase Optimization System

**Niche:** [[niches/food-distributors/perishable-inventory-management/profile|Perishable Inventory Management]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No commercially available product generates SKU-level probabilistic demand forecasts for perishable products and converts them into purchase orders that minimize spoilage + stockout cost subject to supplier minimums, warehouse capacity, and shelf-life constraints.
**Tags:** #gradient-boosting #lstm #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
A mid-market food distributor's buyer sets purchase quantities for 3,000+ perishable SKUs daily using a combination of ERP trailing averages and personal judgment. The buyer who has done this for 10 years carries a mental model of seasonal patterns, weather effects, and substitution dynamics. But this mental model cannot scale: with 3,000 SKUs, the buyer focuses attention on the top 100 items (which represent 40% of revenue) and applies simple rules to the remaining 2,900 (which represent 60% of revenue and a disproportionate share of spoilage because they get less attention). When the experienced buyer retires, the replacement over-orders by 5-15% for 6-12 months while rebuilding the mental model — costing millions in additional spoilage.

## Why Nobody Has Built This
Building a perishable purchase optimization system requires solving three problems simultaneously: (1) probabilistic demand forecasting (not point forecasts — the buyer needs to know "there is 80% probability that demand exceeds 50 cases and 20% probability it exceeds 80 cases" to make risk-adjusted decisions), (2) censored demand correction (when a product stocks out, observed demand is zero but actual demand was positive — models trained on raw order data underforecast), and (3) constrained purchase optimization (converting forecasts into POs subject to supplier MOQs, truck capacity, warehouse space, and shelf-life-aware FIFO rules). Each component is well-understood in isolation, but the end-to-end system that connects to a food distributor's specific ERP and generates actionable POs has not been productized.

## What to Build
An ML pipeline that: (1) ingests 2-3 years of daily order data from the distributor's ERP, plus weather forecasts, local event calendars, and supplier promotional calendars, (2) trains a gradient-boosted or LSTM model to produce SKU-level demand distributions for days t+1 through t+7, (3) corrects for censored demand during historical stockout periods, (4) feeds demand distributions into a purchase optimization engine that generates recommended POs minimizing E[spoilage cost] + E[stockout cost] subject to supplier and warehouse constraints, and (5) presents the buyer with recommended POs highlighting high-uncertainty items for manual override. Pre-built connectors for the top 5 food distribution ERPs.

## Target Customer
Buyers and inventory managers at food distributors carrying 1,000+ perishable SKUs. Approximately 2,000-3,000 US distributors at this scale. Price model: $2K-$8K/month based on SKU count, justified by spoilage reduction.

## Impact If Built
Spoilage reduced by 30-50%, worth $1M-$5M annually for a $200M distributor. Stockout rate reduced from 5-8% to 2-3%, retaining $500K-$2M in revenue that would have gone to competitors. Buyer onboarding time reduced from 6-12 months to 2-3 months because the system provides the demand intelligence that previously required years of experience.
