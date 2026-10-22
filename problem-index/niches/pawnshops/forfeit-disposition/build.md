# A Per-Item Channel Decision at Forfeit

**Niche:** [[niches/pawnshops/forfeit-disposition/profile|Forfeit Disposition]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each forfeit goes to the shelf by default, when the store's own history could say which items belong online, which in a wholesale lot and which at the refiner.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #markov-decision-processes #evaluation-metrics #revenue-impact #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to turn a forfeited item into the most cash in the fewest days" — but for precious metal the contest is sorting and timing scrap lots against spot and a refiner's assay, and for everything else it is identifying, pricing and listing one-of-one used goods to buyers beyond the store; different inputs, clocks and winners. Decomposed into contested sub-niches below.

## The Problem
When a ticket forfeits, the item is tagged and put out. If it does not sell it ages, is marked down, and eventually goes to a wholesaler or the refiner at a fraction of its loan cost. The routing decision that matters most is made by default.

## Why Nobody Has Built This
POS systems treat a forfeit as a stock receipt, not a decision. The data needed — sale probability by channel and price for this kind of item in this store — exists only as history nobody has modelled.

## What to Build
At the moment an item clears its hold, estimate net value and days to sale for each channel — floor, online, wholesale, refiner — using the store's sales history, marketplace fees, spot price and the item's condition grade, and route it. Re-evaluate weekly with markdowns. Report realised value against the original loan so the lending guide learns.

## Target Customer
Merchandising leaders at chains; multi-store independents with an online channel.

## Impact If Built
More forfeits reach the channel that pays most for them, aged stock falls, and the disposition results feed back to lending — the loop the industry lacks.
