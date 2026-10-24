# A Cutting Plan That Knows the Ad and the Box

**Niche:** [[niches/grocery-stores/meat-seafood-cutting-room/profile|Meat & Seafood Cutting Room]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Meat cutters decide every morning how each box is split between premium cuts and grind, from memory of what sold and a glance at the box, with no plan that weighs margin, demand and shelf life together.
**Tags:** #tacit-knowledge-ml #gradient-boosting #optimization-fundamentals #time-series-forecasting #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each delivery of subprimals and fish into the cuts, grinds and trays that sell before their date, and whoever raises the department's realised margin per pound received takes the account.

## The Problem
A box of beef round can become top round steaks, London broil, stew meat, cube steak or ground round. Each has a different price, sales rate and shelf life. An experienced cutter balances these by feel: more steaks before a grilling weekend, more grind when the case is full of steaks marked down. A new cutter follows a fixed chart or yesterday's sales, and the department either marks down steaks or runs out of grind.

## Why Nobody Has Built This
Store meat software prints labels and records sales; it does not plan cutting. Yield data from cutting tests is held by packer sales reps and filed in spreadsheets. Many chains moved to case-ready product, so software investment went to the packers.

## What to Build
A morning cutting plan per store. Forecast demand per cut for the next three days, from sales, ad and weather. Use yield coefficients per subprimal learned from the store's own scale records (pounds received against pounds labelled per cut). Add shelf life per cut. Solve for the split that maximises expected margin net of markdowns, show it to the cutter as a box-by-box plan, and learn from what the cutter changes.

## Target Customer
Meat merchandising directors at chains that still cut in store, especially regional and independent chains.

## Impact If Built
For a meat department selling ~$1.5M a year, raising realised margin by 1 point through better cut mix is ~$15,000 a year per store (estimate).
