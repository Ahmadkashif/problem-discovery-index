# Deductions on Both Sides of the Wholesaler

**Industry:** [[consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Deduction platforms recover invalid retailer claims for brands that make what they sell; a wholesaler also has to re-bill the valid ones to the hundred suppliers that caused them, and no tool runs that second ledger.
**Tags:** #large-language-models #gradient-boosting #bert #feature-engineering #automation #revenue-impact #data-integration

## The Problem
A wholesaler selling to Walmart, Target, Amazon, home centres and regional chains is paid short on almost every remittance. The EDI 820 lists deduction codes, 812 adjustments arrive separately, and some claims exist only in a retailer portal. An accounts receivable analyst researches each one: finds the purchase order (EDI 850 or a PDF), the ship notice (856), the invoice (810), proof of delivery, the allowance in the vendor agreement and the promotion email that set it. D&H Distributing told iNymbus it handles thousands a month. Claims under a write-off threshold are never opened, and claims nobody reaches age past the retailer's window, which runs from days to months depending on the charge (search summary).

The second ledger is what makes the wholesaler different. It bought the goods from dozens or hundreds of suppliers whose own agreements say which charges pass back: a defective allowance, a shortage packed at origin, a carton mislabelled by the factory, a markdown the brand agreed to fund. Most of those valid deductions are absorbed because nobody connects the retailer's claim to the supplier, the SKU lines and the clause.

## What Already Exists
CPG deduction platforms: Glimpse (200+ customers by its own count), Confido (250+ brands), SPS Revenue Recovery (built from SupplyPike and Carbon6), HighRadius's deductions module, iNymbus and Vividly. They pull portal claims, match documents, file disputes and post the cash, and they are good at it for brands. The maker-side version of this work is profiled at [[niches/consumer-products-makers/deduction-chargeback-recovery/profile|Deduction & Chargeback Recovery]].

## The Customisation Gap
A wholesaler needs the pass-back ledger built in. Each retailer deduction has to be split by SKU line to the supplier of each line, matched to that supplier's agreement clause, turned into a supplier debit memo with the retailer's evidence attached, and tracked until the supplier accepts or offsets it. It also needs wholesaler cases the brand tools rarely see: store-direct and drop-ship shipments, price protection and markdown money shared with brands, and the same SKU bought from two suppliers. A two-week MVP fits here. It parses X12 812 and 820 files into a deduction queue, classifies reason codes, reads 850s or PDF purchase orders for agreed prices and allowances, matches 856 and 810 records and proof of delivery, and drafts either the retailer dispute packet or the supplier debit memo.

## Impact If Solved
For a wholesaler with ~$150M of big-box sales and deductions at ~4% (~$6M a year, estimate), recovering half of an estimated 10% invalid share and re-billing half of an estimated 20% supplier-caused share returns ~$900K a year (estimate) without adding analysts.
