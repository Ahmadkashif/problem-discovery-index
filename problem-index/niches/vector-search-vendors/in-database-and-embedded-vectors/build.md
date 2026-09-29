# The Vectors and the Rows That Disagree

**Niche:** [[niches/vector-search-vendors/in-database-and-embedded-vectors/profile|In-Database & Embedded Vectors]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A document is updated in the application database and its vector is updated by a separate asynchronous process, and every failure of that process leaves a search index that confidently returns stale content.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #automation #compliance #change-point-detection #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to be good enough inside the system the developer already runs — and whoever does that takes the market, because the buyer's real alternative is not another vendor, it is not adopting one.

## The Problem
A knowledge base article is edited to correct a dangerous instruction. The row updates transactionally. The embedding job that should re-vectorise it fails silently — a rate limit, a timeout, a deploy that dropped the queue — and the old vector remains. The assistant retrieves the superseded text and repeats the dangerous instruction. A document is deleted for legal reasons and its vector survives, so a supposedly removed passage keeps surfacing. Both failures are invisible: the search works, the results look plausible, and nothing compares the index against the source.

## Why Nobody Has Built This
The embedding step is a call to an external service, which cannot participate in the database transaction, so eventual consistency is genuinely forced by the architecture. Vendors treat synchronisation as the application's responsibility, which is technically defensible and leaves the hardest correctness problem with the least-equipped party. Nobody checks, because checking requires comparing two systems and no tool does it. And the failure is silent by construction.

## What to Build
Make the vector a derived property of the row rather than a separate object. Manage the embedding lifecycle inside the database: a trigger or change stream that marks a row's vector stale on update and a worker that re-embeds with retries, backoff and a dead-letter path — so the staleness is represented in the data rather than living in a queue nobody watches, which is the structural fix. Expose staleness in query results, so an application can choose to exclude or flag a stale vector rather than serving it unknowingly. Make deletion synchronous and transactional, since a surviving vector after a deletion is a compliance failure and is strictly easier to get right than an update. Run a continuous reconciliation between rows and vectors and report the drift count, which is cheap, catches everything the pipeline missed, and is the standing metric nobody has. Version the embedding model with each vector, which the embedding dependency niche develops and which is what makes a corpus-wide re-embedding tractable. Handle partial re-embedding under a model change without a full rebuild. And make this the default behaviour rather than a pattern in the documentation, because the developer choosing an in-database vector is explicitly buying the absence of things to get right.

## Target Customer
Application developers, small platform teams, and the database and extension vendors for whom this is the natural differentiator against a dedicated service.

## Impact If Built
Stale and orphaned vectors are silent by construction and are the dominant correctness failure at this scale. Representing staleness in the row and reconciling continuously catches what the pipeline missed; transactional deletion closes the compliance case outright.
