# Steps Accumulate and Nothing Is Removed

**Niche:** [[niches/ci-cd-platforms/test-selection-and-duration/profile|Test Selection & Pipeline Duration]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every team adds a step to the pipeline and nobody removes one, so duration grows monotonically and the growth is nobody's metric.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to run only the tests a change could plausibly break, with evidence that nothing was missed — and whoever does that takes the platform account, because everyone runs everything and nobody has the evidence to stop.

## The Problem
The pipeline has thirty-one steps. Eleven were added in the last two years, each for a good reason at the time: a linter after a style argument, a licence check after an audit, a security scan after an incident, a report generation nobody reads, a notification to a channel that no longer exists. Four of them have never failed. Two duplicate each other. One checks for a class of problem that a later step also catches. Nobody has looked, because looking is nobody's job and removing a check is the kind of decision that gets remembered if something later goes wrong.

## Why It's Still Broken
Adding a step is a local decision with a local benefit and a cost paid by everybody; removing one is a decision with a diffuse benefit and a concentrated risk. That asymmetry guarantees monotonic growth, exactly as it does with dashboards, templates, clause libraries and alert rules everywhere else in this vault. Nothing reports a step's history or its cost. And pipeline duration is reported as a single number that grows slowly enough that no individual quarter looks alarming.

## What a Fix Looks Like
Report each step's cost and value, and make removal reversible. Per step: total time consumed across all runs, how often it has failed, and when it failed whether the pipeline was already failing for another reason — which distinguishes a step that catches things from one that merely re-reports them. Identify steps that have never failed, which is a substantial population and is the obvious starting list. Identify redundancy, where a step's failures are always accompanied by another step's, meaning one of them is sufficient. Report the duration trend with the additions marked, so growth is attributable to decisions rather than appearing as drift. Make disabling reversible and time-boxed — disable for four weeks and see whether anything happens — since that converts an irreversible-feeling decision into an experiment. Require an owner and a review date for new steps, so the next decade's accumulation has a mechanism. And publish the cost of each step in engineer-hours per month, because a linter that costs ninety hours a month across the organisation is a different proposition once the number is visible.

## Who Feels the Pain
Every developer waiting for steps that have never caught anything; platform teams who suspect the pipeline is bloated and cannot prove it; and organisations whose delivery speed degrades by a few percent a quarter with no attributable cause.

## Impact If Fixed
Per-step cost and failure history are queries over data every platform stores, and the never-failed list is usually long enough to produce an immediate reduction. Time-boxed reversible disabling is what makes the removal decision politically possible.
