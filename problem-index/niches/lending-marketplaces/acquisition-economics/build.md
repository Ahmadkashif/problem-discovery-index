# Bidding on Expected Funded Value

**Niche:** [[niches/lending-marketplaces/acquisition-economics/profile|Acquisition Economics]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bid is set on the probability of a form submission when the thing being bought is a borrower who will eventually be funded.
**Tags:** #gradient-boosting #evaluation-metrics #revenue-impact #confidence-intervals #logistic-regression #causal-inference #time-series-forecasting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to bid on a borrower's expected funded value rather than on their click probability — and whoever gets the funded signal into the bid takes the traffic everyone else is overpaying for.

## The Problem
A click from a borrower with a strong profile seeking a large loan in a state well served by high-bidding lenders is worth many times a click from a borrower who will be declined everywhere. The bidding system treats them as the same event, because the conversion it reports is the form submission. The consequence is systematic overpayment for low-value traffic and underbidding on the segments that actually fund, in a business where acquisition is most of the cost base.

## Why Nobody Has Built This
The conversion signal available to the ad platform ends at the form, so bidding was built around it — and no downstream value was ever fed back because the funded outcome lives in a different system and, for many lenders, does not exist at all. Value prediction requires the outcome data the routing problem is also missing. Marketing is measured on cost per lead, which the current setup optimises perfectly. And the two teams do not share a target.

## What to Build
Predict the value and bid on it. Model expected funded value at the moment of the click from the query, channel, geography, device and whatever profile signal exists, which is the core and is what turns a uniform bid into an informed one. Feed funded outcomes back as conversion values to the ad platforms, since they support value-based bidding and are currently being fed a constant. Use the routing layer's approval predictions as the value estimate where funded data is thin, which links the two problems and makes each more valuable. Measure channel quality by funded rate rather than by lead volume, because channels differ enormously and the difference is currently invisible. Attribute value by segment rather than by campaign average, as the average conceals the variation that the bidding should exploit. Handle the delay between click and funding, since the signal arrives weeks later and the bidding needs an estimate now. Distinguish borrowers who will fund somewhere from those who will fund with a high-bidding lender, because both matter and they are different. Reconcile organic and paid against the same value measure, as they are currently evaluated on incompatible terms. Run holdouts to establish incremental value, since much paid traffic is buying borrowers who would have arrived anyway. And report cost per funded loan as the headline metric, which is the number that makes every other decision correct.

## Target Customer
Performance marketing and finance leadership, data teams bridging routing and acquisition, and bid management vendors feeding constant conversion values.

## Impact If Built
The ad platform's conversion signal ends at the form, so bidding was built around it and no downstream value ever came back. Predicting funded value at the click turns the largest cost in the business from uniform bidding into an informed one.
