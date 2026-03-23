# AOI Defect Classification Tuned for Electronics Assembly

**Niche:** [[niches/contract-manufacturing/electronics-pcba-assembly/profile|Electronics PCBA Assembly]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AOI systems from Koh Young and Mirtec detect anomalies in solder joints, but their defect classification generates 30-60% false call rates on fine-pitch components — flooding quality staff with alarms that experienced inspectors would immediately dismiss as acceptable variation.
**Tags:** #cnns #transfer-learning #evaluation-metrics #tacit-knowledge-ml #quick-win

## The Problem
Automated Optical Inspection (AOI) systems inspect every solder joint on every board and flag conditions that deviate from programmed acceptance criteria. For standard components (0805 passives, SOICs), AOI classification accuracy is good. For fine-pitch components (0201 passives, QFN/BGA packages, connectors), the false call rate — joints flagged as defective that are actually acceptable — runs 30-60%. Each false call requires a human inspector to review the flagged joint under magnification and disposition it as accept or reject. A line running 500 boards/day with 50 false calls per board generates 25,000 human review decisions daily — an enormous labor sink that exists because the AOI's defect classification isn't tuned to the specific acceptance criteria for each component type and solder joint geometry.

## What Already Exists
Koh Young Zenith, Mirtec MV-6 OMNI, and Viscom S3088 provide 3D AOI with built-in defect classification algorithms. These algorithms use manufacturer-trained models that work across a broad range of applications but are not optimized for the specific component mix, solder paste brand, and reflow profile at a particular EMS facility. Programming a new product on AOI requires extensive tuning by an AOI engineer to reduce false calls.

## The Customization Gap
A false-call-reduction layer needs: (1) facility-specific fine-tuning — training the classifier on the disposition decisions (accept vs. reject) made by experienced inspectors at this specific facility on this specific product, creating a site-calibrated acceptance model; (2) component-type-specific classification — different defect thresholds for 0201 passives vs. QFN vs. through-hole connectors, reflecting the different acceptance criteria and visual characteristics; (3) continuous learning — updating the model as inspectors disposition new edge cases, reducing false calls over time without manual AOI reprogramming.

## Target Customer
AOI engineers and quality managers at EMS companies running 3+ AOI systems, where false call management consumes significant inspection labor.

## Impact If Solved
Reduces AOI false call rate from 30-60% to under 10% on fine-pitch components. For a line generating 25,000 false calls/day, reducing to 5,000 recovers 80% of human review labor. At 15 seconds per review decision, this saves 80+ inspector-hours daily across a high-volume EMS facility.
