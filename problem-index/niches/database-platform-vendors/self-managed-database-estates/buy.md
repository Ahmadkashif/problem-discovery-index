# The Managed Service Automation, Unbundled

**Niche:** [[niches/database-platform-vendors/self-managed-database-estates/profile|Self-Managed Database Estates]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every capability a managed database service provides exists as open components — failover, backup, pooling, monitoring, operators — and assembling them into something operable is left to the customer.
**Tags:** #graph-theory #change-point-detection #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give an organisation running its own databases the operability a managed service provides, without requiring it to move them — and whoever does that takes an enormous installed base that cannot use anything currently on offer.

## The Problem
High availability managers, backup tools, connection poolers, monitoring exporters and container operators all exist as mature open source components, and a managed service is substantially an integration of equivalents with an operations team behind it. The self-managed organisation is handed the components and expected to be the integration and the operations team, which is exactly the work they adopted a database to avoid.

## What Already Exists
Open source high availability and failover managers; backup and point-in-time recovery tools; connection poolers; monitoring exporters with extensive metric coverage; database operators for container platforms; and configuration management. Every component is mature and widely used.

## The Customization Gap
The adaptation is from components to an operable system in an environment the vendor does not control. It requires: (1) an opinionated integrated assembly rather than a toolkit, since the value is precisely in not having to make forty integration decisions, and a product that offers configurability in place of opinion reproduces the problem; (2) heterogeneity tolerance, because this estate spans versions, operating systems, deployment models and configurations, and a product that requires uniformity excludes the customers who most need it; (3) safe operation without control of the environment, meaning every automated action must be verifiable and reversible in a setting the vendor cannot inspect fully — which is a stricter requirement than a managed service faces and is the real engineering difficulty; (4) an agent and permission model that a security function will approve, since these environments are frequently the ones with the strongest controls; and (5) incremental adoption, because a product that must own the whole estate before providing value will never get past the first database.

## Target Customer
Enterprise database teams, database software vendors with self-managed installed bases, and the open source ecosystem projects whose components this would integrate.

## Impact If Solved
Every component exists and the integration is the product, which is the same observation that makes managed services valuable and has not been offered to the population that cannot use them. Heterogeneity tolerance and verifiable reversible actions are the two adaptations that distinguish this from a managed service's internals.
