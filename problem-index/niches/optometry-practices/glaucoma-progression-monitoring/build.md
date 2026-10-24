# Cross-Device Progression Engine

**Niche:** [[niches/optometry-practices/glaucoma-progression-monitoring/profile|Glaucoma Monitoring & Progression Detection]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine that reads OCT, fields and pressures from any device and any year, removes artefacts, and gives each eye one progression trend and risk.
**Tags:** #cnns #transfer-learning #survival-analysis #gaussian-processes #tacit-knowledge-ml #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to catch glaucoma progression at the first visit it shows, and whoever leaves the smallest share of progressing eyes flagged a visit late takes the account.

## The Problem
Each device's progression analysis reads only its own scans, and OCT layer thicknesses differ between manufacturers. Practices that change devices, or that share patients with an ophthalmologist on a different platform, lose the trend. Doctors compare printouts by eye.

## Why Nobody Has Built This
Device makers have no reason to read competitors' scans. Harmonising thickness maps across devices needs paired scans and longitudinal outcomes that no single practice holds. The market is fragmented, with many small practices each owning a different mix of devices.

## What to Build
Ingest DICOM and vendor exports from each device. A CNN checks segmentation quality and flags myopic patterns. Thickness maps are mapped to a common scale using paired scans. A Gaussian-process trend over structure and function, with a survival model for risk, produces one per-eye progression view that the OD sees in the exam. Each call is recorded so it can be graded later.

## Target Customer
Multi-OD groups and rollups with mixed device fleets, then larger independent practices.

## Impact If Built
If a group following ~5,000 glaucoma and suspect eyes flags progression one visit earlier in 10% of progressing eyes, it prevents measurable field loss for dozens of patients a year (estimate) and keeps baselines through every device change.
