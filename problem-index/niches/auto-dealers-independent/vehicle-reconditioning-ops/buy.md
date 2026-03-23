# Recon Cost Tracking and Budget Alerts

**Niche:** [[niches/auto-dealers-independent/vehicle-reconditioning-ops/profile|Vehicle Reconditioning Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Expense tracking tools exist, but none connect per-vehicle reconditioning cost to the acquisition price and target margin in real time — so dealers don't know they've exceeded their recon budget until the car is already on the lot.
**Tags:** #linear-regression #regression #tabular-ml #data-integration #revenue-impact

## The Problem
At acquisition, a dealer sets a mental recon budget: "I bought this car for $8K, recon should be under $1,200, I'll retail at $12K for a $2,800 gross." But recon costs arrive in pieces — $400 mechanic invoice today, $300 body shop bill next week, $150 detail next week, $200 tires next Friday — and nobody totals them against the budget until the car is listed. By then, the recon hit $2,100, the realistic gross is $1,700, and the car shouldn't have been reconditioned at all. The budget overrun is invisible during the recon process because cost tracking is retrospective, not real-time.

## What Already Exists
QuickBooks tracks vendor invoices but doesn't link them to specific VINs or compare them to per-vehicle budgets. Franchise recon tools (Rapid Recon) track recon cost per vehicle but require a workflow integration that independents don't have. DMS tools (Frazer, DealerCenter) track total recon cost per vehicle but only after invoices are manually entered, which may happen days or weeks after the work is done.

## The Customization Gap
The missing feature is real-time recon cost accrual per VIN that compares to the budget set at acquisition. When a mechanic's $400 invoice is entered (or better, received via photo/text from the vendor), the system immediately updates the running recon total for that VIN, compares to the budget, and alerts if the vehicle is on track to exceed its target gross. The alert should fire before additional work is authorized — giving the recon manager the option to stop further reconditioning and wholesale the vehicle instead of completing recon on a money-losing unit.

## Target Customer
Dealer principals and recon managers who discover recon budget overruns only after the fact, at the point of pricing — too late to change course.

## Impact If Solved
Prevents recon budget overruns on 10-20% of vehicles where stopping or diverting to wholesale would have been the better decision. On a 30-unit dealer losing $500 average per overrun on 5 vehicles/month, real-time budget tracking saves $2.5K/month. Enables data-driven recon budgeting: historical cost-by-category data improves future recon estimates at acquisition.
