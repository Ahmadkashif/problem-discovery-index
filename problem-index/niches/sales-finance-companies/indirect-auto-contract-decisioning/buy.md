# Card-Issuer Decision Management Adapted to Dealer Paper

**Niche:** [[niches/sales-finance-companies/indirect-auto-contract-decisioning/profile|Indirect Auto Contract Decisioning]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Card issuers run champion–challenger strategy testing on every decision; indirect auto lenders decide on deals whose terms a dealer changes between submissions, which the generic tools do not model.
**Tags:** #gradient-boosting #hypothesis-testing #evaluation-metrics #causal-inference #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to give the dealer a workable decision before another lender does," but prime and non-prime paper are won differently — prime by deciding the most applications automatically at a stable loss rate, non-prime by structuring counteroffers the dealer can close and the borrower can pay — with different inputs, staff and winners. Decomposed into contested sub-niches below.

## The Problem
Decision strategy in auto lending is changed by committee and judged a year later. Lenders want to test a new cut-off, a new stipulation rule or a new dealer tier on a slice of traffic and know quickly whether it changed look-to-book and early default.

## What Already Exists
Enterprise decision management platforms (FICO's decisioning products, Experian PowerCurve, Provenir) with champion–challenger testing built for card and personal loan originations.

## The Customization Gap
Auto needs: the deal as a negotiated object (the dealer resubmits with changed down payment or vehicle after a counter); dealer-level randomisation, because dealers notice when a lender changes behaviour; look-to-book and booking rate as outcomes alongside loss, since a declined deal costs future dealer traffic; collateral inputs (VIN decode, book value, advance) as first-class variables; and fair lending testing of every challenger before it touches live traffic.

## Target Customer
Credit strategy teams at mid-size and large indirect lenders already licensing a decision platform.

## Impact If Solved
Strategy changes tested in weeks on dealer-randomised traffic instead of debated in committee and discovered in the vintage curve.
