# Dead Code Detection and Clone Analysis

**Niche:** [[niches/llm-application-tooling/prompt-library-hygiene/profile|Prompt Library Hygiene]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering built dead code detection, clone analysis and refactoring tools for exactly this shape of decay, and prompt registries have folders.
**Tags:** #word-embeddings #k-means-clustering #evaluation-metrics #automation #descriptive-statistics #data-integration #graph-theory #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell a team which of their prompts are used, which duplicate each other and which can be deleted — and whoever does that takes the account, because the estate only grows and nobody can safely remove anything.

## The Problem
An asset that accumulates, whose copies diverge, and which nobody dares delete is code, and the profession built a whole toolchain for it: dead code detection from static and runtime coverage, clone detection at several levels of similarity, refactoring tools that extract a shared piece safely, and deprecation processes. Prompt registries offer folders, tags and a search box, and the estate behaves exactly as an untended codebase does.

## What Already Exists
Dead code detection from coverage and call graph analysis; clone and duplicate detection at token, structure and semantic levels; automated refactoring with extract-and-replace; deprecation tooling with usage-driven timelines; and dependency graphs showing what references what.

## The Customization Gap
The adaptation is to an artefact whose behaviour cannot be verified by types or tests in the ordinary sense. It requires: (1) usage established from production telemetry rather than from static analysis, since prompts are referenced dynamically and the call graph does not exist — this makes runtime usage the only reliable signal and the join to traces the enabling piece; (2) clone detection on meaning as well as text, because two prompts can say the same thing in different words and text similarity misses exactly the duplicates worth merging; (3) refactoring validated behaviourally, since extracting a shared fragment is only safe if the resulting prompts behave the same, which requires running them rather than type-checking them; (4) composition primitives, so shared policy language can be defined once and included, which is the structural fix that prevents recurrence and which most registries do not support; and (5) deprecation driven by observed usage decay rather than by a declared timeline.

## Target Customer
Prompt registry vendors, platform teams, and the developer tooling community for whom prompt estates are a new instance of a familiar decay.

## Impact If Solved
The toolchain for exactly this decay is mature and the registries offer folders. Runtime usage from production traces replaces the missing call graph, and composition primitives are the structural fix that stops the duplication recurring.
