# Age-Normed Vital Sign Alerting and Dosing Guardrails

**Niche:** [[niches/urgent-care/pediatric-urgent-care/profile|Pediatric Urgent Care]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Pediatric UC triage nurses and MAs stop relying on age-based vital sign reference cards taped to the wall — getting EHR-integrated alerts that automatically flag vitals outside normal range for the patient's specific age and weight.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #worker-facing #quick-win

## The Problem
When a medical assistant enters vitals for a 14-month-old in Experity — heart rate 155, respiratory rate 32, blood pressure 85/50 — the system either flags nothing (because these are within adult normal ranges) or flags everything (because adult alert thresholds trigger on every pediatric patient). The MA must mentally reference an age-based vital sign chart (often a laminated card taped to the wall or a poster in the triage room) to determine if these vitals are normal for a 14-month-old. They are, in fact, completely normal — but a new MA without pediatric experience might not know that. Conversely, a heart rate of 180 in the same patient is significantly tachycardic and requires immediate provider attention, but the system treats both values identically because it has no concept of age-normed ranges.

## What Already Exists
Hospital pediatric EHRs (Epic, Cerner) have age-normed vital sign ranges built into their systems, but these are enterprise platforms priced for hospitals, not freestanding UCs. UC EHRs (Experity, Athenahealth) use adult-default vital sign alerting. Standalone pediatric reference apps (Pedi QuikCalc, PediSafe) provide age-normed ranges and dosing calculations on a smartphone but are disconnected from the EHR — the MA checks the app, then decides whether to flag the provider, with no documentation trail.

## The Customization Gap
A pediatric vital sign alerting layer for UC needs to: integrate with the existing EHR at the vital sign entry point; reference the patient's age (calculated from DOB, not manually entered) and weight to determine appropriate normal ranges for each vital sign; flag values outside age-normed ranges with severity levels (borderline vs. critical); auto-calculate weight-based medication doses when the provider prescribes (ibuprofen at 10mg/kg, amoxicillin at 45mg/kg/day) and alert on dosing errors; and create an audit trail showing that age-appropriate evaluation was performed. This is not a standalone app — it must be embedded in the clinical workflow where vitals are entered and medications are prescribed, requiring EHR integration that smartphone reference apps cannot provide.

## Target Customer
Clinical directors and IT administrators at pediatric UCs currently using adult-defaulting EHR systems, and MAs/triage nurses who rely on wall charts and reference apps for pediatric vital sign interpretation.

## Impact If Solved
Eliminates reliance on manual age-normed vital sign interpretation, reducing missed abnormal vitals in pediatric patients (estimated to occur in 5-8% of pediatric UC visits due to MA unfamiliarity with pediatric ranges). Prevents weight-based dosing errors at the prescribing point rather than catching them at the pharmacy. Creates documentation that supports the standard of care for pediatric vital sign evaluation — critical for malpractice defense in missed diagnoses.
