# The Code as a Dependency Graph, Not a Document

**Niche:** [[niches/electrical-contractors/code-standards-development-bodies/profile|Electrical Code & Standards Development Bodies]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A single proposed change to a definition can alter the meaning of provisions in eleven other articles, and the committee finds out because a member happens to remember.
**Tags:** #graph-neural-networks #graph-theory #bert #transformers #large-language-models #word-embeddings #evaluation-metrics #compliance #data-integration #revenue-impact

## The Problem
The code is a dependency structure published as a numbered document. Articles reference each other explicitly, inherit definitions, and depend on tables and exceptions written decades apart by different committees. During a revision cycle, thousands of public inputs are processed by many panels working in parallel, each seeing its own scope. A change accepted in one article can silently alter the effect of a provision in another, and the mechanism for catching that is a correlating committee plus the institutional memory of long-serving members. Errors that survive become field problems for hundreds of thousands of electricians and are corrected three years later, or immediately through a formal interpretation that itself becomes another artefact to track.

## Why Nobody Has Built This
The code was written as a document for print and its structure lives in numbering rather than in explicit relationships. Cross-references are stated in prose, and the more consequential dependencies — a provision whose meaning rests on a definition it never cites — are not stated at all. Recovering them requires reading meaning rather than citations. Standards development is also a consensus process where the committee structure is the safeguard, and anything that appears to substitute analysis for committee judgment is treated cautiously, correctly.

## What to Build
A dependency graph over the code at provision level: explicit cross-references, definitional dependencies, table and exception relationships, and the inherited relationships where one provision's meaning rests on another without citing it. Built once by mining the existing text and prior cycles, maintained as edits are made. Each proposed input is then evaluated against the graph and returns a scoped impact statement — these are the provisions whose meaning changes, in these panels' scopes, with these downstream effects — which is delivered to the committee as evidence rather than as a decision. Across the cycle, the graph identifies where two panels are proposing changes that interact, which is the failure mode the correlating process exists to catch and currently catches by memory. The same structure lets the organization publish what the code cycle has never had: a machine-readable statement of what changed and what it affects, which is the single most requested thing by every downstream publisher, trainer, and enforcement body.

## Target Customer
VPs of standards development and chief engineers at code bodies, and the state adoption authorities and enforcement agencies who currently reconstruct change impact themselves, differently, fifty times over.

## Impact If Built
Protects the integrity of a document that is adopted into law, at the point where the current process depends on individual memory. It also creates a saleable derivative — structured change impact — that every publisher, trainer, and jurisdiction downstream currently produces independently and badly.
