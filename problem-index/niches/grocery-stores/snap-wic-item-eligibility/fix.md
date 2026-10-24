# The Shelf Tag and the Register Disagree

**Niche:** [[niches/grocery-stores/snap-wic-item-eligibility/profile|SNAP & WIC Item-Eligibility Compliance]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Fix (Pain Point)
**One-liner:** A WIC shopper picks an item tagged "WIC approved" and the register rejects it, because the shelf-tag file and the state's product list were updated on different days.
**Tags:** #data-integration #evaluation-metrics #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep every register's SNAP and WIC eligibility flags right across states, waivers and court orders, and whoever has the fewest wrongly blocked or wrongly allowed benefit scans per million takes the account.

## The Problem
WIC shoppers rely on shelf tags to find approved brands and sizes. The register checks the state's product list, which changes as states add and drop items. When the tag file lags the list, the shopper is turned away at checkout with a child and a line behind them, and the cashier has no way to fix it.

## Why It's Still Broken
Shelf tags are printed from the chain's item file in weekly batches, while the WIC list arrives on the state's schedule. Nobody compares the two, and register rejections are not reported back.

## What a Fix Looks Like
Compare each new WIC list against the shelf-tag file daily. Print correction tags for the stores affected, and log every WIC rejection at the register with the item, so repeat rejections trigger a check. The same comparison works for SNAP waiver flags.

## Who Feels the Pain
WIC shoppers turned away at checkout; cashiers who absorb the frustration; and store managers who field complaints to the state agency.

## Impact If Fixed
If a 100-store chain sees ~20 wrong-tag WIC rejections per store per month (estimate), a daily comparison removes most of ~24,000 failed transactions a year.
