# Finding Out After It Shipped

**Niche:** [[niches/customer-data-platforms/the-data-engineer/profile|The Data Engineer]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The engineer learns about every instrumentation change from an alert after deployment, by which point the data is already wrong and the team has moved to the next sprint.
**Tags:** #change-point-detection #workflow-orchestration #automation #worker-facing #quick-win #evaluation-metrics #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to give the one person accountable for event consistency a way to enforce it on teams they do not control — and whoever does that resolves an accountability gap the whole architecture creates.

## The Problem
A team ships on Tuesday. On Thursday an alert fires because an event volume dropped. The engineer investigates, identifies the release, works out what changed, and contacts the team. The team has moved on to other work, the developer who made the change is in a different context, fixing it requires a release, and in the meantime two days of data are wrong and will stay wrong. The engineer does this several times a month. Every instance was preventable at the moment of the change, and every instance is handled after it, because the only signal available is a downstream alert.

## Why It's Still Broken
The detection is downstream by construction, since the data platform only sees events after they are emitted — the observation point is after the last moment anyone could have acted. Product teams do not tag changes as instrumentation-affecting, because they frequently do not know they are. The engineer has no visibility of roadmaps or pull requests. And a retrospective complaint is a weak intervention that damages the relationship it depends on.

## What a Fix Looks Like
Move the observation earlier. Watch the product teams' repositories for changes touching instrumentation, which is the fix and moves detection from days after deployment to the moment the code is written — the information is in a pull request and the data platform has simply never looked there. Comment on the pull request with the downstream impact, so the developer sees it in context and can decide, which is both earlier and more collegial than any alert. Detect instrumentation changes automatically rather than relying on teams to flag them, since they mostly do not know. Provide a pre-release check the team can run themselves, which respects their autonomy and removes the engineer from the path. Alert in staging rather than in production, because the same check in a lower environment costs nothing and prevents everything. Give the engineer a feed of upcoming changes rather than a feed of past breakages, which reverses their entire working posture. Make a fast fix possible where prevention failed, since some changes will ship regardless and a rapid correction limits the damage. Mark the affected data period so downstream consumers can exclude it, which prevents silent corruption of every derived number. Track prevented versus detected breaks, since that ratio measures whether the intervention works. And build the relationship on prevention rather than complaint, because the engineer's effectiveness is ultimately social and a tool that makes them the bearer of bad news undermines them.

## Who Feels the Pain
Engineers investigating breakages after the fact, repeatedly; product teams receiving complaints about changes they did not know mattered; and organisations whose customer data has permanent gaps nobody will backfill.

## Impact If Fixed
The observation point is after the last moment anyone could act, because the platform only sees events once emitted. Watching repositories and commenting on the pull request moves detection to where the decision is made and is information nobody has thought to look at.
