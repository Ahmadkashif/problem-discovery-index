# One Record From Bid Assumptions to Contract-Year Actuals

**Niche:** [[niches/ambulance-services/county-911-exclusive-contracts/profile|County 911 Contracts & Exclusive Operating Areas]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An operator prices a five-year 911 contract on call volume, payer mix, collection rate and unit-hours, then runs it on CAD and billing data that nobody joins back to the bid.
**Tags:** #time-series-forecasting #linear-regression #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor here is fighting to hold a county's or city's 911 ambulance contract. But the contract is won at bid, by pricing years of call volume, payer mix and collections into a subsidy or franchise fee, and kept month by month, by deploying units against the response-time standard. The two contests have different people, clocks and winners. Decomposed into contested sub-niches below.

## The Problem
A 911 bid rests on a handful of assumptions: calls a year and their growth, transport ratio, payer mix, collection rate by payer, unit-hours to meet the standard, and penalty exposure. Once the contract starts, actual calls arrive in CAD, collections in billing and penalties in the county's monthly report. Each team reports its own number. Nobody shows which bid assumption was wrong, so the next bid repeats the error.

## Why Nobody Has Built This
Bids are prepared by a small corporate development team or a consultant, years apart. CAD, ePCR and billing vendors each hold one part of the record, and the operator's finance team sees results only at the contract level.

## What to Build
A contract record that stores each bid's assumptions as forecasts and grades them monthly against CAD volumes, billing collections by payer and county penalty reports. It feeds the variances into the next bid in that county and in similar ones. This is the shared spine of both sub-niches: the bid model in [[niches/ambulance-services/exclusive-operating-area-bids/profile|🎯 Exclusive Operating Area Bids & Contract Pricing]] and the deployment plan in [[niches/ambulance-services/system-status-deployment/profile|🎯 System Status Management & 911 Unit Deployment]].

## Target Customer
Vice-presidents of operations and corporate development at multi-county private operators and hospital-based 911 services.

## Impact If Built
If a regional operator holding ten contracts worth ~$30M a year each (an estimate) avoided one first-year contract loss of ~$2M (an estimate) across its next round of rebids, the record would pay for itself many times over.
