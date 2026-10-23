# Approved, Then Denied Because the Date or Code Moved

**Niche:** [[niches/physician-practices/ordering-practice-prior-authorization/profile|Prior Authorization at the Ordering Practice]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** An authorization covers a specific code, unit count and date window; when the service is rescheduled or the radiologist adds contrast, the claim denies for no authorization even though one was obtained.
**Tags:** #data-integration #descriptive-statistics #workflow-orchestration #revenue-impact #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor here is fighting to get the ordered service approved before it is due. But scans and procedures are won by first-pass approval on payer and radiology benefit manager criteria, while infused and injected drugs are won by benefits investigation, step-therapy evidence and funding before the first dose. Staff, vendors and win conditions differ. Decomposed into contested sub-niches below.

## The Problem
The MRI was approved for 70551 within 60 days. The patient rescheduled to day 64, or the radiologist performed 70553 with contrast. The procedure was approved for one level and the surgeon treated two. The claim denies, and appeals on technical authorization denials rarely succeed.

## Why It's Still Broken
The authorization number lives in a worklist or a note field. The schedule, the performed code and the claim sit in three systems that do not compare against the authorization's terms. Staff who obtained the approval have moved on to the next forty requests.

## What a Fix Looks Like
Each authorization becomes a structured record (codes, units, dates, site, rendering clinician) linked to the scheduled appointment. Rescheduling outside the window or a code change at the point of service triggers an alert and an update request to the payer before the claim drops.

## Who Feels the Pain
Authorization coordinators; billing staff working technical denials; practices writing off procedures that were approved.

## Impact If Fixed
Catching date and code mismatches before billing could recover ~1%–2% of procedure revenue now written off to technical denials (estimate).
