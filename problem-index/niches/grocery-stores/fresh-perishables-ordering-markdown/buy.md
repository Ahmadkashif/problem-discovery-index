# Centre-Store Replenishment Engines Adapted to Fresh

**Niche:** [[niches/grocery-stores/fresh-perishables-ordering-markdown/profile|Fresh Perishables Ordering & Markdown]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Chains already run replenishment engines that order centre-store goods without a human; extending them to fresh needs shelf life, random weight and condition in the model.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #data-integration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to cut fresh-department shrink without emptying the shelves". But that contest splits in two. Ordering vendors win before the truck arrives, by cutting the most shrink at an unchanged in-stock rate. Markdown, surplus and dynamic-pricing vendors win after the product is aging, on margin recovered per lot. The buyers, data and winners differ. Decomposed into contested sub-niches below.

## The Problem
Most chains already pay for a replenishment system that writes centre-store orders automatically from forecasts and on-hand counts. Fresh was carved out and left to department managers, so the chain runs two ordering worlds with different data and different accountability.

## What Already Exists
Blue Yonder, RELEX, SAP and Oracle Retail replenishment, built for items with long shelf life, unit counts and stable demand.

## The Customization Gap
Fresh needs a different model inside the same engine. Shelf life must be a constraint, so the order covers demand until the product dies rather than until the next delivery. Random-weight items must be ordered in cases and sold in pounds. On-hand is unreliable after culls, so inventory must be estimated rather than trusted. Product condition at receipt changes remaining life. Promotion lift is sharper and cannibalises neighbouring items. And the manager must be able to override with a reason that the engine learns from.

## Target Customer
Replenishment directors at chains already licensing an enterprise engine who want fresh inside it rather than a second vendor.

## Impact If Solved
Moving fresh ordering into an engine the chain already runs could free ~30 minutes a day per department manager across ~5 fresh departments a store, ~900 hours a store a year (estimate).
