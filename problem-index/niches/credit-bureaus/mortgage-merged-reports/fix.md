# Rapid Rescores Assembled by Email and PDF

**Niche:** [[niches/credit-bureaus/mortgage-merged-reports/profile|Mortgage Merged Reports & Score Transition]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** When a paid-off card or a reporting error is costing a borrower a price tier, the loan officer emails statements to the reseller, who re-keys them into a rescore request to each bureau.
**Tags:** #large-language-models #transformers #evaluation-metrics #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver the merged report and whichever score set each lender's investors now accept — Classic FICO, VantageScore 4.0, later FICO 10T — straight into the lender's pricing and underwriting engines, and whoever re-plumbs the score transition without breaking a lender's pricing or pull-through takes the account.

## The Problem
A rapid rescore updates a borrower's file before closing with proof of a payoff or a correction. The loan officer collects the creditor letter or statement, sends it to the reseller, the reseller submits it to each bureau, and the updated scores come back days later (estimate). Documents are rejected for missing account numbers or dates, and the cycle restarts against a closing date.

## Why It's Still Broken
Rescores are a small, per-request service squeezed between the lender's and the bureaus' systems; nobody owns the document check.

## What a Fix Looks Like
Validate the proof document at upload — creditor, masked account number, balance, date — against the tradeline on the merged report; submit to all three bureaus in one step; and show the expected score and price effect before the request is sent.

## Who Feels the Pain
Loan officers and processors racing a closing; borrowers paying a higher rate for a debt they already paid.

## Impact If Fixed
Rescores that succeed first time, and borrowers priced on their current file.
