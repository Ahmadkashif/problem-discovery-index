# The Creative Judged Only on Cost Per Install

**Niche:** [[niches/game-user-acquisition-firms/creative-practice-and-honesty/profile|Creative Practice & Ad Honesty]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The winning creative in every test is the one with the lowest cost per install, and nobody has looked at what happened to those installs.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #survival-analysis #confidence-intervals #causal-inference #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to establish whether ads depicting mechanics the game does not have actually acquire anything of value after the churn they cause — and whoever measures that takes the account.

## The Problem
Creative testing is fast and mechanical: run variants, compare cost per install, scale the winner. The whole pipeline is built around a metric available within hours. Retention and value from those installs arrive weeks later, in a different report, attributed to a source rather than to a creative. So the creative that acquires the cheapest installs wins every test, and whether it acquired anybody worth having is never part of the decision.

## Why It's Still Broken
The two metrics live in different systems on different timescales — a decision made on a metric available today will never be influenced by a metric available in a month, no matter how much more important the second one is. Creative-level attribution decays. The testing cadence is fast by design. And nobody reports creative-level retention.

## What a Fix Looks Like
Add one late metric to the creative report. Report day-seven retention by creative alongside cost per install, which is the fix and is an attribution join the data usually supports. Rank creatives on cost per retained player rather than cost per install, since that single change reorders most creative tests. Look at first-session length by creative, as expectation mismatch shows up immediately and needs no long horizon. Preserve creative-level attribution long enough to measure, which is a tracking decision rather than a modelling one. Hold the top creatives by install cost and check their cohorts at thirty days before scaling further. Report store rating movement against creative campaigns, which is a documented and ignored cost. Flag creatives whose retention is far below the game's baseline. Keep a record of which creatives were scaled and what their cohorts did, so the pattern accumulates. Present both metrics in the same report rather than in two systems. And make the retention column part of the standard creative test output, which is the change that alters behaviour.

## Who Feels the Pain
Publishers acquiring users who leave in the first minute; UA teams optimising a metric that misleads them; players who installed something that was not what they saw; and the store rating, which absorbs it.

## Impact If Fixed
A decision made on a metric available today will never be influenced by a metric available in a month, however much more important it is. Putting retention by creative in the same report reorders most creative tests.
