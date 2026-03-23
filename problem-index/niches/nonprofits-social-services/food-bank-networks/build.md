# Perishable Inventory Demand Matching

**Niche:** [[niches/nonprofits-social-services/food-bank-networks/profile|Food Bank Networks]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can match perishable food supply (arriving unpredictably from 200+ donors) with demand across 100+ partner agencies in real time, minimizing waste while maximizing nutritional diversity.
**Tags:** #reinforcement-learning #recommendation #time-series-forecasting #tabular-ml #automation

## The Problem
A regional food bank receives 10-30 truckloads of donated food per week, much of it perishable with 2-7 days of remaining shelf life. The operations team must decide within hours which partner agencies get what food, considering each agency's storage capacity (many pantries have no refrigeration), client demographics (diabetes-friendly options, culturally appropriate foods), distribution schedule (some agencies distribute only once per week), and transportation logistics. Currently this allocation happens via phone calls and gut instinct, resulting in 8-15% food spoilage and systematic under-service of agencies that are harder to reach.

## Why Nobody Has Built This
The matching problem combines supply uncertainty (what's arriving tomorrow is unknown), demand heterogeneity (each agency serves different populations with different needs), constraint complexity (cold chain capacity, delivery windows, volunteer availability), and a non-standard objective function (maximize nutritional impact, not revenue). Commercial food distribution software optimizes for profit margin; food banks optimize for a multi-dimensional social good metric that doesn't exist in any off-the-shelf system.

## What to Build
A supply-demand matching platform where donors and food bank receiving staff log incoming inventory with quantities, categories, and expiration dates. The system matches available food to partner agencies based on agency capacity, client needs, expiration urgency, and distribution schedules, producing an optimized allocation plan. For perishable items, the system sends real-time alerts to the closest agencies with capacity, enabling same-day rescue distribution.

## Target Customer
Operations managers at regional food banks distributing 10M+ pounds of food annually to 100+ partner agencies. There are 200 Feeding America member food banks in the US.

## Impact If Built
Reduces perishable food spoilage from 12% to 4%, increases equitable distribution across partner agencies by 30%, and eliminates the 3-5 hours per day operations staff spend on phone-based allocation.
