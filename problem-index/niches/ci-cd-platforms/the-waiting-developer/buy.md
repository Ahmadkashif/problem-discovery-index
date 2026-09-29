# Test Prioritisation Research, Unapplied

**Niche:** [[niches/ci-cd-platforms/the-waiting-developer/profile|The Waiting Developer]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Test case prioritisation has been studied for twenty-five years with published algorithms and evaluation metrics, and most pipelines run tests in the order the files appear on disk.
**Tags:** #gradient-boosting #logistic-regression #optimization-fundamentals #graph-theory #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to shorten the interval between a developer pushing a change and knowing whether it worked — and whoever does that takes the engineering organisation, because that interval is paid by every developer every day and appears in no budget.

## The Problem
Ordering a test suite so that failures are found as early as possible is test case prioritisation, a research area with twenty-five years of published work, standard evaluation metrics and repeated industrial validation. The practical state of the art in most organisations is alphabetical, or whatever order the test runner discovers files in, which is effectively random with respect to failure probability.

## What Already Exists
Test case prioritisation research with coverage-based, history-based and learned approaches; test impact analysis relating changes to affected tests; failure prediction from code and test features; and evaluation metrics designed for this exact objective. Several published industrial deployments at large companies with reported results.

## The Customization Gap
The adaptation is to a continuous, parallel, multi-team pipeline. It requires: (1) history-based rather than coverage-based prioritisation as the practical default, since coverage instrumentation is expensive and frequently unavailable while failure history is free and is nearly as effective — this is the pragmatic choice that makes deployment possible; (2) parallelism-aware ordering, because the research mostly assumes sequential execution and the objective in a parallel pipeline is to minimise time-to-first-failure across workers, which is a different scheduling problem; (3) change-awareness, so tests related to the modified code are prioritised, which requires the test impact analysis that this industry's selection niche depends on and which is the largest single source of signal; (4) flakiness exclusion, since prioritising by recent failure will put the flaky tests first and produce a fast, meaningless failure — the two capabilities must be joined or the prioritisation is actively harmful; and (5) continuous learning, because the failure distribution shifts with the codebase and a model trained once will decay.

## Target Customer
CI platform vendors, test tooling vendors, platform engineering teams, and the build system vendors whose dependency graphs supply the impact analysis.

## Impact If Solved
Twenty-five years of research addresses exactly this and most pipelines run tests in file order. History-based prioritisation is nearly as effective as coverage-based and costs nothing, and joining it to flakiness detection is what prevents it backfiring.
