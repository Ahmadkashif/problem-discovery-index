# One Underwriting Record From Application to Death Claim

**Niche:** [[niches/life-insurance-carriers/life-underwriting-new-business/profile|Individual Life Underwriting & New Business]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers grade mortality by block and never by decision, because the underwriting decision, its evidence and its reasoning are not stored in a form that can be joined to what happened to the life.
**Tags:** #survival-analysis #causal-inference #feature-engineering #evaluation-metrics #confidence-intervals #data-integration #tacit-knowledge-ml #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to place each applicant in the right risk class faster, but writing it produces two contests with different winners: issuing more cases with no fluids or APS while holding mortality slippage, and turning the referred cases' medical records into a defensible class in days. Decomposed into contested sub-niches below.

## The Problem
A carrier knows its actual-to-expected mortality by issue year, class, face band and channel. It cannot say whether cases decided by the rules engine, by a junior underwriter or by a senior one perform differently within a class. It cannot say which requirement, the APS, the lab panel or the Rx history, actually changed decisions that later mattered. The new-business system keeps the decision, the admin system keeps the policy, the claims system keeps the death, and the reasoning was never kept anywhere.

## Why Nobody Has Built This
The outcome takes a decade or more to become credible, longer than any vendor contract or underwriting leader's tenure. Workbench vendors sell throughput, not grading. Reinsurers hold more mortality data than any one carrier but study it by treaty and block, not by the cedent's underwriting decisions.

## What to Build
A decision ledger written at issue: path (accelerated, full, referred), evidence received, findings that drove debits and credits, underwriter, confidence and overrides, all captured from the workbench with no extra typing. It is joined continuously to lapse, contestable investigations, post-issue audits, reinsurer facultative quotes and death claims. Survival models by decision attribute, with honest intervals, show where early signals diverge long before full credibility.

## Target Customer
Chief underwriters and chief actuaries at the top ~50 individual life writers (estimate), and the reinsurers that share their mortality risk.

## Impact If Built
The carrier can see which underwriting paths, evidence and people carry mortality information. Requirement budgets, routing and pricing then follow evidence rather than habit.
