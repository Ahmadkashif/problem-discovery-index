# Real-Time Load Profitability Scorer

**Niche:** [[niches/owner-operator-trucking/dry-van-long-haul/profile|Dry Van Long-Haul Operators]]
**Industry:** [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool scores loads by predicted net profit per hour — operators compare rate-per-mile, which ignores deadhead, fuel variance, tolls, detention risk, and backhaul opportunity.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A dry van operator sees a load posting: $2,800, Chicago to Atlanta, 715 miles, $3.92/mile. Looks good. But the operator is currently in Indianapolis (180 miles deadhead to Chicago), the route crosses the Appalachian grades (higher fuel consumption), I-24 has $45 in tolls, the shipper is known for 3-hour detention, and Atlanta is a soft outbound market (the next load will pay $1.80/mile heading back north). True net profit per hour might be $18 — below the operator's cost of capital. An experienced operator senses all of this in seconds. A new operator takes the load and loses money.

## Why Nobody Has Built This
Building a load profitability model requires integrating 8+ data sources in real time: load board feeds, GPS position, fuel prices by location, toll databases, ELD hours remaining, facility-level detention history, and lane-level market forecasts. The feature engineering is massive and the training data (what loads experienced operators actually take and what they actually net) doesn't exist in a structured dataset — it must be constructed by instrumenting operators' accept/reject decisions. No single vendor controls enough of the data stack to build this without significant data partnerships.

## What to Build
A load-scoring layer that sits on top of existing load boards (DAT, Truckstop) and ranks every available load by predicted net profit per hour, accounting for: deadhead to pickup, route-specific fuel cost, tolls, predicted detention time at origin and destination, HOS-feasibility, and backhaul market strength at destination. The score includes a confidence interval and flags loads where the model's ranking differs significantly from the posted rate-per-mile ranking — these are the hidden gems.

## Target Customer
Dry van OTR operators making 15-25 load decisions per week, currently evaluating loads by rate-per-mile alone.

## Impact If Built
Improving load selection quality by even 10% translates to $15,000-$30,000/year in additional net income per operator. Across 150,000 dry van OOs, even 5% adoption would redirect $100M+ annually from broker margin to operator income.
