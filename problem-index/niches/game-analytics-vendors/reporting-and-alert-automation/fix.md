# The Alert Everybody Muted

**Niche:** [[niches/game-analytics-vendors/reporting-and-alert-automation/profile|Reporting & Alert Automation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The retention alert fires most days, everyone filtered it into a folder, and the day it mattered nobody saw it.
**Tags:** #quick-win #change-point-detection #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get the right number to the right person at the right moment without an analyst assembling it, and whoever automates that takes the account.

## The Problem
Analytics alerts are set on round numbers — retention below a threshold, revenue below a figure — chosen once with no reference to how the metric actually varies. They fire on ordinary fluctuation, recipients filter them away, and the alert becomes noise. When something genuinely happens the alert fires into a folder nobody opens. The alerting is worse than none, because everyone believes they are being watched.

## Why It's Still Broken
The threshold ignores variance — an alert that does not know a metric's normal range will fire on normal behaviour, and the only available response is to stop looking. Nobody owns alert quality. Muting is invisible. And nobody has counted how often each alert led to an action.

## What a Fix Looks Like
Audit the alerts before setting any new ones. List every alert, how often it fired, and whether anyone acted, which is the fix and usually shows most of them have never been useful. Delete the alerts that have never led to action, which is the largest immediate improvement. Set remaining thresholds from the metric's own historical variance rather than a round number. Account for day-of-week and seasonal patterns, since most false alerts come from ignoring them. Require an alert to say what to do, otherwise it is a notification. Route to the person who can act rather than to a broad channel. Group related alerts so one event produces one message. Check whether recipients have muted, which is the real measure of alert quality and is usually knowable. Review the alert set quarterly with a named owner. And set fewer alerts than feels comfortable, because a small set that is read beats a large set that is filtered.

## Who Feels the Pain
Teams who missed the real movement; analysts who set alerts nobody reads; leaders who believe they are being alerted; and the credibility of the whole monitoring layer.

## Impact If Fixed
An alert that does not know a metric's normal range will fire on normal behaviour, and the only available response is to stop looking. Auditing which alerts ever led to action, then deleting the rest, is an afternoon.
