# Buy: Preference Elicitation Adapted to a Manager Who Will Not Complete a Form

**Niche:** [[niches/recruiting-tech-vendors/hiring-manager-calibration/profile|Hiring Manager Feedback & Calibration]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Preference elicitation and conjoint methods recover what people value from their choices; they assume a respondent who agreed to participate.
**Tags:** #bayesian-inference #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #hypothesis-testing #descriptive-statistics #tacit-knowledge-ml #automation
**Contested on:** Whether choice-based elicitation methods work on operational decisions rather than on designed comparisons.

## The Problem

Recovering preferences from choices is a developed methodology. Conjoint analysis, discrete choice modelling and pairwise comparison methods are standard in market research and product design, with well-understood designs, estimation approaches and software.

They assume a designed experiment: a respondent who consented, presented with constructed alternatives varying on controlled attributes, in a sufficient number of comparisons. A hiring manager provides none of that. They make a dozen decisions on real candidates who vary on everything at once, in no designed pattern, and will not sit for an exercise.

## What Already Exists

Conjoint and discrete choice software. Bayesian preference estimation. Pairwise comparison and ranking elicitation methods. Recommender systems' preference learning from implicit feedback, which is the closest existing fit. Structured interview scorecards. Intake meeting templates.

## The Customization Gap

**The choice set is observational, not designed.** Candidates vary on many correlated attributes simultaneously, with no balance and no orthogonality. Estimating preferences from this is closer to observational causal inference than to conjoint, and the identification is genuinely weaker — which the method must acknowledge rather than paper over.

**The sample is a dozen, not hundreds.** Choice modelling assumes enough comparisons to estimate part-worths. Here the estimate must come from very few decisions with heavy priors, pooling across similar roles and managers, and reporting wide uncertainty. Small-sample Bayesian estimation is the right frame and is not how conjoint software is built.

**The attributes have to be extracted from unstructured documents.** Conjoint attributes are specified by the researcher. Here they must be inferred from resumes — which dimensions even distinguish these candidates — before any preference can be estimated. That extraction is the substantive prerequisite.

**The respondent must be able to correct the inference in one sentence.** No elicitation method has an output designed to be corrected conversationally by a busy non-participant. Presenting the estimate as a plain-language hypothesis and accepting a free-text correction is the interaction that makes it work, and it is a product design rather than a statistical one.

**The stated and revealed preferences will differ and both matter.** The job description is a stated preference and the decisions are revealed. Where they diverge, neither is simply wrong — the manager may have unstated requirements or may be applying criteria they would not defend. Surfacing the divergence rather than resolving it is the useful output.

## Target Customer

ATS and recruiting intelligence vendors building manager calibration features. Also market research methodologists, for whom operational preference recovery from small observational choice sets is a genuine methodological problem with applications well beyond hiring.

## Impact If Solved

The choice modelling estimation, Bayesian preference machinery and implicit-feedback methods get reused, and the observational identification, small-sample priors, attribute extraction, correctable presentation and stated-versus-revealed divergence get built. Concretely: a preference estimate from twelve real decisions that a manager corrects in one sentence.
