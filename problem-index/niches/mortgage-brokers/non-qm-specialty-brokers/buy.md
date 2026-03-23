# Bank Statement Income Calculation Automation

**Niche:** [[niches/mortgage-brokers/non-qm-specialty-brokers/profile|Non-QM & Specialty Lending Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** OCR and document extraction tools can read bank statements — but they can't calculate qualifying income using the lender-specific methodologies (12-month vs. 24-month, gross deposits vs. net after exclusions, expense factor vs. actual P&L) that differ across every non-QM lender.
**Tags:** #ocr #llm #nlp #automation #revenue-impact

## The Problem
Bank statement lending requires calculating the borrower's qualifying income from 12-24 months of personal or business bank statements. The calculation methodology differs by lender: Lender A uses average monthly deposits minus a 50% expense factor; Lender B uses average monthly deposits minus actual verified business expenses; Lender C excludes transfers between accounts, round-number deposits (potentially loan proceeds), and deposits over 50% of the monthly average (outliers). A loan processor manually reviews every page of 12-24 bank statements, categorizing each deposit, applying the lender's specific exclusion rules, and computing qualifying income. This takes 4-8 hours per file and is the most error-prone step in non-QM processing.

## What Already Exists
Document OCR platforms (Blend, Ocrolus, SimpleNexus) can extract transaction data from bank statement PDFs — converting pages into structured transaction records. Income verification platforms (Truework, The Work Number) verify W-2 employment income but don't handle bank statement income. Accounting tools (QuickBooks, Xero) categorize business transactions but aren't integrated into mortgage workflows.

## The Customization Gap
The gap is between raw OCR extraction (transactions as structured data) and lender-specific income calculation (qualifying income as a dollar amount). The tool needs to: (1) apply lender-specific deposit classification rules (which deposits to include, which to exclude, how to handle transfers); (2) compute qualifying income using the specific lender's methodology (gross deposits with expense factor, net deposits after exclusions, or P&L-based); (3) flag questionable deposits for manual review (large round-number deposits, unusual spikes, account-to-account transfers); (4) produce a bank statement analysis summary formatted for lender submission with clear documentation of the calculation methodology applied.

## Target Customer
Loan processors and senior loan officers at non-QM-focused brokerages processing 5+ bank statement loans per month who currently spend 4-8 hours per file on manual bank statement analysis.

## Impact If Solved
Reduces bank statement income calculation from 4-8 hours to 30-60 minutes per file. Eliminates calculation errors that cause 10-15% of bank statement loan submissions to be returned for recalculation. Enables processors to handle 3-4x the non-QM file volume without additional hiring.
