# Sales Rep Account Churn Prevention

**Industry:** [[restaurant-suppliers|Restaurant Suppliers]]
**Type:** High Impact
**One-liner:** Every lost restaurant account is $8K-$25K in annual revenue that walked to a competitor because nobody noticed the order frequency dropping.
**Tags:** #gradient-boosting #binary-classification #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
Independent restaurant suppliers lose 5-12% of accounts annually, and most churn is invisible until the account stops ordering entirely. A typical rep manages 100+ accounts and cannot mentally track whether Tony's Pizzeria shifted from 3 orders/week to 1 order/week over the last month. By the time the rep notices, the chef has already established a relationship with a competing distributor. At a $20M independent distributor, 5% churn represents $1M in lost annual revenue — most of which was preventable if flagged 4-6 weeks earlier.

## Why It's Unsolved
The signal is in ERP order history data that already exists, but independent distributors lack the analytics capability to extract it. Churn in foodservice distribution is not binary — a restaurant may reduce spend category by category (first losing produce, then proteins, then dry goods) rather than leaving all at once. Seasonal restaurants, menu changes, and temporary closures create noise that simple threshold alerts cannot distinguish from genuine defection patterns. The reps who are best at retention do this pattern recognition intuitively, but they can only hold ~20 accounts in active mental focus at any time.

## What a Solution Looks Like
A model trained on 2-3 years of order history across all accounts, predicting 30-day churn probability per account per week. Inputs include order frequency, basket composition changes, SKU-level substitution patterns, payment timing shifts, and seasonal baselines. Output is a ranked list pushed to each rep's phone every Monday: the 5-10 accounts most likely to churn this month, with the specific behavior change driving the score (e.g., "protein orders down 40% vs. 90-day average"). The rep calls or visits those accounts that week.

## Impact If Solved
Recovering even 20% of at-risk accounts at a mid-size distributor ($20M revenue) saves $200K-$400K annually. Across the independent distribution segment, systematic churn prevention could shift $2-3B in revenue retention industry-wide. Reps become more effective without working harder — they just know where to focus.
