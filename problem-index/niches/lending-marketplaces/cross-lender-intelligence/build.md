# The Only Empirical Picture of the Market

**Niche:** [[niches/lending-marketplaces/cross-lender-intelligence/profile|Cross-Lender Intelligence]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same borrower shopping across many lenders over years is a view nobody else has, and it is used to decide which ad to show them.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #evaluation-metrics #confidence-intervals #k-means-clustering #revenue-impact #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to turn the view of the same borrower shopping across many lenders over years into answers no individual lender can produce — and whoever organises it owns the only empirical picture of how credit is actually priced and granted.

## The Problem
Each lender sees its own applicants and its own decisions. The marketplace sees borrowers approaching many lenders with the same profile at the same moment, and the same borrowers returning months and years later in changed circumstances. That view answers questions the industry currently addresses with survey data and guesswork: how appetite differs between lenders at the same profile, how pricing moves through a cycle, how borrowers actually shop, and what happens to the ones who are declined everywhere.

## Why Nobody Has Built This
The data was collected to route leads, so its analytical value was incidental — nobody was ever asked what else the shopping record could answer. Outcome data is partial, which makes the deepest questions harder and was taken as a reason not to start. The commercial model is lead fees, where intelligence products are a distraction. And publishing market intelligence could strain lender relationships.

## What to Build
Characterise the market from the shopping record. Model borrower shopping behaviour across lenders — how many are approached, in what order, over what period, with what outcome — which is the core and is computable today without any lender cooperation. Characterise lender appetite by profile from observed routing, application and known funding patterns, since even partial signal across many lenders produces a real picture. Detect appetite shifts early, because a lender tightening shows in its behaviour weeks before it is announced and that is valuable to everyone including the lender. Track pricing dispersion at the same profile, as the spread between lenders for an identical borrower is large, unexamined and directly useful. Follow the declined borrower over time, since what happens to people the market turns down is a question with policy weight and nobody can answer it. Produce benchmarks lenders would pay for, which is the commercial path and also the argument that wins outcome data. Publish selectively, because being the source of the market's empirical picture is a durable position. Use the intelligence internally for routing and acquisition first, as that is the fastest return. Handle privacy and fair lending explicitly, since analysis of credit outcomes by population is both valuable and sensitive. And validate against any external data available, so the picture is anchored rather than self-referential.

## Target Customer
Data and commercial leadership, lenders who cannot see the market, regulators and researchers studying credit access, and market data vendors with no equivalent view.

## Impact If Built
The data was collected to route leads and nobody asked what else the shopping record could answer. Modelling how borrowers shop and how lender appetite differs at the same profile needs no lender cooperation at all.
