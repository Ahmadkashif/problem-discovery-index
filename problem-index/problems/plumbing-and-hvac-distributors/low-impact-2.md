# Seasonal Buys Planned on Last Summer and the Last Rule

**Industry:** [[plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Demand-planning software forecasts SKUs from sales history; it doesn't know that condensers sell on heat waves, that water heaters fail on cold snaps, or that a regulator can strand a warehouse of R-410A units and then change its mind.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #gradient-boosting #monte-carlo-methods #data-integration #automation #revenue-impact

## The Problem
A residential HVAC distributor makes its year in a few weeks. Condensing units, coils and furnaces have to be in the right branches before the first heat wave or cold snap, because a dealer whose customer has no cooling buys from whoever has the matched system that day. The buy is placed months ahead, often on manufacturers' early-order or pre-season programmes with dating terms, and the branch and purchasing managers set it largely from memory of last year, the tonnage mix in their territory and what the manufacturer is allocating. Water heaters work the same way in reverse: failures rise in cold weather, and a plumber with a flooded basement buys the first 50-gallon unit in stock (recalled pattern).

Regulation now moves the target. Watsco converted more than $1B of inventory to A2L products in 2025 as the transition touched ~55% of its products, and the industry planned around EPA's 1 January 2026 deadline for installing R-410A equipment, which EPA's May 2026 final rule then lifted for pre-2025 units, effective 27 July 2026. Distributors that had marked R-410A stock down to clear it, and those that had held it back, got opposite results. SEER2 regional rules, the 2029 water-heater standard and manufacturers' allocation during shortages all change what can be sold where and when.

## What Already Exists
Inventory and demand-planning tools such as Netstock, GAINS, Blue Ridge, Slimstock and ToolsGroup, plus the replenishment modules in Eclipse, Infor CSD and Prophet 21, forecast SKU demand from history, set min/max and suggest purchase orders. Weather feeds and degree-day data are freely available. Watsco and Ferguson build their own.

## The Customisation Gap
The industry-specific layer is weather, regulation and matched systems. Forecasts need cooling and heating degree-days and extreme-event forecasts by branch, the installed base's age and refrigerant, regulatory cutoffs and regional efficiency rules as hard constraints, manufacturers' allocation and pre-season terms, and the fact that a condenser is only sellable with the coil and furnace that complete an AHRI-matched system, so components have to be planned as sets. It also needs a sell-down plan for stock a rule may strand, with the probability that the rule changes. Generic tools treat each SKU alone and each year like the last.

## Impact If Solved
If peak-week stock-outs on matched systems fall by a third and year-end obsolete stock by ~10–20% (estimate), a distributor with ~$100M of seasonal inventory frees several million dollars of working capital and keeps the dealers it would otherwise lose on the hottest week.
