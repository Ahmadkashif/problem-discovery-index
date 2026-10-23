# Quoting by Predicted Edit Effort

**Niche:** [[niches/document-preparation-services/transcription-platforms/profile|General Transcription Platforms (Per-Minute, Hybrid)]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platforms charge and pay the same per minute for a clean monologue and an eight-person focus group, though the human effort differs several-fold and the machine already knows which is which.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to justify a human-verified tier priced near eight times the machine transcript, file by file, as recognisers improve, and whoever predicts which minutes actually need a human, and prices and routes them that way, takes the account.

## The Problem
A customer uploading a file chooses machine or human at a flat rate. Customers with clean audio overpay for the human tier and drift to machine-only, while customers with hard audio get human transcripts at a price that doesn't cover the editing. The platform learns how hard a file was only after an editor has spent the time.

## Why Nobody Has Built This
Flat per-minute pricing is simple to sell and to explain to contractors. Difficulty-based quotes need a model the platform trusts enough to put a price on, and a policy for when it is wrong. The data to train it sits in operations logs that were never joined to the recogniser's output.

## What to Build
A difficulty model trained on the platform's history: audio features (noise, overlap, speaker count, speaking rate, channel), recogniser confidence and n-best disagreement, domain vocabulary density and the customer's style requirements, predicting editor minutes per audio minute and how much the human pass changes meaning-bearing words. It drives quotes in three or four bands, worker pay posted before a file is claimed, and a "machine is enough for these segments" recommendation with the evidence shown to the customer.

## Target Customer
Heads of operations and pricing at transcription platforms; enterprise transcription buyers who want to pay for the human pass only where it matters.

## Impact If Built
Fewer customers lost to machine-only on clean audio, margin restored on hard audio, and hard files claimed on time because they pay what they cost.
