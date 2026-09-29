# Fix: One Cancellation Restarts Everything

**Niche:** [[niches/recruiting-tech-vendors/interview-coordination/profile|Interview Scheduling & Coordination]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An interviewer drops out the evening before and the coordinator starts the whole negotiation again, losing another week.
**Tags:** #descriptive-statistics #evaluation-metrics #workflow-orchestration #confidence-intervals #graph-theory #quick-win #worker-facing #automation
**Contested on:** Whether a dropped interviewer will be substituted rather than rescheduled around.

## The Problem

A panel is finally scheduled for Thursday. On Wednesday evening an interviewer drops out — a conflicting meeting, illness, a customer escalation.

The coordinator's options as the process is currently built: reschedule the whole panel, which restarts the two-day negotiation and pushes the candidate out a week; or drop the interviewer and proceed with an incomplete panel, which means someone assesses nothing and the hiring decision is made on less evidence.

The option nobody takes is substitution, because there is no list of who else could do that interview. The manager knows one or two people who could; nobody has written it down; and at six in the evening with the panel tomorrow, nobody is going to find out.

Cancellations are frequent — interviewing is the thing that gets dropped when something urgent happens — so this is not an edge case, it is a regular event with a full week of cost each time.

## Why It's Still Broken

Interviewer qualification is undocumented, so substitution is impossible at speed even when a substitute exists and would be happy to help.

Panels are also named rather than specified, so the panel's composition is a list of people rather than a list of competencies, and there is nothing to substitute against.

And the cancellation arrives out of hours to a coordinator with no authority to change a panel the manager composed.

## What a Fix Looks Like

Write down who can do what, and let the coordinator substitute.

Build the interviewer list per competency, per team. Who can run the system design interview, who can run the coding interview, who can do the values interview. A spreadsheet is sufficient to start and it can be assembled in a week by asking each manager.

Specify panels by competency rather than by name. The panel needs a system design assessor, not specifically Priya, and writing the requisition's panel template that way makes substitution a routine action rather than a negotiation.

Give the coordinator standing authority to substitute from the list. Without it, the substitution requires the manager's approval at nine in the evening, which means it does not happen.

Keep a nominated backup per competency per week, on a rotation. Someone who has agreed to be the fallback for that week is far easier to call than someone who has not.

Make the drop-out notification actionable. When an interviewer declines, the system should immediately show who else is qualified and free, so the coordinator is choosing rather than searching.

And track the cancellation rate by interviewer and team. Where it concentrates — usually on the most senior and most overloaded — the answer is a broader pool rather than more chasing, and the data is what makes that argument.

## Who Feels the Pain

Candidates, losing a week and frequently losing interest, which is where offer competition is decided. Coordinators, whose two days of work is undone by one email and who have no authority to fix it. Hiring managers, whose requisition ages for a reason they will attribute to the pipeline. And the interviewers who never cancel, who absorb an ever-larger share of the load.

## Impact If Fixed

A cancellation becomes a substitution taking minutes rather than a reschedule taking a week. The interviewer list, assembled in a week, makes panel composition robust rather than fragile. And the load stops concentrating on the people who always say yes.
