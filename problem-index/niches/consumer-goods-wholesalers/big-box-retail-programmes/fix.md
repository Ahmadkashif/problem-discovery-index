# Direct-Import and Domestic Terms Tangled in One Item Master

**Niche:** [[niches/consumer-goods-wholesalers/big-box-retail-programmes/profile|Big-Box Retail Programmes]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Fix (Pain Point)
**One-liner:** The same item ships domestic to one retailer and direct-import to another, but the item master holds one cost and one margin, so the importer cannot tell which terms to offer at the line review.
**Tags:** #feature-engineering #monte-carlo-methods #data-integration #revenue-impact #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep its items through each retailer's annual line review. But the review is won on two different measures with different winners: everyday items on automatic replenishment are kept on how few of the retailer's ordered units the importer ships short, and one-shot seasonal and promotional buys on how little markdown money the retailer claims back. Decomposed into contested sub-niches below.

## The Problem
On domestic terms the importer pays freight and duty, holds the stock and absorbs fines. On direct-import terms the retailer takes title at the Asian port and pays the duty itself. The tariff changes of 2025–2026 moved those two cost stacks in different directions, and retailers shifted items between them. The importer's ERP still carries one standard cost per SKU.

## Why It's Still Broken
Direct-import orders often run outside the ERP, through the factory and a forwarder, and the cost of holding domestic stock (warehousing, fines, deductions) is never allocated back to items.

## What a Fix Looks Like
A per-item, per-terms margin model: factory cost, freight, duty borne by whom, US warehousing, expected fines and deductions on domestic terms, and agent commission on direct import. It is recomputed with each tariff change and shown side by side for every item up for review.

## Who Feels the Pain
VPs of Sales choosing what to offer, finance teams reconciling programme profit, and merchants asked to quote both ways.

## Impact If Fixed
Choosing the better terms on the ~20% of items where the choice is close (estimate) is worth ~0.5–1 point of programme margin, ~$0.5–1M a year on $100M (estimate).
