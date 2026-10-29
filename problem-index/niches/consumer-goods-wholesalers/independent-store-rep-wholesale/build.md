# Reorder Prompts Before the Shelf Is Empty

**Niche:** [[niches/consumer-goods-wholesalers/independent-store-rep-wholesale/profile|Independent-Store Wholesale Through Reps & Trade Shows]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict when each store is running low on the wholesaler's lines from its own order history and send a ready-made reorder to the store or its rep before a competitor's line takes the shelf.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the line an independent store reorders between markets, and whoever earns the most reorders per active store takes the account.

## The Problem
Independent stores rarely send sell-through data. They reorder when the owner notices a gap, and by then the space may have gone to a line the owner saw on Faire.

## Why Nobody Has Built This
Wholesalers have years of store order history but not the analysts to model it, and rep groups own the visit schedule. Store sell-through is not shared.

## What to Build
A time-to-reorder model per store and line, built from order history, season, store type and region, and comparable stores' cadence. It triggers a suggested reorder (items, quantities, minimums met) sent by email, Faire Direct link or the rep's app, and records which prompts converted.

## Target Customer
VPs of Sales at gift, toy and outdoor wholesalers with several thousand active store accounts.

## Impact If Built
Lifting reorders per active store from ~2.5 to ~3 a year (estimate) on 3,000 stores at ~$600 per reorder adds ~$900K of sales a year (estimate).
