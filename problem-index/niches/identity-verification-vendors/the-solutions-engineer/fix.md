# The Same Escalation Every Week

**Niche:** [[niches/identity-verification-vendors/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The same three failure patterns generate most escalations and each one is investigated from scratch.
**Tags:** #worker-facing #quick-win #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #large-language-models #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to let a solutions engineer explain why one specific person could not open an account — and whoever makes the decision articulable changes what the escalation conversation can be.

## The Problem
Escalations cluster. A particular document type that reads badly on a common phone model, a name format that breaks the database match, a jurisdiction whose new licence is not supported, a liveness check that fails in certain lighting. Each escalation is investigated individually, explained individually, and closed individually. The pattern is obvious to any engineer who has been there a year, is recorded nowhere, and reaches the product team as anecdote if at all.

## Why It's Still Broken
Escalations are tickets, so they are resolved and closed — a queue designed around individual resolution has no concept of a pattern across its items. Nobody categorises the causes. Engineers are measured on response time. And the product roadmap is driven by customer requests rather than by escalation data.

## What a Fix Looks Like
Categorise the escalations and read them as a whole. Classify every escalation by failure cause in a fixed vocabulary, which is the fix and takes seconds per ticket while making the pattern visible for the first time. Report the top causes by volume, since a handful will dominate and each is a concrete product defect. Write a standing explanation for each known pattern, so engineers stop composing the same answer. Feed the top causes into the roadmap as evidence, which is a stronger input than the feature requests currently driving it. Detect a new pattern early from a cluster of similar escalations, because that is the leading indicator of a document revision or a device issue. Share the known patterns with customer-facing teams, as they can often answer without escalating at all. Publish a short internal knowledge base from the patterns, since the knowledge currently lives with whoever has been there longest. Track resolution time by cause, which shows where tooling would help most. Close the loop when a fix ships, so the engineers see the effect. And measure escalation volume as a product quality metric, because it is one and is currently treated as a support cost.

## Who Feels the Pain
Engineers re-investigating the same patterns; customers escalating recurring issues with no resolution; applicants failing for reasons the vendor already knows about; and product teams working from anecdote.

## Impact If Fixed
A queue designed around individual resolution has no concept of a pattern across its items, so recurring defects are rediscovered weekly. Classifying escalations by cause makes the dominant failure modes visible and turns support load into roadmap evidence.
