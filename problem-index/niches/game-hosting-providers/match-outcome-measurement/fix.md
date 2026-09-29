# The Player Who Queued Four Times and Never Again

**Niche:** [[niches/game-hosting-providers/match-outcome-measurement/profile|Match Outcome Measurement]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A player had four one-sided matches in a row, stopped playing, and appears in no report anywhere.
**Tags:** #quick-win #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #causal-inference #change-point-detection #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to put a number on what a mismatched match, a long queue and excess latency each cost in whether the player queues again — and whoever produces that number takes the account.

## The Problem
The clearest evidence of matchmaking failure is a player who had a run of bad experiences and stopped. It is visible in the data — consecutive one-sided matches, repeated long queues, a string of high-latency sessions, then nothing. Nobody produces this cohort as a report. Churn is reported in aggregate and attributed to content, competition or natural decay, and the specific mechanism sitting in the session log is never examined.

## Why It's Still Broken
Churn analysis stops at the aggregate — a departure explained by a general trend is never traced to the specific sequence that caused it, so the mechanism stays invisible even though it is fully recorded. Session data and churn data live in different systems. Nobody owns the question. And the aggregate explanation is always available.

## What a Fix Looks Like
Produce the cohort and look at what happened to them. Identify players whose last sessions contained a run of poor experiences and report that cohort's size, which is the fix and is a query rather than a model. Compare their final session pattern against players who continued, since the contrast is usually stark enough to need no statistics. Count consecutive rather than average bad experiences, as the run is what matters and averaging destroys it. Break the cohort out by region and time of day, which locates the thin-population problems. Show the size of the cohort as a share of total churn, which is the number that gets attention. Look at new players separately, because a poor early run is disproportionately fatal and disproportionately fixable. Check whether they returned later, as some do and the distinction matters. Feed confirmed patterns into an alert rather than a one-off analysis. Present it as a mechanism rather than as blame for the matchmaking team. And run it monthly so the trend is visible against configuration changes.

## Who Feels the Pain
Players who had a bad run and left; studios attributing churn to the wrong cause; platform teams tuning against no evidence; and the acquisition budget replacing them.

## Impact If Fixed
A departure explained by a general trend is never traced to the specific sequence that caused it, so the mechanism stays invisible though fully recorded. Producing the bad-run cohort is a query that names a share of churn nobody had attributed.
