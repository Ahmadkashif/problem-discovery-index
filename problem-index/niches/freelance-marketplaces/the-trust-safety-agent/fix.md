# Fix: The Agent Never Learns Whether They Were Right

**Niche:** [[niches/freelance-marketplaces/the-trust-safety-agent/profile|The Trust & Safety Agent]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** An agent makes forty account decisions a day and receives feedback on almost none of them, so ten years of experience produces the same error rate as one.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #confidence-intervals #cross-validation #worker-facing #workflow-orchestration #quick-win
**Contested on:** Whether outcome feedback can reach the person who made the decision, given that the worst errors are the ones that generate no signal at all.

## The Problem

An agent suspends an account. The account holder either appeals or does not. If they appeal and win, the agent may hear about it as a correction. If they do not appeal — because they do not know how, because the appeal form is discouraging, because they gave up — the agent hears nothing and the decision is recorded as correct.

An agent clears an account. If the account was fraudulent, the fraud continues and surfaces months later as client complaints, chargebacks or a press story, attributed to nobody in particular. If the account was fine, nothing happens, which is indistinguishable from the fraud case in the agent's experience.

So the feedback the agent receives is almost purely the subset that generates a complaint, which correlates with the account holder's articulacy and persistence rather than with the correctness of the decision. Agents develop confidence rather than calibration, and the function's error rate is unknown in both directions.

## Why It's Still Broken

The outcome signal is genuinely delayed and partly unobservable. A wrongly cleared fraudster reveals themselves over months, if at all, and a wrongly suspended freelancer who leaves quietly produces no data at all. There is no clean label.

But the deeper reason is that nobody constructed the labels that are available. Cleared accounts subsequently confirmed fraudulent, suspended accounts subsequently reinstated on appeal, suspended accounts whose clients later complained the work stopped for no reason — all of these are in the platform's records and none is routed back to the agent who made the call. The infrastructure is a reporting job that was never assigned.

And the metrics point elsewhere. Agents are measured on handle time, queue throughput and policy adherence — whether the decision followed the documented process, not whether it was right. An agent can be fully compliant and consistently wrong.

## What a Fix Looks Like

Construct the feedback that exists and route it, then measure agreement for everything else.

Build the delayed label pipeline. For every decision, attach outcomes as they arrive: appeal filed, appeal outcome, subsequent confirmed fraud on a cleared account, subsequent reinstatement, chargebacks or client complaints on an account cleared, and the account's activity trajectory after review. Route these to the deciding agent on a defined cadence — a weekly digest of "here is what happened to the accounts you decided six weeks ago" — and aggregate them into a per-agent accuracy picture. All of this is a join over existing tables.

Correct for the appeal bias explicitly rather than ignoring it. Appeal rates vary enormously by language, tenure, earnings and geography, and treating an unappealed suspension as correct systematically understates errors against exactly the populations least able to contest them. Measuring the appeal rate by cohort and reporting the suspension record adjusted for it is uncomfortable and is the honest number.

Sample the silent cases. Take a random sample of suspensions that were never appealed and re-review them blind. This is the only way to see the error class that generates no signal, it is a small ongoing cost, and it is the single most informative measurement available in this function.

Measure inter-agent agreement, as with disputes. Route a standing sample to a second agent blind, record both decisions, report agreement by case type. Where agreement is poor, the policy is underspecified and needs deciding centrally rather than per-ticket.

Change what the agent is measured on. Handle time and policy adherence with no accuracy component produces fast, compliant, uncalibrated decisions. Adding a calibration measure — even an imperfect one — changes behaviour immediately, and is the reason to build the rest.

## Who Feels the Pain

Agents, who do consequential work for years without ever learning to do it better, and who carry the knowledge that some of their decisions were wrong without knowing which. Freelancers wrongly suspended who never appealed and simply lost their income. Clients exposed to frauds that were reviewed and cleared. And the platform, which cannot state its own enforcement error rate in either direction — an answer it will eventually be asked for by a regulator, a court or a journalist.

## Impact If Fixed

Agents get the feedback loop that turns experience into skill, which is the normal condition of skilled work and is absent here. The platform learns its error rate in both directions, including the silent errors against the people least able to complain. And enforcement decisions become measurable, which is the precondition for being able to defend them.
