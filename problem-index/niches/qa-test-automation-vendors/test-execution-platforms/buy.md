# Test Effectiveness Measurement That Exists

**Niche:** [[niches/qa-test-automation-vendors/test-execution-platforms/profile|Test Execution Platforms]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mutation testing measures whether a suite would actually detect a defect, has been researched for forty years, and is used almost nowhere while line coverage is used everywhere.
**Tags:** #monte-carlo-methods #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #cross-validation #descriptive-statistics #automation
**Contested on:** Every serious competitor here is fighting to be where and how an organisation's tests actually run — and that contest is an infrastructure business in one market and a trust business in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
Mutation testing answers the question coverage pretends to: introduce a small defect and see whether any test fails. It has a forty-year research history, mature implementations for the major languages, and a clear interpretation — a suite that does not detect an introduced defect would not detect a real one either. It is used by a small minority, because it is computationally expensive and because coverage is free. The category therefore measures lines executed and calls it quality.

## What Already Exists
Mutation testing frameworks for most major languages; the mutation operator literature with established defect classes; techniques for reducing the cost including mutant selection, incremental analysis and parallel execution; defect prediction research; and escaped defect analysis methodology from quality engineering practice.

## The Customization Gap
The adaptation is to a cost budget and a continuous pipeline. It requires: (1) incremental rather than full mutation analysis, running only mutations related to changed code, which reduces the cost by orders of magnitude and makes it viable in a pipeline — this is the change that moves it from research to practice; (2) mutant selection informed by real defect patterns rather than by exhaustive operator application, since the useful question is whether the suite catches the defects that actually occur and the vendors' fleet contains that distribution; (3) an interpretable output, because a mutation score is a number and what a team needs is the specific behaviours that are unprotected; (4) application to end-to-end and interface tests, where mutation is harder than at the unit level and where the category's spend is concentrated — which requires mutating behaviour rather than code and is the genuinely novel piece; and (5) an escaped-defect join as the validating measure, since mutation score is a proxy and the real test is whether suites with better scores let fewer defects through.

## Target Customer
Test automation vendors, quality engineering functions, and the platform teams who own the pipeline budget.

## Impact If Solved
A forty-year-old technique answers the question the universally-used metric only pretends to, and cost is the reason it is unused. Incremental analysis addresses the cost directly, and extending mutation to interface-level tests is where the category's actual spend is.
