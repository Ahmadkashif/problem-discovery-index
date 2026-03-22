# Pelvic Floor Patient Intake and Self-Assessment Platform

**Niche:** [[niches/physical-therapy/pelvic-floor-specialists/profile|Pelvic Floor PT Specialists]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Patients disclose pelvic floor symptoms through a private, sensitive digital intake that uses patient-friendly language — arriving at their evaluation with a severity score and symptom profile already prepared, eliminating the awkward verbal screening that deters patients from seeking care.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #worker-facing #data-integration

## The Problem
Pelvic floor PT patients are uniquely difficult to intake. Many have never told anyone about their symptoms — leaking urine when they laugh, pain during intercourse, inability to use a tampon, fecal urgency. Standard PT intake forms ask about "chief complaint" and "pain location" — they don't ask about pelvic symptoms because they're designed for orthopedic patients. This forces one of two bad outcomes: (1) the patient fills out a generic form and the therapist must verbally screen for pelvic symptoms in person (awkward for both, especially in a waiting room), or (2) the therapist sends a custom PDF questionnaire via email (not HIPAA-secure, clunky to fill out on a phone, and not connected to the EMR). Many patients who would benefit from pelvic floor PT never seek treatment because the intake process doesn't feel safe.

## Why Nobody Has Built This
Pelvic floor PT is a small specialty within an already-niche market (physical therapy). EMR vendors build intake forms for the largest customer segment (orthopedic PT), not for a subspecialty with 4% market share. The sensitivity of the content creates additional product complexity — the language must be carefully crafted to be clinically precise without being clinical-sounding (patients don't know what "dyspareunia" means, but they know "pain during sex"), and the UX must feel private and non-judgmental. Building this well requires collaboration with pelvic floor PT clinicians and patient advocates, not just software engineers. The business case is also challenging: the patient is the user but the PT practice is the payer, and small pelvic floor PT practices have limited software budgets.

## What to Build
A HIPAA-compliant digital intake platform designed specifically for pelvic floor symptoms. The patient receives a link before their appointment and completes a guided self-assessment covering: urinary symptoms (frequency, urgency, leakage triggers, nocturia), bowel symptoms (constipation, urgency, incontinence), sexual function (pain, difficulty, avoidance), pelvic pain patterns (location, triggers, duration), pregnancy and birth history (for postpartum patients), and emotional impact (how symptoms affect daily life, relationships, activity avoidance). Language is patient-friendly with optional clinical terminology tooltips. The output generates: (1) a symptom severity score using validated instruments (PFDI-20, PFIQ-7, PISQ-12), (2) a therapist-facing summary organized by symptom domain with severity flags, and (3) a pre-populated initial evaluation template in the PT's EMR. The platform can also serve as a patient education tool — normalizing pelvic floor dysfunction and explaining what pelvic floor PT involves before the first visit.

## Target Customer
Solo and small-group pelvic floor PT practices that need a professional, sensitive intake workflow to reduce patient barriers to care and streamline pre-evaluation preparation.

## Impact If Built
Reduces patient no-show rates for initial pelvic floor evaluations (currently 25-35%) by making the intake process feel safe and private before the in-person visit. Saves 10-15 minutes per evaluation by providing the therapist with structured symptom data instead of conducting a verbal interview from scratch. Increases referral conversion by providing OB/GYNs and urologists with a patient-friendly intake link they can share alongside referrals.
