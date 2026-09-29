# Verification Before the Money Moves

**Niche:** [[niches/payroll-platforms/payroll-tax-content-filing/profile|Payroll Tax Content & Filing]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A payroll tax error is discovered when an agency notice arrives, which is months after the money moved and after employees have been under-withheld all year, and the check that would have caught it is computable in the seconds before disbursement.
**Tags:** #hypothesis-testing #change-point-detection #descriptive-statistics #confidence-intervals #evaluation-metrics #compliance #automation #data-integration
**Contested on:** Every serious competitor in payroll is fighting to determine the correct taxing jurisdictions, rates and rules for every employee every period and verify them before the money moves — and whoever catches an error pre-disbursement rather than pre-notice takes the account.

## The Problem
An employee moved to a municipality with a local income tax. Their address was updated in the HR system and the work location was not, so the local tax was never withheld. The payroll ran correctly according to its configuration for eleven months. A notice arrives from the municipality. The employer owes the tax, penalties and interest, the employee owes eleven months of tax they did not budget for, and correcting it requires amended filings across three quarters. Every pay period in that sequence was an opportunity to notice that an employee with an address in a taxing municipality had no local tax withheld — which is a check, not a model.

## Why Nobody Has Built This
Payroll systems are built for correctness of execution rather than for verification of configuration: the engine applies the rules it is given, faithfully, and there has never been a layer that asks whether the rules it was given are the right ones for this employee. The feedback loop is agency notices, which are slow, which means the industry has calibrated its quality processes around a months-long detection latency and built reconciliation capability rather than prevention. And the pre-disbursement window is short and the run is sacred, so adding a check that could block a payroll is a product risk nobody has wanted to take — which is addressable by designing the check to flag rather than to block.

## What to Build
A pre-disbursement verification layer that checks the run against expectations rather than recomputing it. Jurisdiction expectation per employee derived independently from their residence and work location against boundary data, compared to the jurisdictions actually applied — which catches the missing local tax, the wrong reciprocity treatment and the stale work location. Period-over-period distributional checks per employee and per jurisdiction, since most errors show as a discontinuity: a tax that stopped, a rate that changed, a wage base that was hit early. Aggregate reconciliation against expected liability by jurisdiction before remittance rather than after. Anything anomalous is flagged with the specific employees and the magnitude, surfaced to the payroll practitioner in the pre-run review that already exists, and never silently blocks a run. The measured outcome is the share of errors caught pre-disbursement rather than by notice, which is the number this niche is contested on and which no provider currently reports.

## Target Customer
Payroll providers of every size, payroll tax content and filing specialists, and the large employers running payroll in house.

## Impact If Built
Catching an error before disbursement rather than at a notice changes the remedy from an amended filing and an employee tax surprise into a correction on the pre-run report. The employee-side consequence is the one that matters most: an under-withheld employee discovers at tax time that they owe money because of an employer configuration error, which is a household financial event caused entirely by a check nobody ran.
