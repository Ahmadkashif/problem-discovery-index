# Build: Deletion as a Platform Capability

**Niche:** The Engineer Who Must Delete It
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A deletion capability built into the data platform — subject-keyed, propagating downstream, verifiable, with an honest position on what cannot be deleted — instead of a script per request.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation #data-integration #workflow-orchestration #worker-facing
**Contested on:** Whether deletion is a capability the systems were built with, or a script an engineer writes each time.

## The Problem

Deletion is treated as an operation to be performed rather than as a capability to be built. Each request arrives as a task, and the engineer's job is to make the data go away across systems that were not designed for it.

The specific difficulties recur at every organisation. A columnar warehouse where deleting one row means rewriting a partition. Append-only event streams. Object storage with no index by subject. Application logs containing identifiers in unstructured text. Search indexes built from the data. Feature stores holding derived values. Caches. Non-production environments seeded from production. And backups, which are immutable deliberately.

Each organisation solves these independently, badly, under deadline. The solutions are not shared because they are scripts in a repository rather than a pattern anyone has written up. And the resulting deletion is unverified — the engineer runs the script, sees no errors, and reports completion.

The underlying failure is architectural. If systems had been designed with a subject key and a deletion path, this would be a routine operation. They were not, because deletion was never a design requirement, and it still is not in most architecture practice.

## Why Nobody Has Built This

**It is an engineering problem sold into a legal budget.** Privacy platforms are bought by counsel and stop at the ticket. The capability needed is data platform engineering, which a privacy vendor does not build and a data platform vendor has not prioritised.

**Retrofitting deletion is expensive.** Adding a subject key and a deletion path across an existing estate is a substantial engineering programme with no feature output, which loses every prioritisation argument until a regulator creates a deadline.

**Backups genuinely have no clean answer.** Immutability is a security property nobody should give up. The honest position — data persists in backups until expiry, here is the period — is available and is rarely stated plainly.

**Derived data is conceptually hard.** Whether a model trained on someone's data must be retrained, and whether an aggregate computed from it must be recomputed, is legally unsettled and technically expensive. Most organisations resolve this by not thinking about it.

**Verification creates evidence of failure.** Checking afterwards produces a record of what was not deleted, which is the same disincentive that runs through this whole category.

**Nobody owns the pattern library.** The solutions are similar across organisations and are never shared, because they are internal scripts and nobody publishes their deletion architecture.

## What to Build

**Establish a subject key across the estate.** A consistent identifier for the data subject propagated through every system that holds their data, so deletion is a keyed operation rather than a search. This is the architectural prerequisite and everything else is far easier once it exists.

**Provide deletion primitives per system type.** Warehouse partition rewriting, event stream compaction, log redaction, object storage indexing by subject, search index removal, cache invalidation. A library of implemented patterns per common platform, so no organisation solves the warehouse problem from scratch again.

**Propagate deletion downstream automatically.** Change data capture carrying deletions through pipelines, so removing a row from the operational database removes it from everything derived. This is standard data engineering applied to a problem where it is essentially unused.

**Verify and report.** Re-query after deletion and confirm absence, per system, with the result recorded. The engineer gains evidence rather than a claim, which is protective for them as well as for the organisation.

**Take an explicit position on backups.** A stated retention period, a documented process for handling a restore that reintroduces deleted data, and honest disclosure. The restore case is the one nobody handles and it is the mechanism by which deleted data reappears.

**Handle derived data with a stated policy.** Aggregates recomputed or exempted, feature stores purged, indexes rebuilt, models flagged with a documented position. The answer may legitimately be that a model is not retrained; what is not acceptable is that nobody considered it.

**Make deletability a design requirement.** A checklist item in architecture review for new systems: how will a subject's data be deleted from this. Preventing the next generation of undeletable systems is worth more than retrofitting the current one.

## Target Customer

Data platform and engineering leadership at organisations with high request volumes, where the bespoke-script approach has already become an operational burden.

The data platform vendors themselves, for whom subject-keyed deletion is a natural capability their customers repeatedly build badly.

Privacy engineering functions as the internal advocate, since they experience the failure and cannot fix it from their side of the organisation.

## Impact If Built

Deletion becomes a platform capability invoked rather than an engineering task performed, which is the difference between an operation that scales and one that does not.

A published pattern library would stop every organisation solving the same warehouse, log and stream problems independently, which is a substantial industry-wide duplication.

And making deletability a design requirement is the intervention with the longest payoff: the current difficulty exists entirely because nobody asked the question when the systems were built.
