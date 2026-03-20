# Supplier Invoice Reconciliation Against PO and Receiving

**Industry:** [[food-distributors|Food Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic AP automation chokes on catch-weight pricing, grade adjustments, and promotional allowances — the three things that make every food distribution invoice uniquely complex.
**Tags:** #bert #transformers #word-embeddings #transfer-learning #attention-mechanisms #feature-engineering #evaluation-metrics #automation #data-integration

## The Problem
A mid-size food distributor processes 2,000-5,000 supplier invoices per week, and 30-50% of them have line-item discrepancies that require manual resolution. The root cause is industry-specific pricing complexity: catch-weight items (meat, cheese, produce) are ordered by the case but invoiced by the pound at receiving weight, so every line has an expected variance that must be compared against tolerance thresholds. Grade adjustments occur when produce arrives as US #2 instead of US #1, triggering a price reduction that the supplier may or may not have applied. Promotional allowances (off-invoice deductions, bill-backs, volume rebates) create credits that span multiple invoices and must be tracked against promotional calendars. AP clerks spend 15-25 hours per week manually matching invoices to POs and receiving records, chasing $50K-$200K in weekly discrepancies.

## What Already Exists
AP automation platforms like Coupa, AvidXchange, and BILL (formerly Bill.com) handle standard three-way matching (PO, receipt, invoice) well for fixed-price goods. They can extract invoice data via OCR, match against PO numbers, and flag quantity or price mismatches. Some offer food-industry templates, but none natively handle catch-weight tolerance logic, grade-based price adjustments, or multi-invoice promotional allowance tracking.

## The Customisation Gap
The system needs three food-specific capabilities. First, catch-weight tolerance matching: for each SKU, maintain a per-supplier weight-per-case distribution and auto-approve invoices within 2 standard deviations while flagging outliers. Second, grade-adjustment detection: when receiving records note a grade downgrade, automatically calculate the contractual price reduction and verify the invoice reflects it — or generate a credit memo if it does not. Third, promotional allowance ledger: ingest promotional calendars from suppliers, track which invoices fall within promotional periods, and automatically apply or verify off-invoice deductions, bill-backs, and end-of-quarter volume rebates across invoice batches.

## Impact If Solved
AP clerk time on invoice reconciliation drops from 15-25 hours/week to 3-5 hours/week (80% reduction). Missed credits and overpayments — typically $200K-$500K annually for a $350M distributor — are captured automatically. Supplier payment cycle accelerates by 3-5 days, unlocking early-payment discounts worth $100K-$300K/year.
