# Markdown Timing and Depth

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Type:** High Impact
**One-liner:** The platform tells an independent retailer which items to mark down, when, and by how much, using sell-through curves learned across hundreds of thousands of merchants — the capability enterprise retail has had for two decades and nobody below it can buy.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #logistic-regression #causal-inference #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
A specialty retailer buys a season's inventory months ahead. Some of it sells at full price. Some of it does not, and every week it does not is a week of carrying cost, floor space and capital tied up in goods that are becoming less valuable.

The markdown decision is where the season's margin is decided. Mark down too early and you give away margin on goods that would have sold anyway. Too late and you are clearing at seventy per cent off into an end-of-season market where everyone else is doing the same. Too shallow and nothing moves. Too deep and you leave money on the table and train customers to wait.

Independent retailers make this decision by looking at the rack. They know roughly how far into the season they are, they can see what has not moved, and they discount when the anxiety exceeds the reluctance. Some keep a spreadsheet. Most do not.

Enterprise retail solved this in the 1990s. Markdown optimisation is a mature discipline with well-understood methods, and every large chain runs it with a planning team. It has never been available below that tier, because it required analysts and because the vendors serving independents never attempted it.

The POS platforms hold everything it needs. Item-level sales history by store, by week, with price. Inventory positions. Category and seasonal structure. And, critically, the same item or its close analogue selling across hundreds of other merchants at different price points at different points in the season.

## Why It's Unsolved
A single independent retailer is a small-sample problem in the purest form. One store, one season, a few units of each SKU. There is no way to learn a price response curve from that data alone, which is precisely why the individual merchant's intuition has never been beaten locally and precisely why pooling should win decisively.

Pooling is blocked by the catalogue. To learn that this style of boot sells through in this pattern, you must recognise that merchant A's item and merchant B's item are the same or comparable product — and specialty retail catalogues are free text with no consistent identifier, no shared attribute schema, and vendor style codes that differ by account. The product resolution problem sits underneath the modelling problem and nobody has solved it.

There is a commercial hesitancy too. Advising a merchant to discount is advising them to reduce revenue today for a better outcome overall, and if the advice is wrong the merchant sees the lost margin immediately and the avoided loss never. That asymmetry has kept vendors away from prescriptive recommendations in favour of dashboards, which are safe and useless.

## What a Solution Looks Like
Sell-through curves estimated per product category and seasonal position, pooled across merchants and adjusted for store, market and price point. From those, a projected residual inventory at season end under the current price, and the markdown schedule that maximises total realised margin — presented as a recommendation with the expected outcome and its uncertainty, not as a number.

The price response side needs care. Merchants set prices non-randomly, so observational data confounds price and demand, and the honest approach exploits the natural variation across merchants selling comparable goods at different prices in comparable markets.

The recommendation must be legible. A merchant will act on "this style is tracking twenty per cent behind comparable items at this point in the season, and items in that position that were reduced by fifteen per cent now cleared at a better realised margin than those reduced by forty per cent in eight weeks." They will not act on a score.

## Impact If Solved
Markdown is where independent retail margin is destroyed, and the decision is currently made by nervousness. Bringing enterprise-grade markdown discipline to merchants who could never staff a planning team is the largest single margin improvement available to the sector, and it rests on a pooled sell-through corpus no individual retailer or vendor of spreadsheets could ever build.
