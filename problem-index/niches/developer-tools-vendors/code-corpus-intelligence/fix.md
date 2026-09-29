# Code Quality Measured Without Looking at History

**Niche:** [[niches/developer-tools-vendors/code-corpus-intelligence/profile|Code Corpus Intelligence]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Code quality tooling reports complexity, duplication and coverage computed from a snapshot, while the revision history says directly which code has actually been a problem.
**Tags:** #descriptive-statistics #survival-analysis #graph-theory #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor that gets here is fighting to turn the record of how software is actually written across millions of repositories into a product — and whoever does it holds the only dataset from which the category's central question could be answered.

## The Problem
A quality dashboard flags a module for high cyclomatic complexity. It has been stable for four years, nobody has touched it, and it works. Meanwhile a module with unremarkable static metrics has been modified eighty times in eighteen months, is implicated in three incidents, and every change to it requires a change somewhere else that nothing connects it to. The first is reported as a problem and the second is not, because the tooling looks at the code as it is rather than at what has happened to it.

## Why It's Still Broken
Static analysis was the first thing that could be automated and it established the vocabulary of code quality before revision histories were routinely available in a queryable form. The static metrics have known weak relationships to anything operationally important, which is well documented and has not changed what is reported. History-based signals require joining version control to incident and review records, which nobody has packaged. And the static numbers have the advantage of being computable on a snapshot with no context, which is convenient and is why they persist.

## What a Fix Looks Like
Report what the history says. Change frequency and recency per file and module, which alone reorders the priority list toward code that is actually being worked on. Change coupling — which files consistently change together without any static dependency between them — which reveals hidden architectural problems that no static analysis can see and is among the most useful signals available. Defect and incident association, joining fixes back to the changes and files involved, which is the closest thing to a direct measure of where the problems are. Code survival, since code rewritten repeatedly within months is a different kind of problem from code that has been stable for years, and the static metrics cannot distinguish them. Author concentration, which identifies single-maintainer modules as a risk in the same way the invisible-contribution analysis does for people. And combine with the static metrics rather than replacing them, since complexity in frequently-changed code is a genuine signal while complexity in stable code is mostly not — the interaction is the finding.

## Who Feels the Pain
Teams working from quality reports that point at stable code; engineers who know which modules are the real problem and have no evidence; and organisations whose technical debt prioritisation is driven by a snapshot metric.

## Impact If Fixed
Change frequency, coupling and defect association are all computable from version control that every organisation already has, and they relate to operational reality far more directly than the static metrics do. Change coupling in particular exposes architectural problems that no snapshot analysis can detect.
