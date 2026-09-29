# Fixed in One of the Five Places It Lives

**Niche:** [[niches/llm-application-tooling/prompt-library-hygiene/profile|Prompt Library Hygiene]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** The same policy statement is copied into eleven prompts, a correction is applied to three of them, and the application now states two different policies depending on which path a user takes.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #compliance #automation #graph-theory #quick-win #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to tell a team which of their prompts are used, which duplicate each other and which can be deleted — and whoever does that takes the account, because the estate only grows and nobody can safely remove anything.

## The Problem
The refund window changes from thirty days to forty-five. That number appears in eleven prompts: the support assistant, the chat widget, the email drafter, three experiment variants, two internal tools and three copies nobody remembers making. An engineer updates the four they can find by searching for "thirty days" — missing the ones that say "a month" and the one that says "30". The application now tells some customers thirty days and others forty-five, which is a compliance problem, and nobody will notice until a customer quotes the wrong one back.

## Why It's Still Broken
Prompts are text files with no composition mechanism, so shared statements are copied rather than referenced. Search finds exact matches and the copies are paraphrases. Nothing maps a policy fact to the places it is asserted. And the inconsistency is silent, since each prompt is internally coherent and only the comparison reveals the conflict.

## What a Fix Looks Like
Define the fact once and reference it. Support composition, so a policy statement is defined in one place and included by every prompt that needs it, which is the structural fix and makes the whole class of problem disappear for everything written afterwards. Detect assertions of the same fact across the estate semantically rather than by string matching, since the copies are paraphrases and that is exactly what text search cannot find — this is what makes the existing estate tractable. Maintain a registry of the facts the application asserts, with their current value and where each is used, which is a small artefact with disproportionate value for compliance. Detect conflicts automatically, flagging prompts that assert different values for the same fact, which is checkable continuously and catches the inconsistency the day it appears. Trigger a review of every asserting prompt when a fact changes, so a policy update becomes a checklist rather than a search. Report policy consistency as a compliance-relevant metric, since an application stating two policies is a documented risk once anybody looks. Test the assertions against the source of truth periodically, because prompts drift from policy documents in both directions. And prefer retrieval over assertion for facts that change, since a prompt that looks the policy up cannot be stale.

## Who Feels the Pain
Customers told two different policies by one company; compliance functions discovering the inconsistency after a complaint; and engineers updating eleven copies of a sentence by searching for a phrase they have to guess.

## Impact If Fixed
Semantic detection of the same fact asserted across the estate is what makes the existing sprawl tractable, since the copies are paraphrases that search cannot find. Composition prevents the whole class of problem for everything written afterwards.
