# Selling Ground Truth Without Access to It

**Niche:** [[niches/data-labeling-services/expert-tier-quality/profile|Expert-Tier Quality]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consensus works for bounding boxes and collapses on expert judgement, which is where the market has moved — so the industry is delivering its most expensive product with its weakest quality signal.
**Tags:** #bayesian-inference #expectation-maximization #hypothesis-testing #confidence-intervals #evaluation-metrics #maximum-likelihood-estimation #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish whether an expert judgement is correct when no ground truth exists and reasonable experts disagree — and whoever does that takes the frontier contracts, because consensus arithmetic is the industry's only quality signal and it does not work here.

## The Problem
A contract requires expert assessments of whether a model's chain of reasoning on a graduate chemistry problem is sound. Three chemists assess each trace. They agree on sixty percent. The delivery report presents sixty percent agreement as a quality figure, which the customer reads as forty percent of the work being wrong. In fact some of the disagreement is one annotator being careless, some is a genuine difference of expert opinion about a defensible step, and some is the guideline being ambiguous about what counts as sound. Those three causes require completely different responses and the agreement statistic does not distinguish them, which means the vendor cannot improve the thing the customer is complaining about.

## Why Nobody Has Built This
Consensus was adequate when the work was perceptual and became the industry's quality vocabulary, and it has been carried into a tier where the assumption underneath it — that there is a right answer that competent annotators converge on — does not hold. Separating annotator error from task ambiguity requires modelling both, which is a measurement design problem the delivery organisations are not staffed for. Gold standards, the other mechanism, require the vendor to know the answer, which is precisely what they cannot do at this tier. And the buyers have accepted agreement figures because there is no alternative on offer.

## What to Build
Model annotator ability and task difficulty separately, which is what the measurement literature exists for. Estimate each annotator's reliability per task type from their pattern of agreement across many items rather than from their agreement on one, which distinguishes a careless annotator from one who is correct and unusual — and is the foundational separation. Estimate each item's ambiguity, so that disagreement on a genuinely contested item is reported as ambiguity rather than as error, and the customer receives an honest signal about which parts of their dataset are inherently uncertain. Establish an achievable agreement ceiling per task by measuring what the most reliable annotators achieve among themselves, which sets the expectation the project should be judged against and which nobody currently sets. Adjudicate the genuine disagreements deliberately with a stronger mechanism — a senior panel, a structured argument, a resolution rule — rather than by majority, since majority on a contested expert question is arithmetic rather than judgement. Deliver uncertainty with the labels, because a model trained on a dataset that marks its own contested items is better served than one given false confidence. And validate against the downstream outcome wherever the customer will share it, since whether the data improved the model is the only real test and is occasionally available.

## Target Customer
Frontier laboratories and enterprise model teams buying expert data, and the vendors competing for those contracts, for whom a credible quality framework is the only available differentiation at this tier.

## Impact If Built
The industry's quality vocabulary was built for a task type that is no longer where the money is, and it conflates three causes of disagreement that require different responses. Separating annotator reliability from item ambiguity is the measurement change, and delivering uncertainty with the labels is a better product than false confidence.
