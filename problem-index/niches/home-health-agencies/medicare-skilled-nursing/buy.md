# OASIS Decision Support with Auto-Population

**Niche:** [[niches/home-health-agencies/medicare-skilled-nursing/profile|Medicare-Certified Skilled Nursing Agencies]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** WellSky and HCHB handle OASIS data capture but don't guide clinicians through complex skip patterns or auto-populate from prior assessments — turning a 60-minute assessment into 30 minutes.
**Tags:** #decision-trees #large-language-models #transfer-learning #feature-engineering #automation #compliance #worker-facing #quick-win

## The Problem
OASIS assessments take 45-90 minutes per completion and must be done at admission, every 60-day recertification, and discharge. The assessment has 89 data elements with complex skip patterns that vary based on prior answers. Clinicians frequently answer questions they should skip or skip questions they should answer, causing claim denials. Many OASIS responses are nearly identical across consecutive assessments for the same patient — a stable chronic heart failure patient's functional status doesn't change much every 60 days — yet nurses re-enter everything from scratch.

## What Already Exists
WellSky, Homecare Homebase, and Axxess all have OASIS modules that present the assessment form digitally. Post-completion scrubber tools (SHP, OASIS Answers) review submitted assessments for errors and inconsistencies. These tools catch mistakes after the nurse has already spent an hour completing the assessment, generating rework rather than preventing errors.

## The Customization Gap
What's missing is real-time guidance during the assessment: auto-populating responses from the prior assessment with change-detection highlighting, enforcing skip patterns dynamically so clinicians never see irrelevant questions, validating clinical consistency in real-time (flagging when wound measurements increase but healing status is marked as "improving"), and predicting the PDGM payment group from current responses so agencies understand revenue implications before submission. This requires layering decision-tree logic and LLM-based consistency checking on top of existing EMR data.

## Target Customer
Any Medicare-certified home health agency completing 50+ OASIS assessments per month, particularly those with high claim denial rates or agencies that employ newer clinicians who struggle with OASIS complexity.

## Impact If Solved
Cutting OASIS completion time from 60 minutes to 30 minutes across an agency completing 200 assessments/month reclaims 100 clinician-hours monthly — equivalent to 2.5 full-time nursing weeks redirected to patient care. Reducing OASIS errors by 40-50% would lower claim denial rates and protect an estimated $200K-$400K in annual revenue per mid-size agency.
