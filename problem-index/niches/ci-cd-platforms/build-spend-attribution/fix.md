# Re-Runs Billed as First Runs

**Niche:** [[niches/ci-cd-platforms/build-spend-attribution/profile|Build Spend Attribution]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of pipeline minutes are re-runs of identical changes caused by flaky tests, and nothing separates them from useful work in any report.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to say where build spend actually goes in units somebody can act on — and whoever does that takes the cost conversation, because minutes by repository is not a unit anyone can act on.

## The Problem
The usage report shows total minutes consumed, up eighteen percent this quarter. A meaningful share of those minutes are re-runs: the same commit, the same pipeline, executed again because a test failed intermittently. They produce no new information, they are indistinguishable from first runs in every report, and they are the most directly avoidable cost the organisation has. Nobody has counted them, so the flakiness problem has never had a monetary figure attached and has therefore never competed for engineering time against features.

## Why It's Still Broken
Re-runs are recorded as ordinary executions because the billing model does not care why a job ran. Separating them requires identifying that a run is of an identical commit with an identical configuration, which is trivial and has not been done because nobody asked. And the two facts that would combine into an argument — the flakiness rate and the re-run cost — sit in different reports owned by different concerns, so nobody has multiplied them.

## What a Fix Looks Like
Count the re-runs and price them. Identify re-runs by commit and configuration identity, which is a simple grouping over execution records, and report them as a separate category in every usage view. Attribute each re-run to its cause where possible: flaky test, infrastructure failure, transient dependency error, or a genuine retry of a fixed problem — since those have different remedies and only some are waste. Price the flakiness-caused subset explicitly, which gives the flaky test problem a monetary figure for the first time and is the number that lets it compete for engineering time. Report re-run rate per pipeline and per team, which localises the problem to the suites that cause it. Separate queue time from execution time in the bill, since time spent waiting for a runner is the vendor's capacity problem and should not be the customer's cost. And track the trend, because a rising re-run rate is the leading indicator that the organisation's pipeline signal is degrading — which is the failure the flakiness niche describes and which currently has no early warning at all.

## Who Feels the Pain
Platform teams explaining a rising bill they cannot decompose; developers re-running pipelines several times a day; and organisations whose flakiness problem has no monetary figure and therefore never gets fixed.

## Impact If Fixed
Re-run identification is a grouping over existing records and typically reveals a surprising share of total spend. Pricing the flakiness-caused portion gives the category's defining problem a number, which is what it has always lacked when competing for engineering time.
