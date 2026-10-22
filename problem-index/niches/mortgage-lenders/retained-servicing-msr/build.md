# The Servicing Book as One Ledger

**Niche:** [[niches/mortgage-lenders/retained-servicing-msr/profile|Retained Servicing & MSR Management]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Prepayments, recaptures, servicing costs and delinquencies each live in a different system, so a lender cannot say which of its MSR's value drivers is actually working.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to protect the value of the lender's mortgage servicing rights", but that value is defended in two contests with different winners: keeping the borrower when they refinance or move, which goes to whoever reaches them first with a credible offer, and servicing the loans that stay at a cost and audit standard below the MSR's assumptions, which goes to the subservicers and servicing platforms. Decomposed into contested sub-niches below.

## The Problem
The servicing book generates four streams of evidence: payoffs from the servicing system, new loans from the origination system (some of them recaptured payoffs), cost data from the subservicer's invoices, and delinquency and loss-mitigation outcomes. The MSR's value rests on assumptions about all four. Finance sees the mark, servicing sees the subservicer's reports, and the consumer-direct team sees its own recapture count. No one sees the loan-level chain from payoff to recapture to new servicing.

## Why Nobody Has Built This
Each stream belongs to a different vendor with a different loan key, and the subservicer, not the lender, holds most of the servicing detail. MSR valuation firms receive a tape each quarter, not the operating data.

## What to Build
A loan-level servicing ledger joining payoffs to any subsequent origination by the same borrower or property, subservicer cost and activity by loan, delinquency and loss-mitigation history, and each quarter's valuation assumptions. Survival models for prepayment and recapture on the lender's own book, compared with the valuation firm's assumptions by cohort, and attribution of each quarter's MSR value change to rates, speeds, recapture and cost.

## Target Customer
CFOs and heads of servicing at independent mortgage banks retaining $10B–$200B of servicing.

## Impact If Built
The lender can tell its valuation firm, its warehouse and MSR lenders and its board where the mark is conservative or generous, and target recapture and cost efforts where they move value.
