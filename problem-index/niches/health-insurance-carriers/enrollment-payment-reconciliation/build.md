# A Member-Month Ledger Reconciled Every Cycle

**Niche:** [[niches/health-insurance-carriers/enrollment-payment-reconciliation/profile|Enrollment & CMS Payment Reconciliation]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Plans reconcile enrolment against each payer's file as a monthly exercise, without a single ledger of what each member-month should have earned and why it did not.
**Tags:** #gradient-boosting #k-nearest-neighbors #feature-engineering #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to reconcile every member's enrollment, premium and subsidy record against CMS's, the exchanges' and the states' monthly files before the payment cycle closes, and whoever leaves the fewest unpaid or clawed-back member-months takes the account.

## The Problem
For each member and month, the plan expects a payment: a CMS amount set by risk score and status (institutional, dual, ESRD), a state capitation rate cell, or a subsidy plus premium. The payer's file says something else for thousands of members: wrong status, missing enrolment, a retroactive termination, a different rate cell. Analysts work the discrepancies by report, not by member, and the same root cause recurs every month.

## Why Nobody Has Built This
Each payer's reconciliation lives in a different team and tool, the expected amount is computed in finance, and the corrective transaction is sent from enrolment. Nobody owns the member-month.

## What to Build
A ledger keyed on member × month × payer, holding the expected payment, the received payment and the variance. A classifier assigns each variance a root cause learned from analysts' past resolutions (missing transaction, status mismatch, retro change, rate-cell error, death or move). Corrective transactions are generated where the rule is clear and queued with evidence where it is not. Recovery value is tracked against payers' retroactivity windows.

## Target Customer
Enrolment, billing and Medicare finance leaders at multi-line plans.

## Impact If Built
Fewer unpaid member-months, earlier detection of recurring errors, and a revenue figure finance can trust each month.
