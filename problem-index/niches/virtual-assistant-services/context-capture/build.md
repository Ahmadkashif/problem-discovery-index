# Build: Context Extraction from Work Traces

**Niche:** [[niches/virtual-assistant-services/context-capture/profile|Context Capture]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Read the messages, calendar actions and corrections that the work already produces, and propose the rules and preferences they imply for the assistant to confirm.
**Tags:** #large-language-models #transformers #word-embeddings #evaluation-metrics #confidence-intervals #graph-theory #tacit-knowledge-ml #automation
**Contested on:** Whether an executive's implicit rules can be inferred from the pattern of their corrections.

## The Problem

Everything an assistant learns is learned through a visible event. The executive says "not before ten on Mondays". A meeting is moved and then moved back. An email draft comes back with the tone changed. A supplier is escalated to the executive rather than handled. A task is done one way and corrected to another.

Each of these is a message or an action in a system, timestamped and retained. Together they contain most of what a complete procedure document would say, and nobody reads them for that purpose. The assistant internalises them; the record sits in an inbox.

The extraction is genuinely tractable now in a way it was not three years ago — inferring "this executive does not take meetings before ten on Mondays, with three confirming instances and one exception for the board" from a year of conversation is a summarisation and pattern-finding task over a modest corpus.

## Why Nobody Has Built This

The industry is low-technology by construction — the product is a person and a set of logins, coordinated over messaging — and the agencies are service businesses with little engineering capacity. Nobody in the arrangement is positioned to build software.

Access is also awkward. The traces live in the client's systems, often under the assistant's shared login, and reading them requires a permission conversation with a client who is already nervous about a contractor overseas having access to their inbox. That conversation is avoidable by not building the thing.

And the ownership question, once the context exists as an artefact, is one nobody wants to open — which is the reason capture keeps stalling despite everyone wanting the result.

## What to Build

An extraction and confirmation layer over the work traces.

**Ingest the traces with permission.** Executive-assistant message threads, calendar events with their edit history, task and email actions, document revisions, and escalations. Scope it narrowly and explicitly — the assistant's own working channels rather than the executive's entire inbox — because the permission conversation is easier for a narrow scope and the narrow scope contains most of the signal.

**Find the corrections.** The highest-value signal is a change: an action taken and then altered, an instruction followed by a clarification, a draft returned with edits. Each correction is a rule being taught, and detecting the correction pattern is the core of the extraction.

**Propose structured items with evidence.** "It appears meetings are not scheduled before 10am on Mondays — three instances, one exception on 14 March." Each candidate carries its supporting instances, so the assistant can confirm, amend or reject in seconds and can see why the system believes it.

**Distinguish rules from instances.** A single instruction is not a rule; three consistent ones probably are; an inconsistent pattern is a judgement call that should be recorded as such, with the factors that seem to matter. Getting this distinction right is what separates a useful record from a list of things that happened once.

**Build the relationship map.** Who is escalated, who is handled, who gets same-day replies, who is addressed formally. This is derivable from response patterns and message content and is among the most valuable and least documented parts of the context.

**Keep it current by asking.** Items that have not been confirmed recently, or that a recent action contradicted, get surfaced for a one-tap check. Maintenance by confirmation is what stops the record rotting.

**Handle the sensitivity properly.** Content about named third parties, inferred from private correspondence, assembled by a contractor. Scope limits, executive visibility and correction rights, and a clear statement of what is captured are product requirements, not settings — and getting them right is what makes the permission conversation winnable.

## Target Customer

Agencies, for whom this makes the replacement guarantee real and churn survivable, and for whom it is a genuine differentiator in a market competing on hourly rate. Also assistants directly, since the tool removes unpaid documentation work and makes them better at the job today.

## Impact If Built

The industry's only accumulating asset starts accumulating somewhere other than one person's memory, at close to zero effort. The assistant doing the job now gets a reference that is actually current. And the handover that currently costs a client three months becomes a document that already exists.
