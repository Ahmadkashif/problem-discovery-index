# An Intake Ledger That Re-Checks the Approval Every Time the Exam Changes

**Niche:** [[niches/diagnostic-imaging-centers/order-intake-auth-verification/profile|Referral Order Intake & Authorization Verification]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The approval is verified once at booking; the protocol, date and site change afterwards, and the denial arrives a month later.
**Tags:** #large-language-models #bert #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each faxed or electronic order into a scheduled exam whose authorization matches the exact CPT code, site and date performed, and whoever schedules the highest share of orders with no downstream authorization denial takes the account.

## The Problem
Intake confirms an approval for 72148 (lumbar MRI without contrast) at site A within 60 days. The radiologist protocols with and without contrast, the patient moves to site B, and the exam happens on day 63. Three facts no longer match. Nobody is told, because nothing compares the approval to the exam after booking.

## Why Nobody Has Built This
Authorization tools stop at "status: approved". RIS vendors store the authorization number but not its terms. Matching requires reading approval letters and knowing each benefit manager's rules on CPT variants and amendments.

## What to Build
A per-exam ledger holding the order facts and the approval terms (CPT, units, site, tax ID, window), both extracted from documents and portals. It is re-evaluated on every protocol, schedule or site change. A denial-risk model ranks today's mismatches by dollar value and amendability, routes them to a coordinator with the amendment request drafted, and records the outcome so the rules improve.

## Target Customer
Revenue-cycle leaders at multi-site operators and health-system imaging joint ventures.

## Impact If Built
Preventing most "service does not match authorization" denials at a 150-exam-a-day centre recovers ~$300,000–$500,000 a year of technical fees (estimate). It also stops patients receiving surprise bills for scans they were told were covered.
