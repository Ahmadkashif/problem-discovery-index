# The Rate Sheet Built by Hand Every Morning

**Niche:** [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/profile|Secondary Marketing & Pipeline Risk]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** At many lenders the morning rate sheet is still assembled in a spreadsheet from investor prices and margin grids, then re-keyed or uploaded, and a single bad cell can lock loans below cost.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to forecast which locked loans will fund and to sell each one at its best execution, and whoever earns the most margin per locked loan net of hedge cost and lock concessions takes the account.

## The Problem
Before the market opens, a secondary analyst pulls investor price sheets and MBS prices, applies the lender's margins, adjustments and overlays, and produces rate sheets by product. Reprices during the day repeat the exercise under time pressure. Errors are found when loan officers notice an unusually good price, after some have locked.

## Why It's Still Broken
Pricing engines can load investor prices, but many lenders keep a spreadsheet in the middle because their margin logic (by channel, branch, state and product) grew faster than the engine configuration, and because the analyst trusts the spreadsheet they built. Nothing compares today's sheet with yesterday's and with the market move to flag prices that changed when they should not have.

## What a Fix Looks Like
Move the margin logic into the engine or a governed rules table, generate sheets automatically from the morning's inputs, and run an automated check before release: every price change explained by the market move and any margin change, outliers blocked for review. Reprices drafted automatically when MBS prices cross the tolerance.

## Who Feels the Pain
Lock desk analysts who build and defend the sheet; loan officers whose quotes change mid-morning; capital markets heads who absorb mispriced locks.

## Impact If Fixed
One to two hours a morning returned to the desk (estimate), and the most expensive class of operational error, a mispriced sheet live in the market, caught before release instead of after locks.
