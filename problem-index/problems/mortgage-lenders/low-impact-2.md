# Warehouse Line Allocation and Purchase Exceptions

**Industry:** [[mortgage-lenders|Mortgage Lenders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A lender funds every closing on one of several warehouse lines with different prices, haircuts and eligibility rules, and pays interest on each loan until an investor buys it, yet line choice and purchase-exception chasing are run from a treasury spreadsheet.
**Tags:** #convex-optimization #time-series-forecasting #monte-carlo-methods #feature-engineering #data-integration #automation #revenue-impact

## The Problem
Nonbank lenders fund loans on warehouse lines from banks. FSOC counted about 235 warehouse lenders with ~$285B of total limits at the end of 2023, and the average nonbank had lines from about nine creditors. Each line advances 90–95% of the loan amount, so the lender funds the remaining haircut from its own cash, and each charges its own spread, has its own eligibility rules (non-QM, jumbo, aged loans, loans with missing documents), sublimits and aging limits. Every morning treasury decides which closing goes on which line. Then the loan waits: for the collateral file to reach the investor's custodian, for the investor's purchase review to clear, for exceptions to be fixed. Every day of dwell ties up haircut cash and line capacity, the carry is positive or negative depending on the gap between the note rate and the line's rate, and a loan that ages past the line's limit must be moved or paid down.

Purchase exceptions are the main cause of long dwell. An investor suspends a loan for a missing signature, a mismatch between the note and the closing disclosure, or an unrecorded document, and post-closing staff chase each one by email.

## What Already Exists
Warehouse banks provide portals for funding requests and collateral tracking; origination systems record funding and investor purchase dates; treasury and cash-management software and spreadsheets track balances. Investors' correspondent portals list suspense conditions. MERS tracks registration and transfers.

## The Customisation Gap
Generic treasury tools see cash, not loans. The mortgage-specific logic is: a loan-to-line allocation that minimises expected net carry and haircut cash given each line's price, eligibility and remaining capacity and each loan's expected dwell; a dwell forecast per loan from its product, investor, closing type and current exception status; aging alerts against each line's limit; a single exception queue that pulls suspense conditions from every investor portal and classifies them by fix owner (closer, title agent, settlement agent, borrower); and month-end projections of line usage ahead of rate-driven volume swings, so the lender knows when it needs more capacity before the bank does.

## Impact If Solved
For a lender closing ~$350M a month, cutting average dwell from ~18 to ~15 days (estimate) lowers the average warehouse balance by ~$35M. At a 5–10% haircut that frees ~$1.75–3.5M of the lender's own cash and the same headroom on its lines, which is the binding constraint for a thinly capitalised lender when volume swings. Fewer aged loans also mean fewer forced moves between lines and fewer sales at a discount.
