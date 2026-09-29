# The Dependency Graph and Time to Recovery

**Niche:** [[niches/procurement-spend-platforms/supplier-risk-dependency/profile|Supplier Risk & Dependency]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Risk subscriptions score suppliers and the board's question is about the buyer — which failure stops what, how fast, and how long recovery takes — and that answer is computable from data the company already holds.
**Tags:** #graph-theory #graph-neural-networks #monte-carlo-methods #survival-analysis #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in supplier risk is fighting to tell a company which single supplier failure would actually stop its operations — and whoever maps dependency rather than scoring suppliers takes the account.

## The Problem
A board asks which supplier failures would materially disrupt the company. The supply chain team produces a list of the twenty largest suppliers by spend with their financial health scores. That list is almost certainly not the answer: several of the twenty have multiple qualified alternatives and are easily replaced, while a supplier ranked one hundred and forty by spend provides a single-sourced component in every product the company makes, with tooling it does not own and a qualification cycle of nine months. The company has the bill of materials, the sourcing records, the qualification status and the inventory positions, and has never assembled them into the question.

## Why Nobody Has Built This
The risk market sells data about suppliers, which is a saleable product, and dependency mapping requires the customer's own internal data, which is a services engagement rather than a subscription. Assembling it crosses engineering, procurement, quality and operations systems, which is the usual reason a computable thing stays uncomputed. And the internal build attempts that exist tend to produce a one-time mapping exercise that is out of date within a year, because nothing maintains it as the bill of materials and the supply base change.

## What to Build
A maintained dependency graph with recovery modelled on it. Nodes are suppliers, sites, parts and products; edges carry the sourcing relationship with its qualification status, tooling ownership, lead time and inventory buffer. Revenue is attributed to products so that a disruption's consequence is expressed in the terms a board understands. Failure simulation runs over the graph: if this supplier or this site stops, which parts become unavailable, which products stop, how long the buffer lasts, what alternatives exist, how long each would take to qualify and tool, and therefore what the time to recovery and the revenue at risk are. Criticality is the output of that simulation rather than a spend ranking. Sub-tier dependency is built where possible from what suppliers disclose and, importantly, from the common-source concentration that is invisible at tier one — several tier-one suppliers depending on the same tier-two source is the exposure that has caused the most-publicised disruptions and is not visible in any tier-one assessment. The graph is maintained from the systems it derives from rather than being an exercise.

## Target Customer
Manufacturers and any organisation with physical supply dependency, third-party risk vendors who could extend from supplier data into buyer exposure, and the business continuity functions who currently assess this qualitatively.

## Impact If Built
Time to recovery is the metric a board is actually asking for and no current product produces. Dependency-based criticality reliably reorders the risk register — the suppliers that matter are frequently not the suppliers that are monitored — and the common-source concentration finding is the one that has repeatedly surprised large manufacturers in actual disruptions.
