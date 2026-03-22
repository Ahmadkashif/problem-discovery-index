# Biofeedback Device Data Integration for PT EMRs

**Niche:** [[niches/physical-therapy/pelvic-floor-specialists/profile|Pelvic Floor PT Specialists]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Pelvic floor PTs see home biofeedback device data — pelvic floor EMG readings, exercise completion, contraction quality — inside their clinical documentation instead of checking a separate device app during the visit.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #worker-facing

## The Problem
Pelvic floor PT relies heavily on biofeedback — EMG sensors that measure pelvic floor muscle activation during exercises. In-clinic biofeedback is standard, but patients also use home biofeedback devices (Pericoach, Elvie, Pathway by Prometheus) to perform prescribed pelvic floor exercises between visits. These devices capture valuable clinical data: contraction strength over time, endurance measurements, relaxation ability, and exercise adherence. But this data lives in the device manufacturer's proprietary app, completely disconnected from the PT's clinical documentation. During a follow-up visit, the therapist must ask the patient to pull up the app on their phone, scroll through charts they may not understand, and try to correlate device data with their treatment plan — a clunky process that wastes visit time and loses data fidelity.

## What Already Exists
Home biofeedback devices (Pericoach, Elvie, Pathway) deliver pelvic floor exercise guidance and track metrics through their own mobile apps. PT EMRs (WebPT, Clinicient) handle clinical documentation and treatment planning. MedBridge and PhysiTrack deliver general home exercise programs. None of these systems talk to each other. The biofeedback device captures objective pelvic floor function data that the PT needs for clinical decision-making, but it sits in a consumer health app rather than a clinical system.

## The Customization Gap
The integration gap has two layers. First, raw data connectivity: an API bridge that pulls biofeedback device data (contraction strength, endurance, exercise frequency) from manufacturer platforms into the PT's EMR, presented as a clinical trend chart alongside other outcome measures. Second, clinical interpretation: translating device data into clinically meaningful assessments — "patient's pelvic floor contraction strength increased 40% over 4 weeks but endurance remains below functional threshold" — requires PT-specific logic that neither the device manufacturer (consumer health focus) nor the EMR vendor (general PT focus) has built. The ideal integration would show biofeedback trends on the same screen as other outcome measures (PFDI-20 scores, bladder diary data, pain ratings), giving the therapist a unified clinical picture without switching between applications.

## Target Customer
Pelvic floor PT specialists who prescribe home biofeedback devices and want to incorporate the data into their clinical workflow rather than treating it as a separate, disconnected data stream.

## Impact If Solved
Saves 5-10 minutes per follow-up visit currently spent accessing and interpreting biofeedback data from the patient's phone. Enables data-driven treatment plan adjustments based on objective home performance data rather than patient self-report. Provides clinical documentation of home biofeedback progress that supports continued treatment authorization when insurance is involved.
