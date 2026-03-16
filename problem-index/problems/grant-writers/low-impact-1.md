# Boilerplate and Narrative Reuse Management

**Industry:** [[grant-writers|Grant Writers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Grant writers rewrite the same organizational descriptions, methodology sections, and capacity statements for every proposal because existing document management tools don't understand grant narrative structure or funder-specific tone requirements.
**Tags:** #llm #text-generation #nlp #automation

## The Problem

Every grant proposal contains 30-50% reusable content: organizational background, staff qualifications, evaluation frameworks, sustainability plans, and data management protocols. An experienced grant writer maintains a personal library of these "boilerplate" sections in Word documents, Dropbox folders, or Notion databases. But raw boilerplate never fits a new proposal without modification — each funder uses different terminology, emphasizes different priorities, and imposes different formatting and length constraints.

A writer preparing an NIH R01 application and a Robert Wood Johnson Foundation proposal for the same organization's diabetes prevention program will describe the same program in fundamentally different ways — the NIH version emphasizes mechanistic rigor and research methodology, while RWJF wants community engagement and health equity framing. The writer manually reshapes the narrative for each audience, spending 4-8 hours per proposal on content that is conceptually identical but rhetorically distinct.

## What Already Exists

Google Docs and Notion provide document storage with search. Jasper, Copy.ai, and ChatGPT offer general-purpose text generation and rewriting. Instrumentl recently added a "grant writing assistant" feature. All of these tools treat grant narratives as generic text — they don't understand the structural conventions of grant proposals (specific aims, significance, innovation, approach for NIH; problem statement, goals/objectives, methods, evaluation for foundations) or the funder-specific rhetorical norms that experienced writers internalize.

## The Customisation Gap

The missing tool is a grant-specific content library that indexes narrative blocks by both structural function (e.g., "organizational capacity," "evaluation plan," "sustainability strategy") and rhetorical register (e.g., "NIH-style," "RWJF-style," "DOE-style"). When a writer starts a new proposal, the system retrieves relevant boilerplate sections and adapts them to the target funder's voice, terminology, and length constraints — not generating from scratch (which risks inaccuracy) but transforming existing approved content to fit the new context.

This requires understanding grant-specific conventions: that NIH reviewers want passive voice and methodological precision while foundation reviewers want active voice and community impact stories; that "specific aims" in an NIH proposal maps to "goals and objectives" in a foundation proposal but with different scope expectations; that page limits, font requirements, and margin specifications vary by funder and must be respected in the adaptation.

## Impact If Solved

Saves 4-8 hours per proposal on boilerplate adaptation, representing 15-25% of total proposal preparation time. For a writer producing 20-40 proposals/year, that's 80-320 hours recovered annually — $6,000-$48,000 in billable capacity. Reduces the risk of "stale boilerplate" (using an organizational description that references last year's statistics) by flagging outdated content during retrieval.
