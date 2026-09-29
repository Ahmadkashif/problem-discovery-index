# Self-Service That Nobody Self-Serves

**Niche:** [[niches/bi-analytics-platforms/self-service-analytics-platforms/profile|Self-Service Analytics Platforms]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Self-service analytics is deployed nearly everywhere and every organisation that deployed it still has analysts answering questions all day, which is the category's central unmeasured failure.
**Tags:** #large-language-models #bert #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor here is fighting to let someone who is not an analyst get a correct answer without one — and that contest splits by delivery surface rather than by capability, which is why this niche is not terminal and is decomposed below.

## The Problem
A company buys eight hundred licences, runs training, publishes a governed model and certifies forty dashboards. Eighteen months later the analytics team's queue is as long as it was, the questions in it are mostly answerable from the certified dashboards, and the people asking have licences they do not open. Nobody is doing anything wrong: the asker is not confident they would filter it correctly, the dashboard does not quite answer their actual question, and asking a person takes twenty seconds and is reliably right. The rational individual choice produces the collective outcome the platform was bought to prevent.

## Why Nobody Has Built This
The category measures deployment rather than outcome. Licences, dashboards published and monthly active users are all reported; questions answered without an analyst is not, so the failure has no metric and therefore no owner. Vendors are structurally disinclined to measure it, since the honest number would be uncomfortable. And the two serious attempts to close the gap — conversational querying and embedding analytics into the tools where decisions happen — are different enough from each other that treating them as one roadmap produces a product that is mediocre at both, which is exactly what the incumbents have shipped.

## What to Build
The measurement layer and the trust layer that both sub-niches depend on. Measure the real outcome: questions asked of humans that were answerable from existing assets, which is computable by comparing the analytics team's request queue against the estate's coverage and is a number no organisation currently has. Measure where self-service attempts fail — queries started and abandoned, filters set and reset, exports followed by a chat message — all of which are in the platform's logs and identify the specific point at which people give up. Then build for trust rather than capability, which is the actual constraint: show the definition and the lineage at the point of reading, show when the data was last refreshed and whether the pipeline succeeded, and show who else uses this asset and for what, because social proof is what people actually use to decide whether a number is safe to act on. That layer is what the two sub-niches below build their respective surfaces on, and it is missing from both.

## Target Customer
Data leadership accountable for a self-service programme that has not delivered, and the platform vendors whose renewal conversations turn on adoption they cannot currently explain.

## Impact If Built
The category's central promise is unmet and unmeasured, and the measurement is the prerequisite for any honest attempt at the rest. Trust rather than capability is where the gap actually lives, which is why a decade of interface improvement has not moved it.
