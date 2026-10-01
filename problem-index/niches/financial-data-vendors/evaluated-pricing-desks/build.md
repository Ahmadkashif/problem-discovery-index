# Price Challenges as Labelled Data

**Niche:** [[niches/financial-data-vendors/evaluated-pricing-desks/profile|Fixed-Income Evaluated Pricing]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every client challenge to an evaluated price, and every trade that later prints, grades an evaluator's judgement — and the record is used to resolve tickets, not to learn.
**Tags:** #tacit-knowledge-ml #gradient-boosting #gaussian-processes #confidence-intervals #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price illiquid bonds defensibly every day and survive the client's price challenges — and whoever's evaluations hold up under challenge keeps the fund administrator's NAV process.

## The Problem
Evaluators adjust model prices with judgement — this issuer trades wide of its curve, this dealer's quotes run rich, this sector is repricing faster than the comparables show. Senior evaluators are measurably better and cannot fully say why. Clients challenge prices daily; each challenge is researched, answered and either upheld or not. Subsequent TRACE prints show where the bond actually traded.

## Why Nobody Has Built This
Challenges are handled as a service queue with a response-time target. Evaluator adjustments are logged for audit but not analysed as decisions. The tacit-knowledge obstacles apply: capturing why an adjustment was made, evaluators disagreeing among themselves, and any assistance having to be faster than the evaluator before the NAV deadline.

## What to Build
A decision record per adjustment — evaluator, inputs seen, adjustment and stated reason — joined to later trades and challenges. Grade adjustments by evaluator, sector and reason against subsequent prints. Train a model on the adjustments that improved accuracy to propose adjustments with uncertainty, and to rank the day's evaluations by the likelihood they would be challenged or contradicted by a print, so evaluators look at those first.

## Target Customer
Heads of evaluated pricing at pricing services.

## Impact If Built
Turns evaluator judgement into a measured, transferable asset, and gives the provider a transparency story Rule 2a-5 oversight increasingly asks for.
