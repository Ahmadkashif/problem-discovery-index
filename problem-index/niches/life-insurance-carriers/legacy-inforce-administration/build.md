# Independent Recalculation of Every Policy Before Cut-Over

**Niche:** [[niches/life-insurance-carriers/legacy-inforce-administration/profile|Legacy In-Force Administration & Block Conversions]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Conversions test a sample of policies against the old system's values; the errors live in the policies nobody sampled.
**Tags:** #large-language-models #feature-engineering #data-integration #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to move decades-old policies off legacy administration systems with every cash value, loan and dividend reconciled to the penny, and whoever converts a block with the fewest unreconciled policies at cut-over takes the account.

## The Problem
A universal life block written over twenty years may carry dozens of product versions, riders and state variations, each with its own cost-of-insurance, interest crediting and charge logic. Conversion teams rebuild those rules in the new system and test them on samples. Mismatches that surface after cut-over become policyholder complaints, regulatory findings and correction projects that cost more than the conversion.

## Why Nobody Has Built This
Every block is different, the rules are buried in code and forms, and conversions happen once per block, so tooling has never been worth building for one carrier. TPAs and consultancies sell labour hours.

## What to Build
A recalculation engine that reads policy forms, rate files and admin code (with LLM-assisted extraction, verified by administrators) into executable product specifications. It replays each policy's transaction history from issue, compares every value to the legacy system and the target system, and classifies discrepancies by cause. The same reconstructed block produces the data tape and experience study a buyer or reinsurer needs.

## Target Customer
COOs and conversion programme leads at carriers modernising or divesting closed blocks; in-force acquirers onboarding acquired blocks.

## Impact If Built
Full-population reconciliation instead of samples, faster cut-overs and far fewer post-conversion corrections.
