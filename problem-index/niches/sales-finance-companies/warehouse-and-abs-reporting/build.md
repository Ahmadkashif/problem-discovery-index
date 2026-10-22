# Tape-to-Contract Evidence for Every Pledged Loan

**Niche:** [[niches/sales-finance-companies/warehouse-and-abs-reporting/profile|Warehouse & ABS Collateral Reporting]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Warehouse lenders advance against a spreadsheet of loans and sample the paper once a year; after Tricolor they want proof for every loan, every month.
**Tags:** #large-language-models #transformers #graph-theory #data-integration #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce borrowing base, servicer and asset-level reports from one reconciled loan-level dataset with evidence that each contract exists and is pledged once, and whoever makes the finance company's numbers verifiable by its banks and investors takes the account.

## The Problem
A borrowing base is a list of loans the finance company says are eligible. Field exams sample a few dozen contracts. Falsified or double-pledged collateral can survive that for years, as the 2025 Tricolor charges allege, and honest lenders now pay for the suspicion in tighter advance rates and heavier diligence.

## Why Nobody Has Built This
Contract images, title records and servicing data live in different systems; matching them loan by loan was too labour-intensive to do monthly; and no one holds a cross-facility view.

## What to Build
Match every tape row to its contract image (extracting amount financed, VIN, borrower and dates), its electronic lien or title record and its payment history; report mismatches as exceptions; and issue a per-pool evidence report the lender can rely on. With participants' consent, add a VIN-and-borrower fingerprint registry that flags collateral pledged to two facilities.

## Target Customer
Treasurers of finance companies seeking better advance rates, and the warehouse banks and private credit funds that lend to them.

## Impact If Built
Collateral that can be proven monthly at loan level, cheaper funding for lenders that adopt it, and a structural defence against the next double-pledging scheme.
