# The Owner Who Finds Out at the Annual Inventory

**Niche:** [[niches/pawnshops/independent-single-store-pawnbrokers/profile|Independent Single-Store Pawnbrokers]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Fix (Pain Point)
**One-liner:** An independent's lending mistakes accumulate quietly in aged stock and only show as a number when the year-end count and the accountant's write-down arrive.
**Tags:** #descriptive-statistics #change-point-detection #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give a one-store owner chain-grade loss control — which clerks, categories and loan sizes lose money at forfeit — from the POS data the owner already has, and whoever delivers it without the owner needing an analyst takes the account.

## The Problem
Forfeited items enter stock at the loan amount. If they were over-lent, the loss is realised only when they sell below cost or are written down. A year of over-lending on one category shows up as a single inventory adjustment the owner cannot trace back.

## Why It's Still Broken
Nothing between the ticket and the year-end count measures loss on forfeit as it happens; the POS reports stock value at cost, which hides the problem until it is sold.

## What a Fix Looks Like
A weekly alert computed from the ticket history: categories where recent forfeits are selling below their loan cost, or where shelf time has jumped, with the clerks and loan-to-value bands behind them.

## Who Feels the Pain
Owners facing write-downs; clerks who never learn which loans went wrong; lenders to the shop who see the hit in the accounts.

## Impact If Fixed
Problems surface within weeks rather than a year, when a conversation with a clerk or a tighter lending guide still prevents most of the loss.
