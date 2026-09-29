# Every Score Is an Upper Bound of Unknown Looseness

**Niche:** [[niches/ai-model-evaluation-firms/benchmark-integrity/profile|Benchmark Integrity]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every public benchmark is plausibly inside the training data of the models it measures, the extent is unknowable because training corpora are undisclosed, and the entire industry reports scores as though it were not.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #large-language-models #entropy-cross-entropy-kl-divergence #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to produce a score that survives the question "was this in the training data?" — and whoever does that takes the account, because every number the industry currently sells is an upper bound of unknown looseness.

## The Problem
A procurement team compares two models on a published benchmark. One scores four points higher. Neither vendor will say what was in their training data, and the benchmark has been public for two years, appearing in countless scraped web pages, code repositories and derived datasets. The four-point difference could be capability, could be a difference in how much of the test set each model memorised, and there is no way to tell. The team makes a purchase decision on a number whose meaning is undefined, and everybody involved knows this and proceeds anyway because there is no alternative on offer.

## Why Nobody Has Built This
Detecting contamination without corpus access is genuinely hard, and the available signals are indirect. Labs have no incentive to disclose their training data and several reasons not to. Benchmark maintainers are academics without the resources to run a custody operation. The firms selling evaluations are selling reassurance, and a product that attaches an uncertainty band to every score is a harder sale than one that does not. And the field's norm of reporting bare numbers is so established that deviating looks like an excuse for a lower score.

## What to Build
Measure contamination and report it with the score. Combine the available detection signals into a single reported estimate — performance on perturbed variants against originals, memorisation probes, ordering sensitivity, the gap between a public set and a matched private one — since no signal alone is conclusive and their combination is far more informative than the nothing currently reported. Report every score with a contamination estimate and an interval rather than as a point, which is the product change and the one that requires the field to accept a more honest and less satisfying number. Maintain matched public and private item pairs constructed to the same specification, so the gap between them is a direct measurement rather than an inference — this is the most convincing single design available and it requires operational discipline rather than research. Generate items procedurally where the domain allows, with the generator itself held privately. Track a benchmark's exposure over time — publication date, appearance in scraped corpora, citation and reuse — and publish a decay estimate, since a benchmark's usefulness has a half-life nobody currently states. Separate memorisation from capability in the reporting, because a model that has seen the answer and a model that can derive it are different products for the buyer. And publish the methodology, since a contamination estimate the buyer cannot interrogate has the same problem as the score it corrects.

## Target Customer
Enterprise procurement, regulators and standards bodies, the labs who would benefit from a credible comparison, and the benchmark maintainers whose work is being degraded.

## Impact If Built
The industry sells numbers whose meaning is undefined and everyone proceeds anyway. Matched public and private item pairs turn contamination from an inference into a measurement, and publishing a benchmark's decay estimate states a half-life the field currently pretends does not exist.
