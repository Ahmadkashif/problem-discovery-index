# Two Embedding Spaces in One Index

**Niche:** [[niches/vector-search-vendors/embedding-dependency-management/profile|Embedding Dependency Management]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Migrating to a new embedding model means re-embedding everything, there is no safe intermediate state, and teams end up running for weeks with a corpus half in each space.
**Tags:** #norms-and-inner-products #evaluation-metrics #data-integration #automation #descriptive-statistics #workflow-orchestration #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to keep a corpus coherent when the third-party model that produced its vectors changes underneath it — and whoever does that takes the account, because the vendor's product silently depends on something neither party controls.

## The Problem
A team decides to move to a better embedding model. Re-embedding forty million chunks takes eleven days of provider throughput. During those eleven days the index contains both spaces, and a query embedded in either one retrieves coherently from part of the corpus and randomly from the rest. There is no ordering of the work that avoids this, because the problem is not the order — it is that similarity between the two spaces is meaningless. The team either accepts degraded search for eleven days or builds a parallel deployment by hand, which nothing in the product supports.

## Why It's Still Broken
The mixed state is a genuine correctness problem rather than a performance one, and vendors have treated migration as an operational exercise for the customer. Building a second index doubles storage and requires routing logic the product does not offer. Re-embedding cost makes teams delay until a deprecation forces it, which is the worst moment. And nobody has framed this as a product requirement because the embedding model is nominally outside the boundary.

## What a Fix Looks Like
Make the two-space migration a supported operation. Support parallel indexes per embedding space with explicit routing, so a query is answered from one coherent space and never from a mixture — this is the correctness fix and everything else is convenience around it. Cut over on measured quality, comparing the new space against the old on the customer's own queries before switching, which turns a leap into a decision. Support a shadow period where both are queried and compared without the new one serving, which is how the quality comparison is obtained honestly. Prioritise re-embedding by query traffic, so the documents that are actually searched move first and the practical quality impact of a long migration is small even though its completion is distant. Checkpoint and resume the migration, since an eleven-day job will be interrupted. Report progress in terms that matter — share of query traffic served from the new space — rather than share of documents processed. Provide rollback while both spaces exist, which is cheap during the window and impossible after. And estimate cost and duration before the first vector is embedded, because teams currently commit without knowing either.

## Who Feels the Pain
Teams running degraded search for weeks during a migration; those delaying a beneficial model change because the migration is unmanageable; and the ones forced into it by a deprecation date with no plan.

## Impact If Fixed
There is no safe partially-migrated state because cross-space similarity is meaningless, and the product offers no alternative to living in one. Parallel spaces with explicit routing is the correctness fix, and prioritising by query traffic makes a long migration practically painless well before it finishes.
