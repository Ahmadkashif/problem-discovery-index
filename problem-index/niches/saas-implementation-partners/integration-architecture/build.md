# The Same Dozen Systems, Catalogued

**Niche:** [[niches/saas-implementation-partners/integration-architecture/profile|Integration Architecture]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The endpoints are the same every time and the design is done from scratch every time.
**Tags:** #data-integration #graph-theory #workflow-orchestration #automation #evaluation-metrics #sets-and-logic #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to connect the same dozen enterprise systems without designing the integration from scratch on every engagement — and whoever industrialises that takes the account.

## The Problem
Enterprise integration in this market is a small set of recurring problems: synchronise accounts between two systems, push orders one way and status the other, reconcile a master record across three places, handle a nightly batch that sometimes fails halfway. The systems are the same dozen products. Every engagement designs the mapping, the error handling, the reconciliation and the sandbox strategy again, and discovers the same failure modes in testing.

## Why Nobody Has Built This
Integration platforms provide connectors and leave the pattern to the architect. Each client's data model differs enough to feel unique. The failure modes are learned in production and not written down. And the design work is billable.

## What to Build
Catalogue the patterns, including how they fail. Build a library of integration patterns per system pair with the object mappings, the error handling and the reconciliation approach, which is the core and is what every architect currently reconstructs. Record the failure modes each pattern exhibits in production, since that is the knowledge that separates an experienced architect from a new one and it is entirely undocumented. Parameterise mappings for the client-specific fields rather than rebuilding, as the variation is at the edges and the shape is stable. Provide a standard reconciliation and exception approach rather than designing one per engagement, which is where most production incidents originate. Generate the test harness and the data set from the mapping, which is a large block of mechanical work. Include the sandbox and environment strategy in the pattern, since it is redesigned every time and is the same problem. Capture volume and performance characteristics so sizing is informed rather than guessed. Update patterns as the endpoint platforms release. Record which patterns caused incidents after go-live, which is the feedback loop that makes the library authoritative. And make the library the architect's starting point rather than a reference they may consult.

## Target Customer
Implementation partners and systems integrators, solution architects, integration platform vendors, and enterprise architecture tooling providers.

## Impact If Built
The endpoints are the same dozen products every time and the design is reconstructed on every engagement, including the failure modes. A pattern library that records how each one fails is what an architect currently holds in their head.
