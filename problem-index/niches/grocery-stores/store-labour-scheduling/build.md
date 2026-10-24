# One Workload Forecast for Store and Online Work

**Niche:** [[niches/grocery-stores/store-labour-scheduling/profile|Store Labour Scheduling & Workload Forecasting]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Stores schedule cashiers, stockers and pickers from separate forecasts, so the same person is double-counted on promotion days and nobody is counted when the truck is late.
**Tags:** #time-series-forecasting #gradient-boosting #temporal-fusion-transformers #optimization-fundamentals #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to match each store's scheduled hours to its 15-minute workload of customers, trucks and online orders, and whoever delivers the fewest understaffed intervals at the same payroll takes the account.

## The Problem
The workforce management suite forecasts front-end traffic from sales history. The e-commerce platform forecasts online orders. The receiving team plans for trucks from a delivery calendar that is often wrong. Each feeds a different schedule, and the store manager reconciles them by moving people between tasks on the day.

## Why Nobody Has Built This
Online-order forecasts belong to the e-commerce platform, which is often a third party. Truck arrival data sits with the warehouse or the DSD vendor. Workforce vendors forecast what they can see, which is the store's own sales.

## What to Build
A single 15-minute workload forecast per store and department that combines front-end traffic, online orders by pick window, truck arrivals with live ETAs, and fresh production plans. It converts each into labour hours using task standards and feeds one schedule optimiser that respects posting deadlines, availability and cross-training. On the day, it re-plans when a truck is late or online orders spike.

## Target Customer
VPs of store operations at chains picking online orders in-store with their own staff.

## Impact If Built
For a store with ~4,500 labour hours a week, moving 2% of hours from overstaffed to understaffed intervals is ~90 hours a week put where the work is (estimate), at no extra payroll.
