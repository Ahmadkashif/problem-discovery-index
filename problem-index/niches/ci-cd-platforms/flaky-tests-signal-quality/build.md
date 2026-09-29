# The Habit of Re-Running

**Niche:** [[niches/ci-cd-platforms/flaky-tests-signal-quality/profile|Flaky Tests & Signal Quality]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A test that fails intermittently teaches engineers to re-run rather than investigate, and once that habit forms every failure is re-run — which means the pipeline stops being a signal at exactly the moment it matters.
**Tags:** #logistic-regression #gradient-boosting #hidden-markov-models #graph-theory #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make a pipeline failure mean something again — and whoever does that takes the platform account, because once engineers learn to re-run rather than investigate, every other capability in the category is built on a signal nobody trusts.

## The Problem
An engineer's pipeline fails on a test unrelated to their change. They re-run it; it passes; they merge. This is the correct local decision and it happens perhaps forty times a week across the organisation. Six months later, a genuine regression fails the same way and is re-run past, because nobody now reads a red pipeline as evidence. The organisation has an extensive test suite, a fast pipeline and no signal, and the degradation happened without any single decision that could be pointed at.

## Why Nobody Has Built This
Flakiness detection was implemented as a counter — this test passed on retry — which identifies the symptom and offers nothing about the cause, so the output is a growing list nobody can act on. Attributing a flaky test to its cause requires analysing execution context across many runs, which the platforms have and have not modelled. The cost is diffuse: a re-run is three minutes of compute and a few minutes of attention, repeated invisibly, and it appears in no budget. And the behavioural consequence — that people stop trusting failures — is the real damage and is measured nowhere.

## What to Build
Attribute flakiness to its cause and measure the behavioural damage. Classify each flaky test into the small enumerable set of causes using the platform's own execution record: order dependence, shown by failure correlating with execution position or with which tests ran before; shared state, shown by correlation with parallel workers; timing, shown by correlation with machine load or duration; resource contention; and external dependency, shown by correlation with an outside service's condition. Each has a different and well-known remedy, and naming the cause is the difference between a list and a fix. Rank by cost rather than frequency, where cost includes compute for re-runs, engineer attention, and the delay to merges — which is computable and typically produces a startling total. Measure the behavioural consequence directly: what proportion of failures are re-run without any investigation, and how that proportion has moved, which is the number that describes whether the organisation still has a signal. Detect the transition when a previously reliable test becomes flaky, since that is usually a specific change and is much easier to fix immediately. And place the evidence in front of the engineer at the moment of failure — this test has failed intermittently eleven times this month, the cause is likely ordering, here is the evidence — so re-running is an informed decision rather than a reflex.

## Target Customer
Platform engineering teams, CI vendors for whom this is the most cited complaint about the category, and engineering leadership who have noticed that their test suite no longer prevents anything.

## Impact If Built
Signal degradation is the category's central failure and happens without a decision anybody could point at. Cause attribution turns an unusable list into fixable items, and measuring the re-run-without-investigation rate gives the organisation a number for the damage.
