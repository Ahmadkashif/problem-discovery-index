# Loan Document Extraction & Assembly

**Industry:** [[mortgage-brokers|Mortgage Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic OCR can read a paystub — but it can't calculate qualifying income from a self-employed borrower's three years of K-1s, depreciation schedules, and business bank statements the way an underwriter needs it.
**Tags:** #cnn #bert #ocr #named-entity-recognition #nlp #computer-vision #automation

## The Problem
Loan processors manually extract data from paystubs, W-2s, tax returns (1040s, K-1s, 1120S), bank statements, and asset documentation for every loan file. A typical file has 80-150 pages of documents. The processor must not only extract values but calculate qualifying income according to lender-specific rules — Fannie Mae's income calculation differs from a non-QM lender's, and self-employed borrowers require multi-year trending analysis that no generic OCR tool handles correctly.

## What Already Exists
General-purpose document extraction tools (Google Document AI, Amazon Textract, Ocrolus) can pull fields from structured documents like W-2s and paystubs with 90%+ accuracy. Mortgage-adjacent tools like LoanLogics and Indecomm offer some automation. However, none of these handle the full chain: extracting raw values, applying the correct income calculation methodology based on employment type and lender guidelines, flagging discrepancies between documents, and outputting a completed 1003 income section with an audit trail.

## The Customisation Gap
The gap is industry-specific calculation logic layered on top of extraction. A self-employed borrower's qualifying income requires following specific Fannie Mae Selling Guide Chapter B3-3.4 rules (or equivalent lender overlays): adding back depreciation and depletion, trending income year-over-year, handling negative income years, and reconciling business vs. personal returns. The extraction model needs mortgage-specific entity recognition — "YTD gross" on a paystub means something different depending on pay frequency, and bank statement deposits must be categorized (regular income vs. transfers vs. one-time deposits) according to underwriting standards.

## Impact If Solved
Cuts document processing time from 2-3 hours per file to 15-20 minutes, freeing processors to handle 3-4x more files. Reduces income calculation errors that cause underwriting kickbacks and delays by 50-70%.
