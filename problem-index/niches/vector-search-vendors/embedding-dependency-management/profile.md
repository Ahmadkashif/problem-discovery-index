# Embedding Dependency Management

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to keep a corpus coherent when the third-party model that produced its vectors changes underneath it — and whoever does that takes the account, because the vendor's product silently depends on something neither party controls.

## Profile
**Market Size:** ~$180M US
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Low — the dependency is unmanaged
**Target Buyer:** Anyone whose vectors came from a third-party model
**Automation Potential:** Very High — detection and migration are both mechanical

## What Makes This a Distinct Niche
The vectors in these systems are produced by embedding models supplied by third parties, which change under the customer: a provider updates a model behind an unchanged name, deprecates a version, or ships a new one that is better and incompatible. A corpus embedded with one model and queried with another returns confident nonsense, because the two spaces are unrelated. Re-embedding a large corpus costs real money and days of throughput, and there is no partial state that is safe — a half-migrated index is worse than either endpoint. Nothing in the category manages this dependency, and it is the most consequential thing outside the vendor's control that the vendor is nonetheless positioned to handle.

## Current Tools & Gaps
Manual re-embedding scripts, model version strings in configuration where teams remembered, and full rebuilds as the migration path. The gaps: no per-vector record of which model produced it; no detection of a provider-side change; no safe migration path, so a corpus is either fully old or fully new with a painful interval between; no comparison of quality across models on the customer's own data; and no cost estimate before a migration begins.

## Problems
- [[niches/vector-search-vendors/embedding-dependency-management/build|🔨 Build: The Model Changed Underneath the Corpus]]
- [[niches/vector-search-vendors/embedding-dependency-management/buy|🛒 Buy: Dependency Pinning and Migration Practice]]
- [[niches/vector-search-vendors/embedding-dependency-management/fix|🔧 Fix: Two Embedding Spaces in One Index]]
