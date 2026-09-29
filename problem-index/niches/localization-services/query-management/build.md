# Answer Once, Propagate Everywhere

**Niche:** [[niches/localization-services/query-management/profile|Query Management]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thirty linguists independently ask the same question and thirty answers travel back separately.
**Tags:** #automation #workflow-orchestration #word-embeddings #data-integration #evaluation-metrics #large-language-models #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to answer a linguist's question once rather than thirty times, and whoever routes and propagates those answers takes the account.

## The Problem
A query is raised because a linguist cannot proceed. It travels to a coordinator, who routes it toward whoever can answer — often a source author two organisations away — and waits. Meanwhile linguists in other languages hit the same ambiguity and raise the same query independently. The answers, when they come, return one at a time. The pipeline blocks in thirty places for one missing piece of information.

## Why Nobody Has Built This
Queries arrive through email and chat with no structure to deduplicate on. Routing depends on knowing who can answer, which lives with the coordinator. Nobody measures query-driven delay. And the coordinator absorbing it means the volume never surfaces as a problem worth engineering.

## What to Build
Deduplicate, route and propagate. Detect that queries from different languages are about the same source segment and merge them, which is the core and collapses the volume by the language count. Route to the person who can answer based on the content's origin rather than through a general channel, which is where most of the waiting happens. Propagate an answer immediately to every linguist blocked on it, which is what turns thirty exchanges into one. Maintain a searchable history so a linguist checks before asking, since a meaningful proportion have been answered before. Answer the recurring questions with a standing note attached to the content rather than repeatedly. Track query-driven blocked time per language, which is the measure that shows where the delay actually comes from. Attribute queries back to the source content that generated them, so the upstream fix is possible. Escalate unanswered queries on a schedule rather than leaving the coordinator to chase. Batch queries to each answerer rather than interrupting per query. And treat a high query rate on a release as a source readiness signal rather than a linguist behaviour.

## Target Customer
Language service providers and enterprise localization teams, localization operations, translation management vendors, and workflow tooling providers.

## Impact If Built
One missing piece of information blocks the pipeline in thirty places and produces thirty separate exchanges. Deduplication with answer propagation collapses the volume by the language count.
