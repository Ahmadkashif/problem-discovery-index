# Build: Structured Briefing and Pre-Review Error Detection

**Niche:** [[niches/virtual-assistant-services/task-handoff-and-quality/profile|Task Handoff & Quality Control]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Prompt the missing constraint at the moment of briefing, and check the returned work against the brief before it reaches the executive.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #transformers #workflow-orchestration #descriptive-statistics #worker-facing #automation
**Contested on:** Whether a brief's missing constraints can be identified before the work is done wrong.

## The Problem

Delegation fails one task at a time, and the failure is nearly always a briefing gap. The executive did not say the deck was for the board rather than the team, that the flights had to be refundable, that the email should go out today rather than tomorrow, that the format follows last quarter's. Each omission is obvious in retrospect and invisible at the moment of writing, because the executive holds the context and does not know they have not said it.

The assistant then either asks — costing an exchange and the executive's attention — or guesses. Guessing right is invisible; guessing wrong produces rework and erodes trust. Over a few months, enough wrong guesses and the executive stops delegating anything that matters, which is the common quiet death of these engagements.

## Why Nobody Has Built This

Briefing happens in a message, in the executive's own tools, in the middle of everything else. Any intervention has to live there and be nearly free, and nothing in this industry has been built into the client's messaging at all.

The capability is also new. Recognising that a briefing for a travel booking omits the refundability preference requires understanding both the task type and this executive's history, which is a generative capability that arrived recently and has not been pointed here.

And nobody owns task quality. The agency's quality management is account-level satisfaction; the executive's is their own review; the assistant absorbs the rework.

## What to Build

A briefing assistant at the point of handoff and a check at the point of return.

**Prompt the missing constraints.** When a task is briefed, compare it against what this task type has required before — from the context record and from prior instances of the same task — and surface the two or three things that are usually specified and are not here. "Last time you asked for refundable fares" or "you have not said who the audience is". One line, dismissible, at the moment of writing.

**Offer the prior brief.** For recurring tasks, showing how this was briefed last time is simpler than any model and often sufficient. Most executive delegation is repetitive and most briefs are written from scratch every time.

**Let the assistant clarify cheaply.** A structured clarification — a specific question with the likely options — costs the executive ten seconds rather than a conversation. Most clarification exchanges are long because they are conducted in prose.

**Check the returned work against the brief.** Before it reaches the executive, verify the checkable things: the stated constraints were met, the format matches the example, the named people are correct, the dates are consistent, the figures add up. Many errors that cause rework are mechanical and detectable, and catching them before the executive sees them is worth more than catching them faster afterwards.

**Categorise the errors that get through.** Misunderstood brief, missing context, execution error, changed requirement. The distribution tells the agency what to fix — a high misunderstood-brief rate is a briefing problem, a high missing-context rate is a context problem, and they call for opposite responses.

**Count the round trips.** Per task type, per placement, over time. This is the operational quality metric this industry lacks, it should fall as context accumulates, and a task type where it does not fall is one that is not suited to this delegation.

## Target Customer

Agencies, for whom round-trip reduction is the most legible quality improvement they can offer and one competitors cannot claim. Also clients directly and assistants, who bear the rework and would use a tool that reduced it.

## Impact If Built

Tasks get done right the first time more often, which is the entire difference between delegation that saves time and delegation that consumes it. Mechanical errors stop reaching the executive. And the round-trip count gives the industry an operational quality metric it has never had.
