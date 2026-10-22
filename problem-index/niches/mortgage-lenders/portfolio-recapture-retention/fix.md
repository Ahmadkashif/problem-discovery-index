# Recapture Counted Three Different Ways

**Niche:** [[niches/mortgage-lenders/portfolio-recapture-retention/profile|Portfolio Recapture & Retention]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** The valuation firm, the consumer-direct team and finance each report a different recapture rate, because nobody agreed what counts.
**Tags:** #descriptive-statistics #data-integration #evaluation-metrics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to reach a servicing-book borrower with a credible refinance or purchase offer before a competitor's rate alert or credit-trigger lead does, and whoever identifies the borrower's moment first takes the account.

## The Problem
Is a borrower who pays off and takes a new loan from the same lender's retail branch a recapture? What about a purchase loan on a different property, or a loan the borrower found through a broker who sold it to the lender? Each team counts differently, and the MSR valuation uses yet another figure.

## Why It's Still Broken
Payoffs are recorded at the servicer or subservicer and new loans in the origination system, with no common borrower key, and recapture credit drives loan officer compensation, so every team has a reason to prefer its own definition.

## What a Fix Looks Like
One agreed definition (payoffs in a period matched by borrower and property to new originations within a window, split by refinance and purchase), computed from joined servicing and origination data, and used for compensation, management reporting and the valuation alike.

## Who Feels the Pain
Heads of retention defending budgets; finance reconciling MSR assumptions; loan officers arguing over credit.

## Impact If Fixed
A single recapture number ends the internal dispute and gives the valuation firm a defensible input, which moves the MSR mark directly.
