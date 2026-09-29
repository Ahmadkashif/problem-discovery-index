# Predicting a Mean for a Distribution That Has None Worth Having

**Niche:** [[niches/game-user-acquisition-firms/heavy-tail-estimation/profile|Heavy-Tail Estimation]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The cohort's average value is reported as a number, and in most cohorts almost nobody is anywhere near it.
**Tags:** #quick-win #descriptive-statistics #probability-distributions #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to identify, from a few days of behaviour, the small fraction of players who will produce most of a cohort's value — and whoever does it takes the account.

## The Problem
Cohort value is reported as an average and used as though it described a typical player. In these distributions the average describes nobody: the median player is worth almost nothing and the mean is dragged up by a handful. Two cohorts with identical averages can have completely different compositions — one with many modest spenders, one with a single very large one — and they are worth entirely different amounts as a bidding proposition because the second is far less repeatable.

## Why It's Still Broken
The reporting is a single number — an average reported without a distribution invites everyone to reason about a typical player who does not exist, and the tooling offers nothing else. Distributions are harder to put in a dashboard. The average is what the payback calculation uses. And nobody has asked what the cohort actually looks like.

## What a Fix Looks Like
Report the shape alongside the number. Show the value distribution per cohort rather than the mean alone, which is the fix and needs only a different chart over existing data. Report the share of cohort value from the top one percent, which is the single most informative figure and is never shown. Flag cohorts whose value depends on very few players, since those are the least repeatable and should be bid differently. Show the median alongside the mean so the gap is visible. Compare distribution shape across sources, which frequently differs more than the averages suggest. Track whether a source's tail composition is stable over time, as an unstable one is a risk the average hides. Report confidence on the cohort mean, given that a small cohort's average is nearly meaningless. Use the distribution in the payback calculation rather than the point. Present it to media buyers in a form they can act on, which is what determines whether it changes anything. And stop reporting the mean alone, which is the habit that sustains the misunderstanding.

## Who Feels the Pain
Media buyers treating unlike cohorts as alike; analysts reporting an average that describes nobody; publishers whose acquisition is priced on a summary statistic; and the bidding decisions built on it.

## Impact If Fixed
An average reported without a distribution invites everyone to reason about a typical player who does not exist. Showing the distribution and the top-percentile share is a different chart over data already held.
