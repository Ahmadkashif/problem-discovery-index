# Attrition Forecasting From the Signal Log

**Industry:** [[security-alarm-integrators|Security Alarm Integrators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Churn prediction is a solved problem in subscription software, but an alarm account announces its departure in panel signals, service tickets and fines that generic churn tools never see.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #revenue-impact #automation

## The Problem
An alarm company's balance sheet is its recurring monthly revenue, and that revenue leaks. ADT reported gross revenue attrition of 13.1% for 2025, rising quarter by quarter from 12.6% in the first quarter. Smaller dealers commonly run higher. Because accounts trade at a multiple of RMR (roughly 30–55× by advisers' estimates), a dealer that loses a ~$45-a-month account has lost about $1,350–2,500 of enterprise value, not $45 (estimate). Attrition comes from moves, non-payment, competitor takeovers, dissatisfaction after a false-alarm fine, and contracts that quietly reach term.

Retention teams work from lists: contracts ending in 90 days, accounts 60 days past due, cancellation requests already received. By the time an account is on any of those lists, the decision has usually been made.

## What Already Exists
Generic churn and customer-success platforms (Gainsight, Salesforce Einstein, ChurnZero) score subscription customers from product usage, support tickets and billing. Alarm billing systems such as SedonaOffice and Bold's billing modules track contracts, invoices and cancellations. Interactive platforms like Alarm.com report app engagement to dealers.

## The Customisation Gap
The alarm-specific signals live elsewhere. Some sit in the central-station log. A panel that stops arming has a householder who no longer uses it. Runaway low-battery and AC-loss troubles signal a neglected system. A burst of false alarms precedes a city fine, and a communicator that failed after a POTS cutover makes the system look broken. Others sit in the service system, such as repeat truck rolls for the same zone or an unresolved trouble. And some are external: a property listed for sale, a mover's change-of-address, a permit fine from the city's billing vendor. A useful model also needs alarm contract logic. That means the 36- to 60-month term and its auto-renewal and cancellation rules by state, and, for accounts bought through a dealer programme, the chargeback window during which the originating dealer replaces lost accounts. None of this maps onto a SaaS usage schema, and generic tools treat a silent panel as a happy customer.

## Impact If Solved
A model trained on a dealer's own signal, service and billing history that flags accounts 90–180 days before cancellation would give retention staff time to fix the system, waive a fine, convert the mover's new home or re-sign the contract. Moving gross attrition by a single point on a $359M-RMR book like ADT's is worth roughly $40M of annual revenue (estimate), and far more in portfolio value.
