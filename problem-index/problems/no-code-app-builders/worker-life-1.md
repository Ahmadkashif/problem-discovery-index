# The Citizen Developer's Second Job

**Industry:** [[no-code-app-builders|No-Code App Builders]]
**Type:** Worker Life Changing
**One-liner:** The operations person who built a useful tool stops being its unpaid support desk, because the app documents itself, handles its own failures, and can be handed to someone else.
**Tags:** #large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #worker-facing

## The Problem
Someone in operations, finance or marketing builds a tool because they needed one. It works, colleagues start using it, and it becomes part of how the team operates.

They now have a second job that nobody assigned and nobody counts. When it breaks, they fix it. When someone needs access, they grant it. When a colleague does not understand it, they explain it. When a connected system changes, they discover it through a failure and repair it. When someone asks for a change, they build it, because there is no one else.

None of this is in their role description or their objectives. Their manager sees an operations person spending time on something adjacent to their actual work. Their own performance is measured on the operations work the app was supposed to make easier.

And they cannot stop. Handing it over is not possible because there is nothing to hand over: no documentation, no runbook, no second person who understands it. Leaving means abandoning colleagues who depend on it, which most people will not do.

The trap is that competence created it. The tool exists because this person was capable and helpful, and the reward is an unbounded ongoing obligation.

## Why It Matters to the Worker
This is invisible labour in the most literal sense — it appears in no system, is credited in no review, and is noticed only when it stops. A person can spend a meaningful share of their week on it and have that time counted as underperformance in their actual role.

The support burden is also the worst kind: unpredictable interruptions from colleagues, arriving at whatever moment the app broke, with an implicit urgency because a process is stalled.

There is a career distortion too. Some citizen developers discover they enjoy this and would like to move toward it, and there is no path — they are an operations person who makes tools, in an organisation that has no such role. Others want out and cannot leave, because the thing they built has become load-bearing and abandoning it feels like abandoning the team.

## What a Solution Looks Like
Documentation generated from the application itself. A no-code app is a structured specification — its tables, logic, triggers and connections are all machine-readable — so a plain description of what it does, what it connects to, and what each rule is for can be produced without the builder writing anything. That single artefact is what makes handover possible.

Error handling proposed automatically. Most citizen-built apps fail in predictable ways — a connection times out, a field arrives empty, a rate limit is hit — and the retry, branch or notification a developer would add reflexively can be suggested rather than learned through a broken Tuesday.

Support deflection through a generated explanation for users, so colleagues asking how it works get an answer that is not the builder.

Handover packaging as an explicit, supported action: documentation, connections, credentials, known issues and a second owner, produced as a bundle rather than assembled in a panic during someone's notice period.

And recognition through inventory. An app on a register with a named owner and a criticality rating is visible to a manager, which is the precondition for the time being acknowledged.

## Impact If Solved
No-code created a large population of accidental software owners carrying unbudgeted, uncredited support obligations. Generated documentation and automatic failure handling make these applications transferable, which is what lets the person who built one stop being permanently attached to it.
