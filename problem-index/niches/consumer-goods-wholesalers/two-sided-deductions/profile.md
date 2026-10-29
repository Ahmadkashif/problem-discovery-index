# Retailer Deductions on Both Sides

**Parent Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn every retailer deduction on a wholesaler's invoices into either a recovered credit from the retailer or a debit to the supplier who caused it, and whoever recovers the most deduction dollars from either side takes the account.

## Profile
**Market Size:** ~$4B a year of retailer deductions on consumer goods wholesalers' invoices, of which ~$1.2B is invalid or re-billable to suppliers (estimate)
**Share of Parent Industry:** ~1% of receipts (estimate)
**Digital Adoption:** Medium — claims arrive by EDI and portal; research, filing and supplier re-billing are manual
**Target Buyer:** Controller or CFO; the VP of Credit Services at larger distributors
**Automation Potential:** Very High — retrieval, matching, filing and debit memos are rule-bound document work

## What Makes This a Distinct Niche
A maker disputes deductions against the retailer. A wholesaler does that and more. Each claim has a second possible answer: the charge is valid but was caused by the supplier that made or packed the goods, and the wholesaler's own vendor agreement lets it re-bill. Shortages packed at origin, factory labelling errors, defective allowances and brand-funded markdowns all belong there, split by SKU line across many suppliers. D&H Distributing told iNymbus it handles thousands of deductions a month from shipping direct to stores. The maker-side contest is profiled at [[niches/consumer-products-makers/deduction-chargeback-recovery/profile|Deduction & Chargeback Recovery]], and the food distributor's supplier-invoice side (short-ship credits and promotional allowances matched against purchase orders) at [[niches/food-distributors/invoice-reconciliation-automation/profile|Invoice Reconciliation Automation]]. What differs here is the supplier ledger. The X12 812/820 triage plus 850 and PDF purchase-order intake that drafts the dispute packet is a two-week MVP for this niche.

## Current Tools & Gaps
Glimpse (New York; 200+ customers by its own count; hiring a Founding Forward Deployment Engineer on 2026-10-29), Confido (250+ brands), SPS Revenue Recovery, HighRadius, iNymbus and Vividly. Vividly's checked terms make de-identified customer data "Vividly's property", to be used "to improve the Services". The gap: none of them runs the supplier pass-back ledger.

## Problems
- [[niches/consumer-goods-wholesalers/two-sided-deductions/build|🔨 Build: The Supplier Debit Memo Drafted From the Retailer's Claim]]
- [[niches/consumer-goods-wholesalers/two-sided-deductions/buy|🛒 Buy: Brand Deduction Platforms With a Supplier Ledger]]
- [[niches/consumer-goods-wholesalers/two-sided-deductions/fix|🔧 Fix: Valid Deductions Absorbed Because Nobody Re-Bills Them]]
