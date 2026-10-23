# An Edit-Diff Engine That Learns Each Dictator

**Niche:** [[niches/document-preparation-services/medical-transcription-documentation/profile|Medical Transcription & Healthcare Documentation Editing]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every correction an editor makes to a speech-recognition draft is logged and then ignored, so each new editor relearns every physician's habits one critical error at a time.
**Tags:** #tacit-knowledge-ml #seq2seq #transformers #large-language-models #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to return a health system's residual dictation — the reports front-end speech recognition and ambient scribes don't absorb — inside contract turnaround at an AHDI score of 98 or better, and whoever holds turnaround and accuracy at the fewest editor minutes per line takes the account.

## The Problem
A documentation vendor serving a health system edits drafts from dozens or hundreds of dictators. Veteran editors know who drops negatives, who dictates out of order, who uses a non-standard drug name, and which specialties produce the dangerous mishearings (laterality, dose, "hypo" and "hyper"). The vendor stores every draft and every final, so each correction is a recorded diff. Nothing reads them. When an editor leaves, the vendor keeps the diffs and loses the knowledge.

## Why Nobody Has Built This
Recognition vendors tune acoustic and language models to dictators, but their tuning targets word error rate, not the clinically significant errors an editor catches. Documentation vendors are thin-margin piece-rate shops without ML teams. The diff also lacks the reason for each edit, which has to be captured or inferred before it is useful.

## What to Build
An engine that aligns draft and final at token level, clusters each dictator's recurring corrections, and separates recogniser errors, dictator habits and clinical-plausibility catches, with one-keystroke reason capture only where it is uncertain. It pre-applies high-confidence habits, highlights spans where this dictator's drafts have historically needed a clinical catch, and keeps the profile with the account. Models train per account inside each business-associate agreement unless the contract allows de-identified learning across accounts.

## Target Customer
VP of Operations or Quality at a healthcare documentation vendor; HIM directors running in-house editing teams.

## Impact If Built
New editors reach veteran accuracy on an account in days, critical errors concentrate where attention goes, and lines per hour rise without the turnaround or AHDI score slipping.
