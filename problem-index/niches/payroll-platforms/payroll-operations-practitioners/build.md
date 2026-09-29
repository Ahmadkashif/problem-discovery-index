# Assurance Rather Than a Register

**Niche:** [[niches/payroll-platforms/payroll-operations-practitioners/profile|Payroll Operations Practitioners]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A payroll practitioner reviews a register before submitting because nothing in the system tells them the run is sound, so the final control on tens of millions of dollars of wages is a person scanning columns for anything that looks unusual.
**Tags:** #change-point-detection #hypothesis-testing #descriptive-statistics #confidence-intervals #evaluation-metrics #automation #worker-facing #compliance
**Contested on:** Every serious competitor building for payroll practitioners is fighting to replace a close run on memory and checklists with a process that surfaces what needs attention — and whoever the practitioners trust to tell them what is wrong takes the account.

## The Problem
The register is three hundred pages. The practitioner scrolls it, looking for anything that stands out: a net pay of zero, an unusually large gross, a negative deduction, a location with fewer employees than expected, a tax that stopped. They are good at this and they miss things, because scanning three hundred pages for anomalies is a task humans perform poorly and computers perform perfectly. What they are actually doing is anomaly detection by eye, on a deadline, as the last control before money moves.

## Why Nobody Has Built This
Pre-run reporting was built as a report because that is what the practitioner asked for, and it has been incrementally improved as a report ever since. Nobody reframed it as a set of assertions. There is also a subtle trust problem: a practitioner who has been burned will not stop reviewing the register because a system says it is fine, so the product has to earn trust by finding things the practitioner would have found and by being explicit about what it has and has not checked — which is a design requirement that a report does not have.

## What to Build
A pre-run assurance layer that states what it checked and what it found. Per-employee period-over-period variance with the expected explanation attached, so a large change that is fully explained by a bonus is not flagged and one that is not is. Population-level checks: headcount against the roster, hours distribution against the prior period and against the same period last year, tax and deduction totals against expectation per jurisdiction, net-to-gross ratios by population. Structural checks: zero or negative nets, employees with no tax in a taxing jurisdiction, terminated employees with pay, new hires without setup, deductions exceeding limits. Each check reports pass, fail, or not applicable, with the affected employees and the magnitude — and the honest list of what is not covered, which is what allows a practitioner to review the residual rather than everything. Trust is built by measuring the checks against what practitioners actually catch, reported openly. The outcome is that the practitioner reviews twelve exceptions rather than three hundred pages.

## Target Customer
Payroll providers, employers running in-house payroll, and the payroll service bureaux whose staff perform this review across many clients.

## Impact If Built
The final control on wage disbursement is currently a person scanning for anomalies under time pressure, which is the wrong tool for the task. Converting it into a set of explicit checks with a stated coverage boundary both improves the control and changes the working experience of a profession whose defining characteristic is anxiety about what it might have missed.
