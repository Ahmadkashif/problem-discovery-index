# Tri-Merge Tradeline De-duplication

**Industry:** [[credit-bureaus|Credit Bureaus]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Record-linkage tools can match duplicates in general; a mortgage merged report needs them matched across three bureaus that each describe the same loan differently, under underwriting rules that punish both a missed duplicate and a false one.
**Tags:** #k-nearest-neighbors #word-embeddings #gradient-boosting #feature-engineering #evaluation-metrics #automation #data-integration

## The Problem
Agency mortgage underwriting still requires a tri-merge credit report: the reseller pulls each applicant's file from all three nationwide bureaus and merges them into one report the lender's automated underwriting system reads. FHFA's April 2026 decision to accept VantageScore 4.0 kept the tri-merge requirement intact. Each bureau describes the same account its own way — creditor names abbreviated differently, account numbers masked to different digits, balances as of different reporting dates, a sold loan appearing under the old and new servicer, an authorised-user card carried on one file and not another, a collection appearing as both the original charge-off and the agency's tradeline.

The merge decides what the lender sees. A duplicate left in doubles a monthly payment in the debt-to-income ratio and can push a borrower over an eligibility threshold; a false merge hides a real obligation and exposes the lender to a repurchase. Loan officers and processors catch the visible cases and ask the reseller for corrections or a supplement, which costs days in a transaction with a closing date.

## What Already Exists
General record-linkage and entity-resolution software, the resellers' own merge engines built over decades, and the bureaus' standard file formats. Underwriting systems apply their own rules for duplicate and authorised-user tradelines (recalled).

## The Customisation Gap
Generic linkage matches people or companies; here the entity is an account seen through three reporting systems at three moments. The customisation needed: creditor-name normalisation across servicer transfers and portfolio sales; matching on masked account-number fragments, open dates, original amounts and payment history rather than names; explicit handling of authorised-user, joint and co-signed accounts by ECOA code; collapsing original-creditor and collection tradelines for the same debt; a confidence on each merge decision that the processor can see; and output arranged for the agency underwriting rules, so the merged liability list is the one the underwriting system should evaluate.

## Impact If Solved
Fewer supplements and re-pulls per loan, debt-to-income ratios computed on real obligations, and processors spending their time on the borrower's actual credit questions rather than on spotting the same car loan reported three ways — worth hours per affected file at a reseller handling high volumes (illustrative).
