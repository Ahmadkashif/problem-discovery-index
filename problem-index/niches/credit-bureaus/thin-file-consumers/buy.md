# Open-Banking Aggregation Adapted to FCRA-Grade Reporting

**Niche:** [[niches/credit-bureaus/thin-file-consumers/profile|Thin-File & Credit-Invisible Consumers]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bank-data aggregators move transactions; a consumer report built from them must meet accuracy, dispute and adverse-action duties that aggregation was never designed for.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #compliance #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get rent, utility, telecom or cash-flow data into the lender's production underwriting model rather than a side score, and whoever clears the lender's model validation and fair-lending review first takes the account.

## The Problem
Once cash-flow attributes are used for credit decisions, the provider is a consumer reporting agency, as Plaid recognised by setting up Plaid Check as a separate FCRA entity. Transaction categorisation errors become report inaccuracies, consumers can dispute them, and lenders need adverse-action reasons derived from the attributes.

## What Already Exists
Open-banking aggregators and transaction categorisation engines, used for account verification, personal finance and payments.

## The Customization Gap
The adaptation needs: income and obligation attributes with documented definitions and accuracy measured against ground truth; a dispute path for a consumer who says a deposit is not income; reason codes mapped to cash-flow features; retention and permissible-purpose controls per consent; and versioned attribute definitions so a lender's model does not drift when the categoriser is retrained.

## Target Customer
Aggregators and fintech CRAs moving into underwriting data; lenders' compliance teams evaluating them.

## Impact If Solved
Cash-flow data that meets the same obligations as a bureau file, which is what a lender needs before putting it inside a production model.
