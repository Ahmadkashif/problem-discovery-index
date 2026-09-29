# Pre-Labelling That Anchors the Annotator

**Niche:** [[niches/data-labeling-services/annotation-delivery-platforms/profile|Annotation Delivery Platforms]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** Model-assisted pre-labelling speeds annotators up by showing them a proposed answer, which also makes them agree with it more often than they should, and nobody measures the effect.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #cross-validation #quick-win #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to be how annotation actually gets done — and that contest is a tooling problem for teams doing it themselves and a workforce problem for those buying a result, which is why this niche is not terminal and is decomposed below.

## The Problem
Pre-labelling shows the annotator a model's proposed answer, which they confirm or correct. Throughput rises substantially, which is why it is used. It also anchors them: an annotator shown a plausible wrong answer accepts it more often than one working from nothing, particularly under piece-rate pay where accepting is faster than correcting. The resulting dataset is systematically biased toward the model that produced the pre-labels, which is precisely the wrong property for data intended to improve that model. The effect is well known in the judgement literature and is not measured by anybody in this industry.

## Why It's Still Broken
Pre-labelling's benefit is immediate and measurable in throughput, and its cost is a subtle bias that nobody has instrumented. Measuring it requires a holdout — some items annotated without pre-labels — which reduces throughput and is not in anybody's interest to run. The piece-rate structure sharpens the effect by rewarding speed, which connects to the annotator niche. And the customer receives a dataset whose bias toward their own model is invisible and is exactly the thing that makes it less useful.

## What a Fix Looks Like
Measure the anchoring and design against it. Run a holdout continuously — a small share of items annotated without pre-labels by the same annotators — which quantifies the anchoring effect directly and is the measurement nobody performs. Report the acceptance rate of pre-labels by annotator and by item difficulty, since an annotator accepting nearly everything is a signal and is currently indistinguishable from one who is fast and accurate. Withhold pre-labels where the model is uncertain, since that is where its proposal is most likely wrong and the anchoring most costly, and is a straightforward gating rule. Present the pre-label after an initial independent judgement on the items that matter most, which preserves most of the throughput benefit and removes the anchoring on the high-stakes subset. Pay for correction rather than penalising it, since the piece-rate structure currently rewards acceptance and the incentive is the mechanism. Report the anchoring estimate to the customer, because a dataset biased toward their own model is a property they need to know about. And exclude pre-labelled items from evaluation datasets entirely, since an evaluation set anchored to the model being evaluated is worse than useless.

## Who Feels the Pain
Customers receiving datasets subtly biased toward their own model; annotators whose pay structure rewards agreement; and model teams whose evaluation sets have been contaminated by the model they are evaluating.

## Impact If Fixed
A continuous small holdout quantifies an effect that is currently unmeasured and is known to exist, and costs a few percent of throughput. Gating pre-labels on model uncertainty removes the anchoring where it is most harmful, and excluding pre-labelled items from evaluation sets prevents a contamination that invalidates the measurement entirely.
