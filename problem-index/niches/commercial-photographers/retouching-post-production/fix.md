# The Style Guide Update Nobody's Actions Picked Up

**Niche:** [[niches/commercial-photographers/retouching-post-production/profile|Retouching & Post-Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Fix (Pain Point)
**One-liner:** A brand changes its shadow and margin spec mid-season by sending a new PDF, half the retouchers keep running last season's Photoshop actions, and three nights of images come back rejected.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to return brand-consistent, spec-compliant edits overnight at a defect rate the client's QA never sees, and whoever automates the routine edit without letting errors escape takes the account.

## The Problem
Brand style guides change: a softer shadow, a new background value, a different crop for a new retailer, a revised rule for how much wrinkle reduction is allowed. The update arrives as a revised PDF to an account manager. Each retoucher keeps their own Photoshop actions and presets per client, and some get updated and some don't. The inconsistency shows up as a rejection wave days later, across images from several people.

## Why It's Still Broken
Style rules live in documents, while execution lives in personal scripts on individual workstations, often across several shifts and an offshore team. Nothing checks finished images against the current version of the rules, so the only test is the client's QA.

## What a Fix Looks Like
Turn each style guide into a versioned, machine-readable rule set, with a language model drafting the rules from the PDF for an account manager to confirm. Shared actions and presets are generated from the rule set rather than kept by hand. Every finished image is checked against the current version (margins, background value, shadow opacity, crop) before delivery, with a clear diff when a rule has changed.

## Who Feels the Pain
Retouchers redoing work they did to the old spec; account managers fielding rejection waves; brand QA teams receiving inconsistent batches.

## Impact If Fixed
A spec change takes effect on every workstation the same night, and rejection waves after style updates stop.
