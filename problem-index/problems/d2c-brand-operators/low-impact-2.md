# Inventory Buying Under Demand Uncertainty

**Industry:** [[d2c-brand-operators|D2C Brand Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Demand planning software is a mature enterprise category and the direct-to-consumer brand buying six months of stock is doing it in a spreadsheet against a forecast that is last year plus a growth assumption.
**Tags:** #time-series-forecasting #gradient-boosting #confidence-intervals #optimization-fundamentals #evaluation-metrics #exponential-smoothing #revenue-impact

## The Problem
A brand commits cash to inventory months ahead of selling it. Manufacturing lead times, shipping and customs mean an order placed now arrives for a season the brand is forecasting rather than observing.

Both errors are expensive and asymmetric in ways brands frequently misjudge. A stockout on a strong seller loses margin at full price and — more damagingly — loses the customers who came to buy it. Excess inventory ties up cash the brand needs, occupies warehouse space, and eventually gets marked down, which destroys margin and trains customers to wait for discounts.

The forecast underlying the commitment is usually last year's sales adjusted for planned growth, split by an intuition about size and colour distribution. For a brand with a short history there is no last year, and for a brand growing quickly the historical base is not representative.

Marketing makes it circular. Demand depends on how much is spent acquiring it, which depends on cash, which depends on how much is tied up in inventory. Most brands plan the two separately, which is how a company ends up with stock it cannot afford to advertise.

## What Already Exists
Enterprise demand planning (Blue Yonder, o9, Kinaxis) is mature and priced for enterprises. Inventory planning tools for smaller brands (Inventory Planner, Cogsy, Prediko) exist and are improving. Shopify reports sell-through and stock levels. Three-party logistics providers offer visibility. Forecasting libraries are open and capable. Purchase order and supplier management tools are available.

## The Customisation Gap
Available forecasting tools extrapolate history and stop there. The direct-to-consumer demand curve is driven by marketing spend, which is a controllable input the forecast does not include — so the tool predicts demand as though spend were fixed, when it is the brand's main lever.

Attribute-level forecasting is the second gap. New products have no history, which is precisely when the buying decision is riskiest, and forecasting by product attributes — category, price point, colour family, comparable prior launches — is how a merchandiser reasons and is not what the tools do.

Size and colour distribution is where excess actually accumulates. Aggregate demand can be right while the split is wrong, leaving unsellable sizes at the end of a season, and this is treated as a fixed ratio rather than as something to forecast.

The joint decision is the fourth and largest gap. Inventory and marketing spend are the same working capital allocation problem, and no tool models them together, so brands optimise each against an assumption about the other.

## Impact If Solved
Inventory is where a growing brand's cash goes and where its margin is lost, and the commitment is made months ahead on a spreadsheet forecast that ignores the brand's own main demand lever. Attribute-level forecasting with marketing spend as an input, planned jointly with the acquisition budget, addresses the single most common way these companies run out of money.
