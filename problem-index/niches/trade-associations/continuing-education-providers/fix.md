# Course-to-Board Approval Mapping Drift

**Niche:** [[niches/trade-associations/continuing-education-providers/profile|Continuing Education Providers]]
**Industry:** [[industries/trade-associations|Trade Associations]]
**Type:** Fix (Pain Point)
**One-liner:** CE administrators discover that a course's state board approval lapsed 3 months ago only when a learner complains that their board rejected the certificate — by then, dozens of learners have been issued invalid credits.
**Tags:** #compliance #automation #data-integration #worker-facing

## The Problem
State board approvals expire on different schedules (1-year, 2-year, 3-year, or session-based). An association with 40 courses approved across 20 boards has 800 approval records with different expiration dates. When an approval lapses, the LMS continues to offer the course and issue certificates because the LMS has no concept of board-level approval status — it only knows whether the course is "active." Learners complete the course, receive a certificate with the expired approval number, submit it to their board, and discover it's invalid. The association must then issue corrected certificates, potentially re-apply for approval, and manage angry learners who now have a CE deficit with a licensing deadline approaching.

## Why It's Still Broken
CE approval status is tracked in a spreadsheet maintained by the CE administrator. The LMS has no field for "approved by Board X until Date Y." When the administrator goes on vacation, leaves the organization, or simply misses a renewal in a spreadsheet with 800 rows, invalid certificates get issued. There is no automated check between "course offered for credit" and "course currently approved for credit by this specific board." The failure mode is invisible until a learner or board auditor discovers it.

## What a Fix Looks Like
A compliance integration layer between the approval tracking system and the LMS that: automatically disables credit issuance for a specific board when that board's approval expires, alerts the CE administrator 90 days before any approval expiration, prevents certificate generation with expired approval numbers, and — when an approval lapses unexpectedly — identifies all learners who received certificates during the lapsed period for proactive outreach. The system treats approval status as a real-time constraint on credit issuance, not a static spreadsheet entry.

## Who Feels the Pain
CE administrators who receive panicked calls from learners whose board rejected their certificate, then spend 5-10 hours per incident investigating the approval lapse, issuing corrected certificates, and filing emergency renewal applications.

## Impact If Fixed
Eliminates the 5-15 invalid certificate incidents per year that damage the association's reputation with both learners and boards, saves 50-150 hours of annual incident response time, and protects the association's CE provider approval status (repeat violations can result in provider de-approval).
