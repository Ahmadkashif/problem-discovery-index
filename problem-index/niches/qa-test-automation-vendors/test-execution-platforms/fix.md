# Billed by the Minute, Valued by Nothing

**Niche:** [[niches/qa-test-automation-vendors/test-execution-platforms/profile|Test Execution Platforms]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Test execution is billed per minute and reported as executions and pass rate, which means a suite that tests nothing and runs for an hour looks identical to one that catches defects.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to be where and how an organisation's tests actually run — and that contest is an infrastructure business in one market and a trust business in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
The monthly report shows four hundred thousand test executions with a ninety-seven percent pass rate. Both numbers are presented as good. A ninety-seven percent pass rate on a stable application is close to uninformative — it mostly means the tests ran — and the three percent is dominated by flakiness rather than by defects. The executions are billed. A team that deleted half its suite and kept the half that catches things would show worse numbers on both metrics and would be better off.

## Why It's Still Broken
The runner produces execution counts and pass rates and the billing system produces minutes, so those became the report. Effectiveness requires a join nobody has made. The vendor's revenue is proportional to executions, which removes any incentive to report that most of them are uninformative. And the quality function is measured on suite size and coverage, which are both quantities and both point the same way.

## What a Fix Looks Like
Report effectiveness alongside volume. Failures classified into genuine defect, flake and maintenance break, which is the decomposition that makes a pass rate meaningful and is achievable from the failure and repair history. Tests that have never failed for a genuine reason, which is usually a large fraction and is the pruning list. Defects caught per thousand executions and per unit of cost, which is the efficiency measure the category lacks entirely. Escaped defects joined back to the tests that should have caught them, which is the coverage question asked properly. Cost per defect caught, by test type and by environment combination, which is the number that should drive every decision about what to run and where. And report the suite's trend on these rather than on size, because a growing suite with a falling defect-catch rate is the normal trajectory and is currently reported as progress.

## Who Feels the Pain
Quality teams whose good numbers describe a suite that finds nothing; organisations paying for executions that are uninformative; and developers waiting for a suite whose value nobody has established.

## Impact If Fixed
Failure classification and the escaped-defect join are both achievable from existing data and turn a meaningless pass rate into an effectiveness measure. Cost per defect caught is the metric that would reorder every decision in the category and is reported by nobody.
