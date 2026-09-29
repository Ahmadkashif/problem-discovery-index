# Reconciliation and Pipeline Controls for the Time Feed

**Niche:** [[niches/payroll-platforms/wage-calculation-time-integration/profile|Wage Calculation & Time Integration]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data pipeline monitoring and reconciliation are free, mature disciplines, and the hours feed that determines what tens of millions of people are paid arrives on a Thursday with no volume check.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
The time feed transfers on Thursday morning with 3,140 employee records instead of the usual 3,400, because a location's data failed to sync and the export completed without it. The payroll runs. Two hundred and sixty people are paid nothing or are paid a default, and they discover it on Friday. A volume comparison against the previous period would have caught it in under a second, and volume checks have been standard data engineering practice for a decade.

## What Already Exists
Data observability tooling — freshness, volume, distribution, schema and null-rate checks with alerting — is mature and largely free. Reconciliation practice from financial operations applies directly, as the benefits carrier niche describes. Workflow orchestration with dependency and deadline management is commodity. Every component required to monitor the time-to-payroll feed is standard infrastructure and is not applied to a pipeline whose failure means people are not paid.

## The Customization Gap
The adaptation is to a pipeline with a hard external deadline and a severe failure consequence. It requires: (1) expectation derived from the employer's own roster rather than from the previous file, so that a headcount change is distinguished from a missing location and both are correct — comparing to last period alone gives false alarms in a growing workforce; (2) per-employee completeness rather than aggregate volume, since the employees missing from a feed are a list and should be presented as one; (3) deadline-aware alerting that fires early enough to act, which means monitoring the upstream approval process rather than the file arrival — a feed that will be incomplete is predictable days before it transfers; (4) distributional checks on hours as well as counts, because the second most common failure is hours present and wrong — a location's clock configuration change that halves recorded hours passes every volume check; and (5) alerting to the payroll practitioner in payroll terms, since they are the person who can act and an integration alert reaches an engineer who cannot.

## Target Customer
Payroll providers, time and attendance vendors, and large employers running the integration themselves.

## Impact If Solved
The controls are free and the failure they prevent is a person not being paid, which is the most consequential routine failure in enterprise software. Per-employee completeness against the roster is the specific adaptation, and monitoring the approval process rather than the file is what moves detection from Thursday afternoon to Tuesday.
