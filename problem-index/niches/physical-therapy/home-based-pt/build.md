# Home Environment Fall Risk Assessment Tool

**Niche:** [[niches/physical-therapy/home-based-pt/profile|Home-Based PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Home-based PTs conduct structured, standardized fall risk assessments of patient homes — documenting hazards, linking to DME orders and home modification recommendations, and generating patient/family safety reports.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #tacit-knowledge-ml #worker-facing #compliance

## The Problem
Every home-based PT visit involves implicit assessment of the patient's living environment for fall risks — loose rugs, poor lighting, missing grab bars in bathrooms, cluttered hallways, stairs without handrails, beds that are too low to safely enter/exit. Experienced home PTs develop an eye for environmental hazards through years of practice, scanning a room and immediately identifying the three things most likely to cause a fall. This assessment is currently done ad-hoc, documented in free-text notes if documented at all, and rarely results in a structured action plan. No standardized tool exists to guide the assessment, ensure consistency across therapists, or generate actionable output (DME orders, home modification referrals, patient/family education materials).

## Why Nobody Has Built This
Home environment assessment sits at the intersection of clinical PT practice and home safety evaluation — two domains with different professional frameworks. PT EMRs focus on body-level assessment (ROM, strength, balance scores), not environment-level assessment. Home safety checklists exist in paper form but aren't integrated into clinical documentation or linked to actionable outputs like DME prescriptions. The user base (home-based PTs) is smaller and lower-revenue than clinic-based PTs, making it a less attractive market for EMR vendors. Additionally, the environmental assessment requires capturing spatial and visual information (photos of hazards, room layouts) that text-based EMR documentation doesn't accommodate well.

## What to Build
A mobile-first assessment tool that guides the PT through a structured room-by-room home safety evaluation: bathroom (grab bars, shower chair, toilet height, non-slip surfaces), bedroom (bed height, nightstand placement, path to bathroom), kitchen (reaching hazards, floor surfaces), living areas (rug anchoring, lighting, furniture spacing), and transitions (stairs, thresholds, outdoor paths). Each identified hazard links to: a severity score, a recommended intervention (DME order, home modification, patient education), and a photo documentation slot. Output includes: (1) a clinical summary for the patient's medical record, (2) a patient/family-facing safety report with prioritized recommendations and local contractor/DME supplier contacts, and (3) pre-populated DME prescription forms. Over time, the tool builds a dataset of home hazard patterns correlated with fall outcomes, enabling predictive risk scoring.

## Target Customer
Home-based PTs and home health agency PT directors who want to standardize environmental safety assessments, reduce fall-related liability, and generate documentation that supports continued home health authorization.

## Impact If Built
Standardizes a currently ad-hoc process, reducing variability in fall risk identification between experienced and newer therapists. Generates actionable DME orders and home modification recommendations that are currently lost to free-text documentation. Provides structured evidence supporting homebound status and continued home health PT authorization — protecting revenue and ensuring patients receive needed care.
