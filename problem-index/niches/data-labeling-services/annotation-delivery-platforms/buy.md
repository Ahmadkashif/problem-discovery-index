# Active Learning and Targeted Review

**Niche:** [[niches/data-labeling-services/annotation-delivery-platforms/profile|Annotation Delivery Platforms]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Active learning tells you which items are worth labelling and which labels are worth checking, has a large literature, and annotation projects label uniformly and review by random sample.
**Tags:** #bayesian-inference #gradient-boosting #monte-carlo-methods #evaluation-metrics #confidence-intervals #cross-validation #optimization-fundamentals #automation
**Contested on:** Every serious competitor here is fighting to be how annotation actually gets done — and that contest is a tooling problem for teams doing it themselves and a workforce problem for those buying a result, which is why this niche is not terminal and is decomposed below.

## The Problem
Deciding which items to label to maximise a model's improvement per unit of labelling cost is active learning, with decades of research and mature methods. Deciding which labels to review to maximise error detection per unit of review cost is the same idea applied to quality. Annotation projects label the batch they were given and review a random sample of a fixed percentage, which spends the budget uniformly across items whose value and whose error probability differ enormously.

## What Already Exists
Active learning with uncertainty, disagreement and expected-model-change acquisition strategies; the labelling-budget allocation literature; error prediction from annotator and item features; and the crowdsourcing work on when to collect an additional judgement. All published, with implementations.

## The Customization Gap
The adaptation is to a service relationship with a delivery contract. It requires: (1) an objective that is the customer's model rather than a proxy, since active learning optimises model improvement and the vendor is delivering a dataset — which means the acquisition strategy depends on the customer's training setup and requires a collaboration most contracts do not contemplate; (2) targeted review driven by predicted error, using annotator reliability, item difficulty and time-taken signals, which is the vendor's own quality budget and is entirely within their control — this is the application available immediately without any customer involvement; (3) honest handling of the coverage requirement, since many contracts specify that every item is labelled and active learning's premise is that not every item should be, which is a commercial conversation rather than a technical one; (4) avoiding the bias that active learning introduces, since a dataset selected for informativeness is not representative and a customer using it for evaluation rather than training will be misled; and (5) dynamic allocation within a fixed budget, which is the realistic framing — the same money, spent where it matters.

## Target Customer
Annotation platform vendors, delivery organisations managing quality budgets, and the model teams specifying labelling projects.

## Impact If Solved
Active learning addresses exactly the allocation question and annotation projects spend uniformly. Predicted-error-targeted review is available to the vendor immediately with no customer involvement and improves detected error per unit of review cost substantially.
