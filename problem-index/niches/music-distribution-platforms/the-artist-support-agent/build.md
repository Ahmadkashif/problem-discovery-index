# An Answer Instead of an Explanation

**Niche:** [[niches/music-distribution-platforms/the-artist-support-agent/profile|The Artist Support Agent]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The agent is asked where the money went and can only describe how money generally moves.
**Tags:** #worker-facing #data-integration #workflow-orchestration #large-language-models #evaluation-metrics #automation #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to let an agent answer a royalty question with an actual answer rather than a description of a process — and whoever gives them visibility into the accounting changes what support can be.

## The Problem
An artist asks why their payment dropped by half. The answer exists — a rate change in one territory, a statement that arrived late, a correction applied, a split that changed, a takedown that removed a track. The agent cannot see any of it. They have the artist's statement, the same view the artist has, and a knowledge base describing how royalties work in general. So they explain the system, the artist becomes more frustrated, and the ticket escalates to someone who can query a database.

## Why Nobody Has Built This
Support tooling was built around the ticket rather than around the account, so the agent has the conversation and not the data — a system designed to manage correspondence has no reason to expose an accounting pipeline. Royalty systems were not built to be queried per artist per question. Escalation works, so the gap persists. And nobody measures how many tickets are escalated purely for lack of visibility.

## What to Build
Give the agent the decomposition. Show the agent a line-level view of the artist's statement traced to source, which is the core and converts an explanation into an answer. Explain period-over-period changes automatically, since that is the most common question and the causes are computable. Surface the events affecting this artist — corrections, rate changes, takedowns, split updates, enforcement actions — in one timeline, because the answer is usually one of those and finding it currently requires a specialist. Show the takedown or enforcement reason where policy allows, as an artist told only that their release was removed has no route to remedy. Assemble the case before the agent opens it, so the common questions are answered before the conversation starts. Catalogue the recurring question patterns, since a handful dominate and each is automatable. Let the agent resolve rather than escalate where the fix is mechanical, as most escalations are for visibility rather than authority. Give the artist the same decomposition in their own account, which removes the ticket entirely for many questions. Measure escalation rate by cause, which shows exactly where the visibility gap is. And track how many tickets are about money versus about process, because the split will justify the work.

## Target Customer
Support leadership and agents, artists whose income depends on the answer, royalty operations teams receiving escalations, and support platform vendors.

## Impact If Built
A system designed to manage correspondence has no reason to expose an accounting pipeline, so the agent sees the conversation and not the data. A traced, line-level view with an event timeline converts most escalations into answers.
