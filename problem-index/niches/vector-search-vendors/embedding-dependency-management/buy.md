# Dependency Pinning and Migration Practice

**Niche:** [[niches/vector-search-vendors/embedding-dependency-management/profile|Embedding Dependency Management]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software dependency management solved pinning, deprecation signalling and staged migration decades ago, and the most consequential dependency in a vector deployment is unpinned by construction.
**Tags:** #data-integration #compliance #automation #workflow-orchestration #evaluation-metrics #change-point-detection #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to keep a corpus coherent when the third-party model that produced its vectors changes underneath it — and whoever does that takes the account, because the vendor's product silently depends on something neither party controls.

## The Problem
Depending on an external component that changes is the oldest problem in software distribution, and the answers are mature: pin exact versions, declare compatibility ranges, signal deprecation on a published timeline, support two versions during migration, and provide tooling that reports what would break. A hosted embedding model behind a stable name is a dependency with none of that — no immutable version, no compatibility declaration, and frequently no notice.

## What Already Exists
Package managers with exact pinning and lock files; semantic versioning as a compatibility contract; deprecation policies with published sunset timelines; multi-version support during migration windows; dependency scanning that reports what a change would affect; and content-addressed artefacts whose identity derives from their contents.

## The Customization Gap
The adaptation is to a dependency that is a remote service producing values rather than a library. It requires: (1) behavioural fingerprinting as the version identity, since the provider's version string is unreliable and the honest identity of an embedding model is what it outputs on a fixed probe set — this substitution is the central technique and nothing else in the analogy works without it; (2) compatibility expressed as embedding-space equivalence rather than as an interface contract, which is a genuinely new kind of compatibility statement and is what a provider should be publishing; (3) migration tooling that accounts for the cost of re-deriving every stored value, which package migration never has to do and which dominates here; (4) staged migration with both spaces live, which is closer to a database migration than a dependency upgrade; and (5) pressure on providers for immutable, addressable model versions, since the correct fix is upstream and the vendors are the party with the standing to ask.

## Target Customer
Vector search vendors, application teams, and the embedding model providers who are the unpinnable dependency in this arrangement.

## Impact If Solved
The most consequential dependency in these deployments is unpinnable by construction. Behavioural fingerprinting on a probe set supplies the version identity the provider does not, and it is the substitution that makes the whole mature practice applicable.
