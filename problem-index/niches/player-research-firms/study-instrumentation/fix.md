# The Telemetry Nobody Turned On

**Niche:** [[niches/player-research-firms/study-instrumentation/profile|Study Instrumentation]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The analysis needed to know where each participant died and the build was not logging it.
**Tags:** #quick-win #data-integration #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #compliance #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to capture a session as a synchronised, searchable record rather than as a video file and some notes — and whoever builds that capture takes the account.

## The Problem
The build used for a study is whatever the team had. It often emits no research telemetry at all, so behavioural questions that would be answered by a log — where participants died, how long each area took, which options they opened — have to be answered by watching video and counting. The instrumentation would have been a day of work before the study and is impossible afterwards.

## Why It's Still Broken
Nobody asks for it early enough — a research build request made a week before sessions arrives after the point at which instrumentation could have been added, and the study then works without it. Researchers do not know what to ask for. Developers do not know what researchers need. And the gap is invisible until analysis.

## What a Fix Looks Like
Ask for the events at kickoff with a standard list. Provide the development team a standard research telemetry event list at study kickoff, which is the fix and is a document the firm writes once. Request the research build with enough lead time to instrument it, which is the scheduling change that makes it possible at all. Specify the minimum events — location, progression, deaths, retries, menu opens, session boundaries — rather than asking for telemetry generally. Reuse the same event set across studies so both sides learn it. Ensure timestamps align with the recording, since unsynchronised telemetry is far less useful. Confirm the events are emitting before the sessions rather than discovering afterwards. Provide a small integration the team can drop in, which removes the objection about effort. Note in the findings where a question could not be answered for want of instrumentation, which is what gets it fixed next time. Ask for it in the proposal so it is part of the engagement. And keep the list short, because a long one gets refused entirely.

## Who Feels the Pain
Researchers counting deaths by watching video; clients paying for analysis a log would have done; findings weakened by a missing measure; and the next study, which will repeat it.

## Impact If Fixed
A research build request made a week before sessions arrives after the point at which instrumentation could have been added. A standard short event list at kickoff makes the behavioural questions answerable.
