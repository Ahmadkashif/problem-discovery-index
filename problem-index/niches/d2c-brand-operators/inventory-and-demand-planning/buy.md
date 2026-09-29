# Demand Forecasting and Inventory Optimisation

**Niche:** [[niches/d2c-brand-operators/inventory-and-demand-planning/profile|Inventory & Demand Planning]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Inventory theory and demand forecasting are among the most developed areas of operations research, with open implementations, and this category uses a spreadsheet.
**Tags:** #time-series-forecasting #exponential-smoothing #probability-distributions #convex-optimization #confidence-intervals #gradient-boosting #evaluation-metrics #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to tell a brand how much to buy six months ahead without a stockout or a markdown — and whoever does that takes the account, because that decision commits more cash than any other the brand makes and is currently made in a spreadsheet.

## The Problem
How much to order, when, and how much safety stock to hold is one of the oldest and best-solved problems in operations research. Newsvendor models handle single-season buys with asymmetric costs. Hierarchical forecasting reconciles product, category and total. Intermittent demand methods handle slow movers. Open forecasting libraries make the statistics free. None of it is difficult to access and almost none of it is used by brands whose entire working capital rides on the answer.

## What Already Exists
Time series forecasting with seasonality and trend, in mature open libraries; hierarchical forecasting with reconciliation; intermittent demand methods for slow-moving items; newsvendor and multi-echelon inventory models; safety stock formulas driven by service level targets; and markdown optimisation from retail.

## The Customization Gap
The adaptation is to a brand whose demand is created by its own marketing. It requires: (1) marketing spend and campaign calendar as forecast inputs, since demand here is substantially manufactured rather than exogenous and a forecast that ignores it is forecasting the wrong process — this is the single biggest departure from the retail setting these methods came from; (2) short histories and frequent assortment change, which breaks the long-series assumptions and argues for hierarchical pooling and attribute-based models; (3) new product forecasting as the main case rather than the exception, since these brands launch constantly; (4) returns as a first-class flow, because return rates in apparel and similar categories are high enough to change both the buy and the available inventory materially; and (5) a service level target chosen against the actual cost of a stockout including the wasted acquisition spend, which is a cost retail does not carry and which is large here.

## Target Customer
Brands too small for enterprise planning, the planning software vendors not serving them, and the operations research community for whom marketing-driven demand is an interesting variant.

## Impact If Solved
The methods are free and mature and the money at stake is the brand's entire working capital. Marketing spend as a forecast input is the big departure from retail, since demand here is manufactured rather than observed, and the cost of a stockout includes the acquisition spend that created the demand.
