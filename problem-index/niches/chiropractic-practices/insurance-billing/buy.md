# Payer-Specific Documentation Requirements Dashboard

**Niche:** [[niches/chiropractic-practices/insurance-billing/profile|Insurance Billing & Documentation]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payer policy databases exist, but none aggregate and display the specific chiropractic documentation requirements for each payer — visit limits, pre-authorization triggers, required outcome measures, and documentation elements — in a format the DC can reference during patient care.
**Tags:** #data-integration #compliance #automation

## The Problem
Each insurance payer has different requirements for chiropractic coverage: Blue Cross allows 20 visits per year with no pre-authorization; United requires pre-authorization after 12 visits; Aetna requires functional outcome scores (Oswestry, NDI) at every re-evaluation; Medicare requires subluxation documentation with specific exam elements. The DC treats 30 patients per day from 8-12 different payers and must remember which documentation requirements apply to each patient. Front desk staff verify benefits for visit limits but don't know the clinical documentation requirements. The DC documents the same way for every patient and discovers payer-specific deficiencies only when claims are denied.

## What Already Exists
Availity and Waystar provide payer policy lookup and eligibility verification. Practice management systems store payer fee schedules. Chiropractic billing services maintain payer-specific guidelines internally. None presents the documentation requirements to the DC at the point of care — when they're writing the SOAP note and can actually comply with the requirements.

## The Customization Gap
The gap is a point-of-care reference that shows the DC, for this specific patient and this specific payer: visit count (visit 8 of 20 allowed), pre-authorization status (not required until visit 12), required documentation elements (Aetna requires NDI score — not yet recorded), and any payer-specific compliance notes ("this payer requires X-ray findings for subluxation documentation — imaging report must be in the chart"). Displayed as a sidebar in the EHR during documentation, not as a separate system to look up.

## Target Customer
Multi-payer chiropractic practices billing 10+ different insurance companies, with billing staff spending 5-10 hours per week on payer-specific compliance issues.

## Impact If Solved
Reduces payer-specific documentation deficiencies by 50-60%. Prevents pre-authorization failures that result in non-payment for 5-10% of visits. Provides the DC with real-time compliance awareness that currently exists only in the billing manager's head — removing a key bottleneck when the billing manager is absent.
