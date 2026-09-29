# Navigation and Impact Analysis From Software Tooling

**Niche:** [[niches/data-platform-integrators/the-analytics-engineer/profile|The Analytics Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software tooling made finding the right code and its callers instantaneous, and finding the right model takes a day.
**Tags:** #graph-theory #large-language-models #data-integration #worker-facing #evaluation-metrics #word-embeddings #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to let an engineer answer "can you add a column" without spending the day working out which of four similarly-named models is the right one — and whoever removes that takes the account.

## The Problem
Software development tooling made navigating an unfamiliar codebase fast: jump to definition, find all references, see the call graph, search semantically, and understand the impact of a change before making it. No engineer accepts having to read a whole repository to find where a change belongs. Analytics engineering has a comparable structure — a dependency graph of transformations — and navigates it with a search box and a naming convention.

## What Already Exists
Jump-to-definition and find-references; call and dependency graph navigation; semantic code search; change impact analysis; and refactoring tools that update dependents.

## The Customization Gap
The adaptation is to a graph whose nodes are business concepts as well as code. It requires: (1) navigation driven by business meaning rather than by symbol names, since the engineer's question is about a concept and not an identifier — this is the substantive difference; (2) dependents that include human consumers and external tools, not only other code; (3) impact measured in changed report numbers rather than in compilation errors; (4) no type system or compiler to establish correctness, so impact analysis rests on lineage and usage; and (5) an estate where duplicate near-identical implementations are normal rather than a defect to be refactored away.

## Target Customer
Data platform teams and integrators, analytics engineering leads, catalogue and lineage vendors, and developer tooling providers.

## Impact If Solved
Software made navigation and impact analysis instantaneous and no engineer accepts less. Navigation by business meaning, with human consumers as dependents, is what the analytics version has to provide.
