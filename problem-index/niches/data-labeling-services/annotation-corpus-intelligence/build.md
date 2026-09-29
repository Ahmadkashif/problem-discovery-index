# Millions of Events, Used to Ship Labels

**Niche:** [[niches/data-labeling-services/annotation-corpus-intelligence/profile|Annotation Corpus Intelligence]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendors hold millions of annotation events with identities, timings, revisions, verdicts and outcomes, which is the empirical basis for every question the field guesses at, and they use it to ship labels.
**Tags:** #bayesian-inference #expectation-maximization #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #cross-validation
**Contested on:** Every serious competitor that gets here is fighting to turn millions of annotation events with their outcomes into answers about who is reliable, what agreement is achievable and whether the data helped — and whoever does that holds the empirical basis for questions the whole field guesses at.

## The Problem
A project lead sets a quality target of eighty-five percent agreement because that is the number in the last contract. Nobody knows whether eighty-five is achievable for this task, what the best annotators achieve among themselves, how many annotators per item is worth the cost, or whether the guideline revision in week three helped. The vendor has run four hundred projects, holds every event from every one of them with the outcome attached, and has never computed any of it. The same questions are answered by convention at every vendor in the industry, and the data that would settle them is sitting in four hundred project databases.

## Why Nobody Has Built This
The corpus accumulated as operational exhaust rather than as a deliberate dataset, and the delivery organisation's analytical capacity is consumed by project reporting. Cross-project analysis requires normalising task types across differently-structured projects, which is real data work with no immediate revenue. The downstream link — whether a batch improved a model — requires the customer to share it, which some would and nobody has asked. And the findings would establish limits on what the vendor's own product can achieve, which is uncomfortable and is also the basis of a credible quality claim nobody else can make.

## What to Build
Treat the corpus as the asset it is. Normalise task types across projects, which is the enabling work and turns four hundred isolated databases into one dataset. Estimate annotator ability per task type across projects, which is the capability profile the routing niche needs and is far better estimated across a contributor's whole history than within one project. Establish achievable agreement ceilings per task type empirically, which gives every future project a defensible target instead of a convention and is the single most useful output. Measure the marginal value of each additional annotator per item, which is a pure cost decision currently made without evidence and is directly computable. Measure guideline revision effects across projects, which establishes what kinds of clarification actually work. Pursue the downstream link deliberately, since whether a batch improved a model is the only real validation and some customers will share it in exchange for the resulting insight. Benchmark contributors and projects against the corpus, which is a service customers would buy. And publish the general findings, because a vendor that can state what agreement is achievable on a task type occupies a position no competitor can reach by running one more project.

## Target Customer
The delivery organisations themselves, primarily; and the laboratories buying expert data, who would pay for empirically grounded quality expectations.

## Impact If Built
Every other capability in this industry depends on estimates the corpus could supply and nobody computes. Achievable agreement ceilings alone would replace the conventions that currently set every project's quality target, and the downstream link is the only real validation the field has access to.
