# The Same Failure Every Tuesday

**Niche:** [[niches/data-platform-integrators/the-oncall-pipeline-engineer/profile|The On-Call Pipeline Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The upstream extract is late every Tuesday, the pipeline fails every Tuesday, and someone reruns it every Tuesday.
**Tags:** #worker-facing #quick-win #automation #workflow-orchestration #descriptive-statistics #evaluation-metrics #change-point-detection #data-integration
**Contested on:** Every serious competitor in this niche is fighting to stop one engineer rerunning, backfilling and explaining overnight failures before the morning reports go out — and whoever automates that recovery takes the account.

## The Problem
A large share of overnight failures are the same failure. An upstream job runs long on a particular day, a source system has a weekly maintenance window, a volume spike hits a limit on month end. The pattern is entirely predictable and is handled manually each time because nobody has looked at the incident history as a series. The engineer's week is shaped by a recurring event that could be scheduled around.

## Why It's Still Broken
Nobody looks at the incidents in aggregate — a failure handled individually each time is never recognised as the same failure, because nothing tabulates them and the person on call changes. Alerts are transient. Fixing the cause is unfunded work. And rerunning takes ten minutes, so it never escalates.

## What a Fix Looks Like
Count the failures by cause and fix the top three. Tabulate overnight failures by pipeline and cause over the last quarter, which is the fix and takes an hour with the orchestrator's history. Identify the recurring ones, which will be a small number accounting for most of the volume. Reschedule around the predictable upstream lateness rather than failing against it, which is the commonest and cheapest fix. Make dependencies explicit so a pipeline waits rather than fails when an upstream is late. Add retry with sensible backoff where the cause is transient, which many pipelines still lack. Fix the resource limits that are hit predictably at month end. Track failure volume per week as a visible metric, so the trend is somebody's responsibility. Record the cause on every incident, which is what makes the next tabulation better. Feed the recurring list into the engineering backlog with the on-call hours attached, which is what gets it prioritised. And review it monthly rather than after a bad week.

## Who Feels the Pain
On-call engineers whose weeks are shaped by a predictable event; business users whose reports are late on the same day each week; teams losing people from the on-call rota; and the engineering backlog, which never includes the fix.

## Impact If Fixed
A failure handled individually each time is never recognised as the same failure, because nothing tabulates them and the person on call changes. An hour with the orchestrator's history names the three causes that produce most of the nights.
