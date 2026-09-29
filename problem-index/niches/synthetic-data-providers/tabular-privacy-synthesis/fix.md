# Privacy Accounted Per Table, Released as a Database

**Niche:** [[niches/synthetic-data-providers/tabular-privacy-synthesis/profile|Tabular & Privacy Synthesis]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Each table is generated with its own privacy budget and the customer receives all of them together, where the joint release leaks more than any table does alone and nothing accounts for it.
**Tags:** #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #compliance #graph-theory #bayesian-inference
**Contested on:** Every serious competitor in this sub-niche is fighting to generate a multi-table business database whose keys, constraints and conditional structure survive intact while a defensible privacy claim still holds — and whoever does that takes the account, because it is the only version of the problem enterprise customers actually have.

## The Problem
A thirty-table database is generated table by table, each with a stated privacy parameter. The deliverable reports that parameter. But an individual appears in eight of those tables, and an adversary holding the whole release can link across them — which is the entire reason relational data is more identifying than any single table. The composition is not accounted for, the reported number describes a release that nobody received, and the customer's privacy officer approves on it.

## Why It's Still Broken
Composition across a relational release is genuinely harder to account for than composition across queries, because the same individual contributes to multiple tables in a structure-dependent way and the tight accounting depends on the schema. Doing it properly produces a much larger and much less marketable number. The per-table figure is defensible enough to a non-expert audience, and the audience is non-expert. And no standard exists for how a relational synthetic release should be reported, so every vendor reports the flattering thing.

## What a Fix Looks Like
Account for the release the customer actually receives. Report a whole-release figure alongside any per-table numbers, since the release is what exists and the per-table number describes a counterfactual — and stating both is honest even when the composed figure is uncomfortable. Define the privacy unit explicitly as the individual rather than the row, because an individual contributing a thousand rows across eight tables is the case that breaks row-level accounting and it is the common case in business data. Run linkage attacks across the full release rather than membership inference per table, which is the threat the structure actually creates and is directly measurable. Report the accounting assumptions — adjacency, unit, composition method — since vendors differ on all three and the differences are larger than the differences in the reported values. Flag individuals with high cross-table contribution, since they carry disproportionate risk and are identifiable before release. And where the composed figure is not defensible, say so and reduce the release scope, which is the outcome a correct accounting sometimes requires and which nobody reaches because nobody computes it.

## Who Feels the Pain
Privacy officers approving relational releases on per-table numbers; the individuals whose cross-table presence is the actual exposure; and vendors doing composition correctly who lose comparisons to those who do not.

## Impact If Fixed
The per-table figure describes a release nobody received. Defining the privacy unit as the individual and running linkage attacks across the whole release measures the threat the relational structure actually creates.
