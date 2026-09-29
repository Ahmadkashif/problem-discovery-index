# Disengagement Detected Before It Becomes Absence

**Niche:** [[niches/fitness-wellness-software/remote-coaching-adherence/profile|Remote Coaching — Adherence at a Distance]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A remote client who is struggling stops opening the app before they stop training, and stops training before they stop paying, and the coach learns about all three at the cancellation.
**Tags:** #survival-analysis #change-point-detection #gradient-boosting #hidden-markov-models #confidence-intervals #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in remote coaching software is fighting to keep a client doing the programme when the coach cannot see them and everything is self-reported — and whoever raises sustained adherence takes the account.

## The Problem
A client's app opens drop from daily to twice a week. Their session logs become retrospective — entered in a batch on Sunday rather than at the time. Their check-in responses get shorter. Their message replies slow from hours to days. Every one of those precedes the missed sessions, and the missed sessions precede the cancellation by weeks. A coach with thirty clients might notice. A coach with three hundred, which is the whole point of the remote model, cannot. The platform records every one of those signals with a timestamp.

## Why Nobody Has Built This
The platforms report completion percentage because completion is what a coach asks to see, and nobody has proposed that the interesting signal is behavioural rather than performative. There is also a design caution that deserves respect: monitoring app-opening behaviour and message latency to infer a person's psychological state is close to surveillance, and clients have not consented to being modelled. The answer is that the inference should serve the client — it exists so a coach reaches out at the right moment — and that transparency about what is being used is the condition of doing it at all, not that the capability should be left unbuilt while clients quietly disengage.

## What to Build
An engagement state per client, inferred from the pattern of interaction rather than from completion. App opening frequency and timing, logging latency, check-in response length and sentiment, message reply time, and programme modification requests together separate a client who is busy and fine from one who is sliding — a distinction the completion percentage cannot make, because both show reduced sessions. The output is a short prioritised list for the coach with a suggested opening, because the intervention that works here is almost always a specific, human, non-judgemental message at the right moment, and the right moment is two weeks before the coach would otherwise notice. Clients should be told plainly that their engagement pattern is used to help the coach support them, with the ability to see what the coach sees — which is both the ethical requirement and, in practice, a feature clients respond well to.

## Target Customer
Online coaching businesses of any scale, hybrid coaches, and the coaching platform vendors whose adherence reporting is a percentage.

## Impact If Built
Adherence is the product in remote coaching — a client who does not do the programme gets no result and leaves, and the business's reputation is built on results. Catching disengagement two weeks earlier is the difference between a message that works and a cancellation, and it is the only way a coach serving hundreds can provide the attentiveness that the model promises and usually does not deliver.
