# Build: Resolution as a Measured Quantity

**Niche:** [[niches/digital-bpo-operations/quality-and-resolution/profile|Quality & Resolution Measurement]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Define resolution operationally, measure it on every contact from the transcript and the downstream record, and report it alongside handle time.
**Tags:** #large-language-models #transformers #survival-analysis #confidence-intervals #evaluation-metrics #hypothesis-testing #causal-inference #revenue-impact
**Contested on:** Whether resolution can be established from the contact itself plus what happened afterwards.

## The Problem

The industry sells problem resolution and measures time. Every operational metric describes how an agent spent their seconds; the outcome the client is buying is estimated by a quality analyst reviewing four contacts per agent per month and a survey answered by a small, unrepresentative minority.

The consequences run through everything. Agents optimise what is measured, which is speed. Coaching is based on a sample too small to distinguish an agent's performance from noise. Clients cannot tell a vendor that resolves from one that closes quickly. And the tension the industry is built on — that a complex issue resolved properly takes longer and prevents a repeat contact nobody attributes back — is unmeasurable and therefore unarguable.

The full contact record now supports measurement across every interaction. The corpus is complete, well-structured, and has an outcome signal attached in the form of repeat contacts.

## Why Nobody Has Built This

Partly because the technology to read every transcript and judge whether an issue was resolved is recent. Partly because resolution has no agreed operational definition, and defining it means deciding what counts — which is an argument between the BPO and the client that neither has wanted to start.

And substantially because the measurement is commercially awkward. Contracts are written on handle time and cost per contact. A resolution measure would demonstrate that the targets in those contracts work against the outcome they are meant to proxy, which reopens every commercial conversation the industry has. Managing that tension has been cheaper than confronting it.

## What to Build

An operational definition, a full-population measurement and the analysis that follows.

**Define resolution with the client, explicitly.** Candidate definitions: no repeat contact on the same issue within a window; the customer's stated intent was satisfied within the contact; the downstream transaction completed. Each is measurable, each has failure modes, and choosing among them per contact type is the foundational step. It is a conversation, not a model, and it has to happen first.

**Measure repeat contact properly.** The strongest available signal and a survival problem: time to next contact, same customer, related issue, with issue relatedness judged from the transcripts. It requires the client's contact history across channels, which the BPO may only partly hold — and obtaining it is the single highest-value integration in this niche.

**Score the contact itself.** From the transcript: was the customer's issue identified, was it addressed, did the customer indicate satisfaction, was a commitment made and recorded, was the contact transferred or escalated. Language models do this well and every claim should be anchored to a point in the transcript so a human can check it.

**Combine into a resolution estimate with uncertainty.** In-contact assessment plus repeat-contact evidence plus survey where present. Report an interval, especially at the agent level, where monthly volumes are modest.

**Then run the analysis that matters.** The relationship between handle time and resolution, by contact type. The prediction is that it is positive on complex contacts — longer contacts resolve better — and flat or negative on simple ones, which would mean a uniform handle time target is wrong in a specific and fixable way. Nobody has measured this and it is the central empirical question of the industry.

**Report it next to handle time.** Same dashboard, same cadence, same visibility. A metric that exists in a quality report and not in the operational view will not change behaviour.

## Target Customer

BPO quality and operations leadership, where the internal case is coaching effectiveness and the differentiation case is real — a vendor that can demonstrate resolution has an argument nobody else in a price-competitive market can make. Also client-side vendor management, increasingly dissatisfied with buying on cost per contact.

## Impact If Built

The outcome the industry sells becomes the outcome it measures, on every contact rather than two percent. Coaching rests on a measurement rather than a sample. And the handle-time-versus-resolution tension becomes a quantified fact, which is the precondition for anyone doing anything about it.
