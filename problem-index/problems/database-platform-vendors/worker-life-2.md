# The Developer Writing Queries Blind

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Type:** Worker Life Changing
**One-liner:** Application developers write queries whose production behaviour they cannot predict, discover the problem when data volume grows, and are then blamed for a decision made with no information available at the time.
**Tags:** #gradient-boosting #graph-theory #large-language-models #time-series-forecasting #confidence-intervals #evaluation-metrics #automation #worker-facing

## The Problem
An application developer writes a query, or writes code that generates one through an object-relational mapper. It works. Tests pass against a small development dataset. It ships.

Six months later it is the slowest query in production, because the table grew, or because the ORM emitted a query per row in a loop, or because the join order that was fine at ten thousand rows is not fine at ten million, or because an index that made it fast was on a column the query no longer filters on.

The developer had no way to know. Their development database has a fraction of the data and none of the concurrency. The query plan they could have inspected requires knowing how to read one. The ORM abstracted away the generated SQL specifically so they would not have to think about it.

Then the incident happens and the conversation is retrospective. The developer is asked why they wrote a query that does not scale, and the honest answer — that nothing told them, at any point in the process, that it would not — is accurate and unhelpful.

## Why It Matters to the Worker
Being responsible for behaviour you had no way to observe is the same pattern that appears in cloud cost, and it is equally demoralising here. The feedback arrives months late, from a system the developer does not have access to, in the form of an incident.

It also produces defensive engineering. Developers who have been burned add caching everywhere, avoid joins reflexively, or route everything through a service owned by someone else. None of this comes from evidence about what is actually expensive.

And the knowledge required is genuinely specialised. Reading a query plan, understanding index selectivity and reasoning about join strategies is database expertise, and expecting every application developer to have it is unrealistic — which is precisely why the tooling should carry it.

## What a Solution Looks Like
Feedback at authoring time. A query written in an editor should carry an assessment against production-like statistics — the plan it would take, whether it uses an index, how it scales with table growth — before it is committed. The statistics needed are on the production system and the developer does not need access to the data to use them.

Anti-pattern detection in generated SQL, since the query-per-row loop is the single most common ORM failure and is detectable from the emitted statements in a test run.

Growth projection rather than a snapshot. The useful statement is that this query is fine now and will degrade past a particular table size, which converts an invisible cliff into a known date.

Review-time surfacing, so that a change introducing a query with a poor plan is flagged in the pull request where it can be discussed cheaply.

And attribution back to source. When a slow query appears in production, tracing it to the code that generated it — which ORM call, which file, which line — closes a loop that currently requires a specialist to trace by hand.

## Impact If Solved
Query performance problems are authored months before they manifest, by developers with no way to see what they were creating, and surface as incidents that produce blame rather than learning. Moving the feedback to authoring and review time is where every other class of software defect was moved decades ago, and the database platform is the only party holding the statistics that make it possible.
