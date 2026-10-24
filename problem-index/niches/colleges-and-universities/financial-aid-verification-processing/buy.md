# Mortgage Income Verification Rebuilt for FAFSA

**Niche:** [[niches/colleges-and-universities/financial-aid-verification-processing/profile|Financial Aid Verification, ISIR & Packaging Operations]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** [[industries/mortgage-lenders|Mortgage Lenders]] already extract and verify income from tax returns, W-2s and pay stubs at scale; aid offices do the same work against different rules.
**Tags:** #large-language-models #cnns #transformers #compliance #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to take each student's ISIR to a final, disbursable aid offer, and whoever certifies the most files with no later correction or programme-review finding takes the account.

## The Problem
Verification is document classification, field extraction and comparison against a reference record, done by hand in most aid offices.

## What Already Exists
Mortgage document AI (Ocrolus, and the income calculators built into loan origination systems) classifies borrower documents, extracts income fields, detects tampering and reconciles against application data.

## The Customization Gap
The aid version needs: the federal verification tracking groups and the items each requires; comparison with ISIR fields and the FAFSA's direct data exchange with the IRS rather than an application form; tolerances and correction rules from the Federal Student Aid Handbook; household and parent definitions for dependent and independent students, including divorced and separated parents; special circumstances that trigger professional judgment rather than correction; and each year's rule changes, including the July 2026 loan and Pell provisions.

## Target Customer
Aid offices with high verification volumes, and aid system vendors wanting an extraction layer.

## Impact If Solved
Document reading drops from minutes per file to a review. At ~15 minutes a file across 5,000 verification files, that is ~1,250 counsellor hours a year (estimate).
