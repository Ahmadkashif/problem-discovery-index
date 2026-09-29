# One Ambiguous String, Thirty Queries

**Niche:** [[niches/localization-services/source-readiness/profile|Source Readiness]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Fix (Pain Point)
**One-liner:** A one-word string with no context generates the same question from thirty linguists in thirty timezones.
**Tags:** #quick-win #automation #workflow-orchestration #data-integration #evaluation-metrics #descriptive-statistics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to catch the defects that were created in the source content before they enter thirty language pipelines and multiply — and whoever checks the source takes the account.

## The Problem
A short string — a button label, a status word, a menu item — is sent for translation with no indication of what it refers to or where it appears. Every linguist in every language hits the same ambiguity and raises the same query. Thirty queries route through a coordinator to an author who answers once, and the answer propagates back slowly. The delay affects the release, and the information needed existed in the author's head at zero cost when they wrote it.

## Why It's Still Broken
Context is not captured at authoring — an author writing a string knows exactly what it means and is never asked to record it, so the information is lost at the one moment it is free. The pipeline transmits strings rather than meaning. Queries are handled per language. And the cost lands on the coordinator.

## What a Fix Looks Like
Capture context where it is free and answer once. Require a context note or a screenshot for short and ambiguous strings at authoring, which is the fix and costs the author seconds. Supply the string's location and surrounding interface automatically where the platform allows, which is better than any note. Flag strings that are short, ambiguous or reused before they leave the source, since those are the predictable query generators. Answer a query once and propagate the answer to every language immediately, which is what turns thirty queries into one. Publish answered queries so a linguist checks before asking. Identify the strings that generated queries last release and fix their context permanently. Report query volume by source author or component, which is the feedback that changes behaviour. Give linguists a way to see the string in situ rather than in a list. Batch queries to authors rather than interrupting per language. And treat a high query rate as a source defect rather than as linguists being thorough.

## Who Feels the Pain
Linguists blocked waiting on an answer; coordinators routing the same question thirty times; authors interrupted by questions about something they wrote months ago; and the release date.

## Impact If Fixed
An author writing a string knows exactly what it means and is never asked to record it, so the information is lost at the one moment it is free. A context note at authoring turns thirty queries into none.
