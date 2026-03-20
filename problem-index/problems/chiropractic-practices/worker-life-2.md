# SOAP Note Documentation Burden

**Industry:** [[chiropractic-practices|Chiropractic Practices]]
**Type:** Worker Life Changing
**One-liner:** Chiropractors stop spending 2-3 hours every evening writing SOAP notes for the 20-30 patients they saw that day — because an ambient listening system generates compliant documentation from the clinical encounter in real time.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #loss-functions #entropy-cross-entropy-kl-divergence #evaluation-metrics #worker-facing

## The Problem
Every chiropractic visit requires a SOAP note documenting Subjective complaints, Objective findings (postural assessment, range of motion, orthopedic tests, palpation findings, subluxation levels), Assessment (clinical impression and response to care), and Plan (treatment rendered, home instructions, next visit). A thorough SOAP note takes 3-5 minutes to write per patient. With 20-30 patients per day, documentation consumes 1-2.5 hours of clinical time or — more commonly — is completed after hours at home. Most DCs use templated notes in their EHR (ChiroTouch, Jane App), but templates create compliance risk: identical-looking notes across visits suggest insufficient examination, triggering insurance audits. The documentation must be visit-specific with unique objective findings to withstand audit scrutiny, yet the workflow pressure of a patient every 10-15 minutes leaves no time for detailed writing between patients.

## Why It Matters to the Worker
Documentation burden is the primary driver of chiropractor dissatisfaction and burnout. DCs entered the profession to help patients through hands-on care, not to spend their evenings typing notes. The after-hours documentation creates a second unpaid workday that erodes work-life balance, family time, and mental health. DCs who cut corners on documentation face audit risk — insurance companies retrospectively review notes and claw back payments for visits with insufficient documentation. The choice between thorough documentation (2-3 hours of unpaid evening work) and adequate documentation (audit risk) is a daily stressor that compounds over years.

## What a Solution Looks Like
An ambient clinical documentation system (similar to Nuance DAX or Abridge, but customized for chiropractic workflows) that listens to the clinical encounter and generates a compliant SOAP note. The system recognizes chiropractic-specific terminology (subluxation levels, technique names, adjustment descriptions), auto-populates objective findings from the DC's verbal examination narrative, generates visit-specific language that varies naturally between visits, and formats output for the DC's specific EHR system. The DC reviews and signs each note in under 30 seconds rather than writing it from scratch.

## Impact If Solved
Eliminates 1.5-2.5 hours of daily after-hours documentation work, reclaiming 7-12 hours per week of personal time. Improves documentation quality and compliance by generating audit-resistant, visit-specific notes. Reduces documentation-related insurance audit clawbacks by ensuring every note meets carrier documentation standards. Enables the DC to be fully present with patients during visits instead of mentally composing notes.
