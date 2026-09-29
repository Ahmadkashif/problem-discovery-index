# Assembly Maintenance Adapted to Code and Product Change

**Niche:** [[niches/electrical-contractors/electrical-labor-unit-publishers/profile|Electrical Labour Unit & Estimating Database Publishers]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product data feeds and content management systems keep catalogues current; the database's problem is that a code change silently invalidates the material list inside thousands of assemblies.
**Tags:** #bert #transformers #graph-neural-networks #word-embeddings #change-point-detection #evaluation-metrics #feature-engineering #automation #compliance #data-integration

## The Problem
Estimating databases ship assemblies — a receptacle installation, a panel feed, a lighting circuit — each bundling materials, labour, and the conditions they assume. Those assemblies encode code requirements: conductor sizing, protection, grounding, box fill. When the code cycle changes a requirement, every assembly whose material list depends on it is wrong, and finding them means someone knowing which assemblies embed which requirement. That knowledge is in the heads of the researchers who built them. The same problem arrives continuously from the product side as manufacturers discontinue and substitute parts. Maintenance is therefore a periodic manual sweep, and errors persist in the long tail of assemblies nobody thought to check.

## What Already Exists
Content management and product data tooling is mature. PIM systems handle catalogue currency and part cross-referencing; manufacturer price file ingestion is routine; content management platforms handle versioning and workflow; the document diff tools handle code text comparison.

## The Customization Gap
All of it manages content as records and documents. The dependency that matters here is semantic and physical — an assembly depends on a code requirement not because it cites it but because its material list was constructed to satisfy it, and nothing records that. The adaptation is a requirement-to-assembly dependency layer, built by mining the existing assemblies against the code text so that each assembly carries the provisions its composition assumes, and maintained as assemblies are edited. A code change then resolves to the specific assemblies affected rather than to a general instruction to review. Product substitution runs through the same structure, since a discontinued part matters differently depending on whether the assembly's compliance depends on its specific characteristics. Confidence per dependency matters, because a wrongly asserted dependency creates false work and a missed one ships an invalid assembly.

## Target Customer
Directors of estimating content at database publishers, and the researchers who currently sweep assemblies manually after each code cycle.

## Impact If Solved
Turns the triennial code update from a manual sweep into a scoped task, and catches the long-tail assemblies that currently go stale unnoticed. The dependency layer also gives the database provenance it lacks — why an assembly contains what it contains — which is directly useful when a contractor disputes a takeoff.
