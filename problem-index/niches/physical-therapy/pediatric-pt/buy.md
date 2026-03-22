# Pediatric-Specific Outcome Measurement Module

**Niche:** [[niches/physical-therapy/pediatric-pt/profile|Pediatric PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Pediatric PTs get built-in PDMS-2, GMFM, and Bayley scoring within their EMR — with age-normed calculations, visual trajectory charts, and export formats matching IEP/IFSP documentation requirements.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #compliance

## The Problem
Pediatric PT uses entirely different outcome measures than adult PT. The PDMS-2 (Peabody Developmental Motor Scales), GMFM (Gross Motor Function Measure), Bayley Scales, Alberta Infant Motor Scale, and Bruininks-Oseretsky Test are the standard pediatric assessments — none of which are built into any PT EMR. Therapists administer these assessments, manually calculate raw and standard scores (the PDMS-2 alone has 249 items across 6 subtests requiring age-normed standard score lookups), record results in free-text notes, and then manually re-enter the data when generating IEP progress reports. The manual scoring process takes 15-30 minutes per assessment, introduces calculation errors, and produces data that isn't structured for longitudinal comparison.

## What Already Exists
WebPT and Clinicient/Prompt have adult outcome measures built in — Oswestry Disability Index, DASH, LEFS, and others auto-calculate scores and track trends. Some standalone apps exist for PDMS-2 scoring (manual score calculators), but they're disconnected from the EMR and don't provide longitudinal tracking. Central Reach, designed for ABA therapy practices, has some developmental tracking but is not built for PT clinical documentation. No integrated solution combines pediatric outcome measure scoring with PT clinical documentation and IEP/IFSP-compatible reporting.

## The Customization Gap
The adaptation needed is bringing the same auto-scoring and trend-tracking capability that exists for adult outcome measures to pediatric assessments, within the PT EMR workflow. Specific requirements: (1) digital administration forms for PDMS-2, GMFM, Bayley, and Alberta Infant Motor Scale with item-level data capture, (2) automated raw-to-standard score conversion using age-normed tables (the core manual burden), (3) subtest-level scoring with composite calculations (PDMS-2 has Gross Motor Quotient and Fine Motor Quotient composites), (4) longitudinal trend charts showing standard scores across assessment dates by subtest, (5) export to IEP/IFSP-compatible formats (specific to each school district's reporting template), and (6) goal tracking linked to assessment subtest items (e.g., "Patient will achieve score of 2 on GMFM Dimension D item 52 — standing on one foot for 10 seconds"). This requires deep knowledge of each assessment's scoring manual and the education system's documentation standards.

## Target Customer
Pediatric PT practices and early intervention agencies that administer standardized developmental assessments monthly or quarterly and need to reduce scoring time, eliminate calculation errors, and generate IEP/IFSP-compliant progress documentation.

## Impact If Solved
Reduces assessment scoring time from 15-30 minutes to 2-5 minutes per assessment by automating age-normed calculations. Eliminates scoring errors that can misrepresent a child's developmental status. Provides structured longitudinal data that strengthens IEP/IFSP justifications for continued therapy services — protecting authorization and ensuring children receive needed treatment.
