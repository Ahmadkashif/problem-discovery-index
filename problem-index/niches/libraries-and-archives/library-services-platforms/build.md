# Migration Rehearsal From the Library's Own Data

**Niche:** [[niches/libraries-and-archives/library-services-platforms/profile|Library Services Platforms]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A library learns what its platform migration lost months after cutover, when a patron's holds vanish or an order history cannot be found.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #automation #large-language-models
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to become the system of record a library will not migrate off — but academic libraries choose a platform on how well it manages licensed electronic resources alongside print, and public libraries choose on circulation, holds and patron service across a shared consortium catalogue, and the two contests have different winners. Decomposed into contested sub-niches below.

## The Problem
Moving from one platform to another means extracting bibliographic, item, holdings, patron, circulation, fines, order, invoice and licence data from the old system and mapping it into the new one's schema. Vendors run the migration with their own scripts and a test load or two; the library's staff check samples by hand. Problems surface after go-live: item statuses mapped wrongly, holds lost, local notes truncated, order histories orphaned, electronic portfolios not activated.

## Why Nobody Has Built This
Each vendor builds migration tooling only for migrations onto its own platform, and treats it as a cost of winning the contract. Libraries migrate once a decade, so no buyer accumulates enough repeat demand to fund an independent tool.

## What to Build
A vendor-neutral rehearsal service: extract the library's data, profile it field by field, run the target vendor's mapping on a copy, and diff the result record class by record class, reporting what will be lost, truncated or misclassified and how many patrons, holds and orders each issue touches. LLM-assisted mapping of free-text notes into structured fields covers the long tail.

## Target Customer
Consortium executive directors and technical services heads in the year before a platform migration; migration consultancies serving them.

## Impact If Built
Losses found before cutover rather than after: weeks of post-migration cleanup avoided and a measurable acceptance test the library can hold the vendor to.
