# Holdout Markets as Standard Practice

**Niche:** [[niches/visitors-bureaus/leisure-campaign-attribution/profile|Leisure Destination Marketing & Campaign Attribution]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bureaus spend most of their budgets on campaigns whose effect has never been tested against a market that did not see them.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #time-series-forecasting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show that a campaign caused overnight visits that would not otherwise have happened, and whoever produces an incrementality estimate that both the city's auditor and the hotel board accept takes the account.

## The Problem
A bureau runs a spring campaign in eight drive markets. Afterwards its agency reports how many people who saw the ads later visited, and their spending. Some of those people were coming anyway. The bureau cannot say how many, so it cannot say whether the campaign paid back or which markets and channels worked.

## Why Nobody Has Built This
Holding out markets means not advertising somewhere, which agencies and boards resist. Bureaus buy media in too few markets for clean tests on their own. The vendors who sell attribution are paid by the same budget the test might cut.

## What to Build
An experiment service: matched-market selection from the bureau's origin-market visitor data, randomised holdouts or staggered launches, and lift estimated from panel visits, card spend and hotel demand by origin, with synthetic-control estimates for campaigns that could not hold out. Results build into a library across bureaus, so a small bureau can borrow priors from similar campaigns elsewhere.

## Target Customer
CMOs at large bureaus and state tourism offices, and agencies wanting a defensible measurement product.

## Impact If Built
A lift figure the council's auditor can follow, and budgets moved from markets that do nothing to markets that work.
