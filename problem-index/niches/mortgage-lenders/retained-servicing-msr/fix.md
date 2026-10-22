# The MSR Mark Nobody Checks Against the Book

**Niche:** [[niches/mortgage-lenders/retained-servicing-msr/profile|Retained Servicing & MSR Management]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** Every quarter a valuation firm marks the lender's servicing rights using market prepayment, recapture and cost assumptions, and the lender rarely tests those assumptions against its own loans.
**Tags:** #survival-analysis #hypothesis-testing #evaluation-metrics #descriptive-statistics #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to protect the value of the lender's mortgage servicing rights", but that value is defended in two contests with different winners: keeping the borrower when they refinance or move, which goes to whoever reaches them first with a credible offer, and servicing the loans that stay at a cost and audit standard below the MSR's assumptions, which goes to the subservicers and servicing platforms. Decomposed into contested sub-niches below.

## The Problem
The quarterly mark drives the lender's reported earnings and its borrowing capacity. Its key inputs (prepayment speeds by cohort, recapture rate, cost to service, delinquency transitions) come from the valuation firm's market models, adjusted lightly for the portfolio tape.

## Why It's Still Broken
Testing the assumptions needs loan-level actuals the lender holds in pieces: payoffs at the subservicer, recaptures in the origination system, costs in invoices. Finance accepts the mark because the auditor does, and the valuation firm has no access to the operating data.

## What a Fix Looks Like
A quarterly back-test: actual prepayment speeds by cohort versus assumed, recapture actually achieved versus assumed, and cost per loan by status versus assumed, delivered alongside the mark and discussed with the valuation firm before sign-off.

## Who Feels the Pain
CFOs whose earnings swing with marks they cannot explain; treasury teams negotiating MSR financing; boards deciding whether to sell servicing.

## Impact If Fixed
A few days of analysis a quarter turns the MSR from a number the lender receives into one it can defend, and spots generous or punitive assumptions before an MSR sale or a lender's margin call.
