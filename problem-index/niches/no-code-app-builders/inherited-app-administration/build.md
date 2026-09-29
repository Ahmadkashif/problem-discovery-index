# Handed an App You Cannot Read

**Niche:** [[niches/no-code-app-builders/inherited-app-administration/profile|Inherited App Administration]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An administrator inherits an application whose every element is visible and whose purpose is unknowable, and the only available method is clicking through it and guessing.
**Tags:** #large-language-models #graph-theory #bert #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to make an application readable and safely changeable by somebody who did not build it — and whoever does that takes the IT account, because the alternative is an administrator who can neither modify nor retire what a department depends on.

## The Problem
An administrator is given an app the claims team depends on. It has fourteen tables, sixty-one fields, nine views, four automations and three connected systems. One field is called "Flag2" and is referenced in two automations. One automation runs at 06:00 daily and nobody knows what happens if it does not. Three views appear identical. The claims team says it works and they need it changed to add a new status. The administrator can see everything and understands none of it, and the only person who could explain it left in April.

## Why Nobody Has Built This
Every product in the category is designed for the author, who does not need to understand what they built because they remember it. Comprehension for a second reader was never a use case, and the platforms record no intent — there is no commit message, no comment, no design note, because the interface never asked for one. Static analysis over app definitions is entirely feasible and nobody has built it, since it serves the administrator rather than the builder and the administrator is not who the product is sold to. And handover is treated as an organisational event rather than a product feature.

## What to Build
Comprehension tooling for applications. Generate a structural map: entities and relationships, what writes to what, which automations trigger from which events, what connects outward — a dependency graph derived from the definition, which is complete and machine-readable and which no product renders. Generate a plain-language explanation of what the app appears to do and what each element is for, using the model over names, formulas, views, sample data and automation logic, presented as an interpretation with its evidence rather than as fact. Identify the load-bearing parts: fields referenced by automations, fields exposed on forms, anything feeding an external system, and anything with a downstream dependency — which is the answer to the administrator's real question about what is safe to touch. Flag the suspicious: unreferenced fields, duplicate views, automations that have not fired in months, hard-coded values that look like they should be configuration. Reconstruct history from version data where it exists, which gives some sense of what changed and when even without commit messages. And produce a handover document as an artefact, which is what should have existed and can now be generated retrospectively.

## Target Customer
IT administrators and platform operations teams inheriting citizen-built applications, and the platform vendors whose enterprise story requires that their apps be maintainable by somebody other than their author.

## Impact If Built
The application definition is complete and machine-readable, which makes comprehension a rendering problem rather than an archaeology problem, and nobody has attempted the rendering. Identifying the load-bearing elements answers the administrator's only real question and is derivable directly from the dependency graph.
