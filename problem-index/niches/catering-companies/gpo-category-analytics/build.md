# Billions of Dollars of Weekly Line-Item Food Purchases, Reported as a Savings Percentage

**Niche:** [[niches/catering-companies/gpo-category-analytics/profile|Foodservice GPO Category Analytics]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The purchasing aggregators see what thousands of foodservice operators actually bought, at SKU level, every week, and observe what they switched to when a price moved — a revealed-preference record of the food economy that arrives months ahead of any published index.
**Tags:** #time-series-forecasting #causal-inference #change-point-detection #hypothesis-testing #confidence-intervals

## The Problem
Foodservice group purchasing organisations and the purchasing arms of the large contract caterers aggregate the spend of thousands of operators — caterers, campus dining, healthcare foodservice, restaurant groups — negotiate manufacturer agreements against that volume, and report savings and compliance back to members. Category managers research price movement, substitution options and supply risk across the food basket, and that research is what the negotiation is built on.

The by-product is a dataset with very few peers. Line-item purchases, at item and pack level, across billions of dollars of annual spend, segmented by operator type and geography, refreshed continuously.

Three things sit in it that nothing else captures.

The first is price, in near real time. Published food price statistics are collected on a lag, from samples, at category level. The GPO observes transacted prices at SKU level as they happen. When protein moves, they know within a week.

The second is substitution, which is the valuable one. When a price rises or an item goes short, operators switch — to a different brand, a different pack, a different cut, a different protein entirely. The GPO sees the switch, at the operator level, with the price change that caused it. That is a natural experiment in demand elasticity running continuously across thousands of buyers, and it is the question every food manufacturer spends heavily and imprecisely trying to answer through panels and surveys that do not cover foodservice at all.

The third is supply disruption. Fill rates, back orders and forced substitutions show a shortage forming well before it is reported anywhere.

What the organisation produces from this is a category strategy for the next negotiation and a quarterly savings report for members.

## Why Nobody Has Built This
The revenue model is the reason, and it is structural. A GPO earns rebates on purchasing volume. Analysis is a cost of running the negotiation and a retention feature for members; it is never separately invoiced. There is no line item that would fund a demand elasticity study, so there is no demand elasticity study.

Antitrust caution is real and shapes what gets built. An organisation aggregating purchasing across competing operators is careful about what price information it circulates and to whom, and that caution — properly applied to disclosure — tends to be applied to analysis as well. It is worth separating: measuring elasticity across an aggregated book is not the same act as sharing competitors' prices with each other, and conflating the two has left useful work undone.

Members also frame the relationship as savings, not intelligence. They ask what they saved. They have never asked what the substitution curve looks like, so nobody has built one.

And the data is difficult in an unglamorous way. Distributor-specific item codes, inconsistent pack sizes, brand and equivalent items that must be recognised as substitutes for each other — normalising the item master is a serious project that has never had a sponsor because savings reporting can be produced without it.

## What to Build
**A transacted foodservice price index, published weekly.** Built from actual purchases rather than surveyed prices, at the item granularity operators buy in. This is straightforwardly ahead of every published alternative and is the sort of thing that becomes a reference series.

**Estimate substitution empirically.** A price move on one item followed by a switch to another, repeated across thousands of operators and thousands of price changes, is the cleanest available basis for cross-price elasticity in foodservice. It answers what a manufacturer loses when it takes a price increase — a question worth a great deal to both sides of the negotiating table.

**Detect shortages as change points.** Fill rate and forced-substitution series break before a shortage is public. Watching them for change points turns a reactive scramble into a two-week warning for members.

**Forecast the basket at operator level.** Members plan menus and budgets against next year's food cost, using last year's plus a guess. The corpus supports a real forecast per operator segment, which is the single most requested thing members cannot get.

**Measure whether the negotiation worked.** Savings are reported against a constructed baseline. Whether a negotiated agreement changed realised prices is a causal question, answerable by comparing what happened to items and operators inside the agreement against comparable ones outside it — and it is the question the members are actually paying to have answered.

**Sell the intelligence upward.** Manufacturers want to know how foodservice buyers respond to price and where their share is moving. The GPO knows, holds it, and has never packaged it.

## Target Customer
VP of Category Management or Chief Procurement Officer at a foodservice GPO or contract caterer purchasing arm. The argument is that rebate economics are under permanent pressure from members who can compare programmes on savings percentages, and the transaction corpus is the only asset in the business that cannot be competed away on price.

## Impact If Built
Food cost is the largest controllable line in foodservice and the whole sector plans it from published statistics that are late, coarse and drawn from the wrong market. The organisation holding a real-time transacted record of what foodservice actually pays produces a quarterly savings deck.
