# A Stocking Order Scored Against Last Year's Sell-Through

**Niche:** [[niches/powersports-and-boat-dealers/model-year-stocking-floorplan/profile|Model-Year Stocking & Floorplan Curtailment]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The dealer commits to next season's boats or side-by-sides at the OEM meeting with no model of which configurations sold before their free-flooring period ended last year.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #bayesian-inference #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set a dealer's model-year stocking order and aged-unit plan so that inventory sells before the floorplan's free period ends, and whoever leaves the fewest units past their first curtailment at model-year end takes the account.

## The Problem
The stocking order is the biggest decision a dealer makes all year and the least measured. The general manager picks lengths, engines, colours and packages from the OEM's order tool, guided by last year's memory, the OEM rep's targets and the programme money on offer for early commitment. A year later the outcome is plain in the DMS: which units sold in season, which went past the free period, which were discounted or dealer-traded. Nobody joins that outcome to the order that caused it.

## Why Nobody Has Built This
OEM order tools are built to sell the OEM's plan, not to second-guess it. DMS vendors report aging after the fact. Lenders see aging across many dealers but sell credit, not advice. And a single store's history is thin for any one configuration, so a model needs pooled data across a group or region.

## What to Build
A unit-level history joining each floored unit's configuration, order date, floor date, OEM interest-free end, curtailment dates, discounts and sale date. A survival model estimates each configuration's chance of selling before its deadlines in this market, pooled across stores with a hierarchical prior and adjusted by registration data and boat-show and weather calendars. The planner scores a proposed stocking order before it is submitted: expected units past first curtailment, expected carrying cost, and the swaps that would cut both.

## Target Customer
General managers and dealer principals at multi-store marine and powersports groups first; single stores through a DMS integration.

## Impact If Built
A 300-unit dealer that ends the model year with 20 fewer units past first curtailment (estimate) avoids roughly $100,000–200,000 in interest, curtailment cash and closing discounts.
