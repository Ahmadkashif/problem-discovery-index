# Claim Scrubbing Tool with Acupuncture Rule Sets

**Niche:** [[niches/acupuncture-practices/insurance-claims-automation/profile|Insurance Eligibility & Claims Processing]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General claim scrubbing tools catch standard coding errors but miss acupuncture-specific denial triggers like modifier requirements, visit-cap violations, and state-mandate exclusions.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #compliance #automation

## The Problem
Claim scrubbing tools run claims through coding edits before submission — checking for invalid code combinations, missing modifiers, and documentation gaps. However, their rule sets are optimized for high-volume specialties (primary care, orthopedics, cardiology). Acupuncture's narrow CPT code range (97810-97814 plus a few ancillary codes) has payer-specific rules that generic scrubbers don't encode: "Aetna requires modifier -59 on 97813 when billed with 97140," or "UHC denies 97814 after visit 20 regardless of medical necessity."

## What Already Exists
ClaimMD, Claim.MD, and Optum's claim scrubbing services check standard CCI edits and NCCI rules. Clearinghouses like Office Ally and Trizetto include basic scrubbing. These catch universal errors (missing NPI, invalid date formats) but not payer-specific acupuncture rules, which account for 60-70% of acupuncture claim denials.

## The Customization Gap
The scrubbing engine needs an acupuncture overlay: a rule set of 500-1,000 payer-specific acupuncture billing rules covering allowed CPT/ICD-10 pairings, modifier requirements, visit limits, frequency limits (e.g., "no more than 2 units of 97810 per visit for Anthem"), and state mandate applicability. This rule set would update quarterly as payer policies change, sourced from denial pattern analysis across a network of acupuncture practices.

## Target Customer
Acupuncture billing services managing 5+ practices, and larger clinics billing 200+ claims/month with denial rates above 12%.

## Impact If Solved
Reduces claim denial rates from 15-25% to 5-8%, recovering $2,000-6,000/month per mid-size practice and reducing biller rework time by 40-50%.
