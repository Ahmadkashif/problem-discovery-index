# Rent Setting Without Pooled Competitor Data

**Industry:** [[proptech-platforms|Proptech Platforms]]
**Type:** High Impact
**One-liner:** Price a unit from what one operator legitimately knows — its own enquiry volume, application conversion, renewal acceptance and vacancy cost — rather than from non-public prices contributed by competing landlords.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #time-series-forecasting #feature-engineering #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact

## The Problem
Setting rent is the highest-consequence recurring decision in rental housing. Price above the market and the unit sits vacant, costing a month's rent for every month it is empty plus the turnover expense already incurred. Price below and the operator gives away margin on a twelve-month commitment. The decision is made unit by unit, weekly, across millions of units.

The industry's answer for two decades has been revenue management software that recommends a price from pooled data — including, in the litigated cases, non-public current and future pricing contributed by competing landlords in the same submarket. That architecture is now the subject of federal and state antitrust action and private litigation, and several jurisdictions have banned it outright.

What that leaves is a real and unsolved problem. Operators still have to set rents. Many have reverted to the pre-software method: a leasing manager looks at a handful of competitor listings on public sites, applies judgement, and sets a number. That is worse than the software was, and it is also not obviously legal to do systematically at scale in a coordinated way.

The interesting question is what a single operator can do with only its own data plus genuinely public information — and the answer is a great deal more than the industry currently does, because nobody has tried.

## Why It's Unsolved
The pooled-data approach was easier and it worked, so the harder single-operator problem was never attacked. Building a demand model from one portfolio's own signals requires actual modelling; reading competitors' prices requires only a data-sharing agreement.

The single-operator problem is genuinely harder in a specific way: price experimentation is limited. An operator cannot randomise rents across identical units without a fairness problem and, in some jurisdictions, a legal one. Without variation, estimating a demand curve is difficult, and the observational data is heavily confounded because prices were set in response to the same conditions that drove demand.

The signals that would substitute for competitor prices are also under-collected. Enquiry volume per listing, tour bookings, application starts and abandonments, and the price at which a prospect stopped responding are the operator's own demand curve, and most platforms record only the leases that closed.

And there is now a chilling effect that goes beyond what the law requires. Legal departments, understandably cautious, have restricted analytical work broadly rather than precisely, which has slowed the development of exactly the approach that would resolve the problem.

## What a Solution Looks Like
A demand model per property built from that operator's own funnel. Enquiry volume, tour conversion, application rate and time-to-lease at each price point, over time, form a within-property demand curve that requires no competitor data at all. Public listing data — asking rents that anyone can see — provides market context legitimately.

Renewals are the larger and cleaner opportunity. A renewal offer is a price, the resident's acceptance or departure is the outcome, and the operator has thousands of these with no competitor input required. The trade-off between a renewal increase and the full cost of turnover — vacancy days, make-ready, leasing cost, concession — is computable per unit and is currently approximated by a portfolio-wide rule of thumb.

Where experimentation is possible, it should be small, disclosed and used to identify the demand curve properly rather than to extract from individuals.

## Impact If Solved
Rent setting drives the entire economics of rental housing and the industry's dominant method is under legal challenge, leaving a large, sophisticated market with no defensible technique. A single-operator approach is both lawful on its face and, for renewals in particular, likely more accurate — because the operator's own residents are the population being priced.
