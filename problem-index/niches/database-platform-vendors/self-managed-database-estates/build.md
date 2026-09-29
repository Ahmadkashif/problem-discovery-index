# Operability Delivered Only as a Service

**Niche:** [[niches/database-platform-vendors/self-managed-database-estates/profile|Self-Managed Database Estates]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A decade of database operability improvements shipped as features of managed services, which structurally excluded every organisation that runs its own databases and cannot move them.
**Tags:** #graph-theory #gradient-boosting #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #compliance
**Contested on:** Every serious competitor here is fighting to give an organisation running its own databases the operability a managed service provides, without requiring it to move them — and whoever does that takes an enormous installed base that cannot use anything currently on offer.

## The Problem
A bank runs several hundred database instances across its own data centres. Failover is a pair of scripts written by an engineer who left in 2019 and has been tested twice since. Backups run nightly and the restoration procedure was last exercised during an audit. Version currency is poor because upgrading requires a window and a rehearsal nobody has time for. Performance problems are diagnosed by two people. None of this is neglect: the team is competent and the estate is large, and every tool that would have automated these things was released as a feature of a service they are not permitted to use.

## Why Nobody Has Built This
The commercial logic of the last decade pushed operability into managed services, because that is where the revenue is and because operating the database yourself makes the automation easier to guarantee. Selling software that operates somebody else's database is harder: it must work across versions, configurations and environments the vendor does not control, and the support burden is larger. The open source ecosystem produced components rather than an integrated operability product, which leaves assembly to the customer. And this population is unfashionable, which has kept vendor attention on the cloud-native customer.

## What to Build
Package operability as software that runs against an existing estate. Inventory first, since many of these organisations cannot enumerate their own databases — discovery from network, configuration management and connection records produces the list and is usually the first surprise. Failover automation with routine tested exercises, because the failover path in this population is almost universally untested and its untestedness is the single largest availability risk. Backup verification by actual restoration on a schedule, which is the most common serious finding anywhere in this estate and is entirely automatable. Version and patch currency tracking with an upgrade path that includes rehearsal against a clone of production, since risk is what blocks upgrades and rehearsal is what reduces it. The degradation detection and tuning capabilities from the other niches in this industry, delivered as software rather than as a service feature. And knowledge capture, since the expertise is concentrated in one or two people and their departure is an unquantified organisational risk — encoding the runbooks and the diagnostic reasoning is as valuable here as any automation.

## Target Customer
Enterprise database and infrastructure teams in finance, government, healthcare and manufacturing; the database software vendors whose self-managed customers are their oldest; and the consultancies currently doing this work by hand.

## Impact If Built
An enormous installed base was excluded from a decade of operability progress by a delivery-model decision rather than by any technical barrier. Backup verification and tested failover are the two highest-consequence gaps and are entirely automatable, and the inventory is usually the first thing missing.
