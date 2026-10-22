# One-Pass Proofing That Ends in a Spec-Checked File

**Niche:** [[niches/recording-studios/backlist-volume-narration/profile|Backlist & Independent Volume Narration]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A finished hour of audiobook passes through editing, proofing, pickups and mastering as four separate jobs, when one aligned pass could do most of it.
**Tags:** #transformers #seq2seq #hidden-markov-models #cnns #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to cut the edit, proof and pickup hours behind each finished hour without letting misreads through publisher QC, and whoever gets closest to one clean pass per finished hour keeps backlist programmes from moving to AI narration.

## The Problem
After recording, an editor removes retakes and noises, a proofer listens against the manuscript (about 1.5 hours per finished hour), the narrator records pickups, the editor drops them in, and someone masters to the retailer's spec. Each pass is a full listen. On a 10-hour book that is dozens of hours of listening on top of the recording itself, paid from a per-finished-hour fee that doesn't grow.

## Why Nobody Has Built This
Tools grew up separately: DAWs for editing, Pozotron for proofing, loudness meters for mastering, the retailer's checker at upload. Production houses are small and stitch them together by hand. Speech recognition good enough to align a whole book word by word at low cost is recent.

## What to Build
A single pipeline per chapter: align the raw recording to the manuscript; cut repeated takes automatically by recognising the narrator's restarts; flag missed, added, misread and mispronounced words against the pronunciation guide; detect clicks, breaths and room-tone breaks; generate the pickup list with context playback; drop pickups into place with tone matching; and run the retailer spec check on every file before anyone exports. Each house sees its own hours per finished hour by narrator and title.

## Target Customer
Production houses producing hundreds of backlist titles a year, and narrator-producers working through ACX.

## Impact If Built
Post-production per finished hour falls from several hours toward one (estimate), the difference between human narration losing to AI on backlist economics and keeping its place.
