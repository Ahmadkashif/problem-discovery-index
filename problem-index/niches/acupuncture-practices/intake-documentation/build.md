# AI-Powered Acupuncture SOAP Note Generator

**Niche:** [[niches/acupuncture-practices/intake-documentation/profile|Patient Intake & Treatment Documentation]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool auto-generates complete acupuncture SOAP notes from minimal clinical inputs — combining TCM diagnostic patterns, point selections, and payer-compliant documentation language.
**Tags:** #llm #text-generation #nlp #tacit-knowledge-ml #automation #worker-facing

## The Problem
An acupuncturist treating a patient with migraine headaches needs to document: subjective complaint, TCM tongue/pulse findings, TCM pattern diagnosis (e.g., "Liver Yang Rising"), point selection with rationale, treatment performed, and patient response. This note must satisfy both clinical continuity needs and insurance documentation requirements. Writing it takes 8-12 minutes per patient. For a practitioner seeing 15-20 patients daily, documentation consumes 2-4 hours — often after clinic hours, unpaid.

## Why Nobody Has Built This
Medical AI scribes (Nuance DAX, Abridge) are trained on Western medical terminology and documentation patterns. TCM clinical language — tongue body colors, pulse quality descriptors (wiry, slippery, choppy), pattern diagnoses, point names in pinyin and alphanumeric notation — is absent from their training data. Building an acupuncture-specific scribe requires TCM clinical corpus data that doesn't exist in structured, labeled form. The practitioner's pattern-to-treatment reasoning represents tacit knowledge that varies by training lineage and is difficult to formalize.

## What to Build
An AI note generator that takes minimal structured inputs — chief complaint (selected or spoken), tongue/pulse findings (quick-select or photo), points needled (tapped on body map), and treatment modalities used — and generates a complete SOAP note with: TCM pattern diagnosis, treatment rationale, medical necessity language for insurance, and outcome documentation. The system learns from the practitioner's note history to match their clinical reasoning style and documentation preferences.

## Target Customer
Acupuncturists seeing 12+ patients/day who spend more than 90 minutes daily on documentation.

## Impact If Built
Reduces documentation time from 8-12 minutes to 2-3 minutes per patient, reclaiming 1.5-3 hours daily. Eliminates after-hours documentation work and improves note quality for insurance compliance.
