# The Build History Is in a Different Tool

**Niche:** [[niches/game-analytics-vendors/internal-cause-attribution/profile|Internal Cause Attribution]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Answering why the metric moved starts with opening four tools and writing down dates.
**Tags:** #quick-win #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #change-point-detection #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to establish which of a studio's own actions moved a metric, from data the studio already holds in four different systems — and whoever joins them takes the account.

## The Problem
The first twenty minutes of every investigation are spent reconstructing what happened. The analyst opens the build system, the config console, the content calendar and the campaign dashboard, notes the dates, and assembles a timeline in a document. They do this every time, from scratch, and the timeline is discarded when the investigation ends. Over a year this is a substantial amount of skilled time spent on clerical reconstruction.

## Why It's Still Broken
Nobody maintains the timeline — a record that is reconstructed on demand and discarded afterwards will be reconstructed every time, however many times it is needed. The systems have no shared calendar. Each is owned by a different team. And twenty minutes never feels worth fixing.

## What a Fix Looks Like
Keep the timeline standing rather than rebuilding it. Maintain one shared change calendar covering builds, config, content and campaigns, which is the fix and can start as a shared calendar before it is ever a pipeline. Have each team post their changes to it as part of their own process, which is the only version that stays current. Include enough detail to be useful — what changed, for whom, at what rollout percentage. Keep it queryable by date range, since that is the only access pattern that matters. Overlay it on the main dashboards, which makes it useful to everyone rather than only to analysts. Retain history rather than showing only the upcoming schedule, as investigations look backwards. Automate the feeds from systems that have interfaces, which is most of them. Record confirmed causes against the entries so the calendar accumulates explanations. Assign one owner for the calendar's upkeep, which is what stops it decaying. And start with builds and config alone rather than waiting for a complete integration.

## Who Feels the Pain
Analysts doing clerical work under deadline; product leads waiting for an answer that started with twenty minutes of admin; teams whose changes are invisible to everyone else; and every investigation, which starts from nothing.

## Impact If Fixed
A record that is reconstructed on demand and discarded afterwards will be reconstructed every time, however many times it is needed. One standing shared change calendar removes the first twenty minutes of every investigation.
