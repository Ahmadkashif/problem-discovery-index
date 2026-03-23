# Data-Driven Sales Visit Prioritization for Rep Effectiveness

**Niche:** [[niches/restaurant-suppliers/sales-territory-optimization/profile|Sales Territory Optimization]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product tells a restaurant supply sales rep which accounts to visit this week based on churn risk, cross-sell potential, and visit ROI — reps currently prioritize by habit (same route every week) or squeaky-wheel (whoever called to complain gets the visit).
**Tags:** #gradient-boosting #binary-classification #ranking #tabular-ml #revenue-impact #ai-agent

## The Problem
A sales rep with 100 accounts has time for 20-25 visits per week. Which 20-25 should they visit? Currently, the answer is based on routine (visit the same accounts on the same day every week) and reactive signals (a chef complained, so visit them). This approach allocates sales effort uniformly when it should be allocated dynamically: accounts showing early churn signals (order frequency declining, SKU breadth narrowing) need immediate visits; accounts with cross-sell potential (buying proteins but not produce from us, while comparable accounts buy both) need consultative visits; and stable, satisfied accounts can be visited biweekly instead of weekly without risk. The difference between optimal and current visit allocation is estimated at 20-30% of sales effectiveness — worth $200K-$800K in retained and expanded revenue per rep territory.

## Why Nobody Has Built This
Visit prioritization requires: (1) churn risk scoring from ERP order data (declining order frequency, reduced SKU diversity, increased stockout experience), (2) cross-sell opportunity scoring from peer comparison (what do similar accounts buy that this account does not?), (3) visit ROI estimation (will a visit to this account retain more revenue than a visit to that account?), and (4) route-aware scheduling (the prioritized accounts must be geographically visitible in a single day). This is a classic optimization problem — well-understood in enterprise sales tech (Gong, Clari, Xactly) but never built for the food distribution context where "visit" means an in-person stop at a restaurant kitchen, not a Zoom call.

## What to Build
A weekly visit recommendation engine that: (1) scores every account on churn risk (will this account reduce spend in the next 30 days?), cross-sell opportunity (what category gaps exist vs. peers?), and relationship health (when was the last visit, last complaint, last credit?), (2) ranks accounts by visit ROI (expected revenue impact per visit), (3) generates a recommended weekly visit schedule optimized for geographic efficiency (route-aware clustering of priority accounts), and (4) delivers the recommendation to the rep's phone each Monday morning: "This week: visit these 22 accounts. Focus topics: Tony's Pizzeria [churn risk — protein orders down 20%], Maria's Kitchen [cross-sell — not buying seafood, similar accounts average $800/month in seafood]."

## Target Customer
Sales managers at restaurant suppliers with 3+ outside sales reps. Approximately 2,000-3,000 US suppliers at this scale. Price model: $200-$500/rep/month justified by retained and expanded revenue.

## Impact If Built
Churn detection at the rep level catches declining accounts 4-6 weeks earlier, retaining 15-25% of at-risk revenue. Cross-sell conversion increases 10-15% through systematic opportunity presentation. Rep visit efficiency improves 20-30% — more revenue-impactful visits per week with fewer wasted visits to stable accounts. Combined annual impact of $100K-$400K per rep territory.
