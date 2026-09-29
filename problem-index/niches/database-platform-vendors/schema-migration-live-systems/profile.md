# Schema Migration on Live Systems

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to make changing a schema on a live production system routine rather than an event — and whoever does that takes the database team, because every significant migration is currently planned by whoever has done one before.

## Profile
**Market Size:** ~$1.4B US attributable to schema change tooling and migration services
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — the tools are mature and their operation is expert work
**Target Buyer:** Database and platform engineering
**Automation Potential:** High — the analysis and the procedure are both formalisable

## What Makes This a Distinct Niche
Online schema change tools are mature, the safe procedures are well documented, and every significant migration is still a bespoke, anxious operation planned by whoever has done one before. The reason is that the risk is not in the mechanism but in the specifics: whether this particular change on this particular table at this particular size will take a lock, how long it will run, what it will do to replication lag, whether the application can tolerate the intermediate state, and whether it can be reversed once it has started. Those questions are answerable — the table size, the change type, the engine version and the replication topology determine most of the answer — and are answered instead by an experienced person's recollection and a maintenance window booked at two in the morning. The contest is making the analysis automatic and the execution routine.

## Current Tools & Gaps
Online schema change tools for the major engines, migration frameworks in application ecosystems, and branching database products that changed expectations for development. The gaps: the tools execute a procedure and do not analyse whether this change is safe, which is the part requiring expertise; the application-compatibility half — whether the code can run against both the old and new schema during the transition — is entirely manual and is where the worst failures come from; duration and impact are not predicted, so the maintenance window is guessed; reversal after partial completion is frequently not possible and rarely planned; and every organisation rediscovers the same set of dangerous change types independently.

## Problems
- [[niches/database-platform-vendors/schema-migration-live-systems/build|🔨 Build: Bespoke and Terrifying Every Time]]
- [[niches/database-platform-vendors/schema-migration-live-systems/buy|🛒 Buy: The Expand-Contract Pattern, Unautomated]]
- [[niches/database-platform-vendors/schema-migration-live-systems/fix|🔧 Fix: The Migration Nobody Can Reverse]]
