# Global Period Tracking for Surgical Specialties

**Niche:** [[niches/medical-billing/single-specialty-billing/profile|Single-Specialty Billing]]
**Industry:** [[industries/medical-billing|Medical Billing]]
**Type:** Fix (Pain Point)
**One-liner:** Surgical specialties (orthopedics, general surgery, urology, gynecology) have global surgery periods of 0, 10, or 90 days where follow-up visits are included in the original procedure payment — billing an E/M visit during a global period without the correct modifier results in automatic denial or recoupment.
**Tags:** #decision-trees #feature-engineering #compliance #automation #revenue-impact

## The Problem
When a surgeon performs a procedure with a 90-day global period (e.g., CPT 27447 total knee arthroplasty), all routine follow-up visits for the next 90 days are considered part of the original procedure's payment. If the billing operation submits an E/M code (99213, 99214) for a follow-up visit during the global period without modifier 24 (unrelated E/M service) or modifier 58 (staged/related procedure), the claim will be denied or — worse — paid and later recouped during an audit. The complexity multiplies: different procedures have different global periods (0, 10, or 90 days), the global period start date varies based on date of surgery, some payers calculate global periods differently from Medicare, and when a patient has multiple surgeries with overlapping global periods, tracking which visits are covered by which global period becomes nearly impossible manually. A single-specialty orthopedic billing operation may have 200-400 active global periods running at any time across their patient population.

## Why It's Still Broken
PM systems store procedure dates but don't calculate or display global periods. There is no field showing "this patient is currently in a 90-day global period for procedure X performed on date Y." The billing staff must manually check: (1) Was a surgical procedure performed recently? (2) What is its global period? (3) Is today within the global period? (4) Is the current visit related or unrelated to the surgery? This check takes 3-5 minutes per claim and is often skipped under time pressure. CMS publishes global surgery period indicators in the Medicare Physician Fee Schedule, but this data is not integrated into PM workflows. The result is a steady stream of global period violations — claims denied for unbundling (billing separately for included follow-up) or claims underbilled (legitimate unrelated visits not billed because the biller assumed it was a global period visit).

## What a Fix Looks Like
A global period tracking overlay that integrates with the PM system and provides: (1) Active global period dashboard — for each patient, shows all active global periods with procedure, start date, end date, and remaining days. (2) Claim-time validation — when an E/M code is entered for a patient with an active global period, the system alerts the biller: "This patient is on day 23 of a 90-day global period for CPT 27447 (TKA) performed on [date]. Is this visit related to the surgery? If unrelated, modifier 24 is required. If a staged procedure, modifier 58 is required." (3) Payer-specific period adjustments — tracks payers whose global period rules differ from Medicare (some commercial payers don't recognize global periods at all). (4) Overlapping period resolution — when multiple global periods overlap, identifies which period each visit falls under.

## Who Feels the Pain
The surgical billing specialist who must manually track hundreds of active global periods across patients and payers, and the billing company owner who faces audit liability when global period violations are paid and later recouped by Medicare.

## Impact If Fixed
Eliminates global period-related denials (estimated 5-8% of surgical claim denials) and reduces audit recoupment risk. For an orthopedic billing operation processing 3,000 surgical claims/month, preventing global period errors on 5% of claims avoids 150 denials/month and the associated rework. More critically, it prevents Medicare audit recoupments that can reach $50,000-200,000 for systematic global period billing errors. The biller saves 3-5 minutes per surgical claim on manual global period lookup, recovering 150-250 hours/month.
