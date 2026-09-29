# Nobody Knew What Depended on It

**Niche:** [[niches/customer-data-platforms/downstream-impact-tracing/profile|Downstream Impact Tracing]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every failure in this category has the same shape — something changed and nobody knew what depended on it — and the dependency information is sitting in the definitions the platform already stores.
**Tags:** #graph-theory #data-integration #workflow-orchestration #automation #evaluation-metrics #change-point-detection #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to say what breaks when something changes, before it changes — and whoever builds that lineage across the customer data stack makes every other failure in the category preventable.

## The Problem
A developer renames an event property. Somewhere downstream, four segments use it, two of those segments feed a suppression list, that suppression list is used by three campaigns, and one of those campaigns is legally required to exclude certain customers. None of this is knowable from where the developer is sitting. The same shape recurs everywhere in this category — a warehouse model refactored, a segment definition edited, an identity threshold moved — and in every case the chain from the change to the consequence exists in definitions the platform holds and has never been assembled.

## Why Nobody Has Built This
Lineage tooling grew up in the analytics world and stops where analytics stops, which is exactly one layer above where the customer-facing consequences live — the boundary of the existing tools is the boundary of the problem. The chain crosses several systems with different owners. Activations reach external tools nobody models. And each individual failure is attributed to its own local cause rather than to the missing graph.

## What to Build
Assemble the graph across the whole stack. Parse every definition the platform holds — event schemas, model references, segment logic, journey conditions, activation mappings — into one dependency graph, which is the core and requires no new information because the definitions are already stored. Extend it into destinations, so an audience feeding an advertising platform is a modelled dependency rather than the end of the trace. Provide impact preview before a change, which is the product: a developer, analyst or marketer sees what will be affected at the moment they are deciding. Attach ownership to every node, so an impact has a person rather than a system name. Flag consequential paths specifically — anything reaching suppression, consent or a compliance-relevant campaign — since those deserve a different treatment from a reporting dependency. Surface it in each team's own tooling, connecting to the data engineer's work, because a graph in the data platform's interface is invisible to the person making the change. Detect breaks against the graph so investigation starts with a hypothesis rather than a search. Show the reverse direction too, since an analyst asking why a number changed needs the upstream trace and currently reconstructs it manually. Keep it current automatically, because a lineage graph maintained by hand is wrong within a month and worse than none. And measure how many changes are shipped with impact unknown, since that figure is the category's underlying failure rate.

## Target Customer
Data platform and analytics leadership, customer data platform vendors, and the organisations whose recurring failures all share one missing capability.

## Impact If Built
Existing lineage stops one layer above where the customer-facing consequences live, so the boundary of the tools is the boundary of the problem. Parsing definitions the platform already stores into one graph, extended into destinations, makes the category's recurring failure preventable rather than diagnosable.
