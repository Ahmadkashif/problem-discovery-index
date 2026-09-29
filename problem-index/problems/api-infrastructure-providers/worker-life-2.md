# API Product Manager Deprecating Blind

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Worker Life Changing
**One-liner:** API product managers stop announcing deprecations into silence and extending deadlines indefinitely, because they can see exactly who is still calling and whether migration is progressing.
**Tags:** #gradient-boosting #survival-analysis #graph-neural-networks #time-series-forecasting #confidence-intervals #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
Someone owns the API surface. Their job includes retiring what should not exist any more — old versions, superseded endpoints, fields that were a mistake — and it is the part of the role that reliably fails.

The process is faith-based. Announce the deprecation. Add a response header. Publish a migration guide. Set a date. Wait. As the date approaches, discover that traffic has barely fallen and that nobody knows who the remaining callers are. Extend. Repeat. Eventually stop announcing, because announcements that never conclude train everyone to ignore them.

The product manager cannot answer the questions that would make the decision safe. Who is still calling this. Are they important. Have they started migrating. What would actually break if it were switched off. What is the cost of maintaining it another year.

So they maintain everything, the surface grows monotonically, and the engineering team's capacity is progressively consumed by supporting the past.

## Why It Matters to the Worker
API product management is a role defined by responsibility without authority. The product manager owns the surface and cannot compel any consumer to migrate — internal teams have their own priorities and external consumers have none of theirs.

Failing repeatedly at a visible, stated commitment is demoralising in a specific way. Deadlines announced and abandoned are public, and the role's credibility erodes each time, which makes the next deprecation harder.

There is also an escalating maintenance burden that nobody quantifies. The cost of the accumulated surface is paid by engineering across every release and never appears as a line item, so the argument for a deprecation programme has no numbers behind it and loses to feature work indefinitely.

## What a Solution Looks Like
Consumer visibility from traffic. Who is calling, how often, whether their usage is growing or decaying, and how it compares to their adoption of the replacement — all derivable from the gateway and none of it currently surfaced.

Migration progress as a tracked metric rather than a hope. Each consumer's transition from old to new is observable in their traffic mix, and a deprecation should have a burndown like any other project.

Impact assessment for the switch-off decision: which consumers would break, how critical each is, and what the blast radius actually looks like. That turns an unbounded risk into a known one.

Targeted outreach rather than broadcast. A deprecation notice should reach the specific teams still calling, with their own usage attached — this endpoint, this many calls last week, here is your replacement — which is dramatically more effective than a changelog entry.

And the maintenance cost quantified: what the retained surface costs in test time, incident exposure and engineering attention, so the deprecation programme can win a prioritisation argument for once.

## Impact If Solved
API surfaces only ever grow because retirement is a faith-based process with no feedback loop, and the accumulated cost is real and unmeasured. Traffic-derived consumer visibility and migration burndown turn deprecation into a managed project, which is the only way the surface ever gets smaller.
