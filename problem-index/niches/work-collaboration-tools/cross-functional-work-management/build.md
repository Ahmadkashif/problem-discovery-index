# The Handoff as the Unit of Attention

**Niche:** [[niches/work-collaboration-tools/cross-functional-work-management/profile|Cross-Functional Work Management]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cross-functional programmes are delayed at the boundaries between functions and every tool in the category models the work inside them, so the thing that causes the delay is the thing nothing represents.
**Tags:** #graph-theory #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #change-point-detection #workflow-orchestration #causal-inference
**Contested on:** Every serious competitor in cross-functional work management is fighting to assemble the real state of a programme spanning functions that each work in a different tool — and whoever produces that view without asking anyone takes the account.

## The Problem
A launch slips by five weeks. The retrospective finds that engineering finished on time, legal took eleven days to return a review that was expected to take three, the vendor contract sat for a fortnight waiting for a signature nobody chased, and marketing could not start until both were done. Every function did its own work competently. All five weeks accumulated in the gaps between them — the periods where work had left one function and had not yet been picked up by the next — and no tool in the programme represented those gaps as anything at all.

## Why Nobody Has Built This
The products model tasks, which belong to someone, and a handoff belongs to nobody by construction — it is the interval between one person finishing and another starting, which is exactly the state no assignee field can hold. The dependency feature that exists represents a logical relationship between tasks rather than a physical transfer with a duration and an owner. And the functions on either side each report their own work as on time, which is true, so the delay appears in no function's status and only in the programme's.

## What to Build
Handoffs as first-class objects with their own state, owner and clock. A handoff is created wherever work crosses a function or a system boundary, carrying what is being transferred, who is accepting it, what they need in order to start, and when it was made available. Its state is waiting-to-be-accepted, accepted, or returned, and its elapsed time is measured — which immediately makes visible the interval that every current tool renders as a gap between two green tasks. Acceptance requires the receiving function to confirm they have what they need, which surfaces the second most common failure: work handed over incomplete and returned days later. Ageing handoffs escalate automatically, since the characteristic failure is not refusal but drift. And the programme analysis follows: elapsed time decomposed into work and handoff, per function pair, which is the diagnosis nobody currently has and which reliably shows that the delay lives in a small number of specific boundaries.

## Target Customer
Cross-functional work management vendors, programme and transformation functions, and the operations leaders whose programmes slip in ways no retrospective quite explains.

## Impact If Built
Handoff time is the dominant component of cross-functional elapsed time and is represented nowhere, which is why programme improvement efforts concentrate on making functions faster at work that was not the problem. Measuring it relocates the effort, and the ageing escalation addresses the specific failure — drift rather than refusal — that accounts for most of it.
