# Integration Platforms and Connectors

**Niche:** [[niches/ap-automation-vendors/erp-and-dimension-mapping/profile|ERP & Dimension Mapping]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Integration platforms solved connectivity and transformation, and the hard part here is knowing what the customer's fields mean.
**Tags:** #data-integration #workflow-orchestration #transfer-learning #evaluation-metrics #automation #word-embeddings #confidence-intervals #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to map a customer's chart of accounts, dimensions and custom fields without six weeks of a consultant — and whoever makes the integration cover the non-standard fields wins the deals that die in implementation.

## The Problem
Integration platforms handle connectivity, authentication, transformation, error handling, retry and monitoring, with prebuilt connectors for every major ERP. All of it is solved and widely available. None of it addresses the actual difficulty, which is semantic: determining that this customer's Class dimension means legal entity, that their custom field seven holds the approval group, and that their account 6120 is the one this invoice belongs in.

## What Already Exists
Integration platform connectors and transformation engines; API and authentication management; error handling and monitoring; canonical data models for common objects; and mapping interfaces.

## The Customization Gap
The adaptation is semantic rather than technical. It requires: (1) meaning inferred from field names, usage and content rather than declared in a mapping screen, which is the substantive difference and is the work consultants actually do; (2) a library of accounting configuration patterns, which no integration platform carries and which is the reusable asset; (3) validation against transaction outcomes rather than against schema conformance, since a technically valid mapping can be accounting-wrong; (4) customer confirmation as the interaction rather than customer specification, which suits a finance user who cannot describe their configuration formally; and (5) continuous reconciliation as the ERP configuration drifts.

## Target Customer
Implementation and product leadership, ERP integration specialists, and integration platform vendors for whom accounting semantics are out of scope.

## Impact If Solved
Connectivity is solved and the difficulty is meaning. A library of accounting configuration patterns is the missing asset, and it can be built from mappings the vendor has already performed.
