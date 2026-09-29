# Emergency Detection by Keyword List

**Niche:** [[niches/proptech-platforms/work-order-triage-dispatch/profile|Work Order Triage & Vendor Dispatch]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Whether a maintenance request is an emergency is decided by whether the resident used a word on a list, so a calm description of an active leak is routed as routine and an alarmed description of a dripping tap wakes someone at midnight.
**Tags:** #bert #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #automation #quick-win
**Contested on:** Every serious competitor in maintenance triage is fighting to turn a resident's free-text complaint into the right trade, the right urgency and the right vendor without a site manager reading it — and whoever triages most accurately takes the account.

## The Problem
The after-hours emergency line and the portal both route on keywords: flood, fire, gas, no heat. A resident writes "there's been water coming from under the dishwasher since yesterday, it's spreading toward the carpet" — no keyword, routed to the morning queue, and by the morning it is a subfloor and a neighbour's ceiling. Another writes "EMERGENCY — my tap is dripping constantly" and a technician is dispatched at eleven at night. Both failures are common, the first is expensive and the second is corrosive to the on-call rotation, and the mechanism producing both is a list somebody wrote once.

## Why It's Still Broken
Keyword lists are easy to implement, easy to explain to an owner, and defensible in a dispute — the operator can point to a documented rule. Improving them means replacing an explainable rule with a judgement, which makes people uncomfortable in a domain with habitability obligations and legal exposure. And nobody measures the errors: there is no report anywhere of requests that should have been emergencies and were not, because establishing that requires linking a routine request to the escalated damage that followed, which nobody does.

## What a Fix Looks Like
Classify urgency from the described condition rather than from vocabulary, and measure both error types. The operator's own history contains the cases where a routine request escalated — a follow-up request, a large invoice, a habitability complaint — and those are the labels for the failure that matters. Tune deliberately asymmetrically, because an unnecessary after-hours visit costs a call-out fee and a missed active leak costs a floor, a neighbour's unit and a resident's trust. Keep the keyword list as a floor that can only escalate, never de-escalate, so the change is strictly safer than the current rule. And publish the two error rates — emergencies missed and false emergencies dispatched — which no operator currently has and which is the number that justifies every change to the policy.

## Who Feels the Pain
Residents living with an escalating problem that was classified as routine; on-call technicians woken for dripping taps; and operators absorbing damage costs whose origin is a triage decision nobody reviewed.

## Impact If Fixed
Condition-based urgency classification with an asymmetric threshold is a contained change with a large tail benefit, since the cost of this failure mode is concentrated in a small number of expensive escalations. Measuring the missed-emergency rate is the necessary first step and is available from the operator's own escalation history today.
