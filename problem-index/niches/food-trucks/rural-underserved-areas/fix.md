# Fuel-Adjusted Route Profitability Tracking

**Niche:** [[niches/food-trucks/rural-underserved-areas/profile|Rural & Underserved Area Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Fix (Pain Point)
**One-liner:** Rural operators drive 100-200 miles per day but have no way to know whether distant stops earn enough to cover the fuel cost of reaching them — they keep unprofitable stops out of loyalty until the math becomes undeniable.
**Tags:** #regression #tabular-ml #data-integration #revenue-impact

## The Problem
Fuel is the second-largest expense for rural food trucks (after food cost), often running $150-$400/week. A stop that generates $150 in revenue but requires 40 miles of round-trip driving may net less than $50 after fuel, food cost, and time. Operators currently track total revenue and total fuel expense but do not allocate fuel cost per stop. This means they cannot identify which stops on their route are net-negative and which are subsidizing the unprofitable ones.

## Why It's Still Broken
Per-stop profitability requires combining three data sources: POS revenue per stop (possible with geotagged transactions but not currently segmented), mileage between stops (trackable but not tracked), and per-mile fuel cost (varies with gas prices, truck weight, and terrain). No tool assembles these inputs automatically. Operators who try to calculate this manually face a 30-minute spreadsheet exercise per route day — unsustainable for solo operators working 12-hour days.

## What a Fix Looks Like
Automatic mileage tracking (GPS-based) that segments each route day into stop-to-stop legs, paired with POS revenue per stop and current fuel cost per mile (calculated from fill-up receipts or connected fuel card data). The system produces a per-stop P&L showing revenue minus allocated fuel, food cost, and time — updated weekly. Stops that are net-negative for 3+ consecutive weeks are flagged with a recommendation to drop or replace.

## Who Feels the Pain
Rural operators running 5-10 stop routes across 100+ miles who keep 2-3 unprofitable stops out of habit, losing $2K-$5K annually in fuel-adjusted losses.

## Impact If Fixed
Dropping or replacing 2-3 net-negative stops and optimizing route order to reduce total mileage saves $3K-$7K annually in fuel and recaptures 4-6 hours per week currently spent driving to unprofitable locations.
