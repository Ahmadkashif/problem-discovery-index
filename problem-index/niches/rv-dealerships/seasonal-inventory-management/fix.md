# Floor Plan Interest Bleeding on Slow-Moving Winter Inventory

**Niche:** [[niches/rv-dealerships/seasonal-inventory-management/profile|Seasonal Inventory Management]]
**Industry:** [[industries/rv-dealerships|RV Dealerships]]
**Type:** Fix (Pain Point)
**One-liner:** RV dealers pay $200-$500/month per unit in floor plan interest on inventory that sits unsold from September to March — losing $50K-$200K per winter season on carrying costs alone.
**Tags:** #time-series-forecasting #regression #tabular-ml #revenue-impact

## The Problem
Floor plan financing is the lifeblood of RV dealer inventory — the dealer borrows to purchase inventory and pays interest until the unit sells. At current rates, floor plan interest runs 7-9% annually, or $175-$500 per month on a $30K-$65K unit. During the September-February off-season (in northern states), sales drop 60-70% but inventory stays on the lot. A dealer carrying 150 units through winter at $300/month average floor plan cost bleeds $45,000 per month — $270,000 over a 6-month off-season. The GM knows this is happening but has no tool modeling the total carrying cost or recommending optimal end-of-season pricing to minimize total winter bleed.

## Why It's Still Broken
DMS platforms report floor plan costs per unit but don't aggregate the seasonal impact or model the trade-off between price reduction and carrying cost. The GM's decision is: "Should I drop this $38,000 trailer to $33,000 to sell it in October, or hold it until March and sell it at $36,000 after paying $2,100 in additional floor plan interest?" This is a straightforward financial calculation, but no tool performs it with market-adjusted sell-through probabilities at each price point.

## What a Fix Looks Like
A seasonal carrying cost model that takes each unit's current asking price, floor plan interest rate, projected days-to-sell at current price (based on market data), projected days-to-sell at reduced prices, and outputs the optimal pricing strategy: "Reducing from $38,000 to $34,500 today gives a 72% probability of selling before December 1, saving $1,800 in carrying costs. Net revenue at $34,500 minus saved carrying costs = $36,300 effective price. Holding until March at $36,000 with $2,100 in additional carrying costs = $33,900 effective price. Recommendation: Reduce now." The GM sees carrying-cost-adjusted pricing across all inventory.

## Who Feels the Pain
Dealer principals who see floor plan interest consume 3-5% of annual gross revenue during the off-season without a clear strategy for when and how much to reduce prices, and GMs who are pressured by manufacturers to take on more inventory during summer build season.

## Impact If Fixed
Reduces total winter carrying costs by 25-40% through optimized seasonal pricing decisions, saving $50K-$100K per winter season for a typical northern-state dealer. Frees up floor plan capacity for fresh spring inventory by clearing aging units before winter.
