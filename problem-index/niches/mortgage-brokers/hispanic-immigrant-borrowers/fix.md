# Alternative Credit Documentation Assembly

**Niche:** [[niches/mortgage-brokers/hispanic-immigrant-borrowers/profile|Hispanic & Immigrant Borrower Specialists]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Assembling alternative credit documentation for borrowers with no US credit history — rent receipts, utility bills, insurance payments, phone bills — is a manual, error-prone process that delays ITIN files by 2-3 weeks.
**Tags:** #ocr #named-entity-recognition #nlp #automation #compliance #worker-facing

## The Problem
ITIN borrowers and recent immigrants often have no US credit score, requiring alternative credit verification — typically 3-4 tradelines documented through 12 months of on-time payments for rent, utilities, insurance, or phone service. Processors must contact each service provider (or the borrower's landlord) to obtain verification letters on company letterhead confirming payment history, then organize these into a package that meets the specific wholesale lender's alternative credit requirements. Each lender has different rules: some accept utility bills as self-reported, others require provider verification letters; some accept 3 tradelines, others require 4; some accept phone bills, others don't.

## Why It's Still Broken
Alternative credit is a manual process by nature — it involves calling landlords, requesting letters from utility companies, and collecting physical documents from borrowers who may not have organized records. No lender has digitized the alternative credit verification process because the volume doesn't justify it. The borrower population is often unbanked or underbanked, meaning digital payment records don't exist — the proof of payment is a physical receipt or a cancelled money order.

## What a Fix Looks Like
A structured workflow that guides the processor through each lender's specific alternative credit requirements, generates pre-formatted verification request letters (in English and Spanish) for landlords and service providers, tracks which tradelines have been verified and which are outstanding, and validates the completed package against the target lender's requirements before submission. Includes OCR for processing photos of receipts and money order stubs that borrowers provide via phone.

## Who Feels the Pain
Processors at ITIN-specialist brokerages who spend 4-8 hours per file assembling and verifying alternative credit packages — more time than any other single task in the ITIN origination process.

## Impact If Fixed
Reduces alternative credit assembly time from 4-8 hours to 1-2 hours per file. Eliminates re-work from submitting incomplete alternative credit packages (estimated at 25-30% of initial submissions). Standardizes a process that currently depends entirely on individual processor experience and relationships with local service providers.
