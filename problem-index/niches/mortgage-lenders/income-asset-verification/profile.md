# Income, Asset & Employment Verification

**Parent Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to verify income, employment and assets from third-party data so the agencies grant rep-and-warrant relief on that component, and whoever validates the largest share of files at the lowest cost per loan takes the account.

## Profile
**Market Size:** ~$1B a year in employment and income verification fees, bank-data connections, transcript requests and income-calculation tools paid by mortgage lenders (estimate)
**Share of Parent Industry:** ~8% of mortgage lenders' technology, data and outsourced-service spend (estimate)
**Digital Adoption:** High for data connections; uneven in use, as many files still fall back to paystubs, W-2s and written verifications
**Target Buyer:** COO or VP of Operations, with the Chief Credit Officer
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Fannie Mae's DU validation service and Freddie Mac's equivalent grant enforcement relief from reps and warrants on income, employment and assets verified from approved third-party data, and Fannie says validating all four Day 1 Certainty components cuts repurchase risk by 64%. That turns verification from a cost into a risk transfer, and makes the share of files that validate the metric that matters. Income validation also fails when DU's calculated income does not support the application, so verification and income calculation are one problem.

## Current Tools & Gaps
Payroll-data verification from Equifax's The Work Number (a consumer reporting agency whose industry is queued in this plan as Credit Bureaus), payroll-connector providers (Truv, Argyle), bank-data aggregators (Plaid, Finicity), IRS transcripts, and income-calculation tools. The gaps: lenders order verifications in a fixed sequence regardless of which will succeed for this borrower; re-verification before closing repeats costs; and nothing tells the lender in advance whether a file will validate.

## Problems
- [[niches/mortgage-lenders/income-asset-verification/build|🔨 Build: Validation Predicted Before the Order]]
- [[niches/mortgage-lenders/income-asset-verification/buy|🛒 Buy: Payroll Connector APIs Adapted to Agency Validation Rules]]
- [[niches/mortgage-lenders/income-asset-verification/fix|🔧 Fix: Paying Twice for the Same Verification]]
