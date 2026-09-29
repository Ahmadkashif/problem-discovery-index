# Status Is Typed, Not Observed

**Industry:** [[work-collaboration-tools|Work Collaboration Tools]]
**Type:** High Impact
**One-liner:** Infer what is actually happening from the activity the tools already capture — commits, documents, messages, review cycles — instead of asking people to describe work the system watched them do.
**Tags:** #gradient-boosting #survival-analysis #large-language-models #bert #time-series-forecasting #feature-engineering #confidence-intervals #evaluation-metrics #workflow-orchestration

## The Problem
A work management platform's central artefact is a task with a status field. The field says what someone last set it to. People set it when they remember, when a project manager asks, or immediately before a status meeting — which means the status is a claim made under social pressure rather than an observation.

The consequence runs through everything built on top. Portfolio dashboards aggregate stale fields. Burn-down charts describe a fiction. A project that is genuinely stuck looks fine until the deadline, because the person who is stuck has not changed the field to say so — nobody advertises being blocked.

Meanwhile the same platforms, and the tools integrated with them, hold a detailed behavioural record. Whether anyone has commented on the task in two weeks. Whether the linked document has been edited. Whether the pull request is open and unreviewed. Whether the assignee's activity has moved entirely to other work. Whether the task has been silently re-scoped. Whether it has been reassigned twice.

Every one of those is a stronger indicator of true state than the status field, and none of them is used to compute status.

## Why It's Unsolved
The data model was set early and everything is built on it. A status field is simple, human-legible and auditable, and inference is none of those. A platform that told a customer a task was probably stalled would have to be right, and being wrong in front of a team damages trust immediately.

The signal is also fragmented across tools by design. The task lives in one platform, the work happens in a code repository, a design tool, a document and a spreadsheet, and the connectors sync fields rather than meaning. Any inference worth having needs the activity, and the activity is somewhere else.

There is a surveillance objection that is entirely legitimate. Inferring who is stuck from behavioural signal is a short step from monitoring individuals, and a product that got that boundary wrong would be rejected outright and would deserve to be. The defensible version reports on work rather than on people, and that distinction has to be built in rather than promised.

And the business model points away from it. These platforms are measured on engagement, and status updates are engagement. A product that required fewer interactions would look worse on the metrics the vendor reports.

## What a Solution Looks Like
Status inferred from activity, expressed as a probability with the evidence attached, and shown alongside the declared status rather than replacing it. The useful output is disagreement: this task is marked in progress and has had no activity of any kind for eleven days.

Stall detection is the highest-value case and needs care to be socially acceptable. The right framing is about the work item and its dependencies — this task is blocked pending a review that has been open for nine days — rather than about the person assigned to it. That framing is also more accurate, since most stalls are dependency problems rather than individual ones.

Completion forecasting from actual throughput rather than from estimates. Teams have a measurable historical cycle time by work type, and it is a far better basis for a date than the estimate someone gave in a planning meeting.

And the honest addition: measure where work stalls repeatedly. Recurring bottlenecks at the same review step or the same handoff are organisational findings that no one in the company can currently see.

## Impact If Solved
Every portfolio report, forecast and escalation in these platforms rests on a field people update under social pressure, and the behavioural record that would replace it is already flowing through the same tools. Making status observed rather than declared is the difference between a system of record for work and a system that actually knows anything about it.
