# LEDES Validation Extended From Syntax to Substance

**Niche:** [[niches/legal-practice-software/insurance-defense-platforms/profile|Insurance Defense & Panel Counsel Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every practice management vendor selling to defense firms already ships a LEDES validator that checks whether the file is well-formed, which is the least useful check available given that the carrier's engine rejects on content.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in insurance defense software is fighting to get a firm's invoice through the carrier's bill review engine unreduced on the first pass — and whoever predicts the reduction before submission takes the account.

## The Problem
The firm's billing manager runs the pre-submission check. It confirms the LEDES file parses, the task codes are valid UTBMS values, the totals add up, and the matter number matches. The invoice submits successfully and is then reduced by eleven percent for reasons none of which the validator could have detected, because every one of them is about content: two timekeepers at one deposition, a task performed without the pre-approval the guidelines require for spend above a threshold, a paralegal task billed at an associate rate, a narrative that merges three activities. The validator's clean bill of health is worth nothing and is nevertheless the only pre-submission signal the firm has.

## What Already Exists
LEDES validators are commodity — every billing system serving this market has one, and open implementations exist. UTBMS task code sets are published and stable. The bill review platforms publish submission specifications. Contract analysis and document extraction tooling capable of parsing a sixty-page guideline document into structured provisions is mature and inexpensive. Every component of a substantive validator is purchasable.

## The Customization Gap
The adaptation is to make the guidelines machine-checkable and run them before submission. It requires: (1) parsing each carrier's outside counsel guidelines into checkable rules — staffing limits, pre-approval thresholds, excluded activities, rate schedules by timekeeper level, block-billing and increment rules — with the source provision cited against each; (2) evaluating those rules against the invoice *and* against the matter record, since the staffing and pre-approval checks need to see who attended and what was authorised, not just what was billed; (3) maintaining the rule sets as the guidelines change, which is a content function of the same kind as court rules and should be run as one; (4) reconciling stated guidelines against observed reductions per carrier, because engines enforce things guidelines do not say and ignore things they do; and (5) presenting the result as a pre-submission report the billing manager works, ranked by dollars at risk rather than by rule count.

## Target Customer
Defense firms submitting to two or more carriers with different guidelines, and the billing and practice management vendors serving them who already own the submission path.

## Impact If Solved
A substantive pre-submission check catches the deterministic reductions — staffing, rates, pre-approval, formatting — which are a large share of the total and are entirely avoidable. This is the fastest path into the niche's contested capability because it requires no historical data: the guidelines are enough to start, and the reduction history then refines it.
