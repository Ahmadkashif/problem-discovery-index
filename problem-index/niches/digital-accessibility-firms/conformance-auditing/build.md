# Narrowing What a Person Must Examine

**Niche:** [[niches/digital-accessibility-firms/conformance-auditing/profile|Conformance Auditing]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automation decides the easy portion and a person must look at everything else.
**Tags:** #automation #evaluation-metrics #compliance #cnns #large-language-models #confidence-intervals #data-integration #object-detection
**Contested on:** Every serious competitor in this niche is fighting to cover the portion of accessibility failures that automation cannot decide, because that is where the real barriers are and it requires a person — and whoever closes that gap takes the account.

## The Problem
Automated checking handles what is decidable from markup — a missing alternative text attribute, an unlabelled input, a contrast ratio. Whether an alternative text is meaningful, whether a heading structure reflects the content, whether a custom component behaves as its role implies, whether an error message is comprehensible: these require judgement. The judgement portion is where the real barriers concentrate, it is expensive, and the audit's cost is essentially the cost of that examination.

## Why Nobody Has Built This
Tooling has optimised the decidable portion because it is tractable and sellable. The judgement portion is assumed to be irreducibly manual. Assisting rather than replacing human review is an unglamorous product. And the industry's economics rest on the manual hours.

## What to Build
Narrow and assist the human portion rather than trying to eliminate it. Triage the undecidable items so the human looks at the ones most likely to be problems rather than at everything, which is the core and is where the cost reduction is available. Assist the judgement calls — is this alternative text meaningful, does this heading structure make sense, does this component announce its state — with a suggestion the expert confirms or overrides. Reuse prior judgements on unchanged components, since most of a re-audit re-examines things that have not changed. Report confidence on automated results rather than presenting them as certain, which matters because a clean scan is currently read as a clean site. State coverage honestly — what proportion of criteria were assessed automatically, what manually, what not at all — which is the most useful line in any audit and is usually absent. Prioritise the manual examination by where users actually go, from analytics. Capture the expert's reasoning so it is reusable rather than lost. Compare components against a library of known-good patterns, which catches a meaningful share. Keep the human as the decider throughout, since an automated judgement call that is wrong is worse than no judgement. And measure the manual hours per criterion so the narrowing can be shown to work.

## Target Customer
Accessibility firms and consultancies, in-house accessibility teams, testing tool vendors, and compliance and assurance providers.

## Impact If Built
The judgement portion is where the real barriers are and it is assumed irreducibly manual, so the audit's cost is the cost of looking at everything. Triage and assistance narrow what a person must examine without pretending judgement can be removed.
