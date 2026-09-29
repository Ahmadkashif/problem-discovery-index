# Configuration Checked Against the Law

**Niche:** [[niches/payroll-platforms/wage-calculation-time-integration/profile|Wage Calculation & Time Integration]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A payroll engine applies whatever earnings rules it is configured with, employers configure them from an understanding that may be wrong or stale, and nothing compares the configuration to the law in the places the employees actually work.
**Tags:** #bert #large-language-models #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #automation #descriptive-statistics
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An employer configures overtime at a weekly threshold, which is correct federally and incorrect in the states that also require daily overtime. It configures a shift differential as a flat addition, which is correct as a payment and incorrect as an input to the regular rate for overtime purposes. It treats a monthly production bonus as discretionary, which it is not. Each configuration is applied faithfully to every affected employee every period, and each is a wage underpayment that accumulates silently. The engine is working perfectly. Nobody has checked what it was told to do.

## Why Nobody Has Built This
Providers have drawn a clear line: the employer configures, the provider executes, and the liability follows the configuration — which is a defensible contractual position and is the reason the check does not exist. Performing the check means the provider asserting what the law requires, which is the same liability hesitancy that keeps small-landlord and screening products shipping templates. It also requires representing wage and hour rules in a form comparable to an earnings configuration, which nobody has built, and which is exactly the executable-content problem this vault keeps encountering.

## What to Build
Wage and hour rules as maintained executable content, and a continuous comparison against each employer's configuration per jurisdiction. Overtime thresholds and bases, regular rate composition, differential treatment, meal and rest premium obligations, and daily and consecutive-day rules encoded per jurisdiction with effective dates. Each employer's configured rules are compared against the applicable set for each employee's actual work location, and divergence is reported with the affected population, the effective date and the estimated underpayment — which is what converts a compliance finding into something that can be remediated properly rather than argued about. The provider's posture can remain that the employer configures; being told about a divergence before it accumulates is strictly better for the employer than discovering it in litigation, and both parties should want it. Where a rule requires interpretation, it routes to a human rather than being asserted.

## Target Customer
Payroll providers, payroll tax and compliance content vendors, professional employer organisations, and employers with multi-state hourly workforces.

## Impact If Built
Wage and hour underpayment is among the most litigated employment exposures and is overwhelmingly caused by configuration error rather than by intent, which makes it a detection problem with a clean answer. The affected employees are the ones who were underpaid, sometimes for years, and the comparison that would have found it runs against data both parties already hold.
