# Documentation Generated Rather Than Written

**Niche:** [[niches/data-platform-integrators/model-discovery/profile|Model Layer Discovery]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Building a new asset is faster than finding the existing one, which is the whole reason there are so many.
**Tags:** #large-language-models #word-embeddings #data-integration #automation #evaluation-metrics #graph-theory #workflow-orchestration #transformers
**Contested on:** Every serious competitor in this niche is fighting to make an existing asset findable so nobody builds a duplicate, and whoever makes discovery work takes the account.

## The Problem
Discovery in a data estate fails for unglamorous reasons. Descriptions are empty because writing them is a separate task nobody does. Names followed a convention that decayed. The catalogue was populated at go-live and has drifted since. Search matches strings against names. So an engineer or an analyst looking for something that exists does not find it, builds another, and the estate grows by one more near-duplicate.

## Why Nobody Has Built This
Documentation is treated as a human obligation rather than as generated output. Catalogue products assume descriptions will be written and are mostly empty in practice. Search is string-based because meaning-based search is newer than most of these deployments. And the proliferation it causes is attributed to discipline rather than to discovery.

## What to Build
Generate the documentation and search by meaning. Generate descriptions from the transformation logic, the lineage and the column names rather than waiting for humans to write them, which is the core — a catalogue that depends on manual description will always be empty. Regenerate on every change so the documentation cannot drift from the code. Search by business meaning rather than by name, since the person searching knows what they want and not what it was called. Show usage and freshness in the results so relevance is judgeable at a glance. Mark the authoritative asset per concept, which is the single most useful field and is almost never present. Surface discovery inside the tools people actually use — the transformation framework, the notebook, the reporting tool — rather than in a separate catalogue nobody opens. Suggest existing assets when someone begins creating a new one, which is the intervention that actually prevents duplication. Include example queries, which is how people establish whether an asset is what they need. Keep human description as an optional enrichment on top of the generated baseline. And measure whether search leads to reuse, which is the only metric that matters here.

## Target Customer
Data platform teams and integrators, analytics engineering, catalogue and discovery vendors, and platform providers.

## Impact If Built
A catalogue that depends on manual description will always be empty, which is why building is faster than finding. Generated descriptions with meaning-based search, surfaced where people work, is what makes reuse the fast path.
