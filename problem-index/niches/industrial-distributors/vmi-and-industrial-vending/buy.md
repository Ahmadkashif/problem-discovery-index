# Demand Planning Pointed at a Single Vending Slot

**Niche:** [[niches/industrial-distributors/vmi-and-industrial-vending/profile|Vendor-Managed Inventory & Industrial Vending]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Supply chain planning software forecasts warehouse demand well; it was never set up for thousands of intermittent series inside customers' plants.
**Tags:** #time-series-forecasting #exponential-smoothing #gradient-boosting #feature-engineering #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep the customer's bins, cribs and vending machines in stock at the lowest consigned inventory and the fewest replenishment visits, and whoever replenishes from actual usage signals rather than walk-around counts takes the account.

## The Problem
Distributors already license demand-planning tools for their DCs and branches. Pointing them at point-of-use programmes fails: slot-level series are short and sparse, consumption follows the customer's production rather than the market, and the cost of a stockout depends on the item and the line it serves.

## What Already Exists
Supply chain and demand-planning suites, ERP min/max and reorder-point logic, and the analytics modules inside vending and crib platforms.

## The Customization Gap
Intermittent-demand methods pooled across similar slots and customers; customer calendars (shifts, shutdowns, new jobs) as inputs; item-level stockout costs agreed with the account; consignment ownership and carrying cost; and output as visit plans and refill lists rather than purchase orders to suppliers.

## Target Customer
Inventory planning teams at distributors with large vending and bin fleets.

## Impact If Solved
Point-of-use is the fastest-growing part of the business — Fastenal's managed-inventory share rose from 42.5% to 44.7% of sales in 2025 — so if planning tools already paid for cut consigned inventory by ~10–20% on these programmes (estimate), min/max levels stop being installation-day guesses on the growing share of sales.
