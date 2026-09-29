# Lot Linkage Adapted to Transformation and Commingling

**Niche:** [[niches/food-distributors/food-traceability-compliance-services/profile|Food Traceability Compliance Services]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Track-and-trace platforms follow a lot through custody transfers; food is cut, mixed, repacked, and commingled, and the lot that arrived is frequently not the lot that leaves.
**Tags:** #graph-theory #graph-neural-networks #probability-distributions #confidence-intervals #optimization-fundamentals #evaluation-metrics #compliance #data-integration #automation #workflow-orchestration

## The Problem
The obligation is to produce, quickly, the forward and backward links for an implicated lot. That is straightforward while product moves in sealed cases and impossible to do naively once it is transformed — a case of romaine becomes portions across many outbound orders, a repack blends multiple inbound lots, and a further-processed item contains inputs from several sources. Distributors handle this with lot codes that survive some steps and not others, and reconstructing the linkage during an investigation is a manual exercise performed under a deadline measured in hours while product continues moving.

## What Already Exists
Traceability platforms are numerous. Supply chain visibility products, blockchain-based provenance systems, and the WMS modules all record lot movement through custody events, with reasonable event capture and reporting. Several are marketed directly at this regulation.

## The Customization Gap
Nearly all of them model a lot as a thing that moves. The operative reality is a lot as a quantity that splits, merges, and transforms, where the honest output for many outbound shipments is a set of possible source lots with probabilities rather than a single answer. A platform that reports one source lot where three are possible is producing a false record, which is worse under investigation than an honest set. The adaptation is a mass-balance linkage model over transformation events: inbound quantities, yields, and outbound allocations reconciled so that the implicated set is computed rather than asserted, with the breadth of the set reported explicitly. That breadth is itself the most actionable operational metric in the whole domain — it is the measure of how wide a recall would have to be, and reducing it by changing how product is handled is the single highest-value thing a distributor can do before an outbreak happens.

## Target Customer
Heads of product and regulatory services at traceability providers, and the food safety leaders at distributors who currently discover their linkage breadth during an actual investigation.

## Impact If Solved
Produces an honest answer where current tooling produces a confident wrong one, and turns recall breadth into a managed metric rather than a discovery. That reframing is also the commercial argument: distributors will pay to reduce recall exposure in a way they will not pay to file records.
