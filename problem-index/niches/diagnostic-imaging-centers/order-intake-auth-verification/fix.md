# The Faxed Order Typed In Twice

**Niche:** [[niches/diagnostic-imaging-centers/order-intake-auth-verification/profile|Referral Order Intake & Authorization Verification]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Fix (Pain Point)
**One-liner:** An intake coordinator re-keys every faxed order into the RIS, then again into the payer portal, and the errors become wrong-patient or wrong-exam problems later.
**Tags:** #large-language-models #bert #automation #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn each faxed or electronic order into a scheduled exam whose authorization matches the exact CPT code, site and date performed, and whoever schedules the highest share of orders with no downstream authorization denial takes the account.

## The Problem
Orders arrive as faxes with handwriting, stamps and attached notes. Coordinators type demographics, CPT, ICD-10, laterality and the ordering physician's NPI into the RIS, then re-enter much of it in the portal. A transposed digit or a "left" read as "right" travels with the exam.

## Why It's Still Broken
Referring practices send faxes because it always works. Centres have bought fax servers but not extraction, and RIS intake screens expect typing.

## What a Fix Looks Like
Document extraction that reads each fax into a pending RIS order with confidence scores per field. The coordinator confirms flagged fields only, and the confirmed facts pre-fill the portal check.

## Who Feels the Pain
Intake coordinators handling hundreds of faxes a day; technologists who discover the laterality error with the patient on the table.

## Impact If Fixed
Cutting re-keying from a few minutes to under a minute per order saves one to two coordinator FTEs per 200 orders a day (estimate), and removes a class of laterality and wrong-exam errors.
