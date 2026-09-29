# Build: Net Recovered Hours as a Measured Quantity

**Niche:** [[niches/virtual-assistant-services/delegation-value/profile|Delegation Value Measurement]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure the executive time a delegation consumes as well as the time it saves, per task type, and tell the client which delegations are net positive.
**Tags:** #causal-inference #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #gradient-boosting #revenue-impact #data-integration
**Contested on:** Whether recovered executive time can be established without a counterfactual.

## The Problem

The proposition is that delegating tasks frees an executive's time. Whether it does depends on the balance between the time the task would have taken and the time spent briefing, clarifying, reviewing and redoing — and only the first side is ever considered.

Some delegations are enormously positive: a recurring administrative task with a stable procedure, handled without supervision. Some are negative: a judgement-heavy task briefed in twenty minutes, returned wrong, corrected in a meeting, and eventually done by the executive anyway. Most engagements contain both, and nobody can say which is which, so the client either continues paying for a mixture or cancels the whole thing.

The evidence exists. The briefing conversation is in a message thread. The review and rework are visible as revisions and follow-up messages. The executive's calendar shows what happened to their time.

## Why Nobody Has Built This

The agency is paid for hours and would be measuring something that could reduce them. That is the plain reason and it accounts for most of it — a measurement showing that four of the client's twelve delegated task types are net negative leads directly to a smaller engagement.

The measurement also requires access to the client's own systems, which is a permission conversation nobody wants to start, even though the assistant already has that access for the work itself.

And the causal question is genuinely awkward. Recovered time is a counterfactual — what the executive would have spent had they done it themselves — and it is never observed. That difficulty is real and it is far from insurmountable, since the consumed time is directly observable and the saved time can be estimated adequately.

## What to Build

A measurement of both sides of the ledger, per task type.

**Measure the consumed side directly, because it is observable.** Briefing time from the message thread and any calls. Clarification exchanges, counted and timed. Review and rework — revisions the executive made to returned work, and tasks returned more than once. Interruptions during the executive's focus time. All of this is in the client's messaging and document systems and needs no estimation.

**Estimate the saved side carefully.** For repeatable tasks, the assistant's time is a reasonable proxy adjusted for the executive's speed. For tasks the executive once did themselves, a baseline from before the engagement is far better — which is why a baseline period at onboarding is worth a great deal and is discussed in the fix. State the estimate as a range with the assumption visible.

**Report per task type, not in aggregate.** The actionable finding is that calendar management and inbox triage are strongly net positive, research briefs are marginal, and drafting client-facing communications costs more time than it saves for this executive. An aggregate number tells the client to continue or cancel; a breakdown tells them what to change.

**Track the improvement curve.** Net value per task type should rise over months as context accumulates, and a task type that does not improve after four months is one the delegation is not suited to. This is the measurement that turns an unhappy engagement into a re-scoped one.

**Include the error rate.** Errors on delegated work cost more than the time — a missed meeting, a wrongly addressed message, a bad calendar move — and they should be counted, categorised and tracked, because they are the reason executives stop delegating.

**Handle the access properly.** Scoped, consented, executive-visible, covering the assistant's own working channels rather than everything. Same posture as the context work, and the same conversation.

## Target Customer

Clients directly — the buyer with the interest in knowing — and agencies confident enough to be measured, for whom this is a strong differentiator in a market where everyone claims the same thing and nobody demonstrates it. Executive coaching and chief-of-staff services are a natural channel.

## Impact If Built

The thing being sold becomes the thing measured. A client learns which delegations work for them and which do not, and re-scopes instead of cancelling. Agencies that measure can prove a claim their competitors can only assert. And the common, undiagnosed failure — a delegation that costs more supervision than it saves — gets diagnosed.
