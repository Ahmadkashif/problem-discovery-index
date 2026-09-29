# Legacy Warehouse and BI Migration

**Industry:** [[data-platform-integrators|Data Platform Integrators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Migrating a decade of warehouse logic and four thousand reports is done by translating everything, because nobody can establish which of it anyone still uses.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #gradient-boosting #evaluation-metrics #data-integration #automation

## The Problem
A migration from a legacy warehouse and BI estate — Teradata, Netezza, on-premise SQL Server, with Business Objects, Cognos or an ageing Tableau deployment on top — is one of the largest engagements in this category. The estate contains thousands of stored procedures, views and reports accumulated over a decade, written by people who have left, in dialects with platform-specific behaviours.

The default approach is to translate everything, because deciding what to leave behind requires knowing what is used and what it means, and nobody does. So an organisation pays to migrate reports nobody has opened in three years, and carries a decade of accumulated logic onto a new platform where it immediately begins accumulating further.

The translation itself is laborious and subtly dangerous. SQL dialects differ in null handling, date arithmetic, implicit casting and aggregate behaviour, and a translated query that runs successfully may return different numbers. Validating that a migrated report matches the original requires running both and comparing, which requires the legacy system to stay alive and someone to adjudicate the differences — of which there are always many, most benign and some not.

## What Already Exists
Automated SQL transpilation exists — SQLGlot, vendor migration tools from Snowflake, Databricks and the cloud providers, and specialist vendors like Datametica and Next Pathway. BI conversion tooling handles some report translation between platforms. Lineage and usage reporting exist in the legacy platforms, often disabled or unexamined. Reconciliation frameworks for comparing outputs are usually built bespoke per engagement.

## The Customisation Gap
The highest-value analysis is the one nobody runs at the start: a usage and dependency census of the legacy estate. Which reports have been opened, by whom, how recently; which stored procedures are actually invoked; which tables anything reads. That is available in the legacy platform's own logs and would typically cut the migration scope substantially — which is precisely why a firm billing by scope has little reason to run it first.

The second gap is semantic rather than syntactic translation. Transpilers convert syntax; the risk is in behavioural differences between dialects, and identifying which specific constructs in a given codebase are behaviourally risky — implicit casts, null-sensitive aggregates, date arithmetic across time zones, ordering-dependent logic — is a classification task over the code that would focus validation where it matters instead of spreading it evenly.

The third is the reconciliation itself. Comparing legacy and migrated outputs produces thousands of differences, most explainable by a handful of causes, and clustering them by cause rather than listing them by row converts weeks of adjudication into a day of decisions.

And the opportunity nobody takes is to consolidate rather than translate. Four thousand reports usually represent a few hundred distinct questions asked in slightly different ways, and grouping them by semantic equivalence is the analysis that would let an organisation arrive on the new platform with something maintainable.

## Impact If Solved
Migration scope is set by the size of the legacy estate rather than by what anyone uses, which makes these projects larger, longer and more expensive than they need to be, and delivers a new platform pre-loaded with a decade of dead logic. A usage census, risk-focused validation and cause-clustered reconciliation address the three places the effort actually goes, and semantic consolidation is the difference between migrating a mess and leaving it behind.
