# No Way to Know Whether It Was Needed

**Niche:** [[niches/vector-search-vendors/the-index-rebuild-operator/profile|The Index Rebuild Operator]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Rebuilds are scheduled monthly, or when search feels slow, and nobody measures recall before or after, so the operation is repeated on faith and skipped on optimism in equal measure.
**Tags:** #evaluation-metrics #descriptive-statistics #change-point-detection #confidence-intervals #automation #hypothesis-testing #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make an index rebuild something that happens automatically, online and on evidence, rather than something a person schedules and watches — and whoever does that takes the account, because the rebuild is the category's worst operational experience.

## The Problem
Two organisations run identical workloads. One rebuilds monthly and has never needed to, spending a night a month and doubled capacity on an operation that changes nothing. The other has not rebuilt in a year, has lost eleven points of recall, and does not know. Neither has any measurement distinguishing their situations. The decision is made on a calendar entry someone created during onboarding, or on a vague sense that search has got worse, and both organisations believe they are managing it appropriately.

## Why It's Still Broken
Recall in production is not measured, so the input to the decision does not exist — which is the same gap the drift niche addresses and this is where it costs an operator directly. A calendar is a defensible default nobody gets criticised for. Vendors recommend periodic rebuilds, which is safe advice and converts an unsolved measurement problem into a customer routine. And the organisation that has over-rebuilt for a year has no way to discover it.

## What a Fix Looks Like
Trigger the rebuild on evidence. Measure recall continuously by sampling, which makes the decision input available and is inexpensive, then set the rebuild trigger on a recall threshold the operator chooses rather than on a date — this converts a ritual into a control and is the substance of the fix. Report the recall recovered by each rebuild, so an operation that achieved nothing is visible and the schedule can be relaxed with evidence rather than nerve. Report graph health continuously — tombstone ratio, connectivity, orphan count — which predicts the need before recall visibly moves and gives the operator lead time. Forecast the rebuild date from the current degradation trend, so capacity and windows can be planned rather than reserved permanently. Recommend partial rebuilds where the degradation is localised, which is most of the time and is far cheaper. Report the cost of each rebuild in capacity, elapsed time and engineer hours, since the operation is currently free in every budget and is not. And publish typical degradation rates by mutation profile, so a new deployment starts with a sensible expectation rather than a default monthly entry.

## Who Feels the Pain
Reliability engineers spending nights on operations that changed nothing; organisations silently running degraded because their calendar said quarterly; and the finance functions holding doubled capacity for a ritual.

## Impact If Fixed
The decision input does not exist, so the schedule is a ritual and the risk is unmanaged in both directions. A recall-threshold trigger converts it into a control, and reporting the recall each rebuild recovered lets a team relax the schedule on evidence rather than nerve.
