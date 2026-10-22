# The PDF Statement Keyed by Hand

**Niche:** [[niches/wireless-retail-agents/carrier-commission-recovery/profile|Carrier Commission Recovery]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Fix (Pain Point)
**One-liner:** Some carriers, brands and master agents still send statements as PDFs, and the reconciliation starts with a clerk retyping them.
**Tags:** #large-language-models #transformers #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche (iQmetrix ReconcilePro, outsourced reconciliation services and spreadsheet-run back offices) is fighting to match every carrier statement line to the activation that earned it and file the dispute before the carrier's window closes, and whoever recovers the most short-paid dollars per month-end takes the dealer's reconciliation.

## The Problem
Commission software imports CSV and Excel; Commission Tracker's help pages say PDF statements are entered manually. For prepaid dealers dealing with several brands and master agents, PDFs are common. Keying takes days and introduces errors before matching even begins.

## Why It's Still Broken
Statement layouts change without notice, and template-based PDF extraction breaks each time. The dealer is too small a customer to get the sender to change formats.

## What a Fix Looks Like
Language-model extraction of statement PDFs into the reconciliation schema, with totals checked against the statement's own subtotals and any line that doesn't add up routed to a person. A layout change becomes a review of a few lines rather than a rebuilt template.

## Who Feels the Pain
Back-office clerks and owner-operators at month-end; the reconciliation it delays.

## Impact If Fixed
Days of keying become an hour of review, and reconciliation starts while dispute windows are still open.
