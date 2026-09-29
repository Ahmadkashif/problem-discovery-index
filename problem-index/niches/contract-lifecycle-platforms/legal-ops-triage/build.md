# The NDA and the Dangerous Agreement Look Identical

**Niche:** [[niches/contract-lifecycle-platforms/legal-ops-triage/profile|Legal Operations Triage]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contract requests arrive in one queue where a routine NDA and an agreement with an uncapped indemnity are indistinguishable until somebody reads them, and everything downstream depends on that first decision.
**Tags:** #large-language-models #gradient-boosting #bert #logistic-regression #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance
**Contested on:** Every serious competitor here is fighting to tell a routine agreement from a genuinely dangerous one at the moment it arrives — and whoever does that takes legal operations, because everything downstream depends on the first thirty seconds being right.

## The Problem
Forty requests arrive on Monday. The legal operations coordinator works through them, reading enough of each to decide where it goes. Thirty-one are routine. Six need a lawyer. Two are genuinely significant, and one of those was submitted as a standard supplier agreement by a requester who did not read past the first page. It is assigned to the junior queue on that basis and sits for two days, then another day while it is reassigned. The information that would have flagged it — an uncapped indemnity and a five-year exclusive — was in the attached document the whole time.

## Why Nobody Has Built This
Intake was built as a form and a queue, and routing rules operate on what the requester declared rather than on what the document contains, because reading the document at intake was not technically feasible when these systems were designed. Legal operations has also historically been staffed rather than automated — the answer to a bigger queue was another coordinator. And the triage decision's accuracy is never measured, so its failures are absorbed as delays and attributed to capacity.

## What to Build
Risk assessment at intake, from the document rather than the form. Read the attached agreement and classify it: what type it actually is, whose paper it is, and which risk-bearing provisions are present, absent or unusual — an uncapped indemnity, a long exclusivity, unlimited liability, an assignment restriction, a non-standard data commitment. Combine with the request context — counterparty, value, business unit, urgency — into a risk and complexity assessment with the reasoning shown, since legal operations will not route on an unexplained score. Route on that rather than on the declared type, with the requester's declaration retained as one signal among several rather than as the determinant. Estimate expected effort as well as risk, since those are different and workload balancing needs both. Escalate the rare genuinely dangerous item immediately and visibly, which is the single highest-value behaviour and justifies the whole system on its own. And evaluate the triage afterwards by comparing the assessment against what the reviewing lawyer actually found, which produces both a measure of accuracy and the training data to improve it — and which no legal function currently does.

## Target Customer
Legal operations leadership at companies with a meaningful intake queue, general counsel concerned about what reaches them late, and the CLM vendors whose intake modules are forms.

## Impact If Built
The triage decision determines the value of everything downstream and is currently made from a form the requester filled in. Reading the document at intake is now straightforward, and the immediate escalation of the genuinely dangerous minority is worth the system by itself.
