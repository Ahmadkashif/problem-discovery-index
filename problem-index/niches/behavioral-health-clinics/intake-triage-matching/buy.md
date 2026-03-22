# Clinical Intake-to-Scheduling Automation

**Niche:** [[niches/behavioral-health-clinics/intake-triage-matching/profile|Intake Triage & Patient-Clinician Matching]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic scheduling tools handle appointment booking but know nothing about clinical matching — behavioral health needs intake-to-scheduling that captures clinical information and routes to the right clinician before the patient gives up.
**Tags:** #automation #workflow-orchestration #data-integration #bert #transfer-learning #loss-functions #evaluation-metrics #gradient-boosting

## The Problem
A patient who decides to seek therapy has a 72-hour motivation window — after that, ambivalence wins and they don't follow through. Most multi-clinician practices handle intake via phone call during business hours, meaning evening and weekend inquiries sit until Monday. Even during business hours, the intake coordinator must manually cross-reference the patient's needs against clinician profiles, check availability, and call the patient back — a process that takes 1-3 days. By the time the patient gets a first-session offer, the motivation window has often closed. Practices lose 30-50% of inbound inquiries to this delay.

## What Already Exists
Calendly and Acuity handle self-service appointment booking and are used by solo practitioners. SimplePractice offers a client portal with intake form submission and basic scheduling. Zocdoc handles patient-provider matching for medical appointments. These tools solve scheduling but not the clinical matching step that must happen before scheduling in behavioral health.

## The Customization Gap
Behavioral health intake-to-scheduling requires three layers that generic tools lack. First, a clinical intake form that captures presenting concern, acuity indicators (suicidal ideation screening, substance use, prior hospitalizations), and treatment preferences (modality, therapist characteristics) — not just "what's your insurance and when are you free." Second, matching logic that routes the patient to clinicians based on clinical fit, not just availability — a BERT-based classifier can map free-text presenting concerns to clinician specialty categories. Third, insurance verification before scheduling — confirming the patient's plan is accepted by the matched clinician and checking remaining behavioral health benefits, since many plans have separate behavioral health visit limits. The result is a patient-facing flow where someone submits an intake form at 10pm, gets a matched clinician recommendation by morning, and books their first session — all without a phone call.

## Target Customer
Group practices (5-20 clinicians) currently losing 30-50% of inbound patient inquiries to intake delays, paying $45K-65K/year for a full-time intake coordinator who is overwhelmed during peak inquiry periods (January, September) and underutilized in slower months.

## Impact If Solved
Converts 20-40% more inbound inquiries into scheduled first sessions by eliminating the multi-day intake delay, adding $80K-200K in annual revenue per practice while reducing intake coordinator workload from full-time to 10-15 hours per week of exception handling.
