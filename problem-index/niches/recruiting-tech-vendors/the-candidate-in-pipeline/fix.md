# Fix: The Requisition Closed and Nobody Was Told

**Niche:** [[niches/recruiting-tech-vendors/the-candidate-in-pipeline/profile|The Candidate in the Pipeline]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The role was filled in March and forty candidates are still shown as under consideration, indefinitely.
**Tags:** #workflow-orchestration #descriptive-statistics #evaluation-metrics #compliance #confidence-intervals #quick-win #worker-facing #automation
**Contested on:** Whether closing a requisition will also close the candidates in it.

## The Problem

A requisition fills. The recruiter moves to the next one. The candidates who were screened, interviewed or simply left in the pipeline are never moved to a final status and never told anything.

Some are in "under review" forever. Some were rejected in the system months ago and the notification was never sent. Some interviewed twice, were told a decision was coming, and heard nothing ever again.

This is the single most complained-about experience in hiring, and it is one automated action at requisition close: move every remaining candidate to a closed status and send them a message. The system knows the requisition closed. It knows who is still in it. Nothing connects the two.

## Why It's Still Broken

Closing out candidates is the last task on a requisition that is already done, competing with the next requisition which is already late. It is unmeasured, unrewarded and invisible.

The rejection at this stage is also the most uncomfortable one — these are people who interviewed, who were engaged with, and to whom a template feels inadequate. So it is deferred, and deferral becomes never.

And the ATS does not prompt it. Requisition closure is a status change on the requisition, with no cascade to the candidates, which is a workflow omission nobody has raised because the affected party is not a user.

## What a Fix Looks Like

Cascade the closure. It is one automated action.

On requisition closure, move every candidate not hired to a final status and send a notification. Automatically, as part of the closure, not as a task someone must remember. This single change eliminates the largest population of permanently uninformed candidates in the industry.

Differentiate by how far they got. A candidate who applied and was screened out gets a brief message; one who interviewed three times gets a longer one, and ideally a call. The system knows which is which and the template should follow.

Send the pending rejections. Candidates already marked rejected in the system with no notification sent are a queryable list at any moment, and sending them is a batch action. Most employers have thousands.

Block requisition closure until it is done, or auto-execute it. Making the cascade mandatory is what converts intention into practice.

Say what happened where it is favourable. "The role was filled internally" and "the requisition was cancelled" are both common, both reassuring to a candidate who is otherwise drawing conclusions about themselves, and both entirely safe to say.

And report the number. Candidates left in non-final states on closed requisitions, per quarter. It will be large, it is a count, and nobody has ever produced it.

## Who Feels the Pain

Candidates left indefinitely in a state that says they are being considered, who check the portal for months and draw conclusions about themselves that are entirely wrong. Candidates who interviewed repeatedly and were ghosted, which is the version people tell everyone about. And employers, whose reputation with the exact population they most want is being set by an unexecuted workflow step.

## Impact If Fixed

The largest group of uninformed candidates in hiring is closed out automatically at requisition close. The backlog of unsent rejections goes in one batch. And the most damaging single experience an employer's hiring process produces stops happening, at the cost of a cascade rule.
