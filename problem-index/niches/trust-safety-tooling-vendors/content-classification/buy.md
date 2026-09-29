# Buy: Fairness Evaluation From Machine Learning Research

**Niche:** Content Classification
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning research built a substantial apparatus for measuring disaggregated performance and documenting a model's limits, and trust and safety vendors publish an aggregate.
**Tags:** #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #transfer-learning #descriptive-statistics #compliance
**Contested on:** Whether a classifier works where the harm actually concentrates, or only in the aggregate.

## The Problem

Measuring whether a model performs equally well across groups, and documenting where it does not, is a developed area of machine learning practice.

Disaggregated evaluation reports performance by subgroup rather than in aggregate, and the underlying finding — that aggregate metrics conceal substantial subgroup disparities — is one of the better-established results in the field. Model cards document a model's intended use, its training data, its evaluation and its known limitations in a standard format. Datasheets do the same for datasets. Fairness metrics formalise the different senses in which performance can be equal across groups. And the practice of stating a model's limitations explicitly has become a norm in research publication.

Trust and safety classifiers are deployed models with severe consequences and a known pattern of disparate performance, sold with an aggregate accuracy figure and no documentation of limits.

The apparatus was built by the same research community many of these vendors' engineers come from.

## What Already Exists

Disaggregated evaluation: the methodology and the substantial literature demonstrating that aggregate metrics conceal subgroup disparities, with well-known results in exactly the adjacent domains.

Model cards: a standard documentation format covering intended use, training data, evaluation results including disaggregated performance, and known limitations.

Datasheets for datasets: the equivalent for training data, covering composition, collection and known gaps.

Fairness metrics: the formal apparatus for different notions of equal performance, with open implementations.

Trust and safety products: an aggregate accuracy figure computed on an undisclosed test set.

## The Customization Gap

**The practice exists in research and not in the product.** Vendors whose engineers publish disaggregated evaluations in papers ship products with an aggregate number, which is a norms gap rather than a capability one.

**Model cards would transfer almost unchanged.** Intended use, evaluation, disaggregated results and limitations is exactly the documentation a trust and safety buyer needs and no vendor publishes.

**The relevant subgroups are language and community, not the usual protected attributes.** Fairness work has focused on demographic attributes; here the segments that matter are language, dialect, community norm and content type, which requires different segment definitions.

**Test set composition is the hidden variable.** Disaggregated evaluation requires a test set containing enough of each segment, which means building evaluation data deliberately rather than sampling from training data.

**Commercial disclosure is the obstacle.** Research publishes limitations because the norm rewards it. A vendor publishing limitations is disclosing weaknesses competitors do not, which is the first-mover problem again.

**Regulatory reporting will force part of it.** Platform accountability regimes requiring moderation accuracy reporting will eventually require something better than an aggregate, and vendors have largely not prepared.

## Target Customer

Vendors with research cultures, where the practice already exists internally and shipping it would be a norms decision rather than a capability build.

Platforms subject to moderation accuracy reporting requirements, who need disaggregated figures and are supplied with aggregates.

Regulators and researchers, for whom model cards and disaggregated evaluation are the established formats and who could require them.

## Impact If Solved

An apparatus built by the same research community these vendors draw from applies directly and has not crossed into the products.

Model cards for trust and safety classifiers would transfer almost unchanged and would give buyers, regulators and researchers a documentation standard that currently does not exist in the category.

And building evaluation sets with adequate representation of the segments that matter is the enabling step, because disaggregated reporting is impossible on a test set drawn from the training distribution.
