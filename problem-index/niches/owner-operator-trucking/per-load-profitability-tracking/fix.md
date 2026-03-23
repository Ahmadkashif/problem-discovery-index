# Operating Blind on True Cost-Per-Mile

**Niche:** [[niches/owner-operator-trucking/per-load-profitability-tracking/profile|Per-Load Profitability Tracking]]
**Industry:** [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**Type:** Fix (Pain Point)
**One-liner:** Most operators set a rate floor based on what feels right — not on their actual cost-per-mile, which they've never calculated accurately.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #worker-facing

## The Problem
When a broker calls with a load at $2.40/mile, the operator has 30 seconds to decide. Their decision framework is: "My minimum is $2.50/mile." But where did $2.50 come from? Usually, it's a round number based on industry convention or advice from another driver — not a calculation of their actual fixed and variable costs. An operator whose true cost-per-mile is $1.75 is leaving money on the table rejecting $2.40 loads; an operator whose true cost-per-mile is $2.55 (due to high maintenance costs on an older truck) is losing money on every load at $2.50. Without knowing their actual cost-per-mile, operators either under-price (accepting unprofitable loads) or over-price (rejecting loads that would be profitable).

## Why It's Still Broken
Calculating true cost-per-mile requires dividing total annual costs (truck payment, insurance, fuel, maintenance, tires, permits, ELD, phone, accounting, health insurance) by total annual miles driven. The numerator is scattered across 15+ expense categories in different systems, and the denominator requires a full year of mileage data. Most operators don't have organized expense records, so they use industry average benchmarks ($1.50-$2.00/mile) that may be 30-40% different from their actual costs depending on truck age, insurance rates, fuel efficiency, and home state taxes.

## What a Fix Looks Like
A cost-per-mile calculator that ingests the operator's actual expenses (from connected bank/credit card feeds or manual entry of major categories), divides by ELD-verified annual mileage, and produces a personalized cost-per-mile breakdown: fixed costs/mile (truck payment, insurance, permits), variable costs/mile (fuel at their MPG and current prices, maintenance based on truck age/mileage), and total cost/mile with a recommended minimum rate (cost + target profit margin). Updated monthly as costs and mileage change. Displayed on a card that the operator can reference in 5 seconds during a broker call.

## Who Feels the Pain
The operator who has been running at $2.20/mile all year, proud of staying busy, only to discover at tax time that their actual cost-per-mile was $2.15 — meaning they netted $0.05/mile on 120,000 miles, or $6,000 for a year of 70-hour weeks.

## Impact If Fixed
Knowing actual cost-per-mile enables rational load selection. Operators who price above their true costs consistently net $15,000-$30,000 more per year than those who price by gut feel, because they confidently reject unprofitable loads and don't under-price their service.
