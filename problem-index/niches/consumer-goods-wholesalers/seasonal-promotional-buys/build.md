# Seasonal Bets Graded Before the Purchase Order

**Niche:** [[niches/consumer-goods-wholesalers/seasonal-promotional-buys/profile|Seasonal & Promotional Buys]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Show the merchant how comparable seasonal items sold through, and what markdown money they drew, while the factory order is still a draft.
**Tags:** #tacit-knowledge-ml #contrastive-learning #gradient-boosting #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to pick and size one-shot seasonal and promotional items that sell through at full price, and whoever leaves the retailer claiming the least markdown money per dollar shipped takes the account.

## The Problem
Seasonal items are chosen and sized by merchants on feel, months ahead. The outcome is one season's sell-through and a markdown claim that arrives the following spring, and nobody joins the two to the original decision.

## Why Nobody Has Built This
The outcome data is spread across retailer portals, remittances and the closeout ledger, and the items have no history of their own. Only comparables can inform the bet, and finding them takes item embeddings that importers have never built.

## What to Build
An item ledger for seasonal buys that grades each past item on sell-through at full price, markdown money claimed and leftover stock. Image-and-attribute embeddings retrieve comparables for a new sample, and a quantile model recommends the buy depth that minimises expected markdown money plus leftover cost.

## Target Customer
Merchants and sales heads at holiday, outdoor and promotional importers.

## Impact If Built
Cutting markdown money from ~6% to ~4.5% of seasonal sales (estimate) on a $40M seasonal business saves ~$600K a year (estimate).
