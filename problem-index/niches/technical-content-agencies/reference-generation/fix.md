# The Table Somebody Maintains by Hand

**Niche:** [[niches/technical-content-agencies/reference-generation/profile|Reference Generation & Build Tooling]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The configuration reference is a table a writer updates when someone remembers to tell them.
**Tags:** #quick-win #automation #data-integration #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to generate reference material from the source of truth rather than maintaining it by hand, and whoever makes that generation reliable takes the account.

## The Problem
Every documentation corpus contains hand-maintained tables of things the product defines: configuration options, environment variables, error codes, command flags, permissions. They are updated when an engineer remembers to mention a change, which is sometimes. They are consulted constantly, they are wrong in specific ways nobody can predict, and the writer maintaining them knows they are wrong and cannot verify them without asking about each row.

## Why It's Still Broken
The source is not connected to the table — a list derived from code and retyped into a document has no relationship to the code afterwards, so it can only be updated by somebody remembering. The interface has no specification format. Generation was never attempted for it. And the table looks maintained.

## What a Fix Looks Like
Generate the table from wherever the product defines it. Extract the option list from the product's own definitions rather than maintaining it, which is the fix and is usually a short script against a schema, a parser or a help output. Compare the generated list against the hand-maintained table to find what is wrong, which is a useful one-off finding even before any generation ships. Keep the descriptions in the source's annotations so they are updated where the change happens. Fail the documentation build when the generated list changes unexpectedly, which turns a silent drift into a notification. Start with the most-consulted table rather than all of them. Cover the defaults as well as the names, since a wrong default is the most damaging kind of error here. Mark generated sections clearly so nobody edits them by hand. Retire the hand-maintained version rather than keeping both. Ask engineering to annotate at source, which is a small ask with a clear benefit to them too. And check the remaining hand-maintained tables against the product once, which usually finds enough to justify the work.

## Who Feels the Pain
Readers configuring a product from a wrong table; writers maintaining lists they cannot verify; support teams handling the resulting confusion; and engineers asked to review a table of two hundred rows.

## Impact If Fixed
A list derived from code and retyped into a document has no relationship to the code afterwards, so it can only be updated by somebody remembering. Generating from the product's own definitions is usually a short script.
