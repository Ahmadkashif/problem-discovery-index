# Triage That Can Show Its Reasoning

**Niche:** [[niches/legal-practice-software/legal-aid-intake-triage/profile|Legal Aid & Access-to-Justice Intake]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Legal aid organisations decline most of the people who ask them for help, and the decision rests on priority guidelines applied by different intake workers who have never been measured against each other.
**Tags:** #logistic-regression #decision-trees #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor serving legal aid is fighting to triage far more requests than the organisation can ever serve, defensibly and consistently, and to send the rest somewhere real — and whoever makes that triage defensible takes the contract.

## The Problem
A tenant calls about an eviction with a hearing in nine days. The intake worker screens for income eligibility, case type priority and conflicts, and reaches a decision: full representation, brief advice, or referral. Another worker taking the same call on a different day might reach a different decision, because the guidelines require judgment about urgency and merit that the guidelines cannot fully specify. Nobody knows how often that happens. The organisation cannot say whether it is applying its own priorities consistently, cannot show a funder what its triage actually does, and cannot improve criteria it has never measured.

## Why Nobody Has Built This
The sector has no money and vendors follow money. There is also a well-founded discomfort: a system that scores a person's legal problem to decide whether they get a lawyer is exactly the kind of automated decision that ought to make people uneasy, and the sector's technologists have thought hard about this and been rightly cautious. That caution has been expressed as not building the thing, which leaves the decision with an unmeasured human process that has all of the same problems and none of the visibility. And measurement requires outcome data about people who were turned away, which nobody collects.

## What to Build
A triage layer whose purpose is consistency and evidence, not autonomy. It applies the organisation's own written priorities as explicit, inspectable rules — not a learned score — and surfaces the specific factors and the guideline provisions behind each recommendation, so the intake worker is being shown the organisation's stated policy rather than a model's opinion. It records the worker's decision alongside the recommendation, which produces the first measurement of consistency the sector has ever had, and it flags divergence as a supervision signal rather than a compliance one. Urgency detection — hearing dates, lockout notices, protective order timelines — is mechanical and should be automatic, because the most damaging triage failures are timing failures. Every declined applicant is recorded with the reason, which is what makes the gap evidenceable.

## Target Customer
Legal aid organisations and their case management vendors, state access-to-justice commissions funding sector-wide tooling, and the court self-help centres performing the same triage with less structure.

## Impact If Built
Measured consistency is the first-order gain: organisations that instrument intake generally find meaningful variation between workers on identical facts, and simply showing that changes practice. Automatic urgency detection prevents the worst failures. And a recorded, reasoned decline is what turns "we turned away 6,000 people" into evidence a funder or a legislature can act on, which is the sector's most persistent strategic problem.
