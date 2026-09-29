# Build: A Context Record That Survives the Assistant

**Niche:** [[niches/virtual-assistant-services/context-and-continuity/profile|Context & Continuity]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Accumulate the executive's preferences, relationships, rules and procedures as a structured record built from the work itself, so a replacement starts at month four rather than month zero.
**Tags:** #large-language-models #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #transformers #tacit-knowledge-ml #worker-facing
**Contested on:** Whether tacit working knowledge can be extracted from digital work traces rather than written down by hand.

## The Problem

The asset in this industry is context and the industry has no representation for it. It exists as an assistant's accumulated judgement, is never written down in any complete form, and evaporates on departure.

The consequences are specific. A replacement assistant spends three months being told things the previous one knew. The executive re-explains preferences they have explained twice before. Mistakes recur — a meeting moved that should not have been, a supplier addressed wrongly, an expense submitted the wrong way — that the previous assistant stopped making a year ago. And the client concludes that virtual assistance does not really work, which is a reasonable conclusion from their experience of it.

The work that generated the context is almost entirely digital. Messages between executive and assistant, calendar actions and their corrections, documents produced, forms submitted, decisions escalated. Most of what a good procedure document would say is derivable from it.

## Why Nobody Has Built This

Documentation has been treated as the assistant's responsibility, done by hand, unpaid, competing with the work. Predictably it is done partially and by the most conscientious, who are also the busiest.

The extraction approach was not feasible until recently — inferring an executive's preferences from the pattern of their corrections requires reading a year of unstructured conversation, which now costs very little.

And the ownership question sits underneath and has stopped several attempts. A context record is a description of how a client's business runs, assembled by an agency's worker. Building it forces a conversation about whose it is that nobody in the arrangement wants to have, and the easiest way to avoid the conversation is not to build the thing.

## What to Build

An accumulating context record built from the work, maintained with minimal effort, presented usefully.

**Extract from the traces.** Messages between executive and assistant, which contain the instructions, the corrections and the explanations. Calendar actions and their subsequent edits, which reveal the scheduling logic. Documents and their revisions. Escalations, which mark the boundary of the assistant's discretion. A model reading this produces candidate context items with evidence attached.

**Structure it into categories that are actually useful.** People and how to handle them. Calendar rules and their exceptions. Preferences by task type. Recurring procedures with their steps and gotchas. Standing decisions — what the assistant may do without asking. Vocabulary and shorthand. Each item with a source, a confidence and a last-confirmed date.

**Confirm rather than compose.** The assistant reviews candidate items — is this right, is this still true — in a few seconds each. This is the difference between a system that stays current and one that is written once and rots. Nothing should require writing a document.

**Handle the uncertain and the personal deliberately.** Some inferred context is wrong and some is sensitive — an executive's relationships and habits are personal, and the record should be visible to the executive, correctable by them, and bounded by an agreed scope. Getting this wrong makes the whole thing unacceptable.

**Make the handover the product.** On replacement, the incoming assistant receives the record, ordered by what they will need first, with a guided introduction. The agency's replacement guarantee becomes real rather than a promise to send someone else.

**Measure the ramp.** Time to independent operation, error rate in the first month, escalation frequency and executive-reported satisfaction, for replacements with and without the record. This is measurable, it is the entire business case, and no agency currently tracks any of it.

## Target Customer

Agencies, for whom the replacement guarantee is a costly promise that this makes deliverable and a differentiator in a market competing on price and hourly rate. Also clients directly, particularly those who have been through a replacement and know what it cost them.

## Impact If Built

The industry's only accumulating asset stops being destroyed on a routine event. A replacement assistant becomes productive in weeks rather than months, which makes the service compound rather than reset. And the executive stops re-explaining their own preferences, which is the experience that most sours clients on delegation.
