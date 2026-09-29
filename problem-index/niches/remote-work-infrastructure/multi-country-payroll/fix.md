# Fix: The Error Is Found When the Worker Notices

**Niche:** [[niches/remote-work-infrastructure/multi-country-payroll/profile|Multi-Country Payroll Engine]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** A contribution was calculated on the wrong base for eight months and the first person to notice was an employee reading their own payslip.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #change-point-detection #compliance #cross-validation #quick-win #automation
**Contested on:** Whether payroll output will be checked against expectations before it is paid.

## The Problem

Payroll errors in this setting are usually systematic and quiet. A contribution ceiling not updated, a benefit taxed under the wrong treatment, a leave accrual rate stale after a legislative change — applied consistently to everyone in that jurisdiction, for months.

Nothing detects them. The payroll runs, the payments go out, the filings are made. The error surfaces when a worker reads their payslip carefully and asks, or when an authority reconciles, and by then eight months of payrolls are wrong for every worker in that country.

The checks that would catch it are simple. A worker's net pay changing by an implausible amount period on period. An effective tax rate outside the jurisdiction's possible range. A contribution above its statutory ceiling. A total that does not reconcile against an independent recomputation. All computable before the payment leaves.

## Why It's Still Broken

Payroll is built to execute and the quality assurance is the test suite at development time rather than a check on the output at run time. Once a calculation ships it is trusted.

The systematic errors are also invisible to a per-worker eye. Everyone in the country is wrong by the same amount in the same direction, so nothing looks anomalous relative to anything else — which is precisely why a check against an external expectation rather than against the population is what is needed.

And the correction is expensive, so there is a quiet incentive not to look too hard.

## What a Fix Looks Like

Check the output before it pays. All of it is arithmetic.

Compute a small set of independent expectations per worker per run: period-on-period net change against expected change given known inputs, effective tax rate against the jurisdiction's band range, each contribution against its ceiling and base rules, employer cost ratio against the jurisdiction's typical range. Hold anything outside tolerance.

Check the country aggregate too. Total tax, total contributions and total net for a country, period on period, adjusted for headcount and salary changes. A systematic error moves the aggregate, which is the only place it is visible.

Reconcile against filings every period. What was calculated, what was declared, what was paid. A three-way match, per country, per period. Discrepancies are either payroll errors or filing errors and both need finding in the month rather than the year.

Watch the effective dates. A rule with a known effective date that has passed and whose implementation has not shipped is an error waiting to happen, and it is a due-date query over the change pipeline.

Make it easy for workers to query. A payslip explanation showing how each line was computed, and a route to ask, with the query routed to payroll rather than to support. Workers are currently the detection mechanism and they are given no tools.

And track corrections by cause. Which errors happened, why, how long they ran and how many people they affected — the quality record that says where the next investment should go.

## Who Feels the Pain

Workers, underpaid or overpaid for months in a country whose rules they do not know, and the ones who notice carrying the burden of raising it. Clients, whose statutory position was wrong for eight months. Authorities, receiving incorrect filings. And the platform, whose correction project is far more expensive than the check would have been.

## Impact If Fixed

Systematic errors get held before payment rather than discovered by a worker eight months later. The country aggregate check — the only place a uniform error is visible — gets computed. And the correction burden, which is the most expensive thing that happens in a payroll operation, falls substantially.
