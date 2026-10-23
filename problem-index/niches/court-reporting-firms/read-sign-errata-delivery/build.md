# Errata as a Quality Signal

**Niche:** [[niches/court-reporting-firms/read-sign-errata-delivery/profile|Read-and-Sign, Errata & Certified Delivery]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Errata sheets are the only routine outside check on a reporter's accuracy, and firms attach them to the transcript and never read them as data.
**Tags:** #bert #transformers #logistic-regression #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to close every transcript's review window (signature, errata, certification and delivery to every party) on the jurisdiction's clock without a staff member chasing it, and whoever closes the most transcripts on time with a complete certification record takes the account.

## The Problem
Witnesses who read their transcripts list corrections. Some fix the reporter's errors: a misheard name, a dropped "not". Others change testimony. Firms file both kinds alike, so they cannot say which reporters, case types or audio conditions produce corrections, and counsel learns of substantive changes only by reading every sheet.

## Why Nobody Has Built This
Errata arrive as scans in varied formats, volumes per firm seemed small, and nobody owned quality measurement in an industry that sells certification rather than accuracy statistics.

## What to Build
Extract each errata line, align it to the transcript passage, classify it as reporter correction, clarification or substantive change, and check the audio where the witness claims the reporter misheard. Feed reporter corrections into a per-reporter quality record she controls. Flag substantive changes to every party at the same moment, so the firm stays neutral.

## Target Customer
Agencies managing thousands of read-and-sign transcripts a year; reporters who want evidence of their accuracy.

## Impact If Built
A measured correction rate per reporter and condition for the first time, and substantive testimony changes surfaced at once rather than at trial.
