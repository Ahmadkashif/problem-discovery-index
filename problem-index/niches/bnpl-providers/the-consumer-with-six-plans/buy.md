# Account Aggregation Practice

**Niche:** [[niches/bnpl-providers/the-consumer-with-six-plans/profile|The Consumer With Six Plans]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Open banking and account aggregation gave consumers a combined view of their finances, and instalment obligations are the one thing it does not show properly.
**Tags:** #data-integration #compliance #time-series-forecasting #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to give a consumer a view of what they have actually committed to across providers — and whoever does that serves the only party who could see all of it and has no tool for it.

## The Problem
Account aggregation is established infrastructure. Consumers can connect their accounts, see balances and transactions in one place, and a category of personal finance products is built on it. The technical mechanisms, the consent frameworks and the categorisation pipelines all exist. Instalment obligations pass through as debit card payments to a merchant-like counterparty, are categorised inconsistently, and are not represented as future commitments — so the one financial obligation most likely to cause a consumer difficulty is the one the aggregation shows least well.

## What Already Exists
Account aggregation infrastructure and consent frameworks; transaction categorisation pipelines; personal financial management products built on them; recurring payment detection; and balance and cash flow visualisation.

## The Customization Gap
The adaptation is to an obligation that is a schedule rather than a transaction. It requires: (1) representing future committed payments rather than past transactions, since the harm comes from what is due and aggregation models what has happened — this forward-looking obligation model is the substantive addition; (2) detecting instalment payments reliably in transaction data, which is a categorisation problem complicated by providers appearing under varying descriptors; (3) obtaining the full schedule rather than inferring it, which requires either provider access or extrapolation from the payments seen so far; (4) a consumer population less likely to use financial management apps, so the product must reach them differently; and (5) an intervention layer, since showing the position is only useful if something can be done about it.

## Target Customer
Consumer finance and budgeting vendors, banks, open banking infrastructure providers, and instalment providers willing to serve the whole relationship.

## Impact If Solved
Aggregation gave consumers a combined view and the obligation most likely to cause difficulty is the one it represents worst. Modelling future committed payments rather than past transactions is the addition, and it is what makes the view actionable.
