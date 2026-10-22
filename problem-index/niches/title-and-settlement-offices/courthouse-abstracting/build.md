# A Field Guide to Every Courthouse's Records

**Niche:** [[niches/title-and-settlement-offices/courthouse-abstracting/profile|Courthouse Abstracting in Non-Plant Counties]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** What an experienced abstractor knows about a county — where the online index stops, which years were misindexed, where probate files live — is the difference between a complete search and a claim, and none of it is written down.
**Tags:** #tacit-knowledge-ml #large-language-models #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to return a complete, correctly indexed search from a county with no title plant and no reliable online index inside the agent's turn time, and whoever knows each courthouse's indexing quirks and gaps takes that county's orders.

## The Problem
An agency in one state orders a search in a rural county in another. The abstractor it reaches may or may not know that this county's online index begins in 1985, that judgments before 1990 are only in the clerk's docket books, that one decade of deeds was indexed by first name, or that probate files sit in a different building. When the abstractor retires, the agency's coverage of that county goes with them.

## Why Nobody Has Built This
The knowledge is fragmented across thousands of abstractors in a small, local market with no platform owner. Ordering platforms route orders and collect fees; they do not capture how the search was done.

## What to Build
A county-by-county knowledge base built from abstractors' search logs and structured interviews: index coverage by record type and year, known gaps and misindexing patterns, where each record class is held, and a checklist the search must satisfy in that county. Search results are checked against the checklist before delivery, and abstractors earn a quality score from post-closing defects traced back to the search.

## Target Customer
Agencies and underwriter direct operations ordering searches across many non-plant counties; search-ordering platforms that want a quality layer.

## Impact If Built
Search completeness stops depending on which abstractor picked up the order, and an agency can price a county's risk instead of discovering it.
