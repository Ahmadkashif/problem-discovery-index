# An Instrument for the Person on the Other Side

**Niche:** [[niches/mobile-game-publishers/the-monetisation-manager/profile|The Monetisation Manager]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every instrument a monetisation manager has measures revenue, and none measures the person producing it.
**Tags:** #worker-facing #change-point-detection #evaluation-metrics #confidence-intervals #logistic-regression #compliance #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to give the person tuning monetisation an instrument that says whether the small group producing most of the revenue is all right — and whoever builds it takes the account.

## The Problem
Revenue in these games is extremely concentrated. The manager tuning offers, bundles and randomised rewards can see that a small group produces most of it, and has no way to tell whether a given member of that group is an enthusiast with disposable income or someone in difficulty. The design patterns that maximise revenue from that group are the same either way. The manager is asked to optimise against people they cannot see, and most of them would use a better instrument if one existed.

## Why Nobody Has Built This
The metric set was built to answer revenue questions and nobody asked the other one. A welfare signal implies acting on it, which reduces revenue in a measurable quarter. The data that would indicate distress is behavioural and ambiguous. And no professional standard exists to make it anyone's responsibility.

## What to Build
Give the manager the missing half of the picture. Build a per-player welfare signal from behaviour — escalation rate, spending relative to established pattern, session timing, chasing after losses in randomised mechanics, abrupt cessation — which is the core and is entirely computable from data already held. Distinguish sustained enthusiast spending from a sharp escalation, since the two look identical in aggregate revenue and completely different in the individual series. Surface the signal inside the manager's existing tools rather than in a compliance report, because it only changes decisions if it is present at the moment of the decision. Offer per-player guardrails — cooling-off prompts, limits, reduced offer pressure — as an available action rather than a policy debate. Report a welfare outcome alongside revenue on every monetisation test, which is the change that makes the rest durable. Track players who stopped abruptly after heavy spending, as that population is currently invisible and is the clearest evidence. Let players set their own limits and make it easy, which is both the right thing and the defensible one. Model the revenue cost of guardrails honestly, since pretending it is free is why these proposals fail. Give the manager a documented standard to point at, which is what protects them internally. And keep the individual signal private to the guardrail system rather than exposing it as a targeting input.

## Target Customer
Mobile publishers, monetisation and live product teams, platform holders setting policy, and regulators and consumer protection bodies.

## Impact If Built
The manager is asked to optimise against people they cannot see, and the design that maximises revenue is the same whether the person is fine or not. A behavioural welfare signal in the manager's own tools is what makes a different decision possible.
