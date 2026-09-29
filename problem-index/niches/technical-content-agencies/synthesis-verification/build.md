# Asking What They Are Being Told

**Niche:** [[niches/technical-content-agencies/synthesis-verification/profile|Synthesis Verification]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A growing share of what developers are told about the product is said by a system the company has never queried.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #hypothesis-testing #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to find out what assistants are actually telling developers about a product, from systems nobody controls — and whoever monitors that takes the account.

## The Problem
Assistants answer questions about products continuously, at volume, to developers who never visit the documentation. Some of those answers are wrong: a removed method, a superseded pattern, a parameter that never existed, a version confusion. The company does not know which, how often, or why, because the interaction happens entirely between a third-party system and a user, and nothing in any existing measurement touches it.

## Why Nobody Has Built This
The systems are third-party and their behaviour is opaque and changes without notice. Nobody owns the question — it sits between documentation, product marketing and support. Testing requires a question set and a truth source, neither of which exists. And the problem arrived faster than any measurement practice.

## What to Build
Build the question set, run it continuously, and trace the wrong answers. Maintain a question set covering what developers actually ask — derived from search logs, support tickets and community forums — and run it against the major assistants on a schedule, which is the core and is the only way to see any of this. Compare each answer against a product truth source, which the product team can supply and which is needed for this to mean anything. Classify wrong answers by type — outdated, hallucinated, version-confused, incomplete — since the remedies differ entirely. Trace each wrong answer to its likely source in the corpus where one exists, which makes it actionable. Distinguish answers a corpus change could fix from those it could not, because the second category is a different conversation with a different owner. Track correctness over time and after corpus changes, which is the only way to know whether any of the work helps. Cover the questions that matter commercially rather than every question. Report to product and support as well as documentation, since they receive the consequences. Publish a canonical truth source that assistants can reach, which is the most direct available intervention. And escalate systematic misrepresentation to the assistant providers, which is a channel nobody currently uses.

## Target Customer
Product and documentation leadership, technical content agencies, developer relations functions, and monitoring and measurement vendors.

## Impact If Built
A growing share of what developers are told is said by a system the company has never queried. A question set run continuously against the major assistants is the only instrument that makes any of it visible.
