# Unit-Price Outliers Before the Bid Goes In

**Niche:** [[niches/heavy-civil-contractors/public-bid-tab-unit-price-intelligence/profile|Public Bid Tab & Unit-Price Intelligence]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A model of each item's market price, conditioned on quantity, region and date, can flag the handful of lines in a draft bid that are mis-keyed, unbalanced or out of the market, in minutes, on bid day.
**Tags:** #bayesian-inference #linear-regression #gaussian-mixture-models #hypothesis-testing #large-language-models #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn the bid results of Corps districts, port authorities, transit agencies and railroad owners, plus DOT marine, structures and rail items, into a clean, item-mapped unit-price history the estimator trusts on bid day, and whoever holds the largest correctly mapped item history across those owners takes the account.

## The Problem
A bid schedule has ~20–200 items (estimate). A mis-keyed decimal, an item priced off the wrong unit, or a mobilisation spread that looks unbalanced can lose the job or get the bid rejected, and estimators check by eye at 1 p.m. for a 2 p.m. deadline.

## Why Nobody Has Built This
Bid-tab products report averages; estimating systems don't hold market data. Item codes differ by owner, so cross-owner models need a mapping layer nobody has built for Corps, port and transit items.

## What to Build
Parse results from Corps districts, ports, transit agencies and railroad owners, plus DOT tabulations filtered to marine, structures and rail items, map items to a shared taxonomy with a language model plus human review, and fit a hierarchical price model (log price on log quantity, region, date and item family, with bidder effects). Then score each line of the contractor's draft and return the ranked outliers with comparable lettings. This is the owner's two-week MVP: Corps dredging results plus one state's DOT tabs filtered to structures, marine and rail items. DOT road-and-bridge items are the queued highway contractors build's territory.

## Target Customer
Chief estimators at regional heavy civil, marine, dredging and rail contractors.

## Impact If Built
If the checker catches one costly pricing error or unbalance a year (estimate: ~$50K–$500K of exposure each), and narrows the gap to the low bid on lost lettings, it pays for itself many times over.
