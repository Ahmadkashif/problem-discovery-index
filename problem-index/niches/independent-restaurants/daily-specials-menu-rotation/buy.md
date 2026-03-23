# Specials-Aware Demand Forecasting

**Niche:** [[niches/independent-restaurants/daily-specials-menu-rotation/profile|Daily Specials & High Menu Rotation Restaurants]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Demand forecasting tools predict sales for a stable menu but cannot forecast demand for a dish that has never appeared before — making them useless for daily specials.
**Tags:** #gradient-boosting #time-series-forecasting #regression #tabular-ml #data-integration

## The Problem
A restaurant running 3 daily specials needs to know how many portions to prep. But the special is a new dish — there is no sales history. The chef preps 25 portions based on gut feel, sells 18, and wastes 7 ($70-$150 in discarded product). Alternatively, they prep 15, sell out by 7:30 PM, and turn away customers for the rest of the night. This over/under-prep cycle happens every day.

## What Already Exists
Demand forecasting tools (built into advanced POS analytics or standalone products like 5-Out) predict item-level demand using historical sales data. They work well for stable menu items with 30+ days of sales history. They have no mechanism for predicting demand for a dish that has never been served before.

## The Customization Gap
The tool must forecast demand for new daily specials using proxy signals: the dish's protein category (fish specials historically sell X portions on Thursday), price point relative to the core menu (higher-priced specials sell fewer portions), server enthusiasm scores (specials the servers pitch sell 2-3x more), and seasonal patterns (lighter specials sell better in summer). This requires a "category-level" forecast that transfers learning from past specials to new ones, not an item-level forecast that requires per-dish history.

## Target Customer
Chefs at restaurants running daily specials who currently prep quantities based on gut feel and experience 15-30% over- or under-prep waste.

## Impact If Solved
Reducing daily specials waste by 50% saves $100-$300/week for a typical restaurant running 3 specials/day — $5K-$15K annually, plus the revenue recovery from not selling out on popular specials.
