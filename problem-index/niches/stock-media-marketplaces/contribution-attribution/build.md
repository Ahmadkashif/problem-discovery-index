# What Did This Image Contribute

**Niche:** [[niches/stock-media-marketplaces/contribution-attribution/profile|Contribution Attribution]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compensation is being distributed for a contribution nobody has measured, using data that would allow measuring it.
**Tags:** #causal-inference #contrastive-learning #evaluation-metrics #confidence-intervals #monte-carlo-methods #gradient-boosting #hypothesis-testing #diffusion-models
**Contested on:** Every serious competitor in this niche is fighting to measure what an individual asset contributed to a trained model's behaviour and output — and whoever demonstrates an attribution that survives technical scrutiny gives the whole licensing question a basis it currently lacks.

## The Problem
An image was one of hundreds of millions in a training set. Its contribution is not zero and is not obviously measurable. Influence estimation methods exist, are approximate, are expensive at scale, and have not been applied commercially to this question. The marketplaces have the one thing that makes the problem tractable and unusual: a corpus where every asset has known provenance, human description, licensing history and revealed demand — which supports approaches researchers working on scraped data cannot use.

## Why Nobody Has Built This
The commercial answer was settled by formula before the measurement question was posed, so there was no demand for it — a distribution mechanism that already exists removes the reason to build the thing that would justify it. The methods are genuinely approximate and expensive. A rigorous attribution might produce uncomfortable results in either direction. And no marketplace has a research function pointed at it.

## What to Build
Measure it with the corpus's own advantages. Apply influence and attribution methods to the licensed corpus, which is the core and is research nobody has done on data this clean. Measure output similarity to source assets systematically, since a generated image resembling a specific licensed one is the most direct evidence of contribution and is measurable. Use scarcity and uniqueness as a value dimension, because a rare, hard-to-obtain subject contributes differently from the ten thousandth photograph of a coffee cup and the corpus knows which is which. Use the demand record as a weight, as an asset that buyers repeatedly searched for and licensed is evidence about what capability the model gained. Test by ablation where feasible, since removing a class of assets and measuring capability loss is the cleanest evidence available and is expensive but possible. Express the result as a distribution with honest uncertainty, because a false precision here would be correctly attacked. Distinguish contribution to general capability from contribution to specific outputs, as they are different claims with different remedies. Validate independently, since a self-serving attribution carries no weight. Publish the methodology, because the entire value is in it being examinable. And design it to be auditable by a counterparty, as it will be used in a negotiation.

## Target Customer
Research and rights leadership, contributor representatives, model developers needing a defensible basis, and courts and policymakers assessing the question.

## Impact If Built
A distribution mechanism that already exists removes the reason to build the thing that would justify it. A fully provenanced corpus with descriptions and demand history supports attribution approaches that research on scraped data cannot use.
