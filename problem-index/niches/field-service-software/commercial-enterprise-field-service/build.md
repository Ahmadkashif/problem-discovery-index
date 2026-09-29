# Contract Profitability Forecast Before the Renewal

**Niche:** [[niches/field-service-software/commercial-enterprise-field-service/profile|Commercial & Enterprise Field Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Service contracts are priced from last year's price and evaluated after they expire, so a service organisation discovers which contracts lose money only once it has already renewed them at a loss.
**Tags:** #survival-analysis #gradient-boosting #monte-carlo-methods #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #time-series-forecasting
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A service organisation carries several thousand contracts. Each commits to response times, coverage and included parts for an annual fee. Cost is driven by how often the covered equipment fails, what it costs to fix, and how far the technician has to travel — all of which vary enormously by machine age, duty cycle, site and customer behaviour. Profitability is computed at the account level after the year, in aggregate, with allocations. Renewals are priced by increasing last year's figure. The organisation therefore renews its worst contracts at prices that guarantee another bad year and prices its best ones below what they are worth.

## Why Nobody Has Built This
Cost attribution to a contract requires joining labour, parts, travel and overhead to specific machines and specific entitlements, and enterprise service systems record all of those in different modules with different keys. The forecast itself is a failure-rate modelling problem that service organisations have the data for and rarely the skills to do, since the analytical capability in these companies sits in reliability engineering on the product side rather than in service operations. And commercially, an accurate contract-level profitability view creates uncomfortable conversations with sales, whose incentives are on contract value rather than contract margin.

## What to Build
A per-contract forecast built from equipment-level failure modelling. Expected service events over the coming term are modelled per machine from age, model, duty cycle, environment and its own service history, with the organisation's installed base supplying the base rates. Expected cost per event follows from parts, labour and travel for that site. The output is a distribution of contract cost, which means a renewal can be priced against a stated probability of loss rather than against a margin target applied to a guess. Contracts are ranked by expected margin and by risk, which is the artefact a service director has never had. Where telemetry exists it sharpens the failure model substantially, which is the point at which the two sub-niches diverge — an OEM can do this far better than a third party and should.

## Target Customer
Equipment manufacturers with large service businesses, commercial service providers with contract portfolios, and the enterprise field service vendors whose contract modules currently administer rather than analyse.

## Impact If Built
Repricing a contract portfolio against modelled cost rather than against last year's price typically moves several points of service margin, and service margin is frequently the majority of an equipment manufacturer's profit. The risk-ranked portfolio view also redirects reliability and design attention toward the machines that actually consume service cost, which is a feedback loop most manufacturers do not have.
