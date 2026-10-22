# Triage That Ranks a Collection by Risk Before the Money Runs Out

**Niche:** [[niches/recording-studios/archival-tape-transfer/profile|Archival Tape Transfer & Restoration]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An archive with ten thousand tapes and money to transfer two thousand chooses which ones by an expert's walk along the shelves.
**Tags:** #tacit-knowledge-ml #gradient-boosting #cnns #survival-analysis #feature-engineering #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to transfer degrading tape and disc collections to files and metadata that meet archive standards such as IASA TC-04 and FADGI, at a cost per hour a grant budget can carry, and whoever proves preservation-grade quality at production throughput wins the institutional contracts before working playback machines run out.

## The Problem
Grant-funded digitisation never covers a whole collection. Someone has to decide which carriers go first, weighing rarity, demand and risk of loss. The risk judgement is tacit: an experienced transfer engineer knows that certain tape brands from certain years shed binder, smells vinegar on an acetate reel, and sees edge damage or mould on a box that predicts trouble. Archives without that person guess, and tapes fail on the machine.

## Why Nobody Has Built This
Condition outcomes (played cleanly, needed baking, shed on the heads, unplayable) are known to transfer houses but recorded, if at all, in job notes. Each house's sample is small and specific to its clients, and archives publish condition surveys in inconsistent formats.

## What to Build
A triage model that predicts transfer difficulty and loss risk per item from carrier type, brand and stock number, recording year, storage history, and photos of the reel, box and pack, trained on transfer houses' recorded outcomes. Archives photograph and catalogue carriers on intake and get a ranked list that combines risk with their own priority scores, plus a cost and time estimate for each tier.

## Target Customer
Transfer houses quoting large institutional jobs, and archivists preparing grant applications and digitisation plans.

## Impact If Built
Scarce grant money goes first to the carriers most likely to be lost, and transfer houses quote collections on evidence rather than on a sample of a few boxes.
