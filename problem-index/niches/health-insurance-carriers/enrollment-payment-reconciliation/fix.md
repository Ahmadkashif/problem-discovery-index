# The Retroactive Termination Nobody Recovered

**Niche:** [[niches/health-insurance-carriers/enrollment-payment-reconciliation/profile|Enrollment & CMS Payment Reconciliation]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A state or CMS terminates a member retroactively, recovers the capitation, and the claims the plan paid for those months stay paid.
**Tags:** #data-integration #workflow-orchestration #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to reconcile every member's enrollment, premium and subsidy record against CMS's, the exchanges' and the states' monthly files before the payment cycle closes, and whoever leaves the fewest unpaid or clawed-back member-months takes the account.

## The Problem
Eligibility losses, deaths, moves and Medicaid redeterminations arrive weeks or months late. The payer recovers its payment for the retroactive months. The plan has meanwhile paid claims for those months, and providers can often be billed back only within a limited window (recalled).

## Why It's Still Broken
Enrolment processes the termination, claims never hears about it, and the recovery opportunity expires while the two departments reconcile separately.

## What a Fix Looks Like
On every retroactive termination, automatically identify claims paid for the affected months, route them for recovery or coordination with the member's new coverage within the provider-contract window, and report recovered against lost amounts each month.

## Who Feels the Pain
Finance teams writing off unrecoverable claims; payment integrity teams finding them too late; providers billed back after a long delay.

## Impact If Fixed
Recoveries made inside the window, cleaner books, and fewer surprise recoupments for providers.
