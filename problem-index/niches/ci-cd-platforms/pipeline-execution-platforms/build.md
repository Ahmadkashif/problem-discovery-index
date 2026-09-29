# Paying by the Minute for Work Already Done

**Niche:** [[niches/ci-cd-platforms/pipeline-execution-platforms/profile|Pipeline Execution Platforms]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most pipeline minutes are spent redoing work whose inputs have not changed, and the platforms bill for those minutes rather than eliminating them.
**Tags:** #graph-theory #dynamic-programming #gradient-boosting #optimization-fundamentals #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to be where an organisation's pipelines actually run — and that contest is fought on economics in one market and on control in another, which is why this niche is not terminal and is decomposed below.

## The Problem
A change touches one file in one service. The pipeline rebuilds eleven services, downloads four hundred dependencies, runs the full test suite and republishes six artefacts, because the pipeline was written as a sequence of steps rather than as a graph of dependencies. Almost all of that work is identical to the work done on the previous change. The platform executes it, bills for it, and has all the information needed to know it was unnecessary — the inputs to each step are the same and the outputs are already in a cache somewhere.

## Why Nobody Has Built This
Pipelines are configured as imperative scripts, which makes their inputs opaque: the platform cannot know what a shell command depends on, so it cannot skip it safely. Build systems that model dependencies properly exist and require adopting a different build tool, which is a migration most organisations will not undertake. Caching is offered as a feature the customer configures, and most configurations are copied from an example and never tuned. And the commercial incentive is inverted: a platform paid per minute has no reason to remove minutes, which is the same conflict the observability category has over ingestion.

## What to Build
Make the platform understand what changed. Infer step-level input dependencies from observed behaviour — which files a step reads, which environment it depends on, what it produces — by instrumenting execution rather than asking the customer to declare them, which is the change that makes safe skipping possible without a build system migration. Content-address the results and skip steps whose inputs are unchanged, with the skip recorded and auditable, because engineers will not accept an unexplained skip. Share the cache across the organisation rather than per pipeline or per branch, since in most estates the same work is being done by many people and the cross-user hit rate is the largest available saving. Place execution near the cache and the dependencies, since a substantial share of many pipelines is transferring data across regions. Report what was skipped and what it saved, both to justify the behaviour and because it is the number that makes the platform's value legible. And price it in a way that does not punish the vendor for saving the customer money, which is the structural reason none of this exists and is a packaging problem rather than a technical one.

## Target Customer
Platform engineering teams under build cost and duration pressure, and the vendors willing to compete on total cost of delivery rather than on minutes sold.

## Impact If Built
A large share of pipeline minutes redo unchanged work, and the platform has the evidence to know it. Inferring dependencies from observation avoids the build system migration that has limited every existing solution, and cross-user caching is the largest single saving in most estates.
