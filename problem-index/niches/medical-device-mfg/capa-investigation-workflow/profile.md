# CAPA Investigation Workflow

**Parent Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Category:** Highly Automatable

## Profile
**Market Size:** $8-12B (embedded in quality system operations across all device manufacturers)
**Share of Parent Industry:** ~6% (quality operations cost)
**Digital Adoption:** Medium — CAPA is managed in QMS platforms but the investigation process itself (root cause analysis, evidence gathering, effectiveness verification) is entirely manual
**Target Buyer:** Quality Director or CAPA Manager at device manufacturers (100-2,000 employees)
**Automation Potential:** High — CAPA investigation is rule-heavy, follows defined methodologies (5-Why, Fishbone, Fault Tree), and requires cross-system data correlation that ML can accelerate

## What Makes This a Distinct Niche
CAPA (Corrective and Preventive Action) is the single most FDA-cited quality system element — it appears in more FDA 483 observations and Warning Letters than any other QSR subsystem. The CAPA investigation process is a distinct operational workflow that cuts across complaints, production, supplier quality, and design control. A quality engineer managing 10-20 open CAPAs simultaneously must manually search complaint databases, production records, supplier data, and previous CAPA history to identify root causes — a detective process that averages 45-90 days per investigation. The investigation methodology is well-defined (FDA expects systematic root cause analysis), making it a strong automation target — but the cross-system data gathering that feeds the investigation has never been automated.

## Current Tools & Gaps
ETQ, MasterControl, Veeva Vault Quality, and Greenlight Guru manage CAPA workflow (initiation, investigation assignment, review, approval, effectiveness verification). They provide the workflow container but no assistance with the investigation content — the quality engineer opens the CAPA, receives the complaint or nonconformance description, and must independently search 4-6 systems for related data. None of these platforms suggest potential root causes, surface similar historical CAPAs, or correlate complaint patterns with production parameters.

## Problems
- [[niches/medical-device-mfg/capa-investigation-workflow/build|🔨 Build: ML-Assisted CAPA Root Cause Hypothesis Engine]]
- [[niches/medical-device-mfg/capa-investigation-workflow/buy|🛒 Buy: Cross-System CAPA Evidence Aggregator]]
- [[niches/medical-device-mfg/capa-investigation-workflow/fix|🔧 Fix: CAPA Effectiveness Verification Tracking]]
