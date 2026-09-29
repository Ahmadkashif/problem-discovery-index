# Volume Without Evidence of Value

**Niche:** [[niches/qa-test-automation-vendors/test-execution-platforms/profile|Test Execution Platforms]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category makes it easy to run more tests on more combinations and reports none of the only thing that matters, which is whether any of it finds defects worth finding.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to be where and how an organisation's tests actually run — and that contest is an infrastructure business in one market and a trust business in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
An organisation runs eleven thousand tests across fourteen browser and device combinations on every change. The grid bill is substantial, the suite takes forty minutes, and the reported metrics are executions, pass rate and duration. Nobody can say how many defects the suite caught last quarter, which tests caught them, which combinations have ever caught anything, or what proportion of production defects the suite should have caught and did not. The category's entire commercial logic is the value of finding defects before release, and nothing measures it.

## Why Nobody Has Built This
Pass rate and execution count are produced by the runner for free and became the metrics by default, exactly as coverage did. Measuring defects caught requires joining test failures to the changes that caused them and to the production defects that escaped, which spans the test platform, the version control system and the incident record — three systems and no owner. Vendors billing by execution have no reason to report that most executions find nothing. And a suite's effectiveness is uncomfortable to measure, since the answer is frequently that a large portion of it is finding nothing at all.

## What to Build
The shared measurement layer both sub-niches need: test effectiveness. Join test failures to the changes that caused them and classify each as a genuine defect caught, a flaky failure or a maintenance break, which is the foundational classification and is what distinguishes a useful suite from a busy one. Join production defects and incidents back to the tests that should have caught them, which produces the escape rate — the measure of what the suite is for and the one nobody computes. Report value per test: which tests have ever caught a genuine defect, which have never failed for a real reason, and which fail constantly for maintenance reasons, which produces a ranked list for pruning and for investment. Report value per environment combination, which is the grid question and is the subject of the first sub-niche. Report the cost side alongside it — execution minutes, maintenance effort, developer waiting time — so effectiveness is expressed per unit of cost rather than absolutely. And make this the category's metric, because pass rate rewards a suite that tests nothing and this rewards one that finds defects.

## Target Customer
Quality engineering leadership, platform teams paying for grids and execution, and the vendors willing to compete on effectiveness rather than on volume.

## Impact If Built
The category's commercial logic rests on defects found and nothing measures them, which leaves every decision about what to test and where made on intuition. The escape rate is the measure of what a suite is for and requires only a join between three systems every organisation already has.
