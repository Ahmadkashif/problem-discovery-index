# Program Analysis That Predates the Problem

**Niche:** [[niches/developer-tools-vendors/legacy-codebase-comprehension/profile|Legacy Codebase Comprehension]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Program slicing, dead code elimination, call graph construction and architecture recovery are decades-old compiler and reverse-engineering techniques, and the estates that most need them have none of them.
**Tags:** #graph-theory #spectral-graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #automation #transfer-learning
**Contested on:** Every serious competitor here is fighting to let an engineer understand and safely change a system written decades ago by people who have left — and whoever does that takes the enterprise, because these estates run the business and nobody dares touch them.

## The Problem
Program slicing — determining which statements can affect a given value — was developed in the seventies and is exactly the tool for "what determines this premium". Call graph construction, reaching definitions, dead code analysis and architecture recovery are all mature. The software reverse-engineering literature spent the nineties on precisely the problem of understanding large legacy systems. Almost none of it is available to the engineer maintaining one today.

## What Already Exists
Program slicing and dependence graph construction with published algorithms; dead code and reachability analysis; architecture recovery and clustering research from the reverse-engineering community; parsers for the major legacy languages, some open and some commercial; and language models that read unfamiliar code and explain it with useful accuracy. Change history in version control where these estates were migrated into it.

## The Customization Gap
The adaptation is to languages and idioms the modern tooling world skipped. It requires: (1) robust parsing of dialect variation, since these languages have vendor-specific extensions, embedded sublanguages and decades of compiler-specific behaviour, and parsing is the first place naive attempts fail; (2) data-centric rather than purely control-centric analysis, because in these systems the flow through files and database records carries as much of the logic as the call structure does and control-flow tooling alone misses half the picture; (3) business rule extraction as a distinct output from slicing, since a slice is a set of statements and a stakeholder needs a stated decision with its conditions; (4) honest separation of derived facts from inferred explanation, because the structural analysis is exact and the intent reconstruction is not, and conflating them in a thirty-year-old system is how expensive mistakes are made; and (5) runtime evidence integration for liveness, since static reachability over-approximates badly in these estates and production traces settle it.

## Target Customer
Modernisation consultancies, legacy platform vendors, enterprises with substantial legacy estates, and the static analysis vendors for whom this is an underserved adjacent market.

## Impact If Solved
The analysis techniques predate the problem by decades and have not reached the code that most needs them, because the tooling ecosystem followed developer population rather than installed base. Dialect-robust parsing is the practical barrier, and separating derived fact from inferred intent is what makes the output safe to act on.
