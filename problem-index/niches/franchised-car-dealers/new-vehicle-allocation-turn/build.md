# An Order Desk That Learns From Every Unit

**Niche:** [[niches/franchised-car-dealers/new-vehicle-allocation-turn/profile|New-Vehicle Allocation & Inventory Turn]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The manager's take, decline and trade decisions are never recorded beside the unit's days-to-sale, so the store cannot learn which order calls made money.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #causal-inference #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put the configurations this market buys on the lot without losing allocation, and whoever cuts average days-to-turn on new units takes the account.

## The Problem
Each order cycle a manager scans the allocation offer and decides from experience. Outcomes arrive weeks later in the DMS, unjoined to the decision, so a manager who ordered well and one who got lucky look the same, and a new manager starts from zero.

## Why Nobody Has Built This
Allocation data sits in OEM portals without APIs; outcome data in the DMS; and outcomes for declined configurations don't exist at the store, which needs pooled group data and counterfactual methods to fill.

## What to Build
A desk beside the portal that scores each offered unit with an expected days-to-sale and gross range from survival models on store and group history, shows comparable recent units and the open stair-step gap, and captures the manager's decision and reason in one click. Monthly it grades the manager's calls against the model's and the outcome. The full problem is set out in [[problems/franchised-car-dealers/high-impact|The Order Board Nobody Can Explain]].

## Target Customer
New-car directors and general managers at dealer groups with five or more stores of one brand.

## Impact If Built
Ten fewer days-to-turn on ~950 units a year saves ~$80,000–95,000 in floorplan per store (estimate), plus allocation earned on faster turn.
