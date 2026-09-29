# Approving Without Reading

**Niche:** [[niches/spend-management-platforms/exception-judgement/profile|Exception Judgement]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The manager has forty approvals waiting, approves them all in ninety seconds, and the control is satisfied.
**Tags:** #worker-facing #quick-win #descriptive-statistics #evaluation-metrics #automation #compliance #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of recorded approve-or-deny judgements a month into automated judgement that a controller trusts — and whoever does it takes the approval queue out of the product entirely.

## The Problem
Approval queues arrive as a list of items requiring attention. Most are routine. The manager, who has other work, approves in bulk. The audit trail records forty considered judgements. The control exists on paper and not in fact, and the one item in the batch that genuinely warranted scrutiny received the same ninety milliseconds as the rest. Everyone involved knows this and the process continues because there is no alternative offered.

## Why It's Still Broken
The queue presents every item as equally deserving of attention, so the only rational response at volume is to clear it — a design that treats all exceptions alike produces exactly this behaviour. Approval speed looks like efficiency in reporting. Nobody measures time spent per approval. And admitting the control is nominal is uncomfortable for both the platform and the customer.

## What a Fix Looks Like
Make the queue triaged rather than flat. Group the routine items and present the unusual ones separately, which is the fix and is the difference between a control and a formality. Show why each item was flagged, since a manager cannot judge what they cannot see the reason for. Highlight the item that differs from this employee's or this team's history, as that is the one worth reading. Report time spent per approval, which is a straightforward measurement and will show exactly how nominal the control is. Let managers approve routine batches explicitly as a batch rather than pretending each was considered, because honest bulk approval is better than dishonest individual approval and is auditable. Reduce the volume at source by fixing the rules that generate it, which connects to policy design. Remind on the items still open rather than on the whole queue, since aged items are where risk sits. Show the approver their own approval rate, as awareness alone changes behaviour. Route the genuinely unusual to someone with time, which requires distinguishing the two. And report control effectiveness rather than approval completion, since the latter is currently being reported as if it were the former.

## Who Feels the Pain
Managers clearing queues they cannot read; controllers relying on approvals that did not happen; auditors receiving evidence of a process rather than of a control; and companies paying for control they are not getting.

## Impact If Fixed
A queue that treats every item alike produces bulk approval as the only rational response at volume. Triaging routine from unusual is what converts a formality back into a control, and both are visible in the data today.
