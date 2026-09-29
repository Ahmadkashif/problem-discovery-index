# Buy: Evidence-Based Practice From Medicine and Insurance

**Niche:** Control Efficacy Measurement
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medicine and insurance both moved from expert consensus to outcome evidence, built the institutions to do it, and security compliance is still where medicine was before trials.
**Tags:** #causal-inference #bayesian-inference #survival-analysis #logistic-regression #evaluation-metrics #confidence-intervals #hypothesis-testing
**Contested on:** Whether the relationship between implementing a framework's controls and actually suffering fewer incidents has ever been measured, by anyone.

## The Problem

Two fields have already made the transition security compliance has not.

Medicine moved from expert consensus to evidence over decades, and built the apparatus to sustain it: trial infrastructure, observational study methodology for questions trials cannot answer, systematic review, guideline bodies that grade recommendations by evidence strength rather than asserting them equally, and registries that collect outcomes at population scale. A modern clinical guideline states the strength of evidence behind each recommendation, and practitioners can see which are well supported and which are expert opinion.

Insurance made the same transition earlier and more completely. Actuarial practice exists precisely to relate observable characteristics to loss outcomes, and underwriting reflects measured relationships rather than plausibility.

Security compliance frameworks are consensus documents with no evidence grading, no outcome registry, and no systematic review. They look exactly like pre-evidence clinical guidelines: written by experienced people, plausible throughout, unranked, and untested.

## What Already Exists

Medical evidence infrastructure: the GRADE system for rating evidence quality and recommendation strength; systematic review methodology and the Cochrane apparatus; observational study designs — matched cohorts, case-control, target trial emulation — for questions where randomisation is impossible; patient registries collecting outcomes at scale; and post-market surveillance for detecting effects only visible in large populations.

Actuarial practice: loss modelling, credibility theory for combining sparse data across segments, and the regulatory apparatus that requires insurers to justify rating factors empirically.

Cyber insurance specifically: a growing body of underwriting data relating security characteristics to claims, held commercially and largely unpublished, with a handful of insurers beginning to publish aggregate findings.

Security-adjacent: the Verizon breach report and similar incident datasets, which describe what happened without a denominator of control state; and FAIR, which structures risk estimation from expert input rather than from observed relationships.

## The Customization Gap

**Evidence grading is the most immediately transferable idea.** GRADE lets a guideline say this recommendation rests on strong evidence and that one on expert opinion. Applying the same labelling to framework controls, honestly, would be valuable before any new study is run — most controls would be graded as consensus, which is itself the finding.

**Registries are the missing institution.** Medicine built registries because no single provider had enough events. Security needs the equivalent: a shared, confidential control-state and outcome registry across organisations. The platforms are sitting on the control half and no institution exists to hold the other.

**Target trial emulation fits this problem well.** The medical method for extracting causal estimates from observational data — specify the trial you would have run, then emulate it in the observational corpus — is directly applicable to questions like whether implementing a control reduced subsequent incidents, and is far more rigorous than the naive comparisons a vendor would otherwise reach for.

**Credibility theory handles the sparse-events problem.** Actuarial methods for combining thin data across segments are designed for exactly the low base rate that makes this hard, and are unknown in security analytics.

**The regulatory forcing function is absent.** Insurers must justify rating factors; clinical guidelines face scrutiny. Security frameworks face neither, which is why consensus has persisted unchallenged.

**Confidentiality architecture must come first.** Medical registries solved participation through governance — de-identification, controlled access, research-only use. A security registry needs the same before any organisation will contribute incident data, and it is institutional work rather than technical.

## Target Customer

Cyber insurers are the natural first movers: the actuarial discipline is native to them, they hold outcomes, and better control-effect estimates improve their core business directly.

A research institution or consortium is the credible home for the registry and the evidence grading, because a vendor grading the evidence for controls it sells against would be discounted immediately.

Framework bodies as the eventual consumer — a framework that graded its own controls by evidence strength would be a substantial improvement and none currently could.

## Impact If Solved

Evidence grading applied to existing frameworks is available now, requires no new data, and would immediately tell practitioners which of the hundred controls rest on anything more than plausibility.

A shared registry is the institution this field lacks, and medicine's experience says it is the thing that makes everything else possible — the methods are known and the data collection is the bottleneck.

And importing observational causal methodology would let the question be answered credibly rather than dismissed as vendor analytics, which is the difference between a finding that changes frameworks and one that changes nothing.
