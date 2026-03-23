# Vision System with OEM Workmanship Standard Integration

**Niche:** [[niches/contract-manufacturing/quality-inspection-automation/profile|Quality Inspection Automation]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vision systems from Cognex and Keyence detect surface anomalies, but they can't interpret an OEM's written workmanship standard — distinguishing between a cosmetic scratch that is acceptable per the standard and a functional scratch that requires rejection — the judgment layer that makes inspection useful for production rather than just a source of false alarms.
**Tags:** #cnns #transfer-learning #evaluation-metrics #tacit-knowledge-ml #compliance

## The Problem
OEM workmanship standards are written documents with descriptions like "Surface scratches are acceptable if they do not exceed 0.5mm in width or 10mm in length and are not located within 5mm of a functional surface." Translating this written specification into machine-interpretable acceptance criteria requires: (1) identifying what constitutes a "scratch" versus other surface conditions, (2) measuring scratch dimensions from camera images, (3) determining whether the scratch location is within a functional zone, and (4) applying the dimensional threshold to make an accept/reject decision. Current vision systems detect anomalies but cannot make this multi-criteria disposition decision against a written workmanship standard.

## What Already Exists
Cognex VisionPro and In-Sight provide machine vision with blob analysis, pattern matching, and defect detection. Landing AI provides an anomaly detection platform with limited defect classification. These tools can flag "something is different about this surface" but cannot determine whether that difference is acceptable or rejectable per the OEM's specific written criteria.

## The Customization Gap
A workmanship-standard-aware inspection system needs: (1) defect taxonomy configurable per OEM standard — defining defect categories (scratch, pit, dent, discoloration, contamination) with per-category acceptance criteria; (2) dimensional measurement from images — estimating defect length, width, and depth from 2D or 3D imaging; (3) zone-based disposition — different acceptance criteria for functional vs. cosmetic surfaces, with zone definitions derived from the engineering drawing; (4) standard version management — updating acceptance criteria when the OEM revises its workmanship standard, without retraining the vision model.

## Target Customer
Quality engineers at CMs producing parts for OEMs with formal workmanship standards (aerospace, medical, automotive), where the acceptance criteria are detailed enough to automate but currently applied through human judgment.

## Impact If Solved
Eliminates the false alarm problem that makes current vision systems frustrating — systems that flag every anomaly without understanding what's acceptable generate more work for inspectors, not less. Enables consistent application of OEM workmanship standards across shifts, reducing both quality escapes and over-rejection. For a CM with 20% false alarm rate on current vision systems, reducing to 5% recovers 75% of the human review labor consumed by false alarms.
