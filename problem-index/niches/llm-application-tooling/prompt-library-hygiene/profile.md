# Prompt Library Hygiene

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to tell a team which of their prompts are used, which duplicate each other and which can be deleted — and whoever does that takes the account, because the estate only grows and nobody can safely remove anything.

## Profile
**Market Size:** ~$150M US
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** None — sprawl nobody can safely delete
**Target Buyer:** Teams with accumulated prompt estates
**Automation Potential:** Very High — usage, similarity and equivalence are all computable

## What Makes This a Distinct Niche
Prompt libraries grow into hundreds of overlapping templates that nobody can safely delete, because no one knows which are in use, which duplicate each other, or what any of them do that matters. Every feature adds one, every experiment leaves one behind, every team copies another team's and modifies it slightly. Nothing is ever removed, because removing something requires knowing it is unused and nobody records usage. The estate grows monotonically, the duplicates diverge silently so that two nearly-identical prompts behave differently, and a change intended to fix a behaviour fixes it in one of the five places it lives. Every input to fixing this — usage, similarity, behavioural equivalence — is mechanically computable.

## Current Tools & Gaps
Prompt registries with versioning, folders and tags, and search. The gaps: no usage tracking from production, so nothing is known to be dead; no duplicate or near-duplicate detection; no behavioural equivalence testing, so two similar prompts cannot be merged confidently; no ownership, so nothing has a person to ask; and no lifecycle, so everything is permanent by default.

## Problems
- [[niches/llm-application-tooling/prompt-library-hygiene/build|🔨 Build: Hundreds of Templates Nobody Can Delete]]
- [[niches/llm-application-tooling/prompt-library-hygiene/buy|🛒 Buy: Dead Code Detection and Clone Analysis]]
- [[niches/llm-application-tooling/prompt-library-hygiene/fix|🔧 Fix: Fixed in One of the Five Places It Lives]]
