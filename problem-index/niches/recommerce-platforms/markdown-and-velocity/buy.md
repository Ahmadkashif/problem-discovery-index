# Markdown Optimisation and Revenue Management

**Niche:** [[niches/recommerce-platforms/markdown-and-velocity/profile|Markdown & Velocity]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail markdown optimisation and airline revenue management both solved selling perishable inventory over a finite horizon, and recommerce uses a percentage at thirty days.
**Tags:** #convex-optimization #dynamic-programming #survival-analysis #confidence-intervals #time-series-forecasting #revenue-impact #evaluation-metrics #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to move each unique unit at the right moment for the right price rather than on a schedule — and whoever does that recovers the margin, because a markdown calendar applied to one-of-a-kind inventory is wrong for almost every item on it.

## The Problem
Deciding when and how much to discount inventory that loses value over a horizon is a mature optimisation problem. Retail markdown optimisation solves it for seasonal goods with demand response estimation and a terminal date. Airline revenue management solves the continuous version with a hard expiry. Both produce a policy that depends on remaining time, remaining inventory and observed demand rather than on a calendar of fixed reductions. Recommerce has the same structure with a unit quantity of one.

## What Already Exists
Markdown optimisation with price elasticity estimation and terminal value; dynamic programming formulations of the finite-horizon pricing problem; revenue management with demand forecasting and booking curve monitoring; clearance channel optimisation; and the retail practice of managing to a sell-through target.

## The Customization Gap
The adaptation is to a quantity of one and no comparable history for the specific item. It requires: (1) demand response estimated across similar items rather than from the item's own price history, since a unit of one cannot be observed at two prices — pooling elasticity across comparable items is the substitution that makes the whole apparatus applicable; (2) the item's engagement as the booking curve, since views and saves are the observable demand signal and an airline watches bookings, which is a direct and unused analogy; (3) terminal value that is a disposal cost rather than a salvage value, which reverses the sign of the endgame and should make early exit far more attractive than the retail intuition suggests; (4) storage cost per item per period as an explicit term, since it is a meaningful fraction of a low-value item and is absent from the retail formulation; and (5) computation cheap enough for millions of individual items, which rules out per-item optimisation solved exactly and argues for a learned policy.

## Target Customer
Merchandising and pricing functions, recommerce platforms, and the revenue management community for whom unit-quantity inventory is an unusual and interesting variant.

## Impact If Solved
The structure is a finite-horizon pricing problem with a quantity of one, solved elsewhere and run here on a calendar. Pooled elasticity across comparable items substitutes for the price history a single unit cannot have, and a disposal cost rather than a salvage value should make early exit far more attractive than retail intuition suggests.
