# Bank-Statement Income Graded Against Deal Performance

**Niche:** [[niches/mortgage-lenders/non-qm-alt-doc-lending/profile|Non-QM & Alternative-Documentation Lending]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A non-QM lender's income calculation is graded twice, once by the due diligence firm before securitisation and once by the borrower's payments afterwards, and neither grade reaches the underwriter.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to underwrite bank-statement, DSCR and asset-depletion income in a form that securitisation due diligence firms grade A and rating agencies credit, and whoever produces income analysis that survives third-party review at the lowest cost per loan takes the account.

## The Problem
Bank-statement income is a judgement: which deposits are business revenue, which are transfers, what expense factor applies, whether a declining trend matters. Experienced non-QM underwriters make these calls consistently; new ones do not. The due diligence firm then re-calculates and grades the loan, and months later the loan pays or does not. KBRA and others publish non-QM default studies at deal level; no lender systematically ties its own underwriters' calculations to either grade.

## Why Nobody Has Built This
Grades arrive in the due diligence firm's report format, performance arrives in servicer remittance data, and underwriting worksheets sit in spreadsheets. Most non-QM lenders are young and grew fast through the 2024–25 boom without building the data join.

## What to Build
A record of every income calculation (deposits included and excluded with reasons, expense factor, trend view), joined to the due diligence grade and any exception, and to 6–24 month payment history. Models that learn which calculation choices predict grade exceptions and early delinquency, and a second-read tool that flags new files where the underwriter's choices diverge from the pattern of the lender's best underwriters.

## Target Customer
Chief credit officers at non-QM lenders and the aggregators and depositors that buy from them.

## Impact If Built
Fewer grade exceptions and kick-outs from securitisation pools, and a documented credit process that rating agencies and investors credit at pricing.
