# Slip Forecasts From Every Date a Manufacturer Ever Promised

**Niche:** [[niches/electrical-distributors/gear-lead-time-release-management/profile|Gear Lead Times & Release Management]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distributors receive thousands of promised ship dates a year and overwrite each one when it changes, throwing away the data that would predict the next slip.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get switchgear, transformers and other long-lead gear to the jobsite on the date the contractor's schedule needs, and whoever warns the contractor of a slip earliest takes the account.

## The Problem
When an acknowledgement revises a ship date, the ERP stores the new date and loses the old one. A distributor therefore cannot say how reliable each manufacturer, plant or product family has been, or which open lines are most likely to slip next, and its project managers learn about slips when the contractor does.

## Why Nobody Has Built This
Date history lives in PDFs and portals, not in a database, and each manufacturer formats it differently. Manufacturers have no incentive to publish their reliability, and distributors never kept the revisions.

## What to Build
A capture layer that reads every acknowledgement, revision and ship notice and keeps the full date history per line, then a time-to-event model of slips by manufacturer, plant, product family, configuration, order size and season. Each open line gets a slip probability and expected delay, ranked by the contractor milestone it threatens, with an explanation the project manager can pass on.

## Target Customer
Project management leaders at distributors with large gear books, especially in data center, healthcare and industrial construction.

## Impact If Built
Slips are flagged ~2–4 weeks earlier than today (estimate), the distributor learns which manufacturers to plan buffer around, and contractors get warnings in time to resequence crews instead of standing them down.
