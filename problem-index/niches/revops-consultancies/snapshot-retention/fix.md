# Starting the Series This Week

**Niche:** [[niches/revops-consultancies/snapshot-retention/profile|Forecast Snapshot Retention]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Fix (Pain Point)
**One-liner:** Every week that passes without capture is a week that can never be scored, and nobody has started.
**Tags:** #quick-win #data-integration #automation #workflow-orchestration #descriptive-statistics #evaluation-metrics #compliance #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to capture every forecast at every level before it is overwritten, because nothing downstream is possible without that series — and whoever captures it takes the account.

## The Problem
Organisations know the history would be useful and do not start capturing it, because starting feels like the beginning of a project: agreeing what to capture, where to put it, who owns it, how it feeds reporting. So each week the number is overwritten and another week of evidence is permanently gone. The full version is a project; the useful version is a scheduled export.

## Why It's Still Broken
The good version is imagined as a project — a capture that is scoped as a data programme will be prioritised against other data programmes and lose, when the version that matters is a scheduled query. Nobody owns it. The benefit is a quarter away. And the loss each week is invisible.

## What a Fix Looks Like
Start with the crudest capture that works and improve it later. Schedule a weekly export of the forecast and pipeline to a dated file, which is the fix and takes an hour with no project at all. Include representative-level detail rather than only the rolled-up number, since that is where the analysis will want to go. Date-stamp everything and never overwrite, which is the only rule that matters. Put it somewhere durable rather than on someone's drive. Recover what exists in archived weekly decks and emails, which often yields several quarters of partial history. Record what methodology was in use, in a note beside the file. Improve the mechanism later once the habit exists, rather than designing first. Assign it to one person as a named task, or it will lapse. Review the accumulated series after a quarter, which is when it starts being interesting and when support for a better version arrives. And treat every week not captured as evidence permanently destroyed, which is what it is.

## Who Feels the Pain
Revenue leaders who will ask this question next year; analysts told to establish a trend from nothing; consultancies whose recommendations cannot be evaluated; and the organisation, which will start from zero whenever it finally begins.

## Impact If Fixed
A capture scoped as a data programme will be prioritised against other data programmes and lose, when the version that matters is a scheduled query. An hour of work this week is the difference between having a series next year and not.
