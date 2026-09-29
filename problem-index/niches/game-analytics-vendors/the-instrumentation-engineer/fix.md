# The Special Case Only One Person Knows

**Niche:** [[niches/game-analytics-vendors/the-instrumentation-engineer/profile|The Instrumentation Engineer]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The retention figure is correct because of an adjustment one engineer added two years ago and never wrote down.
**Tags:** #worker-facing #quick-win #data-integration #workflow-orchestration #compliance #automation #descriptive-statistics #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to let one engineer keep data consistent across six live client versions all sending slightly different schemas — and whoever supports that person takes the account.

## The Problem
The transformation layer is full of adjustments that are individually sensible and collectively undocumented: this version double-counts, that one sends the timestamp in a different timezone, this parameter was repurposed after a patch. Each was added for a real reason by one person. Nobody else knows they exist. If that person is unavailable, nobody can explain, modify or defend the numbers the studio runs on.

## Why It's Still Broken
The reasons live in the code's author rather than in the code — an adjustment added under deadline with no comment is indistinguishable later from a mistake, and only one person can tell the difference. Documentation is not part of the task. There is no review. And nothing fails, so nothing prompts anyone to look.

## What a Fix Looks Like
Write down why, not just what. Require a reason and a version reference on every adjustment at the point it is added, which is the fix and costs one line each. Backfill the reasons for the existing adjustments while the person who knows them is still available, which is the urgent part. Test each adjustment so an accidental removal fails visibly rather than silently changing a metric. List the adjustments affecting each published metric, so a disputed number can be explained. Review the list periodically to retire adjustments for versions no longer live. Have a second person read through the layer once, which is the cheapest reduction in key-person risk available. Note which metrics depend on the most adjustments, as those are the least robust. Alert if an adjustment stops matching any traffic, which usually means a version retired or a schema changed. Keep the documentation with the code rather than in a separate wiki. And treat the whole layer as a documented asset rather than as accumulated maintenance.

## Who Feels the Pain
The engineer carrying it alone; the studio if they leave; analysts defending numbers whose derivation they cannot explain; and whoever inherits it.

## Impact If Fixed
An adjustment added under deadline with no comment is indistinguishable later from a mistake, and only one person can tell the difference. A reason line per adjustment, backfilled while that person is here, removes the key-person risk.
