# Open-to-Buy Rebuilt Every Season in a Spreadsheet

**Niche:** [[niches/retail-pos-platforms/specialty-retail-merchandising/profile|Specialty Retail Merchandising]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Open-to-buy is arithmetic over numbers the POS already holds, it determines what a retailer can afford to order, and it is maintained in a spreadsheet the owner rebuilds every season and stops updating by March.
**Tags:** #descriptive-statistics #time-series-forecasting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in specialty retail software is fighting to tell an independent retailer what to mark down, when, and by how much — and whoever moves end-of-season sell-through and margin most takes the account.

## The Problem
An owner sits down before market week to work out what she can spend. Planned sales, planned markdowns, opening inventory, goods already on order, target closing inventory — the calculation is simple and the numbers are all in the POS. She exports them, rebuilds last season's spreadsheet with new dates, gets it roughly right, and then does not update it as the season progresses, because updating means re-exporting. By March the plan is a document rather than a control, and she orders against a feeling about how the season has gone. Overbuying is the most common way an independent retailer runs out of cash, and this is how it happens.

## Why It's Still Broken
Open-to-buy has been treated as an accounting report rather than as a live control, and most POS products either omit it or produce a static version. Maintaining it continuously means the system has to hold planned sales and planned markdowns, which are forecasts rather than records, and vendors have avoided asking merchants to enter plans. The answer is to generate the plan rather than ask for it, which requires the forecasting this niche is about, so the fix and the build note reinforce each other.

## What a Fix Looks Like
Maintain it continuously and generate the plan. Planned sales come from the forecast rather than from the owner's estimate, with the owner able to override; planned markdowns come from the markdown model; on-order comes from purchase orders already in the system; inventory is live. The open-to-buy position updates daily and is visible as one number — what can I still spend this month, this season, in this category — with the components behind it. Alert when the position deteriorates rather than waiting for the owner to look, because the failure mode is not knowing until the cash is gone. At market, on a phone, the buyer should be able to see remaining open-to-buy by category while standing in front of a vendor, which is the moment the number actually governs a decision and the moment it is currently unavailable.

## Who Feels the Pain
Owners overbuying into a cash crunch they did not see coming; buyers making commitments at market with no live budget; and the business itself, for which inventory is usually the largest use of cash.

## Impact If Fixed
A live open-to-buy position is the most direct cash control an independent retailer has and is currently exercised through a spreadsheet abandoned mid-season. Every input already exists in the platform, which makes this a reporting and workflow change rather than a modelling project — and having it available on a phone at market is where it changes an actual decision.
