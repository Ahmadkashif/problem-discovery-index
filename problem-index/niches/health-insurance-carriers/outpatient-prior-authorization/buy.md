# Gold-Card Lists Built From Provider Approval History

**Niche:** [[niches/health-insurance-carriers/outpatient-prior-authorization/profile|Outpatient Prior Authorization & Gold-Carding]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Provider scorecards already exist in every plan's analytics stack; turning them into the gold-card exemptions state laws now require means per-service, per-provider approval rates computed the way each statute defines them.
**Tags:** #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn an outpatient authorization request into a determination inside the 72-hour and seven-day clocks without a fax or a phone call, and whoever auto-approves the largest share of requests a nurse would have approved, with no rise in overturned denials or later-audited approvals, takes the account.

## The Problem
Gold-card laws exempt a provider from prior authorization for a service if the plan approved a high share of that provider's requests over a look-back period. Plans also adopt gold-carding voluntarily to cut volume. Computing eligibility means counting requests, approvals and denials by provider and service under each state's rules, and re-evaluating on the statute's schedule.

## What Already Exists
Provider performance scorecards in payer analytics platforms and BI tools; UM platform reports; rules engines that can exempt a provider once a list exists.

## The Customization Gap
The plan needs a statute-by-statute encoding: which services count, the look-back window, the approval threshold, how partial approvals and withdrawals count, notice periods before revoking an exemption, and the sampling the plan may use to justify revocation. It also needs small-sample handling, because a provider with five requests at 100% is not the same as one with five hundred at 92%. And it needs audit trails for each decision, with exemptions loaded back into the intake rules automatically.

## Target Customer
UM and provider relations leaders at plans operating in states with gold-card statutes, or running voluntary programmes.

## Impact If Solved
Lawful, defensible exemptions that cut request volume for the providers least likely to need review, and revocations that survive challenge.
