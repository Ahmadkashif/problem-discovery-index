# Measuring an Unfamiliar Codebase

**Niche:** [[niches/game-porting-studios/codebase-assessment/profile|Codebase Assessment]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The things that determine a port's cost are measurable in the source and are assessed by reading it for a day.
**Tags:** #graph-theory #feature-engineering #data-integration #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to measure the properties of an unfamiliar game codebase that determine how hard it will be to port — and whoever builds that scanner takes the account.

## The Problem
The cost drivers of a port are concrete: how the renderer is structured and how tightly it is bound to one graphics API, how much platform-specific code has leaked into gameplay systems, how the memory budget was spent, how far the engine has been modified from the standard version, and what middleware and third-party dependencies are present. All of this is determinable from the source and build. It is currently assessed by an experienced person reading code under time pressure, inconsistently, with no record.

## Why Nobody Has Built This
Game codebases are heterogeneous across engines and eras, so a scanner is real work. Access to the source at bid time is limited, which makes the tool's most valuable moment its hardest. Each studio's experts are the current answer. And nobody has treated assessment as a product.

## What to Build
Scan the source and produce the technical director's report automatically. Measure engine divergence from the standard version, which is the core and is the single most consequential and least visible cost driver. Map the graphics API surface and how deeply it is bound into non-rendering code, since that coupling determines the renderer work entirely. Detect platform-specific code and conditional compilation outside the platform layer, as leakage into gameplay systems is the classic overrun. Inventory middleware, third-party libraries and their platform support, which frequently decides feasibility outright. Profile memory and asset budgets from the build rather than from the client's description. Assess threading and synchronisation assumptions, which differ sharply between platforms. Produce a consistent report format so assessments are comparable across projects, which is what makes them accumulate into evidence. Work from partial access — a build, a subset of source, a project file — since full access at bid time is rare and a partial answer beats none. Compare against previously assessed codebases to place a new one in context. And deliver it in a form a technical director can check and override, because their judgement remains the final word.

## Target Customer
Porting and co-development studios, publishers evaluating ports, engine vendors, and code analysis tooling providers.

## Impact If Built
The cost drivers are concrete properties of the source and are assessed by one person reading code for a day. An automated scan makes the assessment consistent, comparable and available at the moment it matters most.
