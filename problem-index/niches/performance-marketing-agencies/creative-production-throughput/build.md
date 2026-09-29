# Forty Assets a Week, Every Week

**Niche:** [[niches/performance-marketing-agencies/creative-production-throughput/profile|Creative Production Throughput]]
**Industry:** [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The account needs forty assets a week indefinitely, and the production process was designed for a campaign that ships once a quarter.
**Tags:** #workflow-orchestration #automation #diffusion-models #transformers #evaluation-metrics #convex-optimization #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to produce assets at the rate the platforms consume them, at a cost that survives the fee — and whoever wins on cost per asset and cycle time takes the volume work the whole category depends on.

## The Problem
The brief goes to a designer. The designer produces a concept. It goes for internal review, then client review, then revisions, then resizing for eleven placements, then localisation for four markets, then tagging, then trafficking into three platforms. Elapsed time: eleven days. The platform will exhaust the concept in six. The process was built when a campaign shipped quarterly and a single hero asset was adapted at leisure, and it has been asked to run continuously at ten times the volume without being redesigned. Every agency in the category is losing money on this or delivering less than the account needs.

## Why Nobody Has Built This
The pipeline is an assembly of disconnected tools with humans between them, and each step was optimised locally while nobody owns the flow — the classic condition of a process that grew rather than being designed. Generative tools sped up one step and left the queue structure intact, which moved the bottleneck rather than removing it. Review is the dominant cost and is a human coordination problem rather than a production one. And agencies price per asset, so throughput improvement reduces revenue unless the model changes with it.

## What to Build
Design the pipeline around continuous flow. Measure the whole cycle and find the actual bottleneck, which is almost always review rather than making, and which local optimisation of the making step cannot touch. Generate variations, resizes and localisations automatically from an approved master, since these are the volume and are mechanical transformations rather than creative work. Batch approvals at the concept level rather than the asset level, so a hundred derived assets inherit one decision — this is the single largest throughput change available and it is a policy choice as much as a technical one. Traffic and tag automatically into every platform, which is a manual step that also destroys the measurement when it is skipped. Enforce the concept taxonomy at production so tagging is never a separate task. Keep a library of reusable components so production compounds rather than restarting. Parallelise properly, since the current process is a queue and most of the work has no real dependency. Support the review that genuinely needs a human with fast, specific tooling rather than a thread. Report cost per asset and brief-to-live time as the operating metrics, because they are the scoreboard and most agencies do not measure either. And align the commercial model to throughput, since a pipeline that halves cost per asset under per-asset pricing halves revenue.

## Target Customer
Performance agencies and production studios, in-house creative operations, and the brands whose creative supply cannot meet their media demand.

## Impact If Built
The process was designed for a quarterly campaign and is running continuously at ten times the volume. Approving at the concept level so derived assets inherit one decision is the largest throughput change available and is mostly a policy choice.
