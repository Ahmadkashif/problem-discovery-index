# Test Infrastructure From Software Engineering

**Niche:** [[niches/ai-model-evaluation-firms/evaluation-platforms/profile|Evaluation Platforms]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software testing has decades of infrastructure for running suites, quarantining flaky tests and reporting regressions, and evaluation platforms rebuilt the easy parts and skipped the hard-won ones.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #hypothesis-testing #data-integration #confidence-intervals #quick-win #descriptive-statistics
**Contested on:** Not terminal — the contest differs by who is being evaluated and why, and the decomposition is recorded in the profile.

## The Problem
Running a suite, reporting pass and fail, integrating with continuous integration, and showing what changed since the last run is what test frameworks have done for thirty years. More importantly, the testing world learned the hard lessons: a flaky test destroys trust in the whole suite, so quarantine it; a test that never fails tells you nothing, so measure coverage of what matters; a regression report that lists three hundred failures gets ignored, so rank and group them. Evaluation platforms copied the runner and none of the lessons.

## What Already Exists
Test runners with parallel execution, sharding and selective reruns; flaky test detection, quarantine and reporting; continuous integration integration with build gating; test impact analysis for selecting the relevant subset; snapshot and approval testing for outputs without an exact expected value; and regression reporting with grouping and triage workflows.

## The Customization Gap
The adaptation is to a suite where every test is stochastic. It requires: (1) flakiness as the normal condition rather than an anomaly, since every evaluation item is non-deterministic to some degree and the testing world's quarantine model assumes flakiness is rare and fixable — here the correct move is repetition and statistical treatment, which is a different response to the same diagnosis; (2) graded rather than binary outcomes, which breaks the pass-fail model every runner is built on and requires thresholds with uncertainty; (3) approval testing adapted to semantically equivalent outputs, since an exact-match snapshot is useless when the output is generated text, and this is the closest existing analogue to what evaluation actually needs; (4) cost-aware selection, because running the full suite per commit is affordable in software and expensive against a frontier model, which makes test impact analysis far more valuable here than it is in its original setting; and (5) regression triage that groups by failure mode rather than by item, since a hundred items failing for one reason is one finding and is currently reported as a hundred.

## Target Customer
Evaluation platform vendors, application engineering teams, and the test infrastructure vendors for whom stochastic suites are an unserved shape.

## Impact If Solved
The testing discipline's hard-won lessons about flakiness, triage and coverage were skipped when the runner was copied. Cost-aware test selection matters far more here than in its original setting, because a full suite run against a frontier model is a budget line.
