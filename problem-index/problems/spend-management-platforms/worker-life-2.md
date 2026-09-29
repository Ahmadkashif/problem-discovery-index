# The Credit Analyst Setting Limits on Twelve Months of History

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Type:** Worker Life Changing
**One-liner:** Analysts extend corporate card limits to companies with almost no credit history, from bank balances and a pitch deck, and find out whether they were right in collections.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #causal-inference #confidence-intervals #evaluation-metrics #worker-facing #revenue-impact

## The Problem
A company applies for a corporate card. It is three years old, venture-funded or bootstrapped, with no meaningful commercial credit file. Traditional underwriting has nothing to work with.

So the analyst uses what exists: bank balances and cashflow through a connected account, revenue from a payment processor if the company shares it, burn rate, runway, the funding round if there was one, and the industry. They set a limit — often a multiple of the balance, adjusted — and it is revisited on a schedule or when the customer asks for more.

The customer requests increases constantly, usually at the least convenient moments: a hiring push, a marketing campaign, an annual software renewal. Each request is a judgement made quickly with partial information.

The signal that matters is the trajectory. A company burning faster than it is growing is a different risk at the same balance than one converging to profitability, and the bank feed shows this clearly. It is read by a person looking at a chart.

Outcomes arrive late and elsewhere. A customer that fails to pay becomes a collections matter; a customer that quietly winds down stops spending and churns. Neither event is systematically joined back to the underwriting decision that set the limit, so the analyst never learns the distribution of their own accuracy.

## Why It Matters to the Worker
The role carries real loss authority with limited tooling. An analyst setting limits across hundreds of companies is making credit decisions that determine the platform's loss rate, from a dashboard and a spreadsheet.

The pressure is directional. Sales and customer success want higher limits, customers want higher limits, and the analyst is the only party arguing for less. Saying no is the whole job's social position.

Volume grows with the customer base while the signal per customer stays thin, so the time available per decision shrinks.

And there is no feedback. Without the join between decisions and outcomes, an analyst cannot tell whether their judgement is good, which means they cannot improve deliberately and cannot demonstrate their value with anything but an aggregate loss number that reflects a hundred other things.

## What a Solution Looks Like
Cashflow trajectory modelled rather than eyeballed. Burn, runway, revenue growth, seasonality and their interaction are a forecasting problem with a clear target, and the platform holds daily bank data across thousands of companies.

Distress prediction with lead time. Companies in trouble change their spending before they miss a payment — vendor mix shifts, renewals lapse, payroll timing changes, discretionary categories collapse. Those patterns are visible in the platform's own transaction data and are a far earlier signal than a balance decline.

Cross-customer base rates. The platform has watched thousands of companies at this stage with these characteristics; what fraction of them failed within a year is knowable, and it is the context an analyst most lacks when looking at a single company.

Limits as a continuous function rather than a periodic review. The data updates daily; the limit changes quarterly. Automating within guardrails removes most of the request queue and makes limits responsive in both directions.

The decision-outcome join. Every limit decision, its rationale, and what happened over the following eighteen months — assembled once, this gives the function the accuracy measurement it has never had.

## Impact If Solved
Credit performance determines whether an interchange-funded business model works, and it is currently managed by analysts reading charts without feedback. Modelling trajectory, predicting distress from spending pattern changes and closing the decision-outcome loop turns limit setting into a measured function and gives the analyst the evidence to hold a line that is currently defended by instinct alone.
