# No Record Means Back to Paystubs

**Niche:** [[niches/credit-bureaus/employment-income-verification/profile|Employment & Income Verification]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** When the database has no record, the applicant uploads photos of paystubs and a processor reads them, and the two answers arrive in formats nobody reconciles.
**Tags:** #large-language-models #transformers #evaluation-metrics #feature-engineering #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to hold a current, employer-sourced record on the applicant at the moment a lender, landlord or benefits agency asks, and whoever answers the most applicants instantly without a paystub upload takes the account.

## The Problem
A no-hit sends the applicant to the fallback: upload paystubs, W-2s or bank statements, or authorise an employer call. Processors read the documents, compute income by hand and key it into the loan or eligibility system, where it sits in a different shape from a database verification. Gig and self-employed income needs bank deposits and 1099s, and each processor calculates it slightly differently.

## Why It's Still Broken
Verification vendors sell the hit; the miss is the buyer's problem, handled by staff and generic document tools.

## What a Fix Looks Like
Return the fallback in the same structure as a hit: document and bank-deposit extraction with the consumer's permission, income and hours computed under the buyer's rules, confidence and source attached, and the result marked clearly as document-derived.

## Who Feels the Pain
Applicants with irregular income, who are asked for the most paperwork; loan processors and eligibility workers reconciling two kinds of answers.

## Impact If Fixed
A no-hit becomes a slower hit rather than a manual file, and the applicants hardest to verify stop being the ones verified least consistently.
