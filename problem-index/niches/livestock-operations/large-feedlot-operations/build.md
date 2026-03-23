# Integrated Cattle Placement and Closeout Projection Engine

**Niche:** [[niches/livestock-operations/large-feedlot-operations/profile|Large Feedlot Operations]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product connects the cattle buying decision (what to pay for incoming feeder cattle) with the predicted closeout outcome (profit or loss 150 days later) using ML-driven projections of gain, health cost, carcass quality, and market price at harvest.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
A feedlot cattle buyer commits $1,500-2,500 per head when purchasing feeder cattle, and the profitability of that decision is not known for 120-180 days — when the finished animal is sold to a packer. Experienced buyers develop an intuitive model that integrates the animal's breed, frame score, flesh condition, source reputation, current corn price, and projected fed cattle futures to arrive at a maximum bid price. This tacit pricing model varies by buyer and is never documented. When a senior buyer retires, the replacement makes costly mistakes for 3-5 years while rebuilding that judgment. Meanwhile, closeout projections (will this pen make or lose money?) are calculated in spreadsheets using static assumptions about gain, feed cost, and market price that drift as conditions change.

## Why Nobody Has Built This
The model requires linking purchase data (price paid, source, arrival condition) through feeding performance (daily gain, feed conversion, health costs) to carcass outcomes (quality grade, yield grade, hot carcass weight) and final revenue (grid pricing, premiums/discounts). This data chain spans 5-6 months per animal and crosses multiple software systems. No single platform collects the full chain, and feedlot operators have been reluctant to share the linked datasets needed to train predictive models because closeout data is competitively sensitive.

## What to Build
A decision-support platform that ingests historical closeout data (purchase price, feeding performance, health cost, carcass data, revenue) from 10,000+ head-lots to build a gradient-boosted model predicting closeout margin at the moment of purchase. The buyer enters the proposed purchase price and cattle description; the system returns projected profit/loss with confidence intervals, sensitivity to corn price changes and fed cattle market movement, and comparison to historical lots of similar cattle. Rolling projections update weekly as actual feeding data accumulates.

## Target Customer
Feedlot managers and cattle buyers at operations placing 5,000-100,000 head annually. Approximately 2,000-3,000 feedlots at this scale in the US. Average contract value: $500-2,000/month depending on head count.

## Impact If Built
Improving placement decisions by $10-20/head across 50,000 head/year represents $500K-$1M in annual margin improvement. Reducing closeout surprises by 30-50% improves cash flow predictability and reduces the frequency of catastrophic pen losses that currently run $100-200/head on the worst closes.
