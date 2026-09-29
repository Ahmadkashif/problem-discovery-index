# Four Models With Nearly the Same Name

**Niche:** [[niches/data-platform-integrators/the-analytics-engineer/profile|The Analytics Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** There are four customer models, three are in use, and nothing says which one anyone should build on.
**Tags:** #worker-facing #quick-win #data-integration #graph-theory #evaluation-metrics #descriptive-statistics #workflow-orchestration #compliance
**Contested on:** Every serious competitor in this niche is fighting to let an engineer answer "can you add a column" without spending the day working out which of four similarly-named models is the right one — and whoever removes that takes the account.

## The Problem
Duplicate and near-duplicate models are the normal state of a mature estate. Several exist for the same business concept, built at different times for different requesters, differing in filters or grain in ways that are not documented. An engineer choosing between them is choosing which definition of a customer or an order the new work will inherit, with nothing to guide them, and whichever they pick, the others continue to exist and to disagree.

## Why It's Still Broken
Nothing declares authority — an estate where no model is marked as the one to use will keep growing alternatives, because every engineer facing ambiguity resolves it by adding one. Naming conventions do not encode authority. Usage is not visible next to the models. And deleting the alternatives is the retirement problem.

## What a Fix Looks Like
Declare which model is authoritative for each concept, which is a decision rather than a project. Mark one model per business concept as authoritative and say so in the catalogue and the code, which is the fix and is a list the team can produce in a workshop. Show usage next to each model so the de facto authoritative one is visible, which usually settles the debate empirically. Document the difference between the alternatives, since the differences are real and undocumented and that is why nobody can choose. Deprecate the non-authoritative versions rather than leaving them equal. Require new models to declare which concept they serve, which surfaces duplication at creation. Flag near-duplicates automatically by comparing definitions, which catches the next one. Route new requests to the authoritative model by default. Record why the alternatives existed, as some differences are legitimate and need to be preserved deliberately. Review the concept list periodically as the business changes. And make the authoritative marking visible in the engineer's own tooling rather than in a wiki.

## Who Feels the Pain
Engineers choosing blind between four definitions; business users receiving different numbers from different reports; the estate, which grows a fifth model each time; and everyone's trust in the platform's numbers.

## Impact If Fixed
An estate where no model is marked as the one to use will keep growing alternatives, because every engineer facing ambiguity resolves it by adding one. Declaring authority per concept is a workshop, not a project.
