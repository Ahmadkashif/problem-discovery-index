# Code Analysis From Software Modernisation

**Niche:** [[niches/game-porting-studios/codebase-assessment/profile|Codebase Assessment]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Legacy modernisation built automated codebase assessment to scope migrations, and porting studios read source for a day.
**Tags:** #graph-theory #data-integration #feature-engineering #evaluation-metrics #automation #sets-and-logic #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to measure the properties of an unfamiliar game codebase that determine how hard it will be to port — and whoever builds that scanner takes the account.

## The Problem
Enterprise software modernisation faces the identical question — how hard will it be to move this codebase to a different platform — and answers it with tooling. Automated assessment platforms scan a codebase, map dependencies, identify platform-coupled code, score migration complexity, and produce an effort estimate before the engagement is priced. Systems integrators bid large migrations on the output. Porting studios bid comparable risk on an afternoon of reading.

## What Already Exists
Automated codebase scanning and inventory; dependency and call graph extraction; platform coupling identification; migration complexity scoring; and effort estimation from scan output.

## The Customization Gap
The adaptation is to real-time game code where the constraints are performance and memory rather than API compatibility. It requires: (1) cost drivers that include frame budget, memory footprint and asset pipeline rather than API surface alone — a port can compile perfectly and still fail entirely on performance, which is the substantive difference; (2) game engines with heavy modification, where enterprise codebases usually sit on standard frameworks; (3) assets and content as part of the scope, with no enterprise analogue; (4) very limited source access at the moment the assessment is most valuable; and (5) a target platform whose constraints are hardware rather than a runtime.

## Target Customer
Porting studios, publishers, engine vendors, and code analysis and modernisation tooling providers.

## Impact If Solved
Modernisation platforms scope migrations automatically and integrators bid on the output. A port can compile perfectly and still fail on performance, so frame and memory budgets have to be part of the assessment.
