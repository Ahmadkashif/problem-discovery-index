# Managed Infrastructure, Unmanaged Database

**Niche:** [[niches/database-platform-vendors/managed-database-services/profile|Managed Database Services]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Managed services handle provisioning, patching, backup and failover, and leave the customer every decision that actually requires database expertise.
**Tags:** #gradient-boosting #time-series-forecasting #change-point-detection #optimization-fundamentals #confidence-intervals #evaluation-metrics #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor here is fighting to run a database well enough that the customer never thinks about it — and that contest is fought on latency in one market and on query cost at scale in another, which is why this niche is not terminal and is decomposed below.

## The Problem
A team adopts a managed database and is relieved of hardware, patching, backups and replica configuration, which is genuinely valuable. They are not relieved of choosing the right instance size, setting the connection pool, deciding which indexes to create and drop, knowing that a particular query will not scale, planning a migration that will not lock the table, or recognising that autovacuum is falling behind. Every one of those requires the specialist they adopted the managed service to avoid needing. When the database degrades, the vendor's position is that the infrastructure is healthy, which is true and is not what the customer thought they were buying.

## Why Nobody Has Built This
The managed boundary was drawn at the infrastructure because that is where the vendor's operational confidence ends: patching a host is safe and reversible, and dropping an index or changing a plan-affecting parameter is neither. The caution is reasonable and has been applied uniformly rather than to the cases that warrant it, which leaves a large set of safe, mechanical improvements unautomated alongside the genuinely risky ones. The vendors also hold fleet-wide knowledge of what works and use it for capacity planning rather than for customer operation. And the boundary is commercially convenient, since operability problems are the customer's.

## What to Build
Move the managed boundary up, safely and in stages. Automate the reversible and mechanical first: statistics maintenance tuned to churn, vacuum and reclamation scheduling, connection pool sizing from observed behaviour, instance sizing from observed resource use including the resources the generic metrics miss, and cache configuration — each of which is safe, well understood, and currently left to a customer who does not know the engine. Recommend with evidence for the consequential decisions — index creation and removal, plan-affecting parameters, partitioning — with the reasoning shown and the change applied under supervision with automatic reversion, which is the deployment pattern the release-safety niche describes and is directly applicable. Draw on the fleet: this workload resembles thousands the vendor has seen, and what worked for them is the strongest available prior and is currently used for nothing customer-facing. State the boundary explicitly, so a customer knows which decisions are the vendor's and which remain theirs, since the present ambiguity is what makes the disappointment sharp. And measure operability rather than availability, because uptime is the metric that lets a vendor say the infrastructure is healthy while the customer's database is failing.

## Target Customer
Platform teams who adopted managed services to avoid needing a specialist and still need one, and the managed service vendors competing on operability rather than on engine features.

## Impact If Built
The gap between managed infrastructure and a managed database is where the customer's actual difficulty lives, and it is where the vendor's fleet knowledge would be most valuable. Automating the safe and mechanical set first is what makes the boundary move without the risk the vendors have reasonably avoided.
