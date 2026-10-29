# Item Margin Net of Every Retailer Claim

**Niche:** [[niches/consumer-goods-wholesalers/big-box-retail-programmes/profile|Big-Box Retail Programmes]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An importer walks into a line review knowing each item's gross margin and not what the retailer took back from it in deductions, fines, markdown money and returns.
**Tags:** #feature-engineering #large-language-models #gradient-boosting #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep its items through each retailer's annual line review. But the review is won on two different measures with different winners: everyday items on automatic replenishment are kept on how few of the retailer's ordered units the importer ships short, and one-shot seasonal and promotional buys on how little markdown money the retailer claims back. Decomposed into contested sub-niches below.

## The Problem
Gross margin per item comes from the ERP. Claims arrive on remittances coded by reason, not by item, and markdown money, defective allowances, fines and co-op are settled weeks or months later. At the line review the importer defends items that lose money and drops items that quietly earn.

## Why Nobody Has Built This
Deduction tools stop at recovery and POS tools stop at sell-through. Allocating a lump claim back to items takes reading the claim's backup, which until recently needed a person.

## What to Build
An item ledger per retailer that allocates every claim to SKU lines, using claim backup, POs and invoices, with LLM reading of unstructured backup. It computes net margin per item per retailer per season and ranks items for keep, fix or drop before the review.

## Target Customer
VPs of Sales and finance leads at importers with three or more big-box accounts.

## Impact If Built
If ~10–15% of an importer's big-box SKUs lose money after claims (estimate), dropping or repricing them lifts programme margin by ~1–2 points (estimate), ~$1–2M a year on $100M.
