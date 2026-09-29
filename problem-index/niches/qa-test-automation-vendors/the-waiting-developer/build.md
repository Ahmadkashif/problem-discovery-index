# A Failure Prompts a Re-Run

**Niche:** [[niches/qa-test-automation-vendors/the-waiting-developer/profile|The Waiting Developer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developers wait for a test suite they have learned to disbelieve, so a failure prompts a re-run rather than an investigation and a pass prompts no confidence at all.
**Tags:** #logistic-regression #gradient-boosting #descriptive-statistics #bayesian-inference #confidence-intervals #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make a test result mean something to the developer receiving it — and whoever does that takes the engineering organisation, because a suite that is disbelieved provides no value regardless of what it costs.

## The Problem
A developer's change fails three tests. Their first action is to re-run, because in this organisation most failures are noise and re-running is faster than reading three stack traces. Two pass on the second run. The third fails again, they look at it, and it is a genuine regression — which they have now spent eleven minutes reaching by a route that mostly consisted of waiting. Their colleague, whose change also failed, re-ran twice and merged when it passed, because at some point re-running is the pragmatic response to a mechanism that is wrong more often than it is right.

## Why Nobody Has Built This
The result is presented as a binary because that is what the runner produces, and the question of whether this particular failure is likely to be real has never been asked by the tooling — although the answer is in the history of that test. The re-run button is the most-used feature in the category and its usage is telemetry nobody reports as a signal about the suite's credibility. And the organisation's metrics are pass rate and coverage, neither of which moves when trust collapses, so the failure is invisible in every report.

## What to Build
Attach credibility to the result. Score each failure by the probability that it is genuine, from that test's own history of failing and passing on re-run, the nature of the change, whether the failure is new, and whether related tests failed — which lets the developer read three failures in order of likely reality rather than treating them equally, and is computable from execution history alone. Suppress the known-flaky ones from blocking while still reporting them, since a failure that everybody re-runs is not providing a signal and is providing a delay. Say what a pass actually covered for this change, since a green result that verified nothing related to what was modified should not be read as assurance and currently is. Relate failures to the part of the change they concern, which turns a stack trace into a location. Measure the re-run rate and the re-run-without-investigation rate, which are the direct measures of whether the suite is believed and which nobody reports. And report the credibility trend, because a declining one is the early stage of the abandonment the maintenance niche describes and currently has no indicator at all.

## Target Customer
Platform and quality engineering teams, test tooling vendors, and the developers who have stopped reading test results.

## Impact If Built
A disbelieved suite provides no decision support regardless of its technical quality, and nothing measures belief. Failure credibility scoring is computable from execution history and changes how three failures are read, and the re-run rate is the honest measure of the suite's standing.
