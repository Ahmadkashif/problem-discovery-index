# The Only Closed Loop in Advertising, Spent Counting Sales That Were Already Happening

**Industry:** [[retail-media-networks|Retail Media Networks]]
**Type:** High Impact
**One-liner:** The retailer shows the ad and rings the sale in the same system, and still reports a ROAS that counts shoppers who searched the brand by name and subtracts nothing for the organic sale the ad displaced.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #monte-carlo-methods #evaluation-metrics #revenue-impact #survival-analysis

## The Problem
A shopper types a brand name into a retailer's search box. The top result is a sponsored placement for that brand, bought at auction. They click it and buy. The retail media network records an attributed sale and reports a return on ad spend in the high single or low double digits, and the brand's e-commerce team takes that number to their trade budget meeting.

Almost none of that sale is caused by the ad. The shopper had already named the product; the organic result directly below it was the same item; in the counterfactual where no ad ran, the overwhelming majority of those shoppers buy anyway. Worse, the attributed sale is frequently a sale the retailer would have made regardless, now with a media fee attached that the brand funded out of the same trade budget that used to buy promotions.

The displacement is the part that is never counted. A sponsored slot occupies a position an organic result would have held. If the displaced result was a different brand, the network has moved a sale between suppliers and counted it as created. If it was the same brand's own organic listing, the network has charged a brand for a sale it was going to get free. Both are ordinary, both are measurable in principle, and neither appears in a standard retail media report.

Around this sits a set of practices everyone in the category can name: attribution windows generous enough to sweep in unrelated purchases, view-through credit on placements barely seen, and comparison across networks made impossible by inconsistent definitions the IAB standards arrived too late to fix.

## Why It's Unsolved
The barrier is not technical and everybody knows it. A retailer can hold out sponsored placements for a random subset of search sessions, or run a geographic or store-level switchback, and read the incremental effect cleanly within weeks. The instrumentation is straightforward and the data is already in one system under one customer identity. This is the easiest causal measurement problem in the entire advertising industry.

It is unsolved because of what the answer would do. Retail media is 70-90% gross margin and has become material to the earnings of several large retailers — in some cases the difference between a growing and a flat operating profit. A measurement upgrade that reduces reported ROAS by a large factor invites budget reallocation away from the channel. The person who would commission the study reports to the person whose number it would reduce.

Brands are not innocent parties either. The e-commerce lead who bought the media also reported the ROAS internally, and an honest number is a worse quarter for them too. So both sides of the transaction have a reason to prefer the inflated figure, and the market clears on a metric neither believes — which is a stable equilibrium, not an oversight.

The one genuinely hard piece is the second-order effect: what the ad load costs in shopper experience, basket composition and return frequency over months. That is a real measurement problem, with long horizons, small per-session effects and enormous confounding, and it is the part no retailer currently has an answer to.

## What a Solution Looks Like
Make incrementality the reported number, not a study. Continuous randomised holdouts at the auction or session level, rotating across categories and query types, produce a permanent stream of causal estimates rather than an annual PDF. Reported per campaign, per keyword class, per placement, with intervals. Brand-name queries and category queries separate immediately, and they are two entirely different products that the industry currently sells as one.

Count displacement explicitly. What the sponsored slot displaced is knowable — the ranking without ads is computable for every impression served — and the value of the displaced item is in the same database. Reporting incremental revenue net of displacement is arithmetic once the counterfactual ranking is retained, and no network does it.

Separate the retailer's question from the brand's. The brand wants incremental units of their product. The retailer wants incremental category revenue, incremental basket, and no long-run loyalty damage — and those objectives conflict, sharply, on exactly the brand-name queries that produce the best reported ROAS. A network that can state both numbers is selling something different from one that reports attributed sales.

And measure the load. Ad density is a shopper-experience variable the retailer controls continuously and can therefore randomise; the cost shows up in basket and return rate over a horizon of months, which requires cohort-level causal analysis rather than campaign reporting, and is the single most valuable unanswered question in the category.

## Impact If Solved
For the retailer this determines whether retail media is a durable business or a harvest. A network that can prove incremental value keeps its budgets when brands eventually force the question — and they are already forcing it, with the largest advertisers now running their own holdouts and finding what everyone expected. For brands it reallocates a budget line measured in billions from placements that buy sales they already had to ones that find demand. And the shopper-experience measurement gives a retailer the one number it currently lacks about a business unit it has come to depend on: what the ad load is costing the store.
