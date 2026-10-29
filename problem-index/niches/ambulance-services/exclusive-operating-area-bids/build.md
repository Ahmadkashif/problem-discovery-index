# Payer-Mix and Net Revenue Forecast for a County Rebid

**Niche:** [[niches/ambulance-services/exclusive-operating-area-bids/profile|Exclusive Operating Area Bids & Contract Pricing]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A bid team forecasts five years of ambulance revenue for a county from one data pack and its own instinct, when census insurance data, NEMSIS call patterns and its own contracts' collections could ground every assumption.
**Tags:** #time-series-forecasting #gradient-boosting #bayesian-inference #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a county's exclusive 911 franchise from its call volume, payer mix and collection history, and whoever has the lowest share of won contracts losing money in their first full year takes the account.

## The Problem
The bid model's riskiest inputs are payer mix and collection rate. A county with a growing Medicaid share, more uninsured residents or more Medicare Advantage enrolment changes net revenue per transport sharply. Bid teams usually extrapolate the county's historical figures, if the incumbent shares them, or borrow from a similar contract.

## Why Nobody Has Built This
Bids are infrequent and each operator sees only its own contracts. The data needed sits in different places: insurance coverage by census tract, NEMSIS call patterns, the operator's collections by payer across its own contracts, and the county's CAD. The consultancies that run bids are paid per engagement and do not keep a graded model.

## What to Build
A forecasting model for net patient revenue per transport by county. It combines census insurance coverage and age structure, call and transport ratios by area from NEMSIS public data and the county pack, and the operator's own collection rates by payer across contracts. Bayesian shrinkage fills the gaps for counties with little history. Every bid's assumptions are stored against the contract, and each won contract's first-year result shows which assumption turned it into a loss, so the next bid starts from that record.

## Target Customer
Corporate development leads at private operators bidding several county contracts a year, and hospital systems deciding whether to bid for their county's 911 area.

## Impact If Built
If better forecasts kept an operator out of one loss-making contract a year, worth ~$2M a year of operating losses (an estimate), the model would pay for itself many times over.
