# Edition Matching Before the Record Loads

**Niche:** [[niches/libraries-and-archives/copy-cataloguing-and-shelf-ready/profile|Copy Cataloguing & Shelf-Ready Records]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A record for the large-print edition gets attached to the paperback, or a new item spawns a duplicate record, and patrons place holds on the wrong thing for years.
**Tags:** #k-nearest-neighbors #transformers #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver a catalogue record a library can load without touching — matched to the exact edition and format and arriving with the item — and whoever does it right for the most formats and languages takes the library's record supply.

## The Problem
Matching an item to a record relies on ISBN, title and publisher strings. ISBNs are reused, missing or applied to multiple formats; titles vary; reprints and new editions look alike. Mismatches create duplicates and wrong holdings that confuse holds and inflate the catalogue, and fixing them later is slow hand work.

## Why Nobody Has Built This
Matching is buried inside OCLC's and the platforms' own load processes, which use deterministic rules tuned for coverage, and vendors are paid per record supplied, not per record correct.

## What to Build
A matching service that scores each incoming item against candidate records using every available signal — title page or cover image, physical description, page count, publisher, series, contributors, pricing and format data from the vendor invoice — and returns a confident match, a probable new edition, or a review flag with the evidence. It runs before load in the library's own workflow and learns from cataloguers' corrections.

## Target Customer
Technical services departments at public library systems and academic libraries loading thousands of records a month; consortia with shared catalogues.

## Impact If Built
Duplicates and wrong-edition attachments caught at the door rather than in years of cleanup, and holds that point patrons at the format they wanted.
