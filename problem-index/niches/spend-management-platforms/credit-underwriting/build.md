# Underwriting That Sees the Outcome

**Niche:** [[niches/spend-management-platforms/credit-underwriting/profile|Credit Underwriting]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model sets the limit, the loss lands in collections months later, and the two have never been introduced.
**Tags:** #gradient-boosting #survival-analysis #change-point-detection #evaluation-metrics #confidence-intervals #time-series-forecasting #revenue-impact #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to set a corporate card limit for a company with twelve months of history and no credit file — and whoever joins the limit decision to what happened afterwards underwrites a book everyone else is guessing at.

## The Problem
An analyst or a model sets a limit from bank balances, revenue trajectory and whatever else is available. The customer spends against it. Some months later they stop paying, or they burn down their runway and shut, or they thrive. That outcome is recorded in collections and in churn, both of which sit outside the credit function's loop. The underwriting model is therefore trained on whatever was available at build time and has not learned from a single account since, in a business where the loss rate determines whether the interchange model works.

## Why Nobody Has Built This
Collections was built as a recovery operation, so its data structure serves recovery rather than model feedback — and the join between a limit decision and an eventual loss was nobody's deliverable. Growth pressure rewards approving quickly. The book is young enough that loss rates have looked manageable. And the daily spending signal, which is the platform's real advantage, was collected for ledger coding rather than for risk.

## What to Build
Close the loop and use the daily signal. Join every limit decision to its eventual outcome — repayment, delinquency, write-off, churn, survival — which is the core and is the feedback loop the credit function has been operating without. Use spending behaviour as a continuous risk signal, since a company whose spend pattern changes is signalling something weeks before a missed payment and no other lender can see it. Detect distress early from the combination of balance trajectory, spend composition and payment behaviour, because that combination is unique to this vantage point. Revisit limits continuously rather than at signup, as a limit set on twelve months of history is stale in six. Model survival rather than only default, since a customer who shuts down is the dominant loss mode in this segment and traditional credit modelling is not shaped for it. Segment performance by sector, stage and vintage, which will reveal that the aggregate loss rate conceals wide variation. Measure underwriting accuracy as a reported metric, since a credit function with no performance measure is a growth function. Use the exception and policy data as an additional signal, because how a company manages its own spend says something about how it is run. Feed early warnings to customer success as well as to collections, as intervening before distress is better for both parties. And stress the book against a downturn, since the portfolio has largely not seen one.

## Target Customer
Credit and risk leadership, boards assessing the credit book, capital providers funding it, and commercial credit vendors with no access to daily spending behaviour.

## Impact If Built
Collections was built for recovery, so the join between a limit decision and its loss was nobody's deliverable. Daily spend and balance behaviour is the earliest distress signal any lender to this segment could have, and it is being collected for ledger coding.
