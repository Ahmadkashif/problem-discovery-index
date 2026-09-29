# Schema Migration on Live Systems

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Online schema change tools are mature and well understood, and every significant migration is still a bespoke, anxious operation planned by whoever has done one before.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #workflow-orchestration #automation

## The Problem
Changing a schema on a live database is one of the routine operations most likely to cause an outage. Adding a column with a default, adding an index, changing a type, adding a constraint, dropping a column that something still references — each has a safe form and an unsafe form, and the unsafe form takes a lock on a large table during production traffic.

The safe procedures are documented and the tools that implement them are mature. Yet every substantial migration at every company is planned individually: someone estimates the duration, chooses a low-traffic window, prepares a rollback, arranges for people to watch, and runs it with the tension the operation deserves.

The reason is that the tools do not know the answers that determine risk. How long will this take on a table of this size with this traffic. Will it lock, and for how long. Is there enough disk for the temporary copy. What breaks if it is interrupted halfway. Is anything still using the column being dropped.

So the expertise required is not in running the migration but in predicting its behaviour, and that expertise is scarce and unevenly distributed.

## What Already Exists
Online schema change tools (gh-ost, pt-online-schema-change, native online DDL in modern engines) implement the safe procedures well. Migration frameworks in every application stack handle versioning and ordering. Expand-and-contract patterns are well documented. Some platforms offer branching and preview databases that make testing easier. Linters exist that flag unsafe migration statements.

## The Customisation Gap
Duration and lock prediction is the missing capability and is the input to every decision around a migration. It is estimable from table size, row width, index count, traffic pattern and engine version, and the vendor has observed the same migration shapes across thousands of customers — which makes it a straightforward regression on a large labelled dataset that nobody has assembled.

Column and index usage verification closes the most common footgun. Dropping a column that something still reads is a self-inflicted outage, and the query log answers definitively whether anything has touched it in the retention window.

Blast radius analysis is the third gap: which queries will change plan, which application paths will be affected, and whether any of them are on a hot path.

Safe rewriting is the constructive version. A migration expressed as an unsafe statement can frequently be rewritten into the safe multi-step equivalent automatically, and linters currently flag the problem without solving it.

## Impact If Solved
Schema migration is a routine operation that carries outage risk and is planned by scarce expertise at every company independently. Predicting duration, locking and blast radius from a fleet-wide corpus of comparable migrations converts an anxious bespoke operation into a scheduled one with a stated risk.
