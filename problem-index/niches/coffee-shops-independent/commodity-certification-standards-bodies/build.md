# Non-Conformance History as a Risk-Based Audit Allocator

**Niche:** [[niches/coffee-shops-independent/commodity-certification-standards-bodies/profile|Agricultural Certification Standards Bodies]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Audits are allocated on a fixed cycle with a random sample, the organization holds years of non-conformance findings across hundreds of thousands of farms, and none of it decides where the auditors go next.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #feature-engineering #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #compliance #data-integration

## The Problem
Assurance capacity is the binding constraint on a certification system and it is allocated almost blindly. Every certified unit is audited on a schedule; within group certifications, a fixed percentage of member farms is sampled, usually at random. Meanwhile the system holds a detailed record of what auditors have found — which non-conformances, at which farms, in which regions, under which group managers, and whether they recurred after corrective action. That record is used to manage individual cases and not to decide where the next audit should go. The consequence is predictable: auditor time is spread evenly across a population whose risk is anything but even, low-risk units are visited as often as high-risk ones, and the failures that eventually surface publicly are frequently in places where the accumulated findings already pointed.

## Why Nobody Has Built This
Risk-based allocation is in tension with the equal-treatment logic certification systems were built on, and there is a real governance concern behind it: a farm sampled more often because a model flagged it deserves an explanation, and an opaque model is not one. Oversight bodies and buyers also expect a defined sampling percentage, so changing allocation requires renegotiating the scheme's own rules rather than merely deploying a system. And the findings data lives in the certification bodies performing the audits rather than centrally, in structures that vary between them, so the corpus is fragmented before any analysis starts.

## What to Build
A risk model over the accumulated assurance record, designed for a governed rather than an automated decision. Findings are normalized into a common structure across certification bodies — which is the substantive data work — and joined to unit, group, region, crop, and time. The model estimates the probability of material non-conformance conditional on history, group management, regional context, and time since last audit, and expresses it as a ranked allocation recommendation with the contributing factors stated explicitly, so a farm surfaced for extra scrutiny has a reason attached. The scheme's minimum sampling requirements remain a floor; the model allocates the discretionary capacity above it. Calibration is monitored continuously, because a risk model in an assurance system that drifts is worse than none. And the same record supports the analysis the organization most needs and cannot currently produce — which corrective actions actually prevented recurrence, which is the entire theory of change behind certification and has never been measured with its own data.

## Target Customer
Directors of standards and assurance at certification bodies running 100-600 staff, and the scheme oversight committees who set sampling rules and currently have no evidence base for the percentages they mandate.

## Impact If Built
Concentrates the system's scarcest resource where the risk actually is, which improves detection at constant cost — and detection failures are the events that damage a certification scheme most. The corrective action analysis matters more still: certification's credibility rests on the claim that findings lead to improvement, and no scheme currently demonstrates that from its own data.
