# The Only Record of What Actually Fails

**Niche:** [[niches/ai-red-teaming-firms/assessment-corpus-intelligence/profile|Assessment Corpus Intelligence]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These firms hold the only cross-model record of which probes succeed against which configurations with which defences in place, and use it one engagement at a time.
**Tags:** #gradient-boosting #evaluation-metrics #hypothesis-testing #confidence-intervals #transfer-learning #descriptive-statistics #causal-inference #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of assessments into an empirical account of which defences actually work — and whoever publishes it defines the field's standard of evidence, which is worth more than the clients it would embarrass.

## The Problem
A defender choosing mitigations has no evidence. They can buy a guardrail product, restructure their prompt, add output filtering, restrict tools or add monitoring, and nothing tells them which of those actually reduces the failure rate for their kind of deployment, by how much, or at what cost in false positives. The evidence exists: these firms have run thousands of assessments across models and configurations, with and without each defence, and observed the outcomes. It sits in per-engagement records because analysing it would produce comparative findings about vendors who are also clients.

## Why Nobody Has Built This
The commercial conflict is direct and stated: publishing which defences work names the ones that do not, and those are sold by companies who commission assessments. Engagement records are not kept in a common schema, so the corpus is not analysable even internally. Client confidentiality covers the engagements, and nobody has asked whether abstracted outcomes are covered by the same terms. And the demand is from defenders, who are not always the buyers.

## What to Build
Record in a common schema, then analyse and publish. Standardise the record — probe, technique class, model and version, configuration, defences present, outcome and success rate — across every engagement and every automated run, which is a working-practice change and is the precondition for the corpus existing at all. Analyse defensive efficacy: for each class of defence, the reduction in success rate across deployments, with the variation, which is the finding defenders most need and which nobody can produce alone. Measure failure class transfer across models, since whether a finding on one model predicts the same on another is a question the whole field guesses at and the corpus answers directly. Track technique decay, so the field learns how quickly a published technique stops working and therefore how much currency matters. Report robustness attributable to a model versus to a deployment's own defences, which tells a buyer where their protection actually comes from. Establish an abstraction that carries the finding without the client, since the technical content and the client identity are separable and the contractual objection applies to one of them. Publish, since the firm that supplies the field's evidence base becomes the reference and the reputational position is worth more than the discomfort. And feed the analysis back into engagement scoping, so assessments concentrate where the corpus says failures concentrate.

## Target Customer
Defenders choosing mitigations, assessment firms, guardrail vendors whose products would finally be evidenced, and the research community with no cross-deployment data.

## Impact If Built
Defenders choose mitigations on marketing because the only evidence sits in per-engagement records. Defensive efficacy across deployments is the finding nobody can produce alone, and abstracting the technical content from the client identity is what makes publication contractually possible.
