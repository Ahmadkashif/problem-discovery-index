# The Change Nobody Could Assess

**Niche:** [[niches/customer-data-platforms/downstream-impact-tracing/profile|Downstream Impact Tracing]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Somebody wants to delete an unused field, nobody can establish what depends on it, so it stays forever and the next person cannot establish it either.
**Tags:** #graph-theory #workflow-orchestration #automation #evaluation-metrics #quick-win #descriptive-statistics #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to say what breaks when something changes, before it changes — and whoever builds that lineage across the customer data stack makes every other failure in the category preventable.

## The Problem
A field looks obsolete. Removing it would simplify a model, reduce cost and remove a source of confusion. Nobody can establish whether anything uses it, so the safe decision is to leave it. The same reasoning applies to an event, a table, a segment and an integration, so nothing is ever removed and the stack accumulates indefinitely. Every organisation in this category has a customer data platform full of things nobody dares touch, not because they are known to be load-bearing but because their status is unknown, and uncertainty always resolves toward inaction.

## Why It's Still Broken
Establishing dependencies requires searching several systems by hand, which costs more than leaving the field in place — the economics of investigation favour inaction every time and the accumulation is the predictable result. There is no cost visibly attached to keeping something. Nobody is responsible for the collection. And a removal that breaks something is a visible failure while an unused field is an invisible cost.

## What a Fix Looks Like
Make the dependency question answerable in seconds. Answer what depends on this from the lineage graph, which is the fix and converts a multi-day investigation into a query — the inaction is entirely rational given the current cost of finding out, and changes the moment that cost falls. Include usage as well as reference, since something referenced by a segment nobody runs is different from something in a live suppression list. Show last-used timestamps across the stack, which resolves most cases without any graph traversal. Flag confirmed-unused items proactively rather than waiting for someone to propose a removal. Attach the cost of keeping — storage, computation, complexity — so the ledger has both sides. Support safe removal with a deprecation period, monitoring and a rollback, which makes the decision reversible and therefore takeable. Track what was removed and what happened, so the organisation builds confidence in the process. Apply the same to segments, integrations and journeys, connecting to the sprawl work, since the pattern is identical across object types. Schedule review rather than waiting for someone to notice. And report the share of the stack whose dependency status is unknown, because that number is the real reason nothing ever gets removed.

## Who Feels the Pain
Engineers maintaining fields nobody uses; organisations paying to store and compute an accumulated stack; and every person who proposes a cleanup and is defeated by the investigation.

## Impact If Fixed
The economics of investigation favour inaction, so uncertainty accumulates by default. Answering the dependency question from a lineage graph converts a multi-day investigation into a query and changes what the safe decision is.
