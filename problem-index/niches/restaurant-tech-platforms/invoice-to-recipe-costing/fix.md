# The Plate Cost That Went Stale in March

**Niche:** [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/profile|Invoice-to-Recipe Costing]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Menu prices are set from plate costs computed once, and nothing in the category alerts an operator when the cost of a dish has moved enough that the price is now wrong.
**Tags:** #change-point-detection #time-series-forecasting #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #automation #quick-win
**Contested on:** Every serious competitor in restaurant back office is fighting to map a distributor invoice line to the recipe ingredient it actually is, at a cost per usable unit — and whoever holds the automatic match rate highest takes the account.

## The Problem
A dish was costed in January at $4.10 and priced at $17. By June the protein has moved up eleven percent, one produce item has doubled seasonally, and the dish costs $4.95 — a margin point and a half, on the restaurant's second-highest-volume entrée. Nobody knows. The back-office system holds every invoice and could compute the current cost of every recipe nightly, and it computes it when somebody opens the recipe. Operators re-cost menus once or twice a year, usually when profitability has already visibly deteriorated, and then wonder where the year went.

## Why It's Still Broken
Costing is modelled as a report rather than as a monitored quantity, so it runs when requested. Continuous costing also exposes the mapping quality problem — a cost that moves because an item was mis-mapped would generate a false alert, and vendors have preferred not to generate alerts they cannot stand behind. And there is a quiet reason on the customer side too: an operator who learns weekly that costs have moved has to decide weekly whether to raise prices, which is a conversation many would rather have annually.

## What a Fix Looks Like
Compute every recipe's cost on every invoice and watch it. Alert on movement that matters — a threshold expressed in margin points rather than in percentage of cost, because a ten percent move on a cheap ingredient is noise and a three percent move on the main protein is not. Decompose the movement to the ingredient responsible, so the alert is actionable: this dish is down 1.4 margin points and 90% of it is the salmon. Distinguish seasonal from structural movement using the item's own history, since an operator should respond differently to a predictable summer produce spike than to a permanent protein increase. Surface menu-level exposure — which dishes carry the most margin risk given their volume and their ingredient volatility — which is a ranking no operator currently has and which tells them where to focus a menu engineering exercise.

## Who Feels the Pain
Operators whose margin erodes invisibly between annual menu reviews; chefs blamed for food cost variance caused by market movement; and the vendors, whose product held the answer the whole time.

## Impact If Fixed
Continuous costing with margin-point alerting turns an annual exercise into a managed one, and on high-volume items the difference over a year is material. It is also almost free to build — every input is already in the system and the calculation already exists — which makes the absence of it a product decision rather than a technical one.
