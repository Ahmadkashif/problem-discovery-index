# Fix: The System Cannot Do It and There Is Nowhere to Say So

**Niche:** The Engineer Who Must Delete It
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The ticket has two states, done and not done, and the honest answer — this system has no deletion path — fits in neither.
**Tags:** #evaluation-metrics #compliance #worker-facing #workflow-orchestration #confidence-intervals
**Contested on:** Whether deletion is a capability the systems were built with, or a script an engineer writes each time.

## The Problem

An engineer receives a deletion task for a system that cannot delete. The backups are immutable. The logs are append-only and unindexed. The model was trained months ago. The event stream has a retention window and no per-subject removal.

The ticket offers two outcomes. Done, or not done with an escalation to a compliance manager who will ask when it will be done, because the statutory deadline is in nine days and the platform is showing this request as at risk.

So the engineer does what is available. They delete from the parts they can reach, mark the task complete, and mentally note the parts they could not. That note goes nowhere. The platform records completion. The confirmation goes to the individual. And the organisation's belief that it deleted the data is formed from a ticket state that does not distinguish full deletion from partial.

The engineer knows the truth and has no way to record it that does not read as failing to do their job. Escalating produces a conversation with someone who cannot change the architecture and a deadline that does not move. Marking it done is the path of least resistance and is what the system is designed to reward.

## Why It's Still Broken

**The workflow has no vocabulary for partial.** Ticketing systems model completion. There is no state for deleted where possible, with this remaining, for these technical reasons — so the information has nowhere to live.

**Admitting a system cannot delete creates an obligation.** Once recorded, it becomes a known architectural gap the organisation must fix or disclose, which is a programme nobody has budgeted.

**The deadline is absolute and the architecture is not negotiable.** The engineer is between a statutory window and a system design decision made years ago, with authority over neither.

**Escalation reaches the wrong person.** The compliance manager cannot rebuild the warehouse. The person who could is not in the workflow.

**Nobody aggregates the pattern.** If every deletion request hits the same three systems, that is a clear architectural priority. Because nobody records the partial failures, the pattern is invisible and the investment is never made.

**Reporting honestly makes the engineer the problem.** In a process measured on requests completed within the deadline, the person who says it cannot be completed is the obstacle.

## What a Fix Looks Like

**Add a partial completion state with a reason.** Deleted from these systems, not deleted from these, because of these technical constraints. This is the fix. It costs a field, it gives the engineer somewhere honest to put the truth, and it makes the organisation's actual position visible for the first time.

**Aggregate the reasons and act on them.** If the same three systems appear in every partial completion, that is the architectural backlog, ranked by evidence. Today the information is destroyed at the moment it is generated.

**Give systems a declared deletion capability.** Each system registered as fully deletable, partially deletable or not deletable, with the reason and any planned remediation. Then a request routed to an undeletable system produces a known outcome rather than an engineer improvising under deadline.

**Take the organisational position once, not per request.** The stance on backups, on trained models and on aggregates should be decided once by counsel and leadership, documented, and applied automatically. Making an engineer improvise a legal position at ten at night is the current arrangement and it is indefensible.

**Route architectural escalations to engineering leadership.** A deletion failing for structural reasons is an engineering matter, not a compliance chase. The escalation should reach someone who can fund a fix.

**Report what the individual is actually told.** If the organisation's position is that backups retain data until expiry, that should be in the confirmation. The engineer knowing something the confirmation does not say is the gap that matters most.

## Who Feels the Pain

The engineer, holding a task they cannot complete, a deadline they cannot move and a workflow with no state that describes their situation — and who marks it done because every alternative is worse for them.

The individual, told their data was deleted on the strength of a ticket state.

The privacy officer, whose confirmations rest on completion records that do not distinguish complete from partial.

And the organisation, which never learns which of its systems cannot delete, because the only people who know have nowhere to record it.

## Impact If Fixed

A partial completion state with a reason is a single field that converts a silently overstated position into an accurate one, and gives the engineer an honest option for the first time.

Aggregating the reasons produces the architectural backlog with evidence attached, which is what would actually get deletion capability funded.

And deciding the organisation's position on backups and models once, centrally, removes an impossible judgement from the engineer and puts it where it belongs.
