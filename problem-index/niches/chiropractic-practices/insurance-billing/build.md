# Real-Time SOAP Note to Billing Code Compliance Engine

**Niche:** [[niches/chiropractic-practices/insurance-billing/profile|Insurance Billing & Documentation]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product analyzes a chiropractor's SOAP note in real-time and verifies that the documented findings, assessments, and treatments support the selected CPT and ICD-10 codes — catching compliance gaps before the claim is submitted.
**Tags:** #llm #text-classification #nlp #compliance #automation

## The Problem
Chiropractors select billing codes (CPT 98940-98943 for spinal manipulation by region count) based on what they did, then write SOAP notes that may or may not adequately document what they did. The disconnect between clinical documentation and billing codes is the #1 cause of claim denials. A DC who adjusted cervical, thoracic, lumbar, and sacral regions bills 98942 (5+ regions) but their SOAP note mentions findings in only cervical and lumbar — the payer denies the claim for insufficient documentation of 5+ regions. The DC didn't do anything wrong clinically; they just didn't document all four regions in the note.

## Why Nobody Has Built This
Chiropractic SOAP notes are written in clinical shorthand with practice-specific abbreviations, non-standard terminology, and varying levels of detail. Analyzing whether a free-text note supports a specific CPT code requires understanding both the code's documentation requirements and the clinical meaning of the note. An LLM-based approach must be fine-tuned on chiropractic documentation patterns and payer-specific requirements — a different compliance standard for Medicare versus Blue Cross versus United.

## What to Build
A real-time documentation compliance engine that runs as the DC completes their SOAP note. As each section is completed, the engine analyzes whether the documented findings support the selected billing codes. Green indicators for compliant documentation, red flags for gaps: "You selected 98942 (5+ regions) but documented findings in only 3 regions — add cervical and sacral findings." Also verifies ICD-10 code support ("M99.01 requires documented segmental dysfunction at the cervical level — add specific subluxation finding"). Runs before claim submission, not after denial.

## Target Customer
Chiropractic practices billing insurance with denial rates above 15%, seeing 100+ insurance patients per week.

## Impact If Built
Reduces claim denial rate from 20% to 5-8% by catching documentation gaps before submission. For a practice submitting 500 claims per month at $75 average reimbursement, reducing denials by 12 percentage points recovers $4,500 per month or $54K per year. Eliminates the rework cycle of denial, appeal, resubmission that consumes 15-20 hours per week of billing staff time.
