# Month-End for the Securitization Analyst

**Industry:** [[sales-finance-companies|Sales Finance Companies]]
**Type:** Worker Life Changing
**One-liner:** The capital markets analyst at a finance company rebuilds the same borrowing base certificates, servicer reports and loan-level tapes every month from servicing extracts and spreadsheets, under deadlines set by banks and trustees, and could get back a week of every month and the confidence that the numbers are right.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #descriptive-statistics #worker-facing #automation #data-integration #compliance

## The Problem
A finance company that funds on warehouse lines and asset-backed securities runs a monthly cycle that lands on one or two analysts. For each warehouse facility, the analyst pulls the servicing extract, applies that facility's eligibility criteria (maximum term, minimum FICO, concentration limits by state, dealer and vehicle age, excess spread tests), computes the borrowing base and prepares the certificate the bank funds against. For each outstanding securitisation, the analyst prepares the servicer report for the trustee — collections, charge-offs, recoveries, delinquency buckets, triggers — on the deal's determination date, and for public deals the loan-level file behind Form ABS-EE, 72 fields per auto loan, filed with the monthly 10-D. Each facility and each deal defines terms slightly differently, so the workbooks multiply.

The work is mechanical and unforgiving. A mis-mapped status code inflates the eligible pool; a missed concentration limit triggers a cure; a delinquency figure that disagrees between the servicer report and the asset-level file draws an investor question or a rating agency call. After Tricolor, warehouse banks are also asking for loan-level evidence that collateral exists and is not pledged elsewhere, which arrives as new spreadsheet requests rather than new systems.

## Why It Matters to the Worker
Month-end compresses into a few days of late nights, reconciling numbers that should have reconciled themselves, with no room for the analysis the analyst was hired for — why a vintage is rolling faster, whether a new dealer cohort is hurting excess spread. The analyst is personally exposed: their signature or their manager's goes on certificates whose errors can become covenant breaches, and in the current climate an error looks like misrepresentation. Knowledge of each facility's quirks lives in one or two heads, so vacations and resignations are risks to the company.

## What a Solution Looks Like
A single loan-level dataset reconciled once from the servicing system, with each facility's and each deal's definitions stored as configuration rather than as workbook formulas. Borrowing base certificates, servicer reports and ABS-EE files generated from it, with cross-checks that the same delinquency appears the same way in every report. Document-reading tools that turn each new facility agreement's eligibility criteria into draft configuration for the analyst to confirm. And a variance explanation for every month-over-month move, so the analyst's review starts from what changed.

## Impact If Solved
Turning a week of rebuilding into a day of review gives the analyst back roughly a quarter of every month (estimate) and removes the error class — inconsistent definitions across reports — that turns a reporting slip into a funding problem.
