# The Supplier Debit Memo Drafted From the Retailer's Claim

**Niche:** [[niches/consumer-goods-wholesalers/two-sided-deductions/profile|Retailer Deductions on Both Sides]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Parse every 812 and 820, read the purchase order, decide dispute, re-bill or accept, and draft the retailer dispute packet or the supplier debit memo with the evidence attached.
**Tags:** #large-language-models #bert #gradient-boosting #feature-engineering #automation #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn every retailer deduction on a wholesaler's invoices into either a recovered credit from the retailer or a debit to the supplier who caused it, and whoever recovers the most deduction dollars from either side takes the account.

## The Problem
An AR analyst can research perhaps thirty deductions a day (estimate). The wholesaler gets thousands a month, so most small claims are written off unread, and the supplier side is almost never worked.

## Why Nobody Has Built This
Brand platforms had no reason to build supplier pass-back. Wholesalers' purchase orders, from retailers and to suppliers, arrive as EDI and PDFs in every format, which until LLMs needed a person to read.

## What to Build
A two-week MVP first. Ingest X12 820 remittances and 812 adjustments into a deduction queue. Classify reason codes, and pull 850s or PDF purchase orders for agreed prices and allowances. Match 856 ship notices, 810 invoices and proof of delivery, and draft the retailer dispute packet or the supplier debit memo for one-click approval. Then add a recovery model trained on dispute outcomes, supplier-agreement clause matching, and portal filing.

## Target Customer
Controllers at wholesalers with three or more big-box accounts and dozens of suppliers.

## Impact If Built
On ~$6M a year of deductions (estimate), working every claim instead of the largest third could add ~$500K–$900K a year of recoveries and re-bills (estimate).
