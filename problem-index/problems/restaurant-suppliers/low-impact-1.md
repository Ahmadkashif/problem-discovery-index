# Menu-Driven Demand Forecasting for Restaurant Customers

**Industry:** [[restaurant-suppliers|Restaurant Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic B2B demand forecasting ignores menu cycles, seasonal dishes, and event-driven volume spikes that drive 40-60% of order variability in restaurant supply.
**Tags:** #gradient-boosting #time-series-forecasting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #gradient-descent #expectation-variance-covariance

## The Problem
Procurement buyers at independent distributors commit to perishable inventory 3-7 days ahead of demand. A buyer ordering 2,000 lbs of salmon on Monday is guessing based on last week's sales and gut feel about the upcoming weekend. They have no systematic way to account for the fact that 15 of their restaurant accounts just launched spring menus featuring salmon, or that a local convention is bringing 10,000 visitors next week. The result is either spoilage (2-5% of perishable revenue) or stockouts that force restaurants to emergency-order from competitors.

## What Already Exists
Time-series forecasting tools like Oracle Demand Planning, Blue Yonder, and even simpler tools like Inventory Planner handle B2B demand forecasting. These work well for stable, repeating demand patterns — office supply distributors, janitorial products, shelf-stable goods. They model seasonality at the calendar level (Q4 holiday bump) and trend at the SKU level.

## The Customisation Gap
Restaurant demand is driven by menu composition, not calendar cycles. A chef adding duck confit to the winter menu creates a demand signal that no generic forecaster captures. The customization needed: ingesting menu data (scraped from restaurant websites, shared via ordering portals, or entered by reps), mapping menu items to ingredient SKUs with approximate portion sizes, and layering local event calendars (conventions, sports events, holidays) onto per-account demand models. The forecaster also needs to handle the high substitution rate in proteins and produce — when salmon prices spike, restaurants switch to halibut within days.

## Impact If Solved
A 30% reduction in perishable spoilage at a $20M distributor saves $120K-$300K annually. Fewer stockouts mean fewer emergency competitor orders, reducing the single biggest churn trigger in the business.
