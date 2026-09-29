# Connection and Resource Configuration

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every engine ships hundreds of tunable parameters with defaults that suit almost no workload, and the guidance available is a decade of blog posts written for different hardware.
**Tags:** #gradient-boosting #bayesian-optimization #gaussian-processes #confidence-intervals #time-series-forecasting #evaluation-metrics #automation

## The Problem
A database's behaviour under load is governed by configuration: memory allocation for shared buffers and work areas, connection limits, checkpoint behaviour, autovacuum aggressiveness, parallelism settings, statement timeouts. The defaults are conservative and generic because they must run anywhere.

Connection management is the most consequential and most misconfigured. Each connection costs memory and process overhead, application frameworks open pools per instance, autoscaling multiplies the instance count, and the database's connection limit is reached under exactly the load that made the application scale out. The remedy — a connection pooler with correctly sized pools — is well known and requires understanding both the application's concurrency and the database's internals.

The available guidance is folklore. Blog posts written for hardware from a previous decade, rules of thumb passed between engineers, and formulas whose derivation nobody remembers. It is applied by teams without a database specialist, because the managed service was supposed to make one unnecessary.

## What Already Exists
Connection poolers (PgBouncer, ProxySQL, RDS Proxy) are mature and effective. Managed services set defaults scaled to instance size, which is better than nothing and still generic. Tuning advisor features exist in some products. Parameter groups allow configuration management. Extensive community documentation exists and is inconsistent across versions and hardware generations.

## The Customisation Gap
Workload-aware configuration is the gap. The correct settings depend on the read-write mix, transaction size, concurrency profile, working set relative to memory, and access pattern — all of which the platform observes directly and none of which feed the defaults it sets.

Fleet-derived tuning is the vendor's unique opportunity: configurations for workloads of a similar shape, and their observed outcomes, are a far better starting point than a formula. Learning the mapping from workload characteristics to good configuration across a large fleet is a well-posed problem nobody has attempted publicly.

Safe automated tuning requires careful sequencing — changing one parameter at a time, observing, and reverting on regression — which is standard practice in adaptive control and absent here.

Connection pool sizing specifically deserves a product rather than a formula, since it is the most common cause of a database-related outage and depends on facts the platform can see on both sides.

## Impact If Solved
Database configuration determines behaviour under load and is set by defaults that suit nobody, adjusted by folklore, at organisations that no longer employ specialists. Workload-aware, fleet-informed tuning is available to managed service vendors and to essentially nobody else.
