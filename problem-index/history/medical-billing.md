# History: Medical Billing

**Industry:** [[industries/medical-billing|Medical Billing]]
**Primary Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** [[origins/hospital-systems/profile|Hospital Systems]]
**Episode Tier:** 1
**Transferable Pattern:** When reimbursement is fixed to a code rather than to the cost actually incurred, the code becomes the entire margin lever — and whoever aggregates the transmission layer between the coder and the payer becomes a single point of failure for an industry that never noticed how far it had consolidated beneath it.

## Before

A patient encounter produced a paper superbill: diagnosis and procedure written in a physician's hand or a coder's shorthand, walked or mailed to a billing clerk, translated into a claim form, mailed to an insurer or to Medicare, and reimbursed — if at all — against whatever the payer decided the actual cost of care had been. Hospitals were paid, in essence, for what they said they had spent. There was no shared code that fixed a price in advance, and there was no electronic path between the clinician who wrote the note and the payer who read it.

## The Origin Event — two federal actions, eighteen years apart, neither a computer

**1983: Medicare adopts the Prospective Payment System.** Robert Fetter and John Thompson at Yale had developed Diagnosis-Related Groups in the early 1970s as a way to classify hospital cases into comparable "products" rather than an undifferentiated stream of costs. New Jersey piloted DRG-based payment from 1980. Congress adopted DRGs nationally for Medicare inpatient reimbursement in 1983, via an amendment folded into the Tax Equity and Fiscal Responsibility Act, replacing cost-based reimbursement with a predetermined rate keyed to the patient's diagnosis rather than to what the hospital actually spent treating them.

This is the moment billing stopped being a record of expenditure and became **a pricing mechanism keyed to a code**. It is arguably the single most consequential fact in this industry's history, and it happened thirteen years before HIPAA and has nothing to do with electronic claims at all — it is a reimbursement-policy decision that made the *content* of a code, for the first time, directly determine a hospital's revenue.

**1996–2000: HIPAA makes the code machine-readable and the claim electronic.** HIPAA's Administrative Simplification title, and the standards issued under it through the following decade, fixed the vocabulary and the wire format: standard code sets (CPT for procedures, ICD for diagnoses, and — confirmed in this vault's prior research — **CDT named a mandatory HIPAA standard code set for dental procedures on 17 August 2000**), and the **837 transaction set** as the standard electronic claim, submitted in the ASC X12 format. A further mandated upgrade, **X12 005010**, was required from 1 January 2012 (enforcement deferred to 31 March 2012) specifically to carry the longer, more granular ICD-10 codes that were still years from mandatory use. The **National Provider Identifier** — one number per provider, replacing a scattering of payer-specific identifiers — became mandatory for HIPAA-covered entities on **23 May 2007**, with a further enforcement grace period into 2008 for smaller plans.

Neither 1983 nor 1996–2007 is a founding moment in the SABRE or ERMA sense. There is no single date this industry can point to and say "that is when it began." What exists instead is a slow tightening of the same screw: **the code determines the payment (1983), the code must be standard (1996–2000), and the code must travel electronically in a single, auditable, machine-parseable format (2000s)**. By the time all three were in place, medical billing had become, structurally, a business about getting a specific string of characters exactly right.

## What Became Cheap

**Transmitting a claim.** Electronic claims through the 837 standard, routed via a clearinghouse, turn around in days rather than the weeks a mailed paper claim took. That is a genuine and large efficiency gain, and it is close to the entire list of what actually got cheaper.

**What did not become cheap — and this is the industry's whole business — is getting the claim accepted.** This vault's own hub note states the operating reality plainly: the average first-pass claim denial rate runs 5–10%, and every denial requires a human to determine root cause — eligibility, a coding error, a missing authorisation, timely filing — then rework and resubmit. Digitisation moved the *paper* faster. It did not reduce the *complexity* the paper was encoding; per [[origins/hospital-systems/legacy|hospital systems' own legacy file]], "digitisation did not simplify the CPT/ICD layer; it made the complexity machine-readable, which is not the same thing as making it simple." Medical billing as an industry exists in the gap between those two sentences.

## How It Was Actually Solved — the Clearinghouse Layer, and Its Single Point of Failure

Between the provider's billing system and the dozens of payers it must satisfy sits the **clearinghouse**: it takes a claim in whatever format a practice-management system produces, validates it, translates it into the correct 837 structure for the destination payer, and routes it. This layer exists because no small billing operation can maintain direct, correctly formatted connections to every payer in the country — it is the same aggregation logic that produced core-banking vendors for credit unions and clearinghouses for card payments elsewhere in this vault, arrived at independently.

That aggregation produced exactly the concentration risk this vault has already documented once, in [[origins/credit-bureaus/legacy|credit bureaus]]: a shared, computed layer that every competitor depends on becomes a single point of catastrophic failure. **Change Healthcare** — by the 2020s one of the largest claims-clearinghouse and payment-processing operations in US healthcare — was acquired by UnitedHealth Group's Optum unit in a deal that closed 3 October 2022 for a reported $13B. **On 21 February 2024, Change Healthcare disclosed a ransomware attack**, attributed to the group calling itself ALPHV/BlackCat, which had gained initial access on 12 February and exfiltrated data before deploying ransomware nine days later. The disruption stopped electronic claims and payment processing across a large share of the US healthcare system: reporting put the number of affected patients near 190 million, and providers reported losses running up to $100M a day while the clearinghouse was down. By 16 April 2024, UnitedHealth Group had advanced over $6B in emergency payments to affected providers just to keep them solvent through the outage.

**This is not a competitive graveyard — nobody out-computed Change Healthcare.** It is the same shape of finding [[origins/credit-bureaus/legacy|credit bureaus' legacy file]] reaches about Equifax's 2017 breach: an industry that consolidated its shared computing layer down to a small number of providers discovers, when one of them fails, that the failure is now systemic rather than local. Medical billing had already lived this once at smaller scale, quietly, in every billing company that has ever had a single clearinghouse connection go down for a day. February 2024 was the moment it happened to the entire country's claims pipeline at once.

## The Binding Constraint

DRG-based reimbursement is fixed to the code, not to the actual cost of the case, and it has never stopped being fixed that way. That single design choice from 1983 is why coding accuracy is the entire margin lever this vault's hub note describes, and why "upcoding" and "DRG creep" have been a recognised, litigated category of Medicare fraud enforcement since shortly after PPS took effect. No software makes the reimbursement rate for a given DRG larger. The only thing software can do is ensure the *correct* code is the one submitted — which is precisely why denial prevention, not denial appeal, is this vault's own high-impact note for the industry, and precisely why it is a prediction problem the industry has mostly built reactive, after-the-fact tooling for instead.

## What's Still Open

- [[problems/medical-billing/high-impact|🔴 Predictive Denial Prevention Engine]] — catching the DRG-era coding error before submission, not after
- [[problems/medical-billing/worker-life-1|🟢 AR Follow-Up Call Burden]]
- [[niches/medical-billing/denial-management-analytics-vendors/profile|Denial Management Analytics Vendors]]
- [[niches/medical-billing/denial-management-appeals/profile|Denial Management & Appeals]]
- [[niches/medical-billing/healthcare-clearinghouses/profile|Healthcare Clearinghouses]] — the layer Change Healthcare's outage exposed
- [[niches/medical-billing/payer-claims-adjudication/profile|Payer Claims Adjudication]]
- [[niches/medical-billing/payment-posting-reconciliation/profile|Payment Posting & Reconciliation]]
- [[niches/medical-billing/cms-program-integrity/profile|CMS Program Integrity]] — the enforcement side of DRG creep
- [[niches/medical-billing/rcm-platform-analytics/profile|RCM Platform Analytics]]

## The Transferable Pattern

> **Find the year the payment stopped tracking the cost and started tracking a code instead. From that year forward, the code is the product, accuracy in the code is the margin, and every business in the industry is, whether it says so or not, in the business of getting the code right before someone downstream gets to decide it was wrong.**

An FDE evaluating any RCM or claims business should ask, before anything else, whether the tooling in front of them intervenes *before* the code is submitted or only *after* it comes back denied. This industry, thirty years into HIPAA and forty into PPS, still runs mostly on the second kind — which is exactly what this vault's own analysis of the opportunity says, arrived at independently of the history that put it there.

**Sources:** Wikipedia, *Prospective payment system*, *Diagnosis-related group*, *Health Insurance Portability and Accountability Act*, *National Provider Identifier*, *ICD-10*, *Change Healthcare*; CMS, EHR/claims standard rules (ASC X12 005010, effective 1 Jan 2012, enforcement to 31 Mar 2012); ADA/CMS, CDT as mandatory HIPAA code set (17 Aug 2000, per this vault's prior research); UnitedHealth Group and Optum press materials, Change Healthcare acquisition (closed 3 Oct 2022) and February 2024 ransomware incident disclosures; contemporaneous reporting on the Change Healthcare attack's scale and UnitedHealth's advance-payment programme; this vault's `industries/medical-billing.md` and `origins/hospital-systems/legacy.md`.
