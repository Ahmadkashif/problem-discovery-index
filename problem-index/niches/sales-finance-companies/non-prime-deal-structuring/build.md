# Counteroffers Ranked by Close Rate and Performance

**Niche:** [[niches/sales-finance-companies/non-prime-deal-structuring/profile|Non-Prime Deal Structuring]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The counteroffer decides both whether the lender gets the deal and whether the deal pays, and analysts compose it by hand with no evidence of which structures do both.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #optimization-fundamentals #causal-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to return a counteroffer on advance, term, down payment and stipulations that the dealer can close and the borrower can pay, and whoever structures the most closable deals that still perform takes the account.

## The Problem
A senior analyst might counter a deal at 110% advance and 66 months with proof of income; a junior one declines it or approves it at 84 months. Each choice changes the probability the dealer books it and the probability it defaults. Neither probability is shown on the screen.

## Why Nobody Has Built This
Counteroffer history is stored as the final terms only; the dealer's resubmission is a separate application; and close rate (did the dealer book with us) and performance live in different systems. Fair lending review of structure decisions adds caution.

## What to Build
Two models trained on the lender's history — probability the dealer books a given structure, and expected early default and loss for that structure — combined into a ranked list of counteroffers for the analyst, each with its expected value, its cue flags and its adverse-action reasons. Senior analysts' past counters are the training signal; fair lending testing runs before release.

## Target Customer
Chief credit officers at non-prime auto, powersports and equipment lenders.

## Impact If Built
Juniors propose structures seniors would, look-to-book rises on the deals worth having, and the lender can show which structures lose money.
