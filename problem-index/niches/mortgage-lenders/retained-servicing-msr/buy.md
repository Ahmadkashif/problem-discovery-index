# Bank ALM Platforms Pointed at the MSR

**Niche:** [[niches/mortgage-lenders/retained-servicing-msr/profile|Retained Servicing & MSR Management]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks have run interest-rate risk models with prepayment assumptions for decades; independent mortgage banks holding MSRs as their largest asset mostly rely on a quarterly third-party mark.
**Tags:** #monte-carlo-methods #time-series-forecasting #survival-analysis #data-integration #compliance
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to protect the value of the lender's mortgage servicing rights", but that value is defended in two contests with different winners: keeping the borrower when they refinance or move, which goes to whoever reaches them first with a credible offer, and servicing the loans that stay at a cost and audit standard below the MSR's assumptions, which goes to the subservicers and servicing platforms. Decomposed into contested sub-niches below.

## The Problem
An independent lender's balance sheet swings with rates through the MSR, and its lenders (MSR facility banks, warehouse banks) and the agencies set liquidity and net-worth requirements around it. Most lenders cannot run rate scenarios on their own servicing book between quarterly marks.

## What Already Exists
Asset-liability management platforms used by banks and credit unions (QRM, ZM Financial, Empyrean, as covered in [[niches/credit-unions/alm-risk-modeling-vendors/profile|🔍 Asset-Liability & Interest Rate Risk Modelling Vendors]]) model prepayment and repricing under rate paths.

## The Customization Gap
An MSR is not a bank balance sheet. The adaptation needs: servicing-fee, float and escrow cash flows; recapture as an offset to runoff; cost to service by delinquency status; Ginnie Mae early buyout economics; the interaction with the origination pipeline as a natural hedge; and scenario output in the form MSR facility lenders and agency eligibility requirements test.

## Target Customer
CFOs and treasurers at lenders whose MSR exceeds their tangible net worth.

## Impact If Solved
Rate-scenario answers between marks, earlier warning of covenant pressure on MSR financing, and a better-informed decision on when to sell servicing.
