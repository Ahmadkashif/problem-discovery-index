# Weld Quality Assessment from Visual Inspection Images

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Type:** High Impact
**One-liner:** Certified welding inspectors who evaluate weld surface appearance for AWS D1.1 acceptance criteria — reading porosity, undercut, overlap, and surface cracking from visual examination — perform a judgment task that takes years to develop and is a production bottleneck in every shop that can't afford enough qualified inspectors to keep pace with welder output.
**Tags:** #cnn #object-detection #multiclass-classification #computer-vision #tacit-knowledge-ml #compliance #revenue-impact

## The Problem

Weld quality inspection is the most critical and most skill-dependent quality step in metal fabrication. AWS D1.1 (structural steel), D1.2 (aluminum), and ASME Section IX (pressure vessels) define acceptance criteria for visual weld inspection — specifying maximum allowable porosity, undercut depth, overlap, crack indications, and reinforcement height. Applying these criteria requires a trained inspector who can recognize these conditions from weld surface appearance under controlled lighting, and judge whether a given indication is within or outside the acceptance boundary.

Certified Welding Inspectors (CWIs) take 3-5 years to develop reliable inspection judgment, and the CWI shortage is acute. A fabrication shop producing 40-60 welds per day with one CWI creates a bottleneck: the inspector either spends the day on routine accept/reject decisions on visually obvious welds (wasting their expertise) or samples inspects (missing defects on uninspected welds). Non-conforming welds that escape inspection generate expensive downstream consequences: field rework on structural components, pressure test failures on vessels, or — worst case — in-service structural failures.

The visual patterns that define weld quality are consistent enough to train a detection model. The surface appearance signatures of porosity (spherical surface interruptions), undercut (groove along the weld toe), overlap (weld metal rolled over the base metal surface), and lack of fusion (visible cold lap at the weld edge) each have characteristic visual features. The challenge is that these features appear at varying scale, orientation, and severity, and the acceptance threshold — is this undercut within the 1/32" maximum? — requires dimensional estimation from visual context.

## Why It's High Impact

A CWI earns $75,000-$100,000 annually. A vision model that handles routine accept/clear decisions on visually unambiguous welds and flags borderline conditions for CWI review multiplies the CWI's capacity by 3-4×. For a structural fabricator with 3 CWIs currently limited to sampling inspection, deploying AI-assisted inspection enables 100% inspection coverage, eliminating the quality escape risk of uninspected welds. The AWS D1.1 compliance documentation generated automatically by the inspection system also eliminates the inspection log paperwork that currently consumes 20% of CWI time.

## What a Solution Looks Like

A CNN detection model trained on weld surface images with labeled indications: defect bounding boxes annotated with defect type and severity classification. At inference time: camera captures weld pass image under controlled LED illumination; model detects and classifies surface indications; for each indication, estimates dimensional severity relative to acceptance threshold; generates pass/reject recommendation with confidence level. Borderline indications (confidence below threshold) are queued for CWI review with the model's classification and supporting image. Acceptance/rejection decision and supporting image are automatically logged to the job quality record.

## Implementation Path

Training data: weld surface images from production (structured photo capture of each weld pass) with CWI-annotated labels — defect type, location, and accept/reject disposition. 2,000-5,000 labeled weld images per defect category provide adequate fine-tuning data for a pre-trained CNN backbone. Illumination control at the inspection station is required for consistent image input. Integration with job shop ERP (JobBOSS, Prodsmart) for quality record generation. Pilot deployment on a single weld type (e.g., fillet welds on structural steel) to demonstrate acceptance before expanding to full defect taxonomy.
