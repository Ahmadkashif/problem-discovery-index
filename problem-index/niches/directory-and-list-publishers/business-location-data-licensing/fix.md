# The Correction Loop That Ends at the Licensee

**Niche:** [[niches/directory-and-list-publishers/business-location-data-licensing/profile|Business Location Data Licensing]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** Map users report every day that a place has closed or moved, and almost none of those corrections reach the compiler whose file the platform licensed.
**Tags:** #large-language-models #evaluation-metrics #data-integration #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to be the licensee's reference file for which businesses exist where right now — catching openings, moves and closures first — and whoever scores freshest in the licensee's own ground-truth audit takes the contract.

## The Problem
The licensee receives user edits, field reports and owner claims, fixes its own copy and moves on. The compiler's next delivery reintroduces the old value, and the licensee scores it as an error in the next audit.

## Why It's Still Broken
Feedback APIs exist on paper but carry free text and no shared identifier, and the licensee has little incentive to curate corrections for a supplier.

## What a Fix Looks Like
A structured correction exchange keyed on shared place identifiers, where the licensee's accepted corrections flow back as labelled outcomes, the compiler confirms or disputes each one, and both sides see the round trip in their audit metrics.

## Who Feels the Pain
Compiler data operations teams scored on errors they cannot see, and licensee place-data teams re-fixing the same records every delivery.

## Impact If Fixed
Each correction is made once, and the compiler gains the best closure labels in the market.
