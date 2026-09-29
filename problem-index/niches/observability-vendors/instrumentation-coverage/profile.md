# Instrumentation Coverage

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to tell an organisation what it cannot see before an incident rather than during one — and whoever does that takes the platform account, because every capability in the category is worthless on a service that emits nothing.

## Profile
**Market Size:** ~$1.1B US attributable to instrumentation, agents and coverage tooling
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Low — coverage is assumed and almost never verified
**Target Buyer:** Platform engineering and the observability practice owner
**Automation Potential:** Very High — expected coverage is derivable from the service inventory

## What Makes This a Distinct Niche
Everything in this category depends on the telemetry existing, and nobody checks that it does. A service is deployed without an agent. A library is upgraded and its automatic instrumentation stops attaching. A new language is introduced and its coverage is partial. Trace context is dropped at a boundary, silently truncating every trace that crosses it. A team disables a signal to reduce cost and does not tell anyone. Each of these is invisible until an incident, at which point the engineer discovers the gap at the worst possible moment. The remarkable part is that expected coverage is entirely derivable — the organisation knows what services it runs, from its deployment system and its cloud inventory — and reconciling that against what is emitting telemetry is a straightforward comparison that no platform performs.

## Current Tools & Gaps
Agents and automatic instrumentation with varying language and framework coverage; open instrumentation libraries; service catalogues maintained by hand. The gaps: nothing reconciles the service inventory against the telemetry inventory, so absence is undetectable; instrumentation health is not monitored, so a library upgrade that breaks auto-instrumentation is silent; trace propagation failures at boundaries are invisible and truncate everything downstream; signal coverage per service — metrics yes, traces partially, logs unstructured — is not reported; and the support burden this generates is substantial and is handled ticket by ticket.

## Problems
- [[niches/observability-vendors/instrumentation-coverage/build|🔨 Build: Discovering the Gap During the Incident]]
- [[niches/observability-vendors/instrumentation-coverage/buy|🛒 Buy: Coverage Reconciliation From Asset Management]]
- [[niches/observability-vendors/instrumentation-coverage/fix|🔧 Fix: The Boundary Where Trace Context Is Dropped]]
