# Lot Pricing From the Manifest

**Niche:** [[niches/consumer-goods-wholesalers/closeout-excess-inventory/profile|Closeout & Excess-Inventory Wholesale]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Price a closeout lot in minutes from its manifest by matching each line to what similar goods actually resold for, in which outlet, and how fast.
**Tags:** #tacit-knowledge-ml #gradient-boosting #k-nearest-neighbors #large-language-models #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a closeout lot from a manifest, a few photos and a deadline, and whoever earns the highest realised margin on the lots it wins takes the account.

## The Problem
A buyer gets a manifest of 400 SKUs and a day to bid. Pricing every line by hand is impossible, so she prices the top lines and guesses the rest, which is where the margin is lost or made.

## Why Nobody Has Built This
Closeout houses keep their resale results in ERPs that were never joined to the original manifests, and the manifests themselves are messy text in every seller's format.

## What to Build
An LLM reads and normalises each manifest line (brand, item, category, condition, pack). A model trained on the house's own past lots predicts resale price, outlet and weeks to sell for each line, discounting by the seller's history of manifest accuracy. It totals a bid range with risk bands and records the buyer's final bid for grading.

## Target Customer
Owners and buyers at closeout wholesalers handling hundreds of lots a year.

## Impact If Built
Improving realised margin by ~2 points (estimate) on ~$30M of annual lot purchases is worth ~$600K a year (estimate), and lets the house bid on lots it currently passes for lack of time.
