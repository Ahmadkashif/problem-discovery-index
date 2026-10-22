# Payoff Routing and Statement Checking

**Niche:** [[niches/title-and-settlement-offices/payoff-statement-procurement/profile|Payoff Statement Procurement]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Payoff requests go out by whatever channel the processor remembers, and the statements that come back are keyed by hand and trusted without a check.
**Tags:** #large-language-models #transformers #gradient-boosting #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to obtain an accurate, good-through payoff statement from every lienholder — servicers, HELOC lenders, private noteholders, judgment creditors — before the Closing Disclosure is final, and whoever gets the right number first with no post-funding shortage takes the agency's payoff desk.

## The Problem
For each lien on the commitment, a processor finds the right payoff department, sends the borrower's authorisation, waits, re-requests when the good-through date passes, reads the statement and keys the figure. Shortages surface after funding, when the servicer's final figure exceeds the wire and the agent must collect from the seller or eat it.

## Why Nobody Has Built This
Servicer channels differ — portals, email, fax — and private payoffs are entirely manual. Agencies see too few of any one servicer's errors to know which statements tend to be short.

## What to Build
Route each payoff request to the right channel from a servicer directory, submit it with the authorisation, extract the statement into fields (principal, interest, per-diem, fees, escrow advances, good-through date, wire instructions), recompute per-diem to the actual funding date, and flag statements likely to be short based on missing fee lines and the servicer's historical shortage pattern. Verify payoff wire instructions against known servicer accounts before disbursement.

## Target Customer
Escrow departments at agencies closing several hundred files a month.

## Impact If Built
Fewer re-requests, fewer post-funding shortages, and a CD balanced on the first payoff.
