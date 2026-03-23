# EHR Billing Module Adapted for Acupuncture Payer Rules

**Niche:** [[niches/acupuncture-practices/insurance-billing-clinics/profile|Insurance-Billing Acupuncture Clinics]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General EHR platforms handle acupuncture scheduling but their billing modules lack payer-specific acupuncture logic.
**Tags:** #llm #text-classification #nlp #compliance #data-integration

## The Problem
Clinics purchase EHR systems like Jane App, Unified Practice, or DrChrono that technically support acupuncture workflows. However, the billing modules treat acupuncture codes identically to any other CPT code — no payer-specific validation, no visit-limit tracking, no state-mandate awareness. Billers must manually cross-reference payer portals and policy documents before every submission batch.

## What Already Exists
Jane App and Unified Practice are purpose-built for acupuncture and offer SOAP note templates and scheduling. Larger platforms like DrChrono and AdvancedMD have broader billing engines with clearinghouse integrations. None of them embed acupuncture-specific payer rules, state mandate lookups, or visit-limit counters into the claim creation workflow.

## The Customization Gap
The billing module needs an acupuncture overlay: a rules engine that knows which payers cover which acupuncture codes in which states, what documentation language is required in SOAP notes to support medical necessity, and how many visits a patient has remaining under their plan. This overlay would turn generic "submit claim" into "submit validated acupuncture claim with auto-attached documentation."

## Target Customer
Clinic owners already paying $200-400/month for EHR who would pay an additional $100-200/month for a billing intelligence add-on.

## Impact If Solved
Reduces biller time per claim from 12-15 minutes to 3-5 minutes, and cuts denial-related rework by 60-70%.
