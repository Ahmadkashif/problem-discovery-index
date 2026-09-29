# Self-Managed Database Estates

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to give an organisation running its own databases the operability a managed service provides, without requiring it to move them — and whoever does that takes an enormous installed base that cannot use anything currently on offer.

## Profile
**Market Size:** ~$3.2B US attributable to self-managed database operations and tooling
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Very Low — the operability improvements of the last decade went to managed services
**Target Buyer:** Enterprise database and infrastructure teams
**Automation Potential:** High — the same automation applies and has not been packaged for this audience

## What Makes This a Distinct Niche
A very large number of production databases are not managed services and will not be for years: they run on virtual machines and hardware in data centres and colocation facilities, in regulated environments where the data cannot move, in estates acquired through acquisition, on versions too old for a managed service to accept, and in organisations whose database teams are perfectly capable and simply have not migrated. Nearly all of the operability progress of the last decade — automated failover, backup verification, tuning advisors, performance insight — was delivered as a feature of a managed service rather than as software, which means this population has been structurally excluded from it. They run scripts written by a predecessor, a monitoring configuration from 2018, and a backup restoration procedure nobody has tested this year. The contest is packaging modern operability as something that runs against a database rather than as a service the database must move into.

## Current Tools & Gaps
Open source high availability and backup tooling, vendor support contracts, monitoring products, and a large body of accumulated scripts. The gaps: high availability is assembled from components and its failover path is rarely tested; backups are taken and restoration is rarely verified, which is the single most common serious finding in this population; version currency is poor because upgrades are manual and risky, leaving known vulnerabilities in place; the fleet is frequently uninventoried, so nobody knows how many databases exist or what versions they run; and the expertise is concentrated in one or two people whose departure is an organisational risk nobody has quantified.

## Problems
- [[niches/database-platform-vendors/self-managed-database-estates/build|🔨 Build: Operability Delivered Only as a Service]]
- [[niches/database-platform-vendors/self-managed-database-estates/buy|🛒 Buy: The Managed Service Automation, Unbundled]]
- [[niches/database-platform-vendors/self-managed-database-estates/fix|🔧 Fix: The Backup Nobody Has Restored]]
