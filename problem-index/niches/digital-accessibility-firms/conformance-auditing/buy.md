# Assisted Review From Static Analysis

**Niche:** [[niches/digital-accessibility-firms/conformance-auditing/profile|Conformance Auditing]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Static analysis learned to rank findings so reviewers look at the likely problems first, and accessibility review looks at everything.
**Tags:** #automation #evaluation-metrics #confidence-intervals #compliance #large-language-models #data-integration #descriptive-statistics #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to cover the portion of accessibility failures that automation cannot decide, because that is where the real barriers are and it requires a person — and whoever closes that gap takes the account.

## The Problem
Static analysis and security review faced the same structure: a tool can decide some things, the rest requires a reviewer, and the reviewer's time is the constraint. The response was triage — rank findings by likelihood and severity, suppress the known-benign, learn from past reviewer decisions, and present the reviewer with the cases most likely to matter. It turned an unusable volume into a working queue. Accessibility review presents everything undecidable equally.

## What Already Exists
Finding triage by likelihood and severity; suppression of known-benign patterns; learning from reviewer decisions; incremental analysis of what changed; and reviewer workflow with evidence attached.

## The Customization Gap
The adaptation is to judgements about comprehensibility and behaviour rather than about code correctness. It requires: (1) the undecidable cases being questions about meaning — is this description useful to a person — rather than about program behaviour, so triage must estimate semantic quality rather than exploitability, which is the substantive difference; (2) rendered pages and dynamic components rather than source code; (3) judgement that depends on context a static view does not have; (4) an expert reviewer whose expertise is assistive technology rather than security; and (5) findings that must map to a published standard rather than to a vulnerability class.

## Target Customer
Accessibility firms, in-house accessibility teams, testing tool vendors, and static analysis and code review vendors.

## Impact If Solved
Static analysis turned an unusable finding volume into a working queue through triage and learned suppression. Judgements about comprehensibility rather than program behaviour is what the accessibility version must estimate.
