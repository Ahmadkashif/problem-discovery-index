# A Half-Completed Task With No Rollback

**Niche:** [[niches/ai-agent-platforms/agent-platforms-and-products/profile|Agent Platforms & Products]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An agent fails four steps into a six-step task having already issued a refund and updated a record, and there is no mechanism to undo what it did or resume where it stopped.
**Tags:** #workflow-orchestration #automation #data-integration #compliance #evaluation-metrics #worker-facing #quick-win #graph-theory
**Contested on:** Not terminal — the contest differs by whether the buyer is building the agent or buying its output, and the decomposition is recorded in the profile.

## The Problem
An agent handling an order change cancels the original order, issues a partial refund, and then fails when the replacement order rejects an out-of-stock item. The customer now has no order and a partial refund. Restarting the task would cancel an order that no longer exists. There is no record of what was done in a form anything can act on, no compensating action defined for the steps already taken, and no way to resume from step five. A human picks up the pieces from a conversation transcript, and the same shape of incident recurs across every deployment in the category.

## Why It's Still Broken
Agents were built as conversations rather than as transactions, and conversation frameworks have no concept of compensation. The compensating action for an arbitrary agent-chosen step is genuinely hard to define in advance, which has been treated as a reason to define none. Partial failure is rare enough per task to be tolerated and severe enough to dominate the support burden. And the customer-facing consequence lands on a support agent rather than on the vendor.

## What a Fix Looks Like
Make the task a transaction with a defined unwind. Record every effectful action with enough detail to reverse it — the tool, the arguments, the identifier of what was created or changed — which is a small addition to the trajectory record and is the precondition for any remedy. Require a compensating action to be declared alongside every effectful tool, so an integration that can issue a refund also declares how to reverse one, which is a contract at integration time and is where this becomes tractable. Support resume-from-step, since most failures are recoverable forward and restarting from the beginning is both wrong and expensive. Offer an unwind path a support agent can trigger, presented as the sequence of compensations with their consequences, rather than leaving them to reconstruct it. Detect partial completion explicitly and surface it as a state, rather than presenting a failed task as if nothing happened. Sequence effectful actions as late as possible in a task, since a plan that does all its reads first and its writes last has a much smaller unwind surface and this is a design guideline nobody states. Alert the customer proactively when a task partially completed, because discovering it themselves is what turns an incident into a complaint. And report partial-completion rates, since they are currently invisible and are the failure mode that costs most per occurrence.

## Who Feels the Pain
Customers left with half a transaction; support agents reconstructing what happened from a transcript; and vendors whose escalation volume is dominated by a failure mode nobody designed for.

## Impact If Fixed
Declaring a compensating action alongside every effectful tool is a contract at integration time and is what makes unwind tractable at all. Sequencing writes late in a task shrinks the unwind surface and is a design guideline the category has never stated.
