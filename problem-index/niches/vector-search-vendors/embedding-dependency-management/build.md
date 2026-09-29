# The Model Changed Underneath the Corpus

**Niche:** [[niches/vector-search-vendors/embedding-dependency-management/profile|Embedding Dependency Management]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Embedding models are supplied by third parties and change under the customer, and the vector database that depends entirely on them does not record which model produced which vector.
**Tags:** #change-point-detection #evaluation-metrics #norms-and-inner-products #data-integration #automation #descriptive-statistics #dimensionality-reduction #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to keep a corpus coherent when the third-party model that produced its vectors changes underneath it — and whoever does that takes the account, because the vendor's product silently depends on something neither party controls.

## The Problem
A provider updates their embedding model behind the same name. New documents are embedded with the new model; the existing four million are not. Queries are embedded with the new model too. The new documents rank well because they share a space with the query; the old ones are effectively random. Search quality falls over weeks as the corpus mixes, nothing errors, and the team spends a month investigating chunking and index parameters. The information required to diagnose it in a minute — which model produced each vector — was never recorded.

## Why Nobody Has Built This
The embedding model is upstream of the database, which lets vendors treat it as the customer's concern, and the boundary is drawn exactly where the problem lives. Providers do not always announce updates or version them meaningfully. Re-embedding is expensive, so acknowledging the problem means proposing a costly remedy. And the failure is gradual and mixes with every other quality complaint, which makes it easy to attribute elsewhere.

## What to Build
Manage the dependency the product silently rests on. Record the model identity and version with every vector, which is a few bytes, is the precondition for every other capability here, and turns a month-long investigation into a query. Detect provider-side drift by re-embedding a fixed canary set on a schedule and comparing, since providers change models without announcement and this is the only reliable detection available. Block or quarantine writes that would mix spaces, so the corpus cannot silently become incoherent — a hard guard is the right default because there is no useful partially-mixed state. Support dual-index migration: build the new space alongside, serve from the old, cut over on verified quality, which the fix note develops. Estimate migration cost and duration before it starts, since teams currently begin and discover. Compare candidate models on the customer's own queries and corpus, because the published leaderboards are on general corpora and the customer's domain is what matters — and this comparison is the thing that makes a migration a decision rather than a reaction. Support partial re-embedding prioritised by query traffic, so the documents people actually search get the new space first. And expose the provider's deprecation timeline in the product, since the migration is frequently forced by a date the team has not noticed.

## Target Customer
Every team whose vectors came from a third-party model, the vector vendors whose product depends on it, and the embedding providers whose customers have no migration path.

## Impact If Built
The category's core product silently depends on an artefact neither party controls and does not record which model made which vector. A few bytes per vector turns a month-long investigation into a query, and a canary set is the only reliable detection of an unannounced provider change.
