# A Gold-Card Ledger Kept by the Practice

**Niche:** [[niches/physician-practices/ordering-practice-prior-authorization/profile|Prior Authorization at the Ordering Practice]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** State gold-card laws exempt clinicians whose requests a payer approves at least 90% of the time, but only the payer computes the rate, and practices cannot check or claim their own status.
**Tags:** #descriptive-statistics #hypothesis-testing #data-integration #compliance #revenue-impact #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor here is fighting to get the ordered service approved before it is due. But scans and procedures are won by first-pass approval on payer and radiology benefit manager criteria, while infused and injected drugs are won by benefits investigation, step-therapy evidence and funding before the first dose. Staff, vendors and win conditions differ. Decomposed into contested sub-niches below.

## The Problem
At least ten states have gold-card laws. Texas now evaluates a year of requests, needs at least five per service, and keeps a 90% approval threshold, yet only ~3% of providers qualified under its 2021 law. Practices cannot tell which of their clinicians are close, which payer evaluations were computed wrongly, or which services would qualify with better first-pass packets.

## Why Nobody Has Built This
Gold-card status is computed by payers from their own records. Practices' authorization histories are scattered across portals, fax logs and EHR worklists, and no vendor sells to the practice on exemption status.

## What to Build
A ledger of every request by clinician, service, payer and outcome, assembled from portal exports, EHR worklists and remittances. It computes each clinician's approval rate against each state's rules (look-back period, minimum count, threshold) and shows the gap to qualification. It flags payer determinations that disagree with the practice's own count and drafts the challenge.

## Target Customer
Specialty groups in gold-card states (Texas, Arkansas, West Virginia, Louisiana, Colorado and others) with high-volume services such as imaging, sleep studies and injections.

## Impact If Built
Each gold-carded clinician-service pair removes its authorization work for the evaluation period. For a busy orthopaedic or cardiology clinician that can save ~3–5 staff hours a week (estimate).
