# Program Comprehension Tooling for Applications Without Code

**Niche:** [[niches/no-code-app-builders/inherited-app-administration/profile|Inherited App Administration]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering has decades of program comprehension research — call graphs, dead code detection, impact analysis, automated summarisation — and none of it has been applied to applications that have no code.
**Tags:** #graph-theory #spectral-graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to make an application readable and safely changeable by somebody who did not build it — and whoever does that takes the IT account, because the alternative is an administrator who can neither modify nor retire what a department depends on.

## The Problem
Understanding an unfamiliar system is a studied problem with real tooling: dependency and call graph extraction, dead code detection, change impact analysis, architecture recovery, and code summarisation with language models. All of it assumes source code. A no-code application has no source code and has something better — a complete, structured, machine-readable definition with no parsing ambiguity at all — and none of the techniques have been applied to it.

## What Already Exists
Program comprehension and architecture recovery research; static analysis frameworks; change impact analysis tooling; dead code and unused dependency detection; code summarisation with language models, which works well; and graph analysis libraries for everything structural. Platforms expose app definitions through export or API in structured form.

## The Customization Gap
The adaptation is to a declarative application definition and a non-engineer reader. It requires: (1) a graph model over the app's own element types — tables, fields, views, forms, automations, connections — which is a simpler and cleaner target than source code and needs defining once per platform; (2) data-flow through automations and formulas rather than control-flow through functions, since the interesting dependencies here are about what writes what rather than what calls what; (3) summarisation aimed at an administrator rather than an engineer, describing business purpose rather than mechanics, which is a different prompt and a different evaluation; (4) honesty about interpretation, because a confident wrong explanation of an inherited app is worse than none and the output must separate what is derived from the structure from what is inferred; and (5) impact analysis that reaches outside the app to connected systems, scheduled deliveries and other apps, since the administrator's risk is mostly external to the thing they are editing.

## Target Customer
No-code platform vendors, IT service management and application portfolio vendors, and enterprise platform teams managing large citizen-built estates.

## Impact If Solved
The input is cleaner than source code and the techniques are mature, which makes this unusually tractable, and it has not been done because the reader was never the customer. Business-purpose summarisation and external impact analysis are the two adaptations that make it useful rather than merely correct.
