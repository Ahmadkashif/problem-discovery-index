# Settlement Distribution Calculation and Disbursement Documentation

**Industry:** [[personal-injury-law|Personal Injury Law Firms]]
**Type:** Worker Life Changing
**One-liner:** Paralegals who manually calculate and document the settlement distribution worksheet — attorney fee, case expenses, each lien payment, and net-to-client — across 20-30 settled cases per month get an automated calculation engine that produces the disbursement sheet and all supporting documentation in minutes.
**Tags:** #arithmetic-and-basic-algebra #feature-engineering #automation #compliance #worker-facing

## The Problem
After a PI case settles, the settlement funds arrive in the firm's trust account and must be disbursed in a specific sequence: case expenses reimbursed, attorney contingency fee calculated, all liens paid, and the balance distributed to the client. The settlement disbursement sheet is a formal accounting document that must be accurate to the penny, signed by the client, and retained in the file. Preparing it requires: retrieving the total case expenses from the case management system (with every receipt), calculating the attorney fee on the net settlement (or gross, depending on the fee agreement), resolving each lien and calculating the payment amount for each, and computing the client's net recovery. When something doesn't reconcile, tracing the discrepancy through the trust ledger, expense records, and lien correspondence takes additional time.

## Why It Matters to the Worker
Disbursement preparation is a high-stakes administrative task performed under time pressure — clients are anxious to receive their settlement funds and call repeatedly asking when the check will arrive. The calculation is not complex, but it requires gathering inputs from multiple places (case management system, lien letters, fee agreement), and errors have serious professional responsibility implications — an attorney who miscalculates and disburses the wrong amount to a lienholder or over-distributes to the client has violated trust account rules. This creates anxiety for the paralegal performing the calculation. The current workflow is a manual spreadsheet built from scratch for each case.

## What a Solution Looks Like
An automated disbursement calculator integrated into the case management system that pulls case expenses automatically from logged records, calculates attorney fee based on the fee agreement terms on file, imports lien resolution amounts from the lien tracking system, and produces a complete disbursement worksheet with all supporting line items. The paralegal reviews the calculated sheet, approves it, and the system generates the client-facing settlement statement and trust accounting entries automatically. Exception handling (a lien amount that doesn't match the letter on file) is flagged for human review.

## Impact If Solved
Reduces disbursement preparation from 45-90 minutes per case to 5-10 minutes of review. For a firm closing 20-30 cases per month, that's 15-30 hours of paralegal time recovered monthly. Eliminates disbursement calculation errors that create professional responsibility exposure.
