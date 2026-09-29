# Conversion Validated by Row Counts

**Niche:** [[niches/hr-tech-platforms/job-architecture-migration/profile|Job Architecture & Migration]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An HCM conversion moves years of employment history and is signed off on record counts and headcount totals, so the defects that matter — broken employment continuity, lost pay history, orphaned reporting lines — are discovered by employees afterwards.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #quick-win
**Contested on:** Every serious competitor in HCM implementation is fighting to infer an employer's job architecture and employment history from the data rather than rebuilding it from spreadsheets — and whoever shortens time-to-configured most takes the implementation.

## The Problem
The conversion moves four thousand employees. Counts match, headcount by department reconciles, and the programme goes live. Over the following months it emerges that employees who transferred between legal entities during an acquisition have broken service dates, which affects their leave accrual and their severance entitlement; that pay history before a particular year did not carry through, which breaks every compensation analysis and several statutory calculations; and that a cohort of people whose managers left during the migration window have no reporting line. Each was discoverable before go-live by a check nobody defined, because the validation was arithmetic rather than semantic.

## Why It's Still Broken
Conversion validation practice was inherited from financial systems, where totals reconciling is genuinely the test. Employment records are structured objects whose meaning lives in continuity, effective dating and relationships, and a headcount total says nothing about any of them. Defining the semantic checks requires HR domain knowledge that conversion teams — staffed with data specialists — do not have and HR teams are too busy during a programme to supply. And a conversion under deadline has every incentive to accept a validation that passes.

## What a Fix Looks Like
Define the properties that must hold and test them across the whole population. Service date continuity through entity transfers, acquisitions and rehires — which is the highest-consequence property and is where most defects concentrate. Pay history completeness and continuity, with distributional comparison by cohort rather than aggregate totals, since the defects live in subpopulations defined by an era or a legacy configuration. Reporting line integrity with no orphans and no cycles. Effective dating preserved on every attribute that has it. Leave and accrual balances reconciled individually rather than in total. Stratified human review that deliberately oversamples the long-tenured, the transferred and the structurally unusual, instead of sampling uniformly. And a signed fidelity report, which turns go-live from an act of faith into an accepted deliverable — and which, being largely reusable, is written once by a partner and applied to every subsequent programme.

## Who Feels the Pain
Employees whose service dates, accruals or pay history are quietly wrong and who find out when it matters; HR teams remediating a conversion for a year after go-live; and implementation partners whose programme is judged by what surfaces afterwards.

## Impact If Fixed
Semantic validation finds systematic defects before go-live rather than in production, and service date continuity in particular affects statutory entitlements for exactly the long-tenured employees who have most at stake. The assertions are reusable across conversions, so the investment is made once and applies to every programme afterwards.
