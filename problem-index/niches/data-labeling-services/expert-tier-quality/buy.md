# Psychometrics for Tasks With No Answer Key

**Niche:** [[niches/data-labeling-services/expert-tier-quality/profile|Expert-Tier Quality]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Item response theory and rater reliability modelling were built to separate assessor ability from item difficulty without an answer key, and the annotation industry uses a majority vote.
**Tags:** #bayesian-inference #expectation-maximization #maximum-likelihood-estimation #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #gaussian-processes
**Contested on:** Every serious competitor in this niche is fighting to establish whether an expert judgement is correct when no ground truth exists and reasonable experts disagree — and whoever does that takes the frontier contracts, because consensus arithmetic is the industry's only quality signal and it does not work here.

## The Problem
Educational measurement and clinical rating have spent a century on exactly this problem: estimating how good an assessor is and how hard an item is, simultaneously, from a pattern of judgements with no answer key. Item response theory, latent class models for rater agreement, and the generalisability theory framework all address it, with mature estimation methods and a substantial applied literature. The annotation industry computes a percentage agreement and a chance-corrected coefficient and stops.

## What Already Exists
Item response theory with its ability and difficulty parameters; latent class and Bayesian models for rater reliability without gold standards, including the classical expectation-maximisation formulations developed specifically for aggregating noisy labels; generalisability theory for decomposing variance across raters, items and occasions; and the crowdsourcing literature, which has produced label aggregation models well beyond majority vote and which the commercial category has largely not adopted.

## The Customization Gap
The adaptation is to expert tasks with few raters and high cost per judgement. It requires: (1) working with two or three raters per item rather than the many the methods usually assume, which means pooling across items and annotators to estimate ability rather than estimating per item — a hierarchical formulation that is standard and is not applied here; (2) handling structured outputs, since an expert judgement is frequently a written rationale or a multi-part assessment rather than a categorical choice, and the aggregation methods assume categories; (3) distinguishing ambiguity from difficulty, because an item on which experts legitimately differ is not the same as one that is hard and has an answer, and the distinction determines what the customer should be told; (4) cost-aware allocation, since the practical question is where to spend the third and fourth expert judgement and the ability and difficulty estimates answer it directly — which is the most immediately valuable application; and (5) explicability to a delivery organisation that will not accept a latent variable model it cannot interpret.

## Target Customer
Data labelling vendors, the frontier laboratories specifying quality requirements, and the crowdsourcing research community whose methods have not reached the commercial category.

## Impact If Solved
A century of measurement theory addresses precisely the no-answer-key problem and the industry uses majority vote. Hierarchical estimation with few raters per item is the adaptation, and cost-aware allocation of additional judgements is the application with the fastest return.
