# Writing for a Reader That Synthesises

**Niche:** [[niches/technical-content-agencies/assistant-readiness/profile|Assistant Readiness]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reader increasingly never arrives, and what they are told is synthesised from a corpus nobody wrote for that purpose.
**Tags:** #large-language-models #data-integration #evaluation-metrics #compliance #automation #word-embeddings #confidence-intervals #transformers
**Contested on:** Every serious competitor in this niche is fighting to make a corpus that produces correct answers when the reader is a machine synthesising from it — and whoever establishes that takes the account.

## The Problem
A growing share of developers get their answer from an assistant that read the documentation on their behalf. The corpus was written for a human who would arrive at a page with context — the version they are on, the section they are in, the prerequisites stated three pages earlier. Synthesised out of that context, statements become ambiguous or wrong: a deprecated method recommended as current, a version-specific parameter presented as universal, a prerequisite omitted.

## Why Nobody Has Built This
The change is recent and the industry's measurement did not survive it. Nobody owns the question of what an assistant says about a product. Writing for machine synthesis is a craft nobody has articulated. And the reader who never arrives is invisible in every existing metric.

## What to Build
Write for synthesis and verify what comes out. Make every statement carry its own context — version, prerequisites, applicability — rather than relying on the reader's position in the document, which is the core and is what makes a statement safe to extract. Structure content semantically rather than visually, so a machine can tell a prerequisite from an aside. Mark deprecated and version-specific material explicitly and machine-readably, since a deprecated method presented as prose is indistinguishable from a current one. Remove ambiguity that a human resolves from context and a machine does not. Test what assistants actually answer about the product and monitor it continuously, which is the outward half. Treat a wrong synthesised answer as a documentation defect with a locatable cause, since it usually has one. Publish canonical machine-readable statements for the facts that matter most — current version, supported parameters, deprecations — which is the highest-leverage move available. Measure the share of readers who never arrive, so the problem is visible to whoever funds the work. Keep the corpus good for human readers, as the two goals mostly agree. And report on answer correctness rather than on traffic, which is the metric the change demands.

## Target Customer
Documentation teams and technical content agencies, developer experience and product leadership, documentation platform vendors, and developer tooling providers.

## Impact If Built
The reader increasingly never arrives and what they are told is synthesised from a corpus written for someone who would. Self-contained statements and machine-readable structure is what makes extraction safe.
