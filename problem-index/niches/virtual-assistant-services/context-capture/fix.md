# Fix: The Correction Is Never Recorded as a Rule

**Niche:** [[niches/virtual-assistant-services/context-capture/profile|Context Capture]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Fix (Pain Point)
**One-liner:** Every time an executive corrects an assistant they are teaching a rule, and the rule is learned by one person and written down nowhere.
**Tags:** #descriptive-statistics #large-language-models #evaluation-metrics #workflow-orchestration #confidence-intervals #worker-facing #quick-win #tacit-knowledge-ml
**Contested on:** Whether a correction will be turned into a recorded rule at the moment it happens.

## The Problem

An executive says "actually, always copy legal on these" or "don't schedule anything the afternoon before a board meeting" or "that supplier goes through procurement, not me". Each is a rule, stated once, in a message, in the middle of other work.

The assistant remembers it. It goes into their head and nowhere else. Over a year there are hundreds, and together they are the whole difference between a new assistant and an experienced one.

Nothing captures them at the moment they are stated, which is the only moment they are cheap to capture — the executive has just articulated the rule, the assistant has just understood it, and writing it down would take fifteen seconds. Instead the plan is to write a procedure document later, from memory, which happens partially or never.

## Why It's Still Broken

Documentation is deferred by default because it is always less urgent than the work. The intention to write it up later is genuine and the later never arrives.

The tooling also has nowhere natural to put it. The correction arrives in a message thread; the documentation lives in a different system; and capturing it means switching context, which under any load does not happen.

And nobody has asked for it. The client assumes the assistant will remember, which they will, for as long as they are there. The agency treats documentation as an onboarding artefact rather than a continuous one.

## What a Fix Looks Like

Capture the rule where it is stated, in one action.

Put the capture in the channel. A reaction, a command or a button on a message that turns it into a context item — no switching, no form, no document. Fifteen seconds at the moment the rule is fresh, when the assistant knows exactly what it means.

Prompt for it. A model watching the executive-assistant channel can flag messages that look like instructions or corrections and ask "is this a rule worth recording?" — one tap to accept, with the wording drafted. This converts capture from a discipline into a prompt, which is the difference between it happening and not.

Review weekly, briefly. Five minutes at the end of the week confirming, editing or discarding the items captured. A short cadence keeps the record accurate and keeps the habit alive.

Show the record back in use. If the context record is what the assistant consults when unsure, it gets maintained, because it is serving them now rather than serving their eventual replacement. A record that only pays off at departure will not be kept.

Let the executive see and correct it. Many will be surprised at what has been inferred about their preferences, some of it wrong and some of it out of date, and a five-minute review by the executive is the highest-quality correction available.

And make it part of the paid engagement rather than something assistants are expected to do in their own time — which is the reason most documentation in this industry is thin.

## Who Feels the Pain

Assistants, who carry hundreds of rules in their head and are asked to reconstruct them at departure. Executives, who state the same preference to a second assistant and then a third. Incoming assistants, who learn each rule by breaking it. And agencies, who promise continuity and deliver a person with no context.

## Impact If Fixed

The rules get recorded at the one moment they are cheap to record, which over a year builds the context document that nobody would ever sit down and write. The assistant doing the job now has a reference. And the executive stops teaching the same rule to every assistant they are sent.
