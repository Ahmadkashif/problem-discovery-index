# Minute Forty, and It Was the First Test

**Niche:** [[niches/ci-cd-platforms/the-waiting-developer/profile|The Waiting Developer]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developers lose fragments of every day to a pipeline they cannot speed up, and discover at minute forty that the failure was in the first test that ran.
**Tags:** #gradient-boosting #logistic-regression #optimization-fundamentals #survival-analysis #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to shorten the interval between a developer pushing a change and knowing whether it worked — and whoever does that takes the engineering organisation, because that interval is paid by every developer every day and appears in no budget.

## The Problem
A developer pushes at 09:40 and switches to something else. At 10:22 they get a notification: failed. They open it and find that a unit test failed — the first one that ran, at 09:43. The pipeline continued for thirty-nine minutes after the outcome was determined, because it was written as a sequence and nothing stops early. The developer has lost the context they had at 09:43, spends ten minutes re-acquiring it, fixes a one-line problem and pushes again, and the loop repeats. Three times in a morning is not unusual.

## Why Nobody Has Built This
Pipelines run to completion because the configuration is a list of steps and stopping early requires knowing that the remaining steps cannot change the outcome, which nothing models. Ordering is as written, and rewriting it for feedback speed is work that benefits everybody and is owned by nobody. Developer waiting time is not a metric anybody reports: pipeline duration is reported as a platform statistic, and the interval from push to answer — including queueing, and including the fact that the answer was determined in the first minute — is not. And the cost is fragments of time distributed across everyone, which is the hardest kind of cost to make visible.

## What to Build
Optimise for the time to the answer rather than the time to completion. Order steps by probability of failure and by cost, using the historical record — which tests have failed recently, which are affected by this change, which are cheap — so the most likely failure is found first, which is a scheduling change with a large effect and no infrastructure cost. Fail fast by default, stopping when the outcome is determined, with a mechanism for the cases where full results are genuinely wanted. Report progressively, so a developer learns at minute two that the fast checks passed rather than learning nothing until the end. Distinguish queued from running in the status, since the developer's response should differ and currently they cannot tell. Predict the outcome early where the evidence supports it, since a pipeline whose most failure-prone steps have passed is very likely to pass and saying so lets the developer move on. Measure the interval from push to answer, per developer and in aggregate, including queue time — which is the metric this niche exists to move and which no organisation currently has. And report the cumulative waiting, because an engineering organisation that sees the total will fund the fix.

## Target Customer
Platform engineering teams, CI vendors competing on developer experience, and engineering leadership who have never seen the aggregate waiting number.

## Impact If Built
Failure-probability ordering and fail-fast are scheduling changes with no infrastructure cost that address the largest share of wasted waiting directly. The push-to-answer metric is what makes the problem visible, and it currently exists nowhere.
