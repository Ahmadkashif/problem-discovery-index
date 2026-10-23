# Baseline Cost Predicted From Delivered History

**Niche:** [[niches/facilities-management-firms/ifm-bid-solutioning/profile|IFM Bid Solutioning & Baseline Pricing]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Providers have years of delivered cost on hundreds of buildings and price each new bid as if they had none.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #monte-carlo-methods #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a five-year, multi-site contract from an asset list and spend history it knows to be wrong, and whoever comes nearest the cost the portfolio actually turns out to have, without pricing itself off the shortlist, takes the account.

## The Problem
Each bid is priced bottom-up from task libraries and the RFP's asset list, adjusted by the bid team's experience. Nobody asks systematically what similar buildings the provider has run actually cost: how many reactive work orders a 20-year-old lab building in a hot climate generates, or how far bid-time asset lists usually miss. The provider's best evidence sits in the CMMS and account financials of its existing book.

## Why Nobody Has Built This
Bid teams and operations teams sit in different organisations, and delivered cost is not stored in a form that joins to bid-time inputs. Accounts churn, and client-owned CMMS instances leave with the account. Pricing software vendors sell to retailers and insurers, not to service contractors.

## What to Build
A model trained on the provider's own delivered history: site attributes, asset counts and ages, climate and use joined to actual first-year and steady-state labour, reactive volume and subcontract spend, and to the asset-list error found in transition. For a new bid it produces site-level cost estimates with calibrated intervals and a portfolio cost distribution, so pricing chooses a point on a known curve. Every bid also writes back its assumptions, so the next model learns from this one.

## Target Customer
Heads of pricing and solution design at IFM providers with several hundred sites of delivered history.

## Impact If Built
Fewer accounts won at a loss, fewer lost on overpricing, and transitions that confirm the price instead of overturning it (estimate: a halving of first-year margin surprises).
