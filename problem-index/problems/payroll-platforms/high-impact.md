# Multi-Jurisdiction Tax Determination and Filing

**Industry:** [[payroll-platforms|Payroll Platforms]]
**Type:** High Impact
**One-liner:** Eleven thousand taxing jurisdictions with independently changing rates, wage bases, reciprocity rules and filing formats — determined correctly for every employee every pay period, and verified before the money moves rather than after a notice arrives.
**Tags:** #large-language-models #bert #transformers #change-point-detection #gradient-boosting #hypothesis-testing #evaluation-metrics #compliance #revenue-impact

## The Problem
Withholding the right tax for one employee requires knowing where they live, where they work, whether those jurisdictions have a reciprocity agreement, which local income taxes apply and at what rate, what the state unemployment wage base is this year for this employer's rate class, which deposit schedule the employer is on, and what filing format each agency expects.

Multiply by every employee, every pay period, across more than eleven thousand jurisdictions that change rates annually and rules unpredictably. Remote work made this dramatically worse: employers who previously operated in one state now have employees in twenty, several of which have local income taxes, and the employer has no idea it has created a nexus obligation.

Errors are expensive in an asymmetric way. Under-withholding is discovered months later, often at year end, and the employer owes the tax plus penalties and interest while the employee faces an unexpected bill. Over-withholding takes money from people who needed it. Mis-filed returns generate agency notices, and resolving a notice takes months of correspondence.

The providers do this remarkably well, and they do it by maintaining large tax research teams who read agency bulletins and update rate tables. That is the moat, and it is a reading operation.

## Why It's Unsolved
The jurisdictions do not cooperate. There is no machine-readable feed of US payroll tax rates. Agencies publish rate changes as PDFs, as web page updates, as mailed notices to employers, and occasionally not at all until a rate is applied. Local jurisdictions are the worst — a municipality may adopt an income tax with minimal publication.

The employer-specific dimension compounds it. State unemployment rates are assigned per employer annually and arrive by mail. Deposit schedules depend on prior-period liability. Neither is knowable from a rate table; both must be captured from documents the employer receives and frequently misplaces.

Verification is the deeper gap. The industry checks its calculations against its own rate tables, which means a wrong table produces confidently wrong withholding across every affected employee until an agency notice arrives. There is no independent check.

And nexus determination — whether an employer has an obligation in a jurisdiction at all — is a legal judgement that depends on facts the payroll system holds but is not asked to reason about.

## What a Solution Looks Like
Rate change monitoring as a detection problem rather than a reading assignment. Agency publications, municipal code and bulletin feeds crawled continuously, changes extracted into structured rate records, and every change flagged against the current table for analyst verification. The research team's job becomes confirming rather than discovering.

Employer-specific document capture: the state unemployment rate notice and deposit schedule change photographed or forwarded, extracted, and applied — rather than typed by whoever opened the envelope.

Independent verification before money moves. Withholding computed for a pay run can be checked for statistical anomalies against the same employees' prior periods and against comparable employees in the same jurisdiction across the provider's whole base. A rate table error shows up immediately as a population-wide shift, which is detectable in seconds and currently detected by an agency months later.

Nexus alerts from the platform's own address data: this employee's work location has created an obligation the employer has not registered for.

## Impact If Solved
Tax accuracy is the entire product, and it is currently protected by a reading operation and no independent check. Detection of rate changes and anomaly verification before disbursement converts the category's largest liability from a discovered error into a prevented one — and the anomaly check rests on a cross-employer base only the providers have.
