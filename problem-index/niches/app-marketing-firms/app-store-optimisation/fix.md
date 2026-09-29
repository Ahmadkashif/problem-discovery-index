# The Store Experiment Run Once a Quarter

**Niche:** [[niches/app-marketing-firms/app-store-optimisation/profile|App Store Optimisation]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The team runs one listing test a quarter, on two variants, stops it early when one looks ahead, and calls the result a finding.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #quick-win #descriptive-statistics #revenue-impact #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to improve the one page that converts every paid click and every organic browse — and whoever tests it properly gets a multiplier on all acquisition spend rather than an improvement to one channel.

## The Problem
The quarterly listing test compares two icon variants. After eight days one is ahead, so the team ships it. The difference was within the range that would occur by chance, the test was stopped when it looked favourable rather than at a pre-planned point, and the result is recorded as a learning about what the audience prefers. That learning then shapes the next quarter's assets. Four such tests a year, each conducted this way, is the entire empirical basis for how the listing evolves, and the process is more likely to produce a random walk than an improvement.

## Why It's Still Broken
Testing infrastructure is limited so tests feel expensive, which makes each one feel too important to run to completion — the scarcity of tests is what produces the impatience that invalidates them. Nobody calculates power. Stopping when ahead is intuitive and is the single most common way a test is invalidated. And there is no record of past tests against later outcomes, so the practice never corrects.

## What a Fix Looks Like
Run fewer, better tests, or more of them properly. Calculate power before each test and state the minimum detectable effect, which is the fix and frequently reveals that a quarterly two-variant test on this traffic cannot detect anything worth shipping. Pre-register the duration and the decision rule, since stopping when ahead is what converts a valid test into a coin flip. Use sequential methods with valid stopping rules if early stopping is genuinely needed, which is a solved problem and permits looking without invalidating. Test larger differences, because a test that cannot detect a small effect can still detect a big one and the practice is currently testing small variations it has no power to resolve. Run tests continuously rather than quarterly, which raises the annual information yield far more than improving any single test. Keep a record of every test and its later outcome, so the practice accumulates rather than producing four disconnected anecdotes a year. Separate the result by traffic source where possible, since paid and organic respond differently and the blended result may apply to neither. Report inconclusive results as inconclusive, which is the honest outcome of most underpowered tests and is currently reported as a preference. Estimate the value of the testing programme, since that is what justifies increasing its cadence. And validate shipped winners against subsequent performance, because a shipped winner that did not hold is the clearest evidence the process needs changing.

## Who Feels the Pain
Teams whose listing evolves by random walk; designers producing assets shaped by invalid findings; and businesses leaving the discipline's highest-leverage gains untouched.

## Impact If Fixed
Test scarcity produces the impatience that invalidates each test, and stopping when ahead turns a valid comparison into a coin flip. Power calculation frequently shows a quarterly two-variant test cannot detect anything worth shipping, which is the finding that changes the programme.
