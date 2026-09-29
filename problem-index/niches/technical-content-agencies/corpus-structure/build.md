# Statements That Survive Extraction

**Niche:** [[niches/technical-content-agencies/corpus-structure/profile|Corpus Structure & Disambiguation]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The sentence is correct on the page and false the moment it is lifted off it.
**Tags:** #data-integration #compliance #evaluation-metrics #automation #word-embeddings #sets-and-logic #large-language-models #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to write statements that stay true when extracted from their surroundings — and whoever establishes that craft takes the account.

## The Problem
Documentation carries context structurally. The version is in the site navigation, the prerequisites are in a section above, the applicability is implied by which guide you are reading. A human reader has all of it. A statement extracted from that structure has none, and a sentence that was precisely correct in place becomes ambiguous or false. The corpus is full of such statements and there is no convention that says they are defects.

## Why Nobody Has Built This
Nobody has articulated the craft, because until recently the reader always had the page. Lightweight markup carries appearance rather than meaning. Adding context to every statement is repetitive and reads badly to a human if done clumsily. And no check exists for context dependence.

## What to Build
Make self-containment a documented standard with a check behind it. Establish a standard that consequential statements carry their own version, applicability and prerequisites, which is the core and is a craft rule the field can adopt. Provide machine-readable markers for version, deprecation and applicability rather than expressing them only in prose, since those are the three that most often invert a meaning. Structure content so a prerequisite, a warning and an example are distinguishable by a machine rather than only by formatting. Detect context-dependent statements automatically — references to "this version", "the above", "as described earlier" — which is a lint rule and catches a large share. Publish canonical statements for the facts most often extracted, which is the highest-leverage authoring change. Write examples that are complete and runnable rather than fragments requiring surrounding setup. Keep it readable for humans, since a corpus that reads badly to satisfy a machine defeats the purpose. Apply the standard to the most-referenced pages first rather than the whole corpus. Give authors the check in their editor rather than in review. And treat a statement that inverts when extracted as a defect with a name, which is what makes it fixable.

## Target Customer
Documentation teams and technical content agencies, developer experience leadership, documentation tooling vendors, and standards and style authorities.

## Impact If Built
A sentence precisely correct in place becomes false when lifted off the page, and no convention calls that a defect. A self-containment standard with a lint rule behind it makes extraction safe.
