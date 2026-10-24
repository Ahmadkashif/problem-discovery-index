# The Repeat Found After the Patient Left

**Niche:** [[niches/diagnostic-imaging-centers/mri-ct-technologists/profile|The MRI & CT Technologist]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A motion-blurred series or a mammogram missing the pectoral muscle is spotted by the radiologist hours later, and the patient has to come back.
**Tags:** #cnns #transfer-learning #object-detection #evaluation-metrics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to let one technologist run a scanner safely through a full shift, and whoever lets a single technologist complete the most exams per shift with no rise in repeat scans or safety events takes the account.

## The Problem
Technologists check images at the console under time pressure. Subtle motion, incomplete coverage or poor positioning is easy to miss when the next patient is waiting, and the radiologist sees it only when reading.

## Why It's Still Broken
Image-quality feedback is informal and delayed, and quality reviews for accreditation sample a few studies a year.

## What a Fix Looks Like
An automated check at the console that flags likely inadequate series or views (motion, coverage, positioning landmarks) before the patient leaves. Flags are logged by technologist so training can follow the patterns.

## Who Feels the Pain
Technologists called out for repeats; patients recalled for a second visit; radiologists writing "limited by motion".

## Impact If Fixed
Catching half of technical recalls at the console saves a scanner slot and a patient trip for each one (estimate). At a busy centre that is several slots a week.
