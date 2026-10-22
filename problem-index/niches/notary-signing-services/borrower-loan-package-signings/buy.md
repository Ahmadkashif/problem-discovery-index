# Document AI Tuned to Wet-Ink Loan Packages

**Niche:** [[niches/notary-signing-services/borrower-loan-package-signings/profile|Borrower Loan Package Signings]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic document AI finds signature boxes; it does not know which of ~120 pages this lender needs initialled by the non-borrowing spouse.
**Tags:** #object-detection #cnns #transformers #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to return a fully executed, error-free loan package before the lender's funding cutoff, and whoever has the lowest redraw rate per hundred signings takes the title company's order flow.

## The Problem
At the end of a signing the agent flips through the package looking for blanks. Under time pressure and kitchen lighting, a missed initial or an undated rider slips through and costs a redraw.

## What Already Exists
Azure Document Intelligence, Google Document AI and AWS Textract detect signatures, checkboxes and dates on scanned forms; closing platforms enforce completion on electronic pages.

## The Customization Gap
The adaptation needs page alignment from phone photos to the unsigned package PDF; per-lender and per-title-company requirement lists (who signs, initials or dates each page); rider and addendum conventions; date logic tied to rescission on refinances; notarial certificate checks under the notary's state (venue, name as signed, commission expiry, legible seal); and on-device processing, because the package holds the borrower's financial data.

## Target Customer
Signing services and title companies; signing agents through a phone app.

## Impact If Solved
Errors are caught while the borrower is still at the table, which is the only moment fixing them is cheap.
