# Buy: Ranking Infrastructure Adapted to an Unobservable Outcome

**Niche:** [[niches/recruiting-tech-vendors/screening-and-matching/profile|Screening & Matching]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Learning-to-rank infrastructure is mature and assumes a relevance label; here the label is what a recruiter did and the outcome is never observed.
**Tags:** #loss-functions #gradient-boosting #evaluation-metrics #confidence-intervals #word-embeddings #causal-inference #compliance #transformers
**Contested on:** Whether ranking infrastructure can be used responsibly when the only available label is the behaviour you are trying to improve on.

## The Problem

Ranking infrastructure is commodity. Learning-to-rank libraries, embedding retrieval, feature stores, real-time serving and experimentation platforms are all mature, and a recruiting vendor can stand up a competent ranker quickly.

The pipeline requires a label. In search, it is a click; in commerce, a purchase. Here the available labels are recruiter actions — advanced, rejected, interviewed, hired — every one of which is the decision being automated rather than an independent measure of its quality. Feeding them into a standard ranking pipeline produces a system that reproduces the decisions with greater consistency and a veneer of objectivity, which is the documented failure mode.

## What Already Exists

LightGBM, XGBoost and TensorFlow Ranking. Embedding models and vector retrieval. Feature stores and serving infrastructure. Experimentation and interleaving frameworks. Fairness libraries. Resume parsing and entity extraction. All production-grade and none of it aware of what its label means here.

## The Customization Gap

**The label is the thing being automated.** No ranking framework has a concept of a label that is itself the target of improvement. Using recruiter agreement requires an explicit acknowledgement in the design that the model can at best match past behaviour, and a deliberate decision about which parts of that behaviour to propagate — which is a modelling choice nobody makes explicitly.

**Proxy variables are the specific hazard.** Names, institutions, postcodes, employment gaps, phrasing and a hundred other features correlate with protected characteristics. Standard feature pipelines maximise predictive power; here the pipeline needs an explicit exclusion and proxy-detection layer, and removing the obvious fields is not sufficient because the information is recoverable from combinations.

**Evaluation cannot use the standard metrics.** NDCG against recruiter labels measures agreement with recruiters. There is no offline metric for what matters, which means honest evaluation is either an audit against independent review or nothing — and a ranking pipeline with no valid offline metric is a very unusual object.

**Exposure decisions are employment decisions.** A candidate ranked below the fold is functionally rejected. Ranking libraries have no concept of a ranked item whose position determines a person's employment prospects, and the resulting obligations — recording the reason, bounded position effects, human review at the margin — have to be built around the stack.

**Regulatory obligations are arriving.** Several regulatory directions treat automated ranking in hiring as an automated employment decision tool with audit, disclosure and record-keeping requirements. The ranking stack has no compliance layer and the obligations attach to the deployment rather than to the library.

## Target Customer

ATS and matching vendors building or rebuilding a ranking layer, who need the hazards named before they build. Also employers' data science teams building internally, and the fairness and ML governance vendors, for whom hiring is the most regulated application of ranking in existence.

## Impact If Solved

The retrieval, serving and experimentation infrastructure gets reused, and the label honesty, proxy exclusion, audit-based evaluation, exposure-as-decision obligations and compliance layer get built. Concretely: a ranking system whose builders can state what its label is and what it therefore cannot claim.
