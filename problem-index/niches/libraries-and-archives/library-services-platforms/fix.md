# Ten Years of Decision History Lost at Cutover

**Niche:** [[niches/libraries-and-archives/library-services-platforms/profile|Library Services Platforms]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Fix (Pain Point)
**One-liner:** Order notes, weeding decisions and licence annotations that explained the collection are dropped in migration because the new platform has no field for them.
**Tags:** #large-language-models #data-integration #evaluation-metrics #quick-win #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to become the system of record a library will not migrate off — but academic libraries choose a platform on how well it manages licensed electronic resources alongside print, and public libraries choose on circulation, holds and patron service across a shared consortium catalogue, and the two contests have different winners. Decomposed into contested sub-niches below.

## The Problem
The only trace of why a title was bought, kept or withdrawn often lives in free-text notes on order and item records. Migration mappings treat those notes as low priority and truncate or discard them.

## Why It's Still Broken
Notes are unstructured, every library uses them differently, and the vendor's mapping specification only covers fields its platform supports.

## What a Fix Looks Like
Before cutover, extract every free-text note, classify it (selection reason, condition, donor, licence term, weeding decision) and store it as structured data in the new platform or in a separate decision archive linked by record identifier.

## Who Feels the Pain
Selectors and collection managers who lose the history behind their collection; directors defending a past decision to a board.

## Impact If Fixed
A decade of collection reasoning survives the migration at the cost of a few days' processing.
