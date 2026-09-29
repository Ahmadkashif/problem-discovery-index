# Nobody Measures Whether the Delegation Saved Any Time

**Industry:** [[virtual-assistant-services|Virtual Assistant Services]]
**Type:** High Impact
**One-liner:** The service is sold as recovered executive hours, billed as delivered assistant hours, and the difference between those two is measured by nobody.
**Tags:** #gradient-boosting #causal-inference #time-series-forecasting #confidence-intervals #large-language-models #evaluation-metrics #revenue-impact #hypothesis-testing

## The Problem
A client engages a virtual assistant to take work off their plate: scheduling, inbox triage, travel, research, document preparation, expense processing. The agency bills for hours delivered and reports them, along with a satisfaction score.

Whether the executive got time back is a different question. Delegation has a cost: explaining the task, answering clarifying questions, reviewing the output, correcting it, and re-explaining for next time. For genuinely routine work with a well-briefed assistant that cost is small and the net saving is large. For ambiguous work with a new assistant it frequently exceeds the task itself, and the executive does more work than if they had done it themselves — a situation everyone in this industry recognises and nobody quantifies.

The failure is invisible in both directions. A client who is not saving time usually attributes it to this particular assistant rather than to the task mix or the briefing quality, and churns to a replacement, restarting the context-building cycle. An assistant who is performing well on unsuitable work has no way to demonstrate it.

The data exists. Calendar and email systems record what was handled, how many exchanges each task required, whether the executive sent a correction afterwards, and how the executive's own time was spent before and after the engagement began. None of it is examined.

The consequence is a service that is procured on faith, renewed on rapport, and churned on a feeling. Agencies report high satisfaction and high turnover simultaneously, which is a signal that the satisfaction measure is not capturing whatever is actually going wrong.

## Why It's Unsolved
Measuring requires access to the client's own systems at a level that is intrusive — calendar, email metadata, how an executive spends their day. Some of that is available with consent and some of it should make everyone uncomfortable, particularly given how easily the same instrumentation becomes surveillance of the assistant.

The agency's incentive is hours. A finding that certain task types do not net out reduces billable volume, and the agency is not paid to identify them.

Attribution is genuinely hard. An executive's time use changes for many reasons, and isolating the assistant's contribution requires either a before-and-after comparison with substantial confounding or a deliberate variation in task allocation that nobody would run.

And the client is often not the buyer of a measurement conversation. Executives engage assistants to reduce administrative load, not to acquire an analytics programme, and a service that arrives with instrumentation is a harder sell than one that arrives with a person.

## What a Solution Looks Like
Measure at the task level rather than the engagement level. How many exchanges a delegated task required, whether it came back for correction, how long it took end to end, and whether the executive touched it again — these are observable from the communication record with consent and they identify which task types actually net out for this pairing. That is more useful than an aggregate and far less intrusive than time-use surveillance.

Build the delegation profile. Different executives can delegate different things successfully depending on how they work, and after a few months the record says which. An agency that could tell a client which task types to delegate and which to keep would be selling advice rather than hours.

Separate briefing quality from assistant performance. Many delegation failures are caused by underspecified requests, and distinguishing that from assistant capability protects the assistant from being churned for a fault upstream — which is currently the default outcome.

Treat the correction signal carefully. Rework rate is the most informative available quality measure and is also the one most easily turned into a monitoring tool pointed at the assistant. The defensible design reports it to the pairing and to the agency in aggregate, not as an individual productivity score, and the distinction matters because this workforce has no bargaining position.

## Impact If Solved
The industry sells one thing and bills another, with no instrument connecting them, which is why engagements churn at a rate inconsistent with the satisfaction scores. Task-level measurement identifies which delegation actually works for this executive, separating briefing quality from assistant performance stops the wrong party being replaced, and a delegation profile turns an hours business into an advisory one — which is the only defensible position as generative tooling absorbs the routine tasks that currently fill the hours.
