# Guidelines That Change With Every Buyer

**Niche:** [[niches/mortgage-lenders/non-qm-alt-doc-lending/profile|Non-QM & Alternative-Documentation Lending]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** A non-QM lender selling to several aggregators underwrites against several overlapping guideline matrices, issued as PDFs and changed by email.
**Tags:** #large-language-models #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to underwrite bank-statement, DSCR and asset-depletion income in a form that securitisation due diligence firms grade A and rating agencies credit, and whoever produces income analysis that survives third-party review at the lowest cost per loan takes the account.

## The Problem
Each buyer's matrix sets its own credit score, LTV, reserve and expense-factor rules by programme, and updates them as its securitisation appetite changes. Underwriters work from the version they last saw; a loan closed to an outdated matrix may have no buyer.

## Why It's Still Broken
There is no agency selling guide for non-QM. Buyers compete on guideline tweaks and issue them in their own formats, and pricing engines encode eligibility only partly and late.

## What a Fix Looks Like
Ingest every buyer's matrix and update into one versioned rules table, check each file at lock and at final approval against every eligible buyer's current version, and flag loans whose eligibility changed between lock and closing.

## Who Feels the Pain
Non-QM underwriters and secondary managers; borrowers whose loans are re-priced at the last minute.

## Impact If Fixed
Fewer loans closed without a buyer and fewer forced sales at a discount, at the cost of a modest rules-management effort.
