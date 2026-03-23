# Alternative Data Credit Assessment for Thin-File Members

**Niche:** [[niches/credit-unions/underbanked-community-cus/profile|Underbanked Community CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A credit assessment model that evaluates thin-file and no-file members using non-traditional data — utility payment history, rent consistency, phone bill patterns, and CU account behavior — giving underbanked individuals access to affordable credit without requiring a FICO score.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #worker-facing

## The Problem
An underbanked member walks into a community CU with no credit score, no recent bank statements, and a pay-as-you-go phone. Traditional underwriting rejects them outright — no score means no loan. They walk across the street to a payday lender that charges 400% APR. The CU has a mission to serve this person but no risk assessment framework that works without bureau data. Loan officers at underbanked-serving CUs develop informal judgment for these members: "she's paid her share account $50 every two weeks for 8 months — she's reliable." But this judgment isn't systematic, isn't auditable, and doesn't scale.

## Why Nobody Has Built This
Fintech alternative credit scoring companies (Upstart, Nova Credit, Petal) target thin-file consumers through DTC lending, not CU lending workflows. Their models are proprietary and their integration requires minimum volume that small CUs can't meet. Building alternative data models requires data sources (utility companies, rent payment processors, telecom providers) that are fragmented and don't offer standardized APIs for credit unions. Fair lending compliance is especially complex — alternative data models must be rigorously tested for disparate impact on protected classes, a validation process that exceeds the capability of small CUs.

## What to Build
A credit assessment model designed for CU deployment that uses: (1) member account behavior (deposit consistency, balance stability, savings growth pattern, overdraft frequency); (2) self-reported bill payment data (utility, rent, phone) verified through bank transaction categorization; (3) employment stability indicators from payroll deposit patterns; (4) CU relationship tenure and engagement signals. The model produces a risk score comparable to FICO in predictive power for the thin-file population, with full explainability for loan officer review and fair lending audit compliance. Deployed as a CU-controlled model (not a third-party score) to maintain the credit union's control over lending decisions.

## Target Customer
CEOs and lending officers at CUs serving underbanked communities who want to extend affordable credit to thin-file members without relying on FICO scores or third-party fintech lending platforms.

## Impact If Built
Enables credit access for 30-50% of applicants currently auto-declined for no score, generating $500K-$2M in new annual loan origination per institution. Diverts members from 300-600% APR payday loans to 18-28% APR CU products — saving each member $500-$2,000 annually in interest costs. Provides an auditable, fair-lending-compliant alternative to subjective loan officer judgment for thin-file applications.
