# Forecasting a Perishable Back Catalogue

**Niche:** [[niches/audio-adtech-networks/inventory-and-yield/profile|Inventory & Yield]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dynamic insertion turned a fixed slot into a perishable, back-catalogue-heavy inventory, and most publishers forecast it with a spreadsheet trend on last month's downloads.
**Tags:** #time-series-forecasting #survival-analysis #convex-optimization #confidence-intervals #evaluation-metrics #revenue-impact #recurrent-forecasting #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to forecast and price a perishable back-catalogue-heavy inventory that dynamic insertion created — and whoever does that properly stops publishers selling next month on last month's downloads.

## The Problem
A publisher must tell an advertiser how many impressions they can deliver next month. The answer depends on how many new episodes will publish, how each will accumulate downloads over its first weeks, how much the back catalogue will produce, how many slots each episode carries, seasonality, and what is already sold. Most publishers estimate it by taking last month's total and adjusting. They oversell and under-deliver, or undersell and leave inventory unmonetised, and both outcomes are absorbed as the nature of the business rather than as a forecasting failure.

## Why Nobody Has Built This
The inventory model changed when dynamic insertion arrived and the forecasting practice did not follow, because the spreadsheet kept producing a number that was approximately right on a monthly total — an approximation that survives at the aggregate hides being badly wrong at the level where commitments are made. Publishers are frequently small with no quantitative capability. Ad servers report what happened rather than what will. And the cost appears as make-goods and unsold inventory rather than as a forecast error.

## What to Build
Forecast the inventory properly. Model episode download accumulation as a curve rather than a total, since a new episode arrives over weeks and the shape is stable per show, which makes a genuine forecast possible where a monthly trend cannot. Model the back catalogue's decay separately, because it produces a long steady tail that behaves entirely differently from new releases and summing them discards the structure. Forecast at slot level with availability, so a seller knows what can be committed rather than what was delivered last month. Attach uncertainty, since an interval lets a seller commit confidently to a lower number rather than optimistically to a higher one and then apologise. Differentiate value by expected exposure, connecting to that niche, so well-positioned slots are priced above poorly positioned ones. Optimise the allocation between direct, programmatic and host-read demand, which is a real yield problem with real money in it and is currently handled by sequence rather than by optimisation. Detect and prevent oversell before the commitment rather than discovering it at delivery. Handle the seasonality, which in audio is pronounced and predictable. Give small publishers a usable version, since most of the category is small and anything requiring analytics capability will not reach them. And report forecast accuracy, because a seller who knows their own error can commit closer to the line and earn more.

## Target Customer
Podcast and audio publishers, network sales operations, and the hosting and monetisation platforms serving them.

## Impact If Built
The inventory model changed and the forecasting practice did not, because a monthly trend stays approximately right at the aggregate while being badly wrong where commitments are made. Modelling episode accumulation curves and back-catalogue decay separately makes a genuine slot-level forecast possible.
