# Price Optimisation Re-Based on Replacement Cost

**Niche:** [[niches/building-material-dealers/commodity-lumber-panel-pricing/profile|Commodity Lumber & Panel Pricing]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Price optimisers learn what customers will pay; for commodity lumber the dealer first needs what it will cost to replace, and a customer's tolerance for repricing.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to reprice every open quote, builder price sheet and counter price to the latest lumber and panel market before the material ships, and whoever lets the fewest packages ship below replacement cost without losing bids to stale prices takes the account.

## The Problem
Optimisers trained on historical margins treat lumber as a product class with a stable cost. In a volatile market their recommendations chase yesterday's cost.

## What Already Exists
Price-optimisation software for distributors and ERP pricing matrices.

## The Customization Gap
Replacement-cost bases by species, grade, size and length; duty and tariff layers for Canadian product; hold periods and escalation terms by customer type; separate logic for counter, custom-builder and production-builder programme pricing; and guardrails that stop margin recommendations from following a falling cost too fast.

## Target Customer
Dealers already running a price-optimisation tool for non-commodity categories.

## Impact If Solved
One pricing system for all categories, with commodity lines priced from replacement cost, avoiding the ~1–3 margin points (estimate) that cost-blind recommendations give away when the market moves.
