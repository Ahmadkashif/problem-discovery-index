# Nobody Knows Which Half Is Dead

**Niche:** [[niches/developer-tools-vendors/legacy-codebase-comprehension/profile|Legacy Codebase Comprehension]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A large fraction of every legacy estate has not executed in years, nobody can prove which fraction, so all of it is carried, analysed, migrated and paid for.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to let an engineer understand and safely change a system written decades ago by people who have left — and whoever does that takes the enterprise, because these estates run the business and nobody dares touch them.

## The Problem
A modernisation programme scopes eleven thousand programs. A significant portion of them have not run in years: superseded batch jobs, code paths for products withdrawn a decade ago, branches for a regulatory regime that ended. Nobody can identify them with confidence, so all eleven thousand are analysed, estimated, migrated and tested. The programme's cost is proportional to a codebase that is substantially larger than the system actually in use, and the most common reason for a legacy modernisation to run over is that it modernised things nobody needed.

## Why It's Still Broken
Static reachability over-approximates heavily in these systems, because dynamic program calls, job control indirection and data-driven dispatch defeat it, so static analysis alone declares almost everything reachable. Runtime evidence exists — these platforms have detailed execution accounting, often for billing purposes — and is not joined to the source inventory, because those are different systems owned by different teams. And deleting anything from a system nobody understands is unthinkable without proof, which is exactly what nobody has assembled.

## What a Fix Looks Like
Join execution evidence to the source inventory, which is the whole fix and is mostly data work. Collect execution records over a long enough window to cover annual and quarterly cycles, since a job that runs once a year at financial close must not be classified as dead. Reconcile against the full program and job inventory, producing a straightforward classification: executed recently, executed within a cycle, never observed. For the never-observed set, establish why — genuinely dead, reachable only in an error path, or invoked dynamically in a way the analysis missed — which is where the careful work is and where a hybrid of static and runtime evidence is decisive. Scope programmes against the live set rather than the inventory, with the dead set carried as a separate and much cheaper track, which is the commercial impact. Retire rather than delete, since these organisations will not delete and archival with a restoration path is sufficient. And report the proportion honestly, because the number is usually large enough that stakeholders will doubt it and the evidence needs to be inspectable.

## Who Feels the Pain
Modernisation programmes scoped against an inventory rather than a system; maintenance teams analysing code that has not run since before they joined; and organisations paying to carry, license and audit software nobody uses.

## Impact If Fixed
Execution accounting already exists on these platforms and joining it to the source inventory is data work rather than research. Scoping a programme against the live set instead of the inventory changes its cost directly, and is usually the single largest available saving.
