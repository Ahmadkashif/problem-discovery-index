# HCPCS Billing Module for Standard PM Systems

**Niche:** [[niches/medical-billing/dme-surgical-billing/profile|DME & Surgical Billing]]
**Industry:** [[industries/medical-billing|Medical Billing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard medical billing PM systems are built around CPT codes for physician services — a HCPCS billing module would add DME-specific code sets, rental/purchase logic, CMN tracking, and competitive bidding validation to existing PM workflows.
**Tags:** #decision-trees #feature-engineering #compliance #data-integration #workflow-orchestration #automation

## The Problem
Small DME companies that can't afford Brightree ($500-1,000+/month) often attempt to use standard PM systems (Kareo, AdvancedMD) for DME billing. The result is a constant struggle: (1) HCPCS codes don't map cleanly to CPT-oriented code fields — some PM systems don't support HCPCS Level II codes natively, requiring workarounds. (2) Rental vs. purchase billing logic doesn't exist — there's no field to indicate whether an item is a rental or purchase, no mechanism to track capped rental periods, and no automatic transition from rental to ownership billing. (3) CMN tracking is impossible — the PM has no concept of a Certificate of Medical Necessity, its expiration date, or its relationship to ongoing claims. (4) Competitive bidding pricing can't be enforced — no mechanism to look up whether a product category and service area fall under Medicare's competitive bidding program and apply the correct bid rate. The DME biller manually tracks all of this in spreadsheets alongside the PM system.

## What Already Exists
Brightree and NikoHealth provide full DME billing platforms with HCPCS support, rental tracking, and CMN management. Standard PM systems (Kareo, AdvancedMD, CollaborateMD) handle physician billing with CPT codes, claim submission, and ERA posting. Some clearinghouses (Availity) accept HCPCS claims without specific DME validation.

## The Customization Gap
A DME module that extends a standard PM system with: (1) HCPCS code library with DME-specific fields — product category, rental/purchase flag, CMN requirement type (form number and clinical criteria), and expected rental duration. (2) Rental period engine — calculates capped rental periods per item per payer, tracks current rental month, and automatically adjusts billing codes at ownership transfer (e.g., switches from E1390 rental to maintenance supply billing for oxygen concentrators at month 37). (3) CMN lifecycle fields — stores CMN receipt date, expiration date, physician signer NPI, and renewal status per patient per item, with automated renewal reminders. (4) Competitive bidding lookup — cross-references the patient's ZIP code and product category against CMS competitive bidding zones, applying bid contract pricing when applicable and flagging items that require a bid contract the supplier doesn't hold. This module transforms an existing PM system into a DME-capable billing platform at a fraction of Brightree's cost.

## Target Customer
Small DME companies (25-200 active patients) currently using a standard PM system or clearinghouse portal for billing, unable to justify Brightree's pricing, and manually tracking rental periods and CMN expirations in spreadsheets.

## Impact If Solved
Eliminates the dual-system workflow (PM + spreadsheets) that consumes 10-15 hours/week for a small DME company's billing staff. Prevents CMN-related claim denials by automating expiration tracking — for a company with 150 active patients, missed CMN renewals typically cause 5-10 denials per month at $200-800 per claim. Ensures competitive bidding compliance, avoiding the audit risk and repayment liability of billing non-contract items. Total estimated value: $3,000-8,000/month in prevented denials and recovered staff time.
