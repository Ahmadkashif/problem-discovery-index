# Roast-to-Retail Demand Intelligence

**Niche:** [[niches/coffee-shops-independent/specialty-roaster-cafes/profile|Specialty Roaster-Cafes]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool connects retail sales velocity to roasting schedules — the owner-roaster mentally bridges two disconnected systems every day.
**Tags:** #gradient-boosting #time-series-forecasting #data-integration #revenue-impact #automation

## The Problem
A roaster-cafe owner checks yesterday's POS sales to see which blends are moving, walks to the roasting room to check roasted inventory, mentally estimates how much of each origin to roast today based on wholesale orders due this week and expected retail demand, then decides whether to pull from green bean reserves or place an emergency order. This daily mental juggling act has no software support — Cropster tracks what was roasted, Square tracks what was sold, but nothing forecasts what should be roasted tomorrow based on both retail and wholesale demand signals.

## Why Nobody Has Built This
The market is fragmented: there are only ~4,000-6,000 roaster-cafes in the US, which is too small for general POS vendors to build for. The integration problem is hard — it requires connecting roasting software APIs, POS APIs, and wholesale order data into a unified demand signal. The roasting workflow is also deeply personal; every roaster has their own batch size preferences, resting time requirements, and quality thresholds that a generic system would need to accommodate.

## What to Build
A demand intelligence layer that ingests POS retail sales by SKU, wholesale order commitments, and Cropster/RoastLog production logs, then forecasts daily roast requirements by origin/blend 7 days ahead. Outputs a roasting schedule that accounts for resting time (roasted beans need 24-72 hours before peak flavor), green bean inventory levels, and roaster capacity constraints. Alerts when green bean stock will fall below the reorder point for any origin.

## Target Customer
Owner-roasters at specialty cafes doing $500K-$2M in combined retail and wholesale revenue, currently running roasting schedules from memory and spreadsheets.

## Impact If Built
Reduces roasted-bean waste by 15-25% (over-roasting beans that don't sell before going stale) and prevents stockouts of popular blends that drive 40-60% of retail revenue. Saves the owner-roaster 5-8 hours per week of mental load on production planning.
