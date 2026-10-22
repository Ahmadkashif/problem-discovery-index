# A RADV Survival Score for Every Submitted Diagnosis

**Niche:** [[niches/health-insurance-carriers/ma-risk-adjustment/profile|Medicare Advantage Risk Adjustment & RADV Defence]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Plans know which diagnoses they submitted and what each is worth, but not which ones a CMS coder would delete if the member were sampled.
**Tags:** #gradient-boosting #large-language-models #bert #survival-analysis #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to submit every diagnosis a member's chart supports, and none it doesn't, before CMS's final submission deadline, and whoever keeps the most submitted diagnoses standing through a RADV medical-record review takes the account.

## The Problem
A submitted diagnosis can come from a claim, a chart review or an in-home assessment, and its support in the medical record ranges from a fully documented, treated condition to a problem-list entry copied forward for years. RADV coders validate against the record. With every contract now audited each year, every unsupported diagnosis is a likely recovery. Yet plans treat their submissions as a list of codes and dollars, not a list of risks.

## Why Nobody Has Built This
Vendors have been paid on diagnoses added, not on diagnoses that survive. Plans' own audit outcomes were sparse when CMS audited a few dozen contracts a year. And building the label requires the plan's internal mock-audit results, coder disagreements and CMS findings in one place.

## What to Build
For each submitted diagnosis, a score of the probability that a certified coder would validate it from the best available record. Inputs are the diagnosis source, the documentation elements present (monitoring, evaluation, assessment and treatment), the provider type, how many times the condition recurs across encounters, and the plan's prior mock-audit and RADV results. The score drives deletions before the final submission deadline, targeted chart pulls where support exists but is not on file, and an audit-ready evidence package for diagnoses likely to be sampled.

## Target Customer
Risk adjustment and compliance leaders at MA plans and risk-bearing provider groups facing annual RADV.

## Impact If Built
Lower recovery exposure, deletions made voluntarily rather than found by CMS, and a submission the compliance officer can defend line by line.
