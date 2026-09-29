# Build: Change Detection and Regression Coverage Across Sixty Regimes

**Niche:** [[niches/remote-work-infrastructure/multi-country-payroll/profile|Multi-Country Payroll Engine]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Detect legislative changes automatically, maintain a regression suite per jurisdiction, and check every payroll run against independent expectations before it pays.
**Tags:** #compliance #large-language-models #change-point-detection #evaluation-metrics #confidence-intervals #cross-validation #automation #descriptive-statistics
**Contested on:** Whether payroll rule changes across dozens of jurisdictions can be detected before they produce a wrong payslip.

## The Problem

Payroll correctness across sixty countries is maintained by people reading. A compliance specialist notices a contribution ceiling changed, writes a specification, an engineer implements it, and it ships — if the specialist read the right thing in time.

The failure modes are all quiet. A change nobody noticed produces systematically wrong calculations until an authority or a worker raises it, by which point several months of payrolls are wrong and the correction is a project. A change implemented in one country breaks an edge case in shared code that no test covers. An interaction between two rules — a benefit's tax treatment against a contribution ceiling — is wrong for a small number of workers and nobody looks.

Each of these is detectable and most are not detected.

## What to Build

Monitoring, regression coverage and pre-payment checking.

**Monitor the sources automatically.** Government gazettes, tax authority publications, statutory instrument feeds and social security agency announcements per jurisdiction, monitored continuously, with a model reading them for payroll-relevant changes and routing them to the specialist for that country. This does not replace the specialist; it stops them having to find the change.

**Track the change through to shipped.** Detected, specified, implemented, tested, deployed, effective date — as a pipeline with an owner and a due date driven by the change's own effective date. A missed change is currently invisible until it is wrong; here it is an overdue item.

**Build a regression suite per jurisdiction.** Golden cases covering the ordinary payroll plus the edge cases — ceiling boundaries, part-month starts and leavers, multiple benefit interactions, bonus periods, thirteenth-month timing, statutory leave accrual at year end. Every change runs against every country's suite, so a fix in one place cannot silently break another.

**Check every run before it pays.** Independent expectations per worker — the period-on-period delta, the implied effective tax rate against the jurisdiction's band, the contribution amounts against the ceiling, the net against a rough independent calculation. Anything outside tolerance holds for review. This is the control that turns an undetected systematic error into a held payment, and it is cheap.

**Reconcile against filings.** What was calculated against what was declared and paid to the authority, per period, per country. A discrepancy is either a payroll error or a filing error and both matter.

**Track the errors.** Corrections issued, their cause, the period affected and the worker count, by jurisdiction. This is the quality record of the payroll function and it is the basis for deciding where to invest.

## Target Customer

Platform payroll engineering and compliance leadership, for whom correctness across a growing jurisdiction count is the operational risk that scales worst with expansion. Also the local payroll partners these platforms integrate, who face the same problem within their markets.

## Impact If Built

Legislative changes are detected rather than found, with a tracked path from detection to deployment. A change in one country cannot silently break another. And every payroll run is checked against independent expectations before it pays, which converts the industry's characteristic quiet systematic error into a held payment and a review.
