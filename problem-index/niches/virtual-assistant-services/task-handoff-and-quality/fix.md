# Fix: Nobody Counts the Round Trips

**Niche:** [[niches/virtual-assistant-services/task-handoff-and-quality/profile|Task Handoff & Quality Control]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Fix (Pain Point)
**One-liner:** A task that took four exchanges and two corrections is recorded identically to one done right the first time, so the cost of bad briefing is invisible.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #worker-facing #automation
**Contested on:** Whether the exchanges a task required will be counted as a quality signal.

## The Problem

Two tasks are completed. One was briefed clearly, done correctly, returned once, accepted. The other took a brief, two clarifying questions, a draft, a correction, a second draft and an acceptance — consuming perhaps forty minutes of the executive's attention against a task that would have taken them twenty to do themselves.

Both appear in the monthly report as one completed task. Both consume roughly similar assistant hours. Nothing anywhere records that the second one was a net loss.

The round trip count is the most direct quality measure available in this industry. It is derivable from message threads and document revisions, it should fall over the life of a placement, and it identifies exactly which task types are worth delegating to this assistant for this executive. Nobody computes it.

## Why It's Still Broken

Reporting is built around hours and task counts because those are what the agency bills and what a client asked for in a monthly summary. Round trips are a quality signal that makes the service look worse in the short run and is not something anyone requested.

The measurement also requires reading the correspondence, which sits in the client's systems and raises the access question this whole industry avoids. The assistant already has that access; nobody has proposed using it for measurement.

And the interpretation is uncomfortable for both parties: a high round-trip count is partly the assistant's execution and partly the executive's briefing, and naming the second is awkward for a service provider.

## What a Fix Looks Like

Count the exchanges and use the count, starting with the easy version.

Count per task, from the message thread and document revisions: how many clarification exchanges before work started, how many revisions after delivery, total elapsed time from brief to acceptance. Simple counting over existing correspondence.

Report it by task type. Some task types will show one exchange and some will show five, and the pattern is stable and highly actionable — a task type averaging four round trips is either badly briefed, badly matched or not suited to delegation, and the right response differs.

Watch the trend. Round trips per task should fall over the first three months as context accumulates. A placement where they do not fall is failing, visibly, in week six rather than month four, which is the early warning this industry lacks.

Attribute carefully and privately. Split the count into pre-execution clarification, which is mostly a briefing signal, and post-delivery revision, which is mostly an execution signal. Share it with the account manager rather than publishing it at either party, and use it to have a specific conversation rather than a general one.

Feed the worst task types back into the briefing fix. A task type with a consistently high clarification count has a missing constraint that is missing every time, and naming it once fixes it permanently.

And put it in the monthly report alongside tasks completed, which changes what the client and the agency are both looking at.

## Who Feels the Pain

Executives, who experience delegation as consuming their attention and cannot say which tasks are responsible. Assistants, who absorb rework caused by briefs they could not have executed correctly and are judged on the outcome. Account managers, with satisfaction scores and no operational detail. And agencies, whose quality management has no metric between "the client is happy" and "the client has asked for a replacement".

## Impact If Fixed

The industry gets an operational quality metric derived from correspondence that already exists. Failing placements become visible in week six through a trend that does not fall. And the task types that are not worth delegating get identified specifically, which is what turns a cancelled engagement into a re-scoped one.
