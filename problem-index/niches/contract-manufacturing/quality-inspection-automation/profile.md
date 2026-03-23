# Quality Inspection Automation

**Parent Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Category:** Highly Automatable

## Profile
**Market Size:** $10-15B (embedded)
**Share of Parent Industry:** ~3-4% (embedded cost across all CMs)
**Digital Adoption:** Medium — AOI systems exist for electronics, but visual inspection for machined parts, castings, and plastic components remains primarily manual
**Target Buyer:** Quality manager or inspection supervisor at CMs with 5+ dedicated inspection staff
**Automation Potential:** High — visual surface defect detection, dimensional verification, and accept/reject disposition follow defined acceptance criteria that are systematically applied but subject to human variation

## What Makes This a Distinct Niche
Quality inspection is a horizontal function across all contract manufacturing — electronics, machined parts, castings, molded plastics, and medical devices all require visual and dimensional inspection against OEM workmanship standards. Inspection labor is one of the highest-cost quality functions: dedicated inspectors performing repetitive accept/reject decisions on every unit. Inspector-to-inspector variation creates both quality escapes (defective products passed) and over-rejection (acceptable products scrapped). The economic case for automation is clear — inspection labor is expensive, human consistency is limited, and the inspection task (compare product appearance to acceptance standard) is structurally amenable to computer vision. Yet deployment remains limited outside electronics AOI because each product requires custom model training.

## Current Tools & Gaps
Cognex VisionPro and Keyence vision systems provide industrial vision hardware. Koh Young and Mirtec provide electronics-specific AOI. Generic anomaly detection models (Landing AI, Instrumental) offer defect detection without labeled training data. No platform provides a rapid-deployment inspection model that a quality engineer (not a data scientist) can configure for a new part number — defining the acceptance criteria, capturing reference images, and deploying a calibrated inspection model — in days rather than months.

## Problems
- [[niches/contract-manufacturing/quality-inspection-automation/build|🔨 Build: No-Code Visual Inspection Model Builder for CMs]]
- [[niches/contract-manufacturing/quality-inspection-automation/buy|🛒 Buy: Vision System with OEM Workmanship Standard Integration]]
- [[niches/contract-manufacturing/quality-inspection-automation/fix|🔧 Fix: Inspector-to-Inspector Variation on Boundary Conditions]]
