# Valid Deductions Absorbed Because Nobody Re-Bills Them

**Niche:** [[niches/consumer-goods-wholesalers/two-sided-deductions/profile|Retailer Deductions on Both Sides]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Fix (Pain Point)
**One-liner:** A shortage packed at the factory or a defective allowance the brand agreed to fund is accepted from the retailer and then never charged to the supplier.
**Tags:** #large-language-models #bert #workflow-orchestration #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn every retailer deduction on a wholesaler's invoices into either a recovered credit from the retailer or a debit to the supplier who caused it, and whoever recovers the most deduction dollars from either side takes the account.

## The Problem
The AR team's job ends when a deduction is resolved with the retailer. Purchasing owns supplier relationships and never sees the accepted claims, so supplier-caused costs stay on the wholesaler's books.

## Why It's Still Broken
Two departments, two systems and no link from a retailer's claim to the supplier's purchase order and agreement.

## What a Fix Looks Like
For every accepted deduction, map the affected SKU lines to their suppliers, check each supplier agreement for a pass-back clause, and queue a draft debit memo with the retailer's backup for purchasing to approve or waive with a reason.

## Who Feels the Pain
Controllers, purchasing managers negotiating supplier terms blind, and CFOs reporting margin.

## Impact If Fixed
If ~20% of accepted deductions are supplier-caused (estimate), queuing them for re-bill surfaces ~$1M a year at a wholesaler with $6M of deductions.
