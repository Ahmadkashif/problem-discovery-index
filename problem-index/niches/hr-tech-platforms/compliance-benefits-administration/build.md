# Verification as a Standing Function

**Niche:** [[niches/hr-tech-platforms/compliance-benefits-administration/profile|Compliance & Benefits Administration]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** HR systems assert what an employee is entitled to and what coverage they hold, nothing ever checks either assertion against the world outside the system, and the error is discovered by the employee.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #data-integration #workflow-orchestration #automation #descriptive-statistics
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An HR system holds a configuration: accrual rates, eligibility rules, plan elections, dependent records. It applies that configuration faithfully and reports the results as fact. Whether the accrual rate matches the current ordinance in the city the employee actually works in, and whether the carrier's record of that employee's dependents matches the system's, are questions nothing in the stack asks. The system is internally consistent and externally unverified, and every failure in this niche takes that shape.

## Why Nobody Has Built This
Verification requires comparing the system's state to an external source — a statute, a carrier file, a regulator's published rule — which is work outside the system's boundary and outside the scope every vendor drew around its product. It also produces uncomfortable output: the first run of any such check finds errors, some of which have been running for years and have affected identifiable people, which creates an obligation to remediate. That is a good reason to build it and a reliable reason it does not get built.

## What to Build
A verification layer that runs continuously against external truth. For compliance, the configured rules for each employee's work jurisdiction are compared against maintained rule content, and a divergence is reported with the affected population and the effective date of the change — so an employer knows not only that it is wrong but since when and for whom. For benefits, the carrier's eligibility record is reconciled against the system of record on a cadence, with discrepancies itemised by employee rather than totalled. Both produce the same artefact: a list of specific people whose entitlement or coverage is not what the employer believes. Remediation workflow is part of the product, including the awkward part — notifying the affected employee, which is the correct thing to do and which no current product supports. The standing metric is the count of unverified assertions, which is the honest measure of how much of the system's output is currently taken on faith.

## Target Customer
HCM vendors, benefits administration platforms, employers with multi-jurisdiction workforces, and the brokers whose clients bear the consequences.

## Impact If Built
The failures this addresses land on individual employees at the worst possible moment — a denied claim, an unpaid entitlement — and are discovered by them rather than by the employer. Continuous verification converts a class of silent, personally consequential error into a list somebody can work, and the first run is invariably the most valuable thing the product ever produces.
