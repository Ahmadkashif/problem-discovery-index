# The Maintenance Cliff

**Industry:** [[no-code-app-builders|No-Code App Builders]]
**Type:** High Impact
**One-liner:** Detect when an app has crossed from a personal convenience into a load-bearing business process, before the person who built it leaves — because that crossing is currently invisible until it becomes a crisis.
**Tags:** #gradient-boosting #graph-neural-networks #change-point-detection #large-language-models #feature-engineering #confidence-intervals #evaluation-metrics #workflow-orchestration

## The Problem
No-code succeeded at its actual promise. Someone in operations who cannot write code builds a tool that solves their problem in an afternoon, and it works. This is genuinely valuable and it is why the category grew.

Then it spreads. A colleague starts using it. A process gets built around it. It connects to two other systems. A year later, a real business function — order exceptions, vendor onboarding, incident triage, commission calculation — runs on an application with no owner of record, no documentation, no tests, no error handling for the cases nobody anticipated, and no runbook.

The crossing from convenience to dependency happens without any event marking it. Nobody decides that this app is now critical; it just becomes so, incrementally, through use.

The crisis arrives predictably. The builder changes roles or leaves. A source system changes an API. A volume spike breaks an assumption. And nobody can safely modify the app, because nobody understands why it does what it does — and nobody can turn it off, because a process depends on it and the process was never written down anywhere except in the app itself.

Every organisation with meaningful no-code adoption has several of these, and cannot list them.

## Why It's Unsolved
The category's premise is that building requires no gatekeeper, and criticality assessment sounds like a gatekeeper. Vendors are commercially and philosophically committed to frictionless creation, and anything that looks like governance is positioned as a large-enterprise add-on rather than as a core concern.

Criticality is also genuinely hard to define. Daily usage by twelve people might be trivial or might be the accounts payable process. What matters is what depends on the app and what happens if it stops, and neither is visible from within the platform.

Nobody owns the problem. IT does not know the app exists. The builder does not consider themselves a software owner. The department benefits and bears no cost until failure. There is no party whose job it is to notice.

And AI-generated app building has made creation dramatically faster over the last two years, which increases the rate at which these dependencies form while doing nothing about their lifecycle.

## What a Solution Looks Like
Criticality inference from observable signals. Distinct user count and its growth, usage frequency and regularity, whether use has spread beyond the builder's own team, the number and nature of connected systems, whether it writes to systems of record rather than only reading, data volume, and whether it operates on a schedule that suggests a process rather than an exploration.

The trajectory matters more than the level. An app whose usage is spreading is becoming critical, and that is the moment to intervene — before the builder leaves, not after.

Bus-factor detection is the sharpest single output: an application that only one person has edited, that many people depend on, whose author's activity is declining, is a specific and nameable risk.

Intervention should be graduated and non-punitive. The right response to a rising app is not to shut it down but to attach documentation generated from its own logic, assign a second owner, add error handling and a backup, and put it on an inventory. Framing it as support rather than as governance is what determines whether builders cooperate.

Fragility analysis completes it: which external dependencies would break this, what happens when a source schema changes, and which failure modes are unhandled.

## Impact If Solved
Organisations are accumulating undocumented, unowned dependencies on software built by people who did not know they were building software, at an accelerating rate. Detecting the crossing point and intervening supportively is the difference between no-code as a capability and no-code as a slowly compounding operational risk.
