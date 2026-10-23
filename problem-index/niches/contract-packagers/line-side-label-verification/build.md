# Verification Configured From the Job, Not the Camera

**Niche:** [[niches/contract-packagers/line-side-label-verification/profile|Line-Side Label Verification, Coding & Inspection]]
**Industry:** [[industries/contract-packagers|Contract Packagers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A camera that has to be re-taught by an engineer for every job is useless on a line that changes job three times a day.
**Tags:** #cnns #object-detection #transfer-learning #transformers #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to catch every wrong label, missing lot code and unreadable barcode at full line speed, and whoever reaches zero escapes with the fewest false rejects stopping the line takes the account.

## The Problem
Co-packers run many short jobs. Each needs different checks: the label version, the barcodes at each level, the lot and expiry format, the variants in a mixed pack. Conventional vision systems are configured per product by a specialist, so most co-packers only use them on long runs and check everything else by eye.

## Why Nobody Has Built This
Vision vendors sell hardware and per-application setup; they assume long runs. Few vendors link a camera to a job record that contains the approved artwork and the code rules.

## What to Build
Verification that reads its configuration from the job: approved artwork, valid barcodes per level, code formats, variant images. A few reference images of good units train a per-job model by few-shot transfer, and it runs on a fixed camera or a tablet or handheld at pack-out. Results are logged against the job and summarised for the client and the auditor.

## Target Customer
Quality managers at co-packers running many short consumer and food jobs; pharmaceutical packagers' clinical lines.

## Impact If Built
Verification on every job rather than only the long runs, set up by the line lead in minutes.
