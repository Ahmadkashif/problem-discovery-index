# Uplift-Targeted Offers by Address Alternative

**Niche:** [[niches/wired-broadband-providers/cable-save-offers/profile|Cable Save Offers Against Fixed Wireless & Fibre]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Save offers go to households ranked by churn risk, when what matters is how much each offer changes the decision of a household with a live alternative.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #hypothesis-testing #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche (BSS churn modules, retention analytics vendors and operators' own data science teams) is fighting to price each save offer to the alternative the household can actually get at its address, and whoever prices save offers to each address's real alternative best takes the account.

## The Problem
High-risk households get the richest offers. Many would have stayed anyway because nothing else is available at their address; others with a fibre build on their street get a token discount and leave. Offer spend and outcomes are poorly connected.

## Why Nobody Has Built This
Uplift models need randomised offer data, which save desks don't generate. Address-level alternatives were not available until the BDC's location-level map, and BSS vendors model risk, not treatment effect.

## What to Build
A model estimating, for each household and each offer, the change in 90- and 180-day retention, using address-level alternatives (fixed wireless eligibility, fibre presence and advertised speeds from the FCC map), promo history, outages and bundle status. A standing randomised holdout is built in, and offers are chosen to maximise retained margin per dollar.

## Target Customer
Retention and pricing leaders at cable operators with at least a few hundred thousand broadband customers.

## Impact If Built
Discount budgets concentrate where they change outcomes; operators typically find a sizeable share of offers going to households that would have stayed (estimate) and can redirect it.
