# Buy: Surrogate Endpoint Validation From Clinical Research

**Niche:** Programme Outcome Measurement
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medicine learned the hard way that a measure that moves is not necessarily a measure that matters, and built the apparatus for validating surrogate endpoints.
**Tags:** #causal-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #survival-analysis #logistic-regression
**Contested on:** Whether simulated performance predicts resistance to real attacks.

## The Problem

Medicine has a specific and hard-won understanding of the situation this category is in.

A surrogate endpoint is a measure that stands in for the outcome you care about because the real outcome is rare, slow or hard to observe. Cholesterol for cardiovascular events. Tumour response for survival. Viral load for disease progression.

The hard-won part is that surrogates can move without the real outcome following. There are well-documented cases where a drug improved the surrogate and worsened mortality, which is why validating a surrogate is now a demanding exercise: the surrogate must be shown to capture the treatment's effect on the real outcome, not merely to correlate with it, and the validation requires trials measuring both.

Simulated click rate is a surrogate endpoint for resistance to real phishing. It is used exactly as an unvalidated surrogate is used — it moves, the movement is reported as the outcome, and the relationship to the real endpoint has never been established.

## What Already Exists

Surrogate endpoint methodology: the formal criteria for surrogate validation, the meta-analytic approaches to establishing whether a surrogate captures a treatment effect, and the regulatory frameworks governing when a surrogate may support a claim.

Cautionary evidence: the documented cases where surrogates misled, which is what drove the methodology and is the most transferable part.

Clinical trial design: randomisation, blinding where possible, pre-registration, and the reporting standards that make results comparable.

Implementation science: the study of whether interventions that work in trials work in ordinary practice, which is the relevant question for a programme delivered at scale.

Security awareness: click rate reporting, with no validation of any kind.

## The Customization Gap

**The surrogate is unvalidated and is used as though it were validated.** This is the whole gap. The methodology for validating it exists and has never been applied.

**The real endpoint is rare, which is what surrogates are for.** Compromises are infrequent, which is precisely the situation the surrogate framework was built for — and which requires the validation rather than excusing its absence.

**Randomisation is possible and unused.** Assigning different programme designs to comparable populations is achievable within a large organisation, and nobody runs it.

**Meta-analysis across customers is the natural approach.** Surrogate validation typically pools trials. A vendor with many customers running different programmes has the equivalent structure and has not exploited it.

**The surrogate is controlled by the party reporting it.** Cholesterol is not set by the drug company. Simulated difficulty is set by the vendor and customer, which makes this surrogate weaker than any clinical one and makes validation more urgent rather than less.

**Nobody requires evidence.** Regulators require surrogate validation for drug claims. No party requires it here, which is why the category has never had to.

## Target Customer

Vendors with large installed bases, who have the meta-analytic structure available and would gain a claim no competitor could match.

Cyber insurers, who accept the surrogate as evidence of a control and price on it, and who would be the natural party to require validation the way a regulator does.

Academic collaborators, for whom this is a well-posed surrogate validation problem in a new domain with abundant data and no prior work.

## Impact If Solved

A discipline that learned the hard way that a moving surrogate can be meaningless has the methodology for checking, and this category has the classic unvalidated surrogate.

The cautionary cases are the most transferable part — the value of the medical experience is the demonstration that surrogates sometimes move in the opposite direction to the outcome.

And meta-analysis across a vendor's customer base is the natural design, available now, and the only route to an answer that would be believed.
