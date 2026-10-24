# Machine-Drafted Runsheets From County Indexes

**Niche:** [[niches/oil-and-gas-producers/runsheets-drilling-title/profile|Runsheets & Drilling Title]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A field landman spends days in a courthouse turning index entries and deed images into a runsheet that a model could draft for them to check.
**Tags:** #large-language-models #transformers #cnns #graph-theory #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver a complete runsheet and ownership schedule for each drilling unit before the spud date, and whoever's ownership schedules need the fewest corrections after first production takes the account.

## The Problem
A runsheet lists every instrument in a tract's chain: grantor, grantee, date, book and page, and what was conveyed or reserved. Building one for a multi-section unit means searching name by name through grantor-grantee indexes, following each owner forward and back, and reading each instrument, often handwritten in the early 1900s. Contract landmen bill by the day for this, and missed instruments become missing owners.

## Why Nobody Has Built This
County records are fragmented across thousands of counties with different indexing and imaging, and handwriting recognition on old deed books was poor until recently. Title attorneys, who carry the liability, have been cautious about machine work.

## What to Build
A pipeline that searches a county's online index or a licensed image source by tract and name, chains instruments by party and legal description into an ownership graph, reads each image to extract interests conveyed and reservations, and drafts a runsheet with confidence flags and links to every image. The landman verifies flagged items and fills gaps from the courthouse. The attorney's examination starts from a linked, searchable chain.

## Target Customer
Land managers at operators and owners of contract land brokerages.

## Impact If Built
If a unit runsheet takes ~10 landman-days today (estimate), cutting it to 3–4 days on counties with online images lowers title cost per unit by more than half. Each missed instrument caught before the opinion avoids a suspended owner after first production.
