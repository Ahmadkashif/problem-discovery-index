# The Order Desk With Six Inboxes

**Industry:** [[consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Worker Life Changing
**One-liner:** The customer service rep who keys every order gets back the evenings of show season and stops being blamed for other people's item numbers.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #worker-facing #automation #workflow-orchestration

## The Problem
A customer service rep at a gift, toy or outdoor wholesaler works orders from six places at once. There are EDI purchase orders that failed validation on a dead item number or an old price, and Faire orders. There are orders written in rep apps such as RepSpark or Pepperi, and paper order forms from the Atlanta and Las Vegas markets, scanned in batches. Independent stores email purchase orders in their own item codes, and the rest come by phone. Each one has to be keyed into the ERP, checked against case packs and minimums, priced on the store's tier, given a ship window ("ship by 15 October for holiday") and released past a credit hold. After a big market the paper backlog can run to a couple of thousand orders (estimate), and it is worked down at night and on weekends.

## Why It Matters to the Worker
The rep is judged on errors, not volume. A wrong case pack or a missed ship window shows up as a return, a deduction or an angry store owner, and it lands on her desk even when the rep group wrote the order wrong. The knowledge that makes her good is all in memory: which store means which item by an old catalogue number, which buyer always wants the holiday order split. None of it is written down, so she cannot take a week off in show season.

## What a Solution Looks Like
One queue for every channel. An intake assistant reads each order, wherever it came from, and drafts ERP lines. It matches the store's own codes and old catalogue numbers to current SKUs from the company's history, applies case packs, minimums and price tiers, proposes the ship window and flags only the lines it is unsure of. The rep reviews and releases, and every correction teaches the matcher. The general version of this intake work is profiled at [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]. The consumer goods version adds show order forms, Faire, seasonal ship windows and store-specific price tiers.

## Impact If Solved
If ~70% of lines release without retyping (estimate), a rep keying ~300 lines a day gets back ~3 hours a day (estimate), and a two-week post-show backlog clears in days instead of weekends.
