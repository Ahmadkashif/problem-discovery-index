# Build: Verified Deletion, Not Requested Deletion

**Niche:** Data Subject Request Fulfilment
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A fulfilment layer that establishes where the individual's data actually is, executes deletion where it can, and verifies afterwards that it is gone — reporting what it could not reach.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #bert #compliance #automation #data-integration #workflow-orchestration
**Contested on:** Whether a deletion is verified across every system that holds the data, or confirmed across the systems someone remembered and could reach.

## The Problem

A deletion request produces a confirmation. The confirmation says the individual's personal data has been deleted. What actually happened is that tasks were sent to a list of system owners, most responded within the window saying they had done it, and the platform recorded completion.

Three separate things are unverified. Whether the list of systems was complete, which depends on a data map built by interview. Whether each owner actually deleted rather than marking the task done. And whether the data is genuinely gone, as opposed to soft-deleted, retained in a backup, copied into a warehouse, present in a log, embedded in a model, or held by a processor who confirmed by email.

The individual receives an unqualified statement. The organisation has, in most cases, no ability to substantiate it. And nobody measures the gap, so the industry has no idea how complete fulfilment actually is — which is a remarkable position for a regulated obligation with statutory deadlines and enforcement attached.

The pieces to do better exist. Subject resolution can find which records belong to the person across systems. Deletion can be executed rather than requested where the system permits. And verification is a query — search for the identifier afterwards and see what comes back.

## Why Nobody Has Built This

**Verification produces failures nobody wants recorded.** A system that checks after deletion will find data that was not deleted, in writing, on a request with a statutory deadline. That record is discoverable and is exactly what an organisation would rather not create.

**The map is incomplete and everyone knows it.** Fulfilment inherits the accuracy of the data map. Building verification on top of an interview-derived map verifies only the part that was surveyed, which is a limitation the product would have to disclose.

**Some systems genuinely cannot delete.** Immutable backups, append-only logs and trained models are not oversights; they are design properties chosen for good reasons. The honest answer is that some data cannot be deleted on request, and nobody wants to be the product that says so.

**Subject resolution is hard.** Finding every record belonging to one person across systems that identify them differently — email in one, internal identifier in another, device identifier in a third — is a real entity resolution problem and is the prerequisite for everything else.

**Deadlines force completion over accuracy.** A statutory window creates pressure to close the request, and marking it complete is what closes it.

**Processors are taken at their word.** An organisation cannot verify that its processor deleted anything, and the contractual confirmation is the only instrument available.

## What to Build

**Resolve the subject across systems first.** Which records in which systems belong to this person, using the identifier graph — emails, internal identifiers, device identifiers, hashed values. Without this, fulfilment is a search for one identifier across systems that may not store it, which is how data gets missed.

**Execute where possible, request where not.** Direct deletion through connectors for systems that support it, with the request path reserved for those that do not. Every system moved from request to execution removes a dependency on a human marking a task complete.

**Verify afterwards, always.** Re-query each system for the identifiers after the deletion window and report what is still there. This is a straightforward check, it is the entire difference between requested and verified deletion, and nobody does it.

**Report coverage and reachability honestly to the organisation.** Which systems were searched, which were reached, which could not be, and what is known to remain — in backups until expiry, in aggregates, in a model. The internal report should be complete even where the individual receives a simpler statement.

**Handle derived data explicitly.** Aggregates, caches, search indexes, feature stores and trained models. Each needs a stated position — removed, will expire, cannot be removed and why — rather than being silently ignored, which is the current practice everywhere.

**Track processor confirmations as claims, not facts.** Record which processors confirmed, when, and in what form, and flag those who habitually confirm without detail. The organisation cannot verify, and it can at least know which of its processors have never given it a reason for confidence.

**Measure fulfilment completeness as a programme metric.** Across requests, what proportion of located data was verifiably deleted. This is the number the industry does not have and it is computable by any organisation willing to verify.

## Target Customer

Privacy operations at organisations with high request volumes — consumer platforms, marketplaces, retail — where the volume makes manual thoroughness impossible and the exposure is largest.

Data engineering as co-buyer, since subject resolution and deletion execution are their systems and their scripts, and the current arrangement lands on them as described in [[niches/privacy-tech-vendors/the-deletion-engineer/profile|🟣 The Engineer Who Must Delete It]].

The privacy platforms, for whom verification would convert their most legally exposed workflow from an orchestration into an assurance.

## Impact If Built

The confirmation sent to an individual could be substantiated, which it currently cannot be at most organisations.

Verification after deletion is a query and would immediately reveal how much data survives a fulfilment — a number nobody in this industry has and everybody assumes is small.

And handling derived data explicitly would force organisations to take a position on models, aggregates and backups, which are the places deletion quietly fails and which every current process passes over in silence.
