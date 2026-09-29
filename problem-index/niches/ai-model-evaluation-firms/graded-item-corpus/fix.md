# Items Every Model Passes

**Niche:** [[niches/ai-model-evaluation-firms/graded-item-corpus/profile|Graded Item Corpus]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of every benchmark consists of items that every current model answers correctly, which cost money to run, contribute nothing to the comparison, and inflate every reported score.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #logistic-regression #automation #quick-win #dimensionality-reduction
**Contested on:** Every serious competitor in this niche is fighting to turn millions of graded items into an empirical account of how well this industry's own measurements work — and whoever publishes it sets the standard the field is judged by, which is worth more than any evaluation contract.

## The Problem
A thousand-item benchmark is run against six models. Six hundred items are answered correctly by all six. Those items cost six thousand model calls, contribute nothing to distinguishing the models, and raise every reported score by a fixed amount that makes the whole scale less informative — the interesting variation is compressed into the remaining four hundred. The benchmark was assembled when models were weaker and has not been revisited. Every firm running it can compute which items these are in a single query and none has.

## Why It's Still Broken
Removing items lowers headline scores, which looks like a regression to anyone not reading the methodology. Benchmark stability is valued, and changing the item set breaks comparability with published history. Item-level analysis is nobody's assigned work. And a high score is a comfortable result for the model vendor, the benchmark and the buyer simultaneously, which is a rare alignment of incentives around doing nothing.

## What a Fix Looks Like
Analyse the items and retire the ones that measure nothing. Compute per-item discrimination across the model population, which is a straightforward calculation on data every firm holds and immediately identifies the dead weight. Report the effective item count — items actually contributing to the comparison — alongside the nominal size, since a thousand-item benchmark doing four hundred items of work should be described that way. Retire saturated items on a schedule and replace them with harder ones, maintaining the bank rather than freezing it, and publish an equating procedure so that scores remain comparable across versions — which is the technique that resolves the stability objection and which assessment solved long ago. Run the saturated set at a low sampling rate rather than removing it entirely, which preserves the ability to detect a regression while recovering most of the cost. Report scores on a scale anchored to item difficulty rather than as a raw percentage, so that saturation does not compress the scale. Prioritise new item construction where the information function is thinnest, which is a targeted use of expensive expert authoring. And publish the item statistics, so the community can see which parts of a benchmark are doing the work.

## Who Feels the Pain
Buyers comparing models on a scale compressed by dead items; firms spending materially on model calls that distinguish nothing; and item authors writing new content with no information about where it is needed.

## Impact If Fixed
Per-item discrimination is one query against data every firm already holds, and it identifies the dead weight immediately. Publishing an equating procedure resolves the comparability objection that keeps saturated benchmarks frozen.
