# Data Quality Tools That Don't Read MARC

**Niche:** [[niches/libraries-and-archives/copy-cataloguing-and-shelf-ready/profile|Copy Cataloguing & Shelf-Ready Records]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data-quality platforms profile and validate any table; a MARC record's rules live in fixed fields, indicators and cataloguing standards they have never seen.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver a catalogue record a library can load without touching — matched to the exact edition and format and arriving with the item — and whoever does it right for the most formats and languages takes the library's record supply.

## The Problem
Vendor record files arrive weekly and are spot-checked, if at all, before loading.

## What Already Exists
Data-quality and observability tools (Informatica Data Quality, Great Expectations, OpenRefine) and MarcEdit's validation functions; OCLC's own record validation.

## The Customization Gap
Library validation needs MARC 21 structure and RDA rules, the library's local profile (call number scheme, local subject fields, item templates), vendor-specific error patterns, authority checks against LC name and subject files, and reports a cataloguer can act on. The generic tools must be taught all of it as rules.

## Target Customer
Cataloguing and technical services managers receiving vendor record loads.

## Impact If Solved
Every load checked automatically, with a short list of records to fix instead of a weekly sample.
