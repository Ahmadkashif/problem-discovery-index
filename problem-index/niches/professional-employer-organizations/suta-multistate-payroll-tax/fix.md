# Wage Bases Restarted When a Client Joins Mid-Year

**Niche:** [[niches/professional-employer-organizations/suta-multistate-payroll-tax/profile|Multi-State Payroll Tax & SUTA Account Administration]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** When a client moves to the PEO in June, its employees' unemployment wage bases often restart at zero under the PEO's account, and the client pays a second round of wage-based tax it did not owe.
**Tags:** #decision-trees #descriptive-statistics #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to report and pay unemployment tax under the right account and rate for every client in every state, whether the state wants PEO-level, client-level or hybrid reporting, and whoever closes each year with no rate-notice errors, misapplied wage bases or penalty notices takes the account.

## The Problem
Federal and state unemployment taxes apply only up to a wage base. Whether wages paid by the client's previous payroll count toward the base after a move to a PEO depends on the state's successor or common-paymaster rules and on the reporting regime. If the PEO restarts the base, the tax is overpaid. If it carries it over where the state does not allow it, the tax is underpaid and a notice follows.

## Why It's Still Broken
The rule varies by state and situation. Year-to-date wages from the prior provider arrive late or incomplete, and the decision is made employee by employee by an implementer under deadline.

## What a Fix Looks Like
A rule table per state for wage-base carryover in PEO transitions, applied automatically when year-to-date wages are loaded. Exceptions are flagged where documentation is missing, and a pre-quarter-end check finds employees whose taxable wages exceed what the rules allow.

## Who Feels the Pain
Client owners paying duplicate tax, payroll tax analysts processing refunds and amendments, and account managers explaining the credits.

## Impact If Fixed
Overpayments avoided at onboarding instead of refunded a year later, at almost no ongoing cost once the rule table exists.
