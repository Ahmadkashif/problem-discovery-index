# Explainability From Credit Model Governance

**Niche:** [[niches/identity-verification-vendors/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit modelling built reason codes and individual-level explanation because the law required it, and identity verification returns a number.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #large-language-models #gradient-boosting #descriptive-statistics #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to let a solutions engineer explain why one specific person could not open an account — and whoever makes the decision articulable changes what the escalation conversation can be.

## The Problem
Credit scoring had to become explainable at the individual level: reason codes identifying the principal factors in a specific decision, methods for deriving them from complex models, documentation standards, and validation that the codes are accurate. The discipline exists because a person denied credit is entitled to know why. Identity verification produces decisions of similar consequence and has no equivalent — not because it is technically harder, but because nothing required it.

## What Already Exists
Reason code derivation methodologies; individual-level attribution for complex models; adverse action explanation standards; model documentation and validation practice; and supervisory expectations enforcing accuracy of explanations.

## The Customization Gap
The adaptation is to a multi-stage pipeline including vision components. It requires: (1) attribution across heterogeneous stages — document read, liveness, face match, database resolution — rather than across features in one model, which is the substantive difference and has no established method; (2) explanations for vision components, where the informative statement is about capture quality or facial similarity rather than a feature contribution; (3) an explanation that must not help an impostor, which credit explanation does not have to consider; (4) delivery in real time to an engineer or an applicant rather than in a mailed notice; and (5) no legal mandate in many use cases, so the discipline must be adopted for product reasons.

## Target Customer
Solutions and compliance leadership, customers with explanation obligations, regulators examining automated decisions, and model explainability vendors.

## Impact If Solved
Credit built individual-level explanation because it had to, and the methods exist. Attribution across a pipeline that includes vision stages is the genuinely new part, and it is what the escalation conversation needs.
