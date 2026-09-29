# Idiomatic for the Language, Wrong for This Codebase

**Niche:** [[niches/developer-tools-vendors/developer-adopted-assistants/profile|Developer-Adopted Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assistants write code that is correct for the language and wrong for this repository, which is the difference between a suggestion a developer takes and one they delete every time.
**Tags:** #large-language-models #transformers #word-embeddings #transfer-learning #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor here is fighting to be the assistant a developer keeps switched on after week three — and whoever wins that takes the account regardless of what was procured, because an unused licence is a cancelled one.

## The Problem
A developer asks for a function to fetch a record. The assistant produces something textbook: a direct client call, an exception on failure, a plain dictionary returned. In this codebase every external call goes through a shared client with retry and circuit breaking, failures return a typed result rather than raising, and the domain objects are dataclasses with validation. The suggestion is competent, conventional and wrong in five ways, all of which the developer must fix. Every one of those conventions is visible in the surrounding code, in the module's imports, and in several hundred prior examples in the same repository.

## Why Nobody Has Built This
Context windows drove the early design toward including nearby code, which captures syntax and misses convention — a convention is a pattern across the codebase rather than a fact in the adjacent file. Extracting conventions requires analysing the repository as a corpus rather than retrieving fragments from it, which is a different architecture from the retrieval most assistants use. The conventions are also unwritten, which is precisely why they must be inferred: a project with a documented style guide has the easy half, and the hard half is the hundred unwritten choices nobody documented and everyone follows.

## What to Build
Convention as a first-class input. Mine the repository for its actual patterns: how errors are handled, how external calls are made, what the layering is, which utilities exist and are expected to be used, how tests are structured, how names are formed — each derived from frequency across the codebase rather than from a style file, which is the same technique the tacit-conventions problem elsewhere in this vault uses on query logs. Weight recent and frequently-modified code more heavily, since the conventions in a module nobody has touched in four years are not the ones the team follows now. Feed conventions into generation explicitly rather than hoping proximity captures them, and check output against them before presenting it, which catches the five wrong things before the developer sees them. Learn from rejection: a suggestion the developer immediately rewrites in a consistent way is a convention being taught, and it is the highest-quality signal available and is currently discarded. Surface the conventions to the team too, since a derived list of a codebase's unwritten rules is genuinely useful for onboarding independently of any assistant.

## Target Customer
Assistant vendors competing on developer retention, editor vendors building assistance in, and the engineering organisations whose adoption stalls because suggestions are consistently wrong in the same ways.

## Impact If Built
Convention mismatch is the most common reason a competent suggestion is useless, and the evidence for every convention is in the repository. Learning from the developer's rewrite closes a loop that every assistant currently throws away.
