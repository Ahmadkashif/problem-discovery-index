# Six Months of Cash on Last Year Plus a Guess

**Niche:** [[niches/d2c-brand-operators/inventory-and-demand-planning/profile|Inventory & Demand Planning]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Demand planning software is a mature enterprise category and the direct-to-consumer brand buying six months of stock is doing it in a spreadsheet against a forecast that is last year plus a growth assumption.
**Tags:** #time-series-forecasting #probability-distributions #confidence-intervals #convex-optimization #revenue-impact #gradient-boosting #evaluation-metrics #exponential-smoothing
**Contested on:** Every serious competitor in this niche is fighting to tell a brand how much to buy six months ahead without a stockout or a markdown — and whoever does that takes the account, because that decision commits more cash than any other the brand makes and is currently made in a spreadsheet.

## The Problem
A brand commits an order for the spring season in October. The quantities come from last spring's sales, increased by the growth rate the team hopes for, adjusted by a merchandiser's judgement about which colours will do well. Three products sell out in five weeks and the demand goes to competitors while the marketing spend that created it is wasted. Four sit until the end-of-season sale and clear at a loss that consumes most of the profit from the three that sold. The brand's own data contained the seasonality, the trend, the size curve, the return rate and the marketing calendar that drove last year's numbers, and none of it was used.

## Why Nobody Has Built This
Enterprise demand planning software is priced and scoped for companies far larger, so these brands are between a spreadsheet and a system they cannot afford or implement. The planner is frequently a merchandiser with no statistical background and no support. The consequences are absorbed as the cost of doing business in fashion or seasonal categories. And the cash impact is visible in the accounts long after the decision that caused it.

## What to Build
Forecast properly and optimise the buy. Produce a statistical forecast per product with seasonality, trend and promotional effects from the brand's own history, which is ordinary time series work and is better than an eyeballed adjustment every time. Forecast a distribution rather than a number, since the buy decision depends on the uncertainty and a point forecast cannot inform a safety stock decision at all — this is the modelling change that matters most. Optimise the buy against the actual costs of being wrong in each direction, since a stockout on a high-margin product and an overbuy on a low-margin one are not symmetric and the classic newsvendor arithmetic settles it immediately once the costs are stated. Take the marketing plan as an input, which the fix note develops. Handle new products with attribute-based forecasting from comparable launches, since new products have no history and are the largest source of error. Account for returns in available inventory, since return rates in several categories are high enough to change the buy materially and are frequently ignored. Model the size and variant curve, since aggregate quantity is right and the split is where stockouts happen. Recommend in-season reorders and markdown timing, because the season is not one decision and treating it as one forgoes most of the recovery. And report forecast accuracy so it improves.

## Target Customer
Merchandising and finance functions at brands too small for enterprise planning software, and the vendors who have not built for them.

## Impact If Built
The inputs a forecast needs are all in the brand's own data and none are used. Forecasting a distribution rather than a number is what makes the buy decision answerable, and the newsvendor arithmetic settles it once the asymmetric costs are stated.
