# Commodity Lumber & Panel Pricing

**Parent Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to reprice every open quote, builder price sheet and counter price to the latest lumber and panel market before the material ships, and whoever lets the fewest packages ship below replacement cost without losing bids to stale prices takes the account.

## Profile
**Market Size:** ~$90B a year of dealer sales of commodity framing lumber, boards and structural panels (estimate; Builders FirstSource reported $3.9B, 25.5% of its 2025 sales, as lumber and lumber sheet goods)
**Share of Parent Industry:** ~19% of the codes' receipts (estimate)
**Digital Adoption:** Low-Medium — ERPs hold price matrices and costs, but repricing to the market is a buyer's judgement applied by hand
**Target Buyer:** Commodity buyer, pricing manager or general manager
**Automation Potential:** Very High — replacement cost, hold periods and margin floors are rules over a market reference

## What Makes This a Distinct Niche
Commodity lumber is the one category whose cost a dealer doesn't control and can't predict. Mills and wholesalers trade framing lumber and panels against weekly assessments (the Random Lengths Framing Lumber Composite weights 15 framing prices, the Structural Panel Composite 11 panel items), CME's futures are thin beside the physical trade, and Canadian softwood carries anti-dumping and countervailing duties (35.16% for most producers until Commerce's seventh-review rates, 24.75%, take effect after their 14 October 2026 announcement) plus a 10% Section 232 tariff since 14 October 2025. The dealer's pricing job is mechanical once the reference is known — replacement cost plus freight and duty, plus margin, applied to every open quote and price sheet within its hold period — which is why it is automatable, and why it is separate from the takeoff, whose contest is quantity. The electrical analogue is [[niches/electrical-distributors/wire-cable-copper-pricing/profile|Wire & Cable Pricing Against COMEX Copper]]; the price assessments themselves are logged as a Pass 2 pocket below.

## Current Tools & Gaps
LBM ERP price matrices and cost updates, licensed price reports, general price-optimisation software (Zilliant, PROS, Pricefx, recalled), and spreadsheets kept by the commodity buyer. The gaps: open quotes never swept when the market moves, duty changes passed through late, and no record of margin lost to stale prices.

## Problems
- [[niches/building-material-dealers/commodity-lumber-panel-pricing/build|🔨 Build: The Daily Sweep of Every Open Lumber Quote]]
- [[niches/building-material-dealers/commodity-lumber-panel-pricing/buy|🛒 Buy: Price Optimisation Re-Based on Replacement Cost]]
- [[niches/building-material-dealers/commodity-lumber-panel-pricing/fix|🔧 Fix: Duty Changes Passed Through a Month Late]]
