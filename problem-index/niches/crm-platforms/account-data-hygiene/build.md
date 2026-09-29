# The Account Hierarchy as a Maintained Structure

**Niche:** [[niches/crm-platforms/account-data-hygiene/profile|Account Data Hygiene]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Enrichment vendors will fill in any field on an account and nobody maintains the relationships between accounts, so the same customer exists four times and nobody can say what a global relationship is worth.
**Tags:** #graph-theory #bert #k-nearest-neighbors #contrastive-learning #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in account data is fighting to keep the relationships between accounts correct — parent, subsidiary, duplicate, acquired — rather than the fields inside them, and whoever holds the hierarchy right takes the account.

## The Problem
A global manufacturer appears in the CRM as the parent company, as two national subsidiaries created by representatives in those countries, as an acquired brand that still trades under its own name, and as a duplicate created by a marketing import with a slightly different legal suffix. Five records. A renewal in one, an open opportunity in another, three years of support history in a third. Asked what this customer is worth in total, what is renewing this year, and who owns the relationship, the organisation produces five partial answers. This is the ordinary condition of enterprise account data and it undermines territory assignment, account planning, revenue reporting and the entire premise of strategic account management.

## Why Nobody Has Built This
Enrichment vendors are paid per record enriched, which makes a product that reduces the record count commercially awkward, and their coverage models are built around company identity rather than around a customer's internal account structure. The CRM vendors treat hierarchy as a customer-configurable field because corporate structures are genuinely idiosyncratic — a customer may want to model by contracting entity, by operating division, or by where the budget sits, and those are different trees. Maintaining any of them requires watching corporate events continuously, which nobody does because it is nobody's product.

## What to Build
A maintained account graph with resolution, structure and event monitoring. Resolution matches records to real-world entities using name, domain, address, registration identifiers, contact overlap and purchased corporate linkage, producing a confidence rather than a merge decision. Structure is modelled as an explicit graph with typed edges — legal parent, operating division, contracting entity, acquired brand — so the several trees a customer needs can coexist rather than competing for one field. Corporate events are monitored continuously from registry, news and linkage feeds, so an acquisition updates the structure rather than degrading it. Duplicates are detected on creation and prevented rather than remediated quarterly. And the headline output is a structural accuracy figure, sampled and audited, because an organisation currently has no idea what proportion of its account graph is correct and every downstream analysis inherits the answer.

## Target Customer
Enterprise sales organisations with global accounts, CRM and master data vendors, and the enrichment providers who could differentiate on structure rather than on field coverage.

## Impact If Built
Account structure is the foundation under territory design, account planning and revenue reporting, and it is currently maintained by accident. Stating a global relationship's total value correctly is the visible benefit; the larger one is that every territory, quota and coverage decision downstream stops being computed on a graph that is quietly wrong.
