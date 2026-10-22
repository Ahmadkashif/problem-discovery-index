# Data Migration Tooling Built for ERP, Not MARC

**Niche:** [[niches/libraries-and-archives/library-services-platforms/profile|Library Services Platforms]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General data-migration and ETL tools move customer and order tables well and have no idea what a MARC holdings record, an item status or a patron block means.
**Tags:** #feature-engineering #data-integration #automation #workflow-orchestration #evaluation-metrics
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to become the system of record a library will not migrate off — but academic libraries choose a platform on how well it manages licensed electronic resources alongside print, and public libraries choose on circulation, holds and patron service across a shared consortium catalogue, and the two contests have different winners. Decomposed into contested sub-niches below.

## The Problem
Libraries leaving a platform need to validate the migration themselves, and the only tools at hand are spreadsheets, MarcEdit and the vendor's own reports.

## What Already Exists
Enterprise ETL and data-quality platforms (Informatica, Talend, Fivetran with dbt) with profiling, mapping and reconciliation for ERP and CRM migrations; MarcEdit for MARC editing.

## The Customization Gap
A library migration needs MARC 21 bibliographic, holdings and authority parsing; item-level status and location mappings that differ per branch; patron data handled under state confidentiality law; circulation and holds state that must survive mid-transaction; and electronic-resource activations checked against a knowledge base. The generic tools need all of that built as connectors and rules before they can reconcile anything.

## Target Customer
Technical services and systems librarians at consortia and large public or academic libraries in a migration year.

## Impact If Solved
A reusable library profile for an existing ETL platform turns migration validation from sampling into a full reconciliation, at a cost a consortium can share across members.
