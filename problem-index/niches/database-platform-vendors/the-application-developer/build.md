# Fine Locally, Catastrophic at Scale

**Niche:** [[niches/database-platform-vendors/the-application-developer/profile|The Application Developer]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Application developers write queries whose production behaviour they cannot predict, discover the problem when data volume grows, and are then blamed for a decision made with no information available at the time.
**Tags:** #graph-theory #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor that takes this seriously is fighting to tell a developer how a query will behave in production at the moment they write it — and whoever does that takes the developer, because the alternative is discovering it when the data grows and being blamed for it.

## The Problem
A developer writes a query that filters on a column and sorts by another. Locally, against four hundred rows, it returns instantly. In production the table has forty million rows, no index covers the combination, and the query sorts the whole filtered set in memory. It passes review, because the reviewer also cannot see the plan. It is fine for eighteen months, until one customer's data reaches a size where the query takes eleven seconds and the connection pool saturates behind it. The incident review identifies the query. The developer had every reason to believe it was fine and no available means of finding out otherwise.

## Why Nobody Has Built This
The database's knowledge lives in production and the developer works locally, and nothing carries the former to the latter. Showing a plan against production statistics from a development environment is entirely possible — the statistics are a small object and the planner can be asked hypothetically — and no product does it. Object-relational mappers deliberately hide the generated query, which is their purpose and which removes the developer's ability to see what they wrote. And the feedback loop is measured in months, which is far too long for anybody to learn from.

## What to Build
Bring production's knowledge to the moment of writing. Make the plan against production statistics available in the development environment and in the code review, which requires only exporting the statistics and asking the planner hypothetically, and is the single most valuable change available here. Flag the small enumerable set of known anti-patterns statically — an unbounded result set, a sort without a supporting index, a filter on a function-wrapped column, a query whose cost grows super-linearly with a table that is growing — since these account for most production surprises and are detectable from the query and the schema alone. Project behaviour at future data volumes, since the specific failure is a query that is fine now and will not be, and the growth trend is known. Show the generated query for object-relational mapper code, in the review, because a developer who cannot see what they wrote cannot be responsible for it. Attribute production slow queries back to the code and the change that introduced them, so the feedback loop closes in days rather than months. And rank by consequence, since a warning on every query trains people to ignore all of them.

## Target Customer
Platform engineering teams, database and developer tooling vendors, and the object-relational mapper and framework projects through which most application queries are actually written.

## Impact If Built
Production statistics are a small object and the planner will answer hypothetically, which makes plan-at-write-time an integration rather than an invention. Projecting behaviour at future volumes addresses the specific failure mode — fine now, not later — that causes most of these incidents.
