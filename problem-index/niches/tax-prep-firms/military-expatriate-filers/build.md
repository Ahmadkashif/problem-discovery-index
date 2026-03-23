# Foreign Earned Income Exclusion Eligibility Analyzer

**Niche:** [[niches/tax-prep-firms/military-expatriate-filers/profile|Military & Expatriate Filer Specialists]]
**Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool analyzes a taxpayer's travel history, residency facts, and employment situation to determine FEIE eligibility, optimal test selection (bona fide residence vs. physical presence), and whether the housing exclusion or deduction is more favorable.
**Tags:** #bayesian-network #multiclass-classification #tabular-ml #compliance #automation

## The Problem
The Foreign Earned Income Exclusion (FEIE, Form 2555) allows qualifying expats to exclude up to ~$126,500 (2024) of foreign earned income from US taxation. Eligibility requires meeting either the bona fide residence test (establishing genuine residence in a foreign country) or the physical presence test (330 full days outside the US in a 12-month period). The preparer must analyze the client's travel history, determine which test they meet, identify the optimal 12-month qualifying period (which may differ from the calendar year), and calculate whether the housing exclusion or housing deduction provides a greater benefit. For clients who traveled to multiple countries, had mid-year relocations, or returned to the US for extended visits, this analysis takes 30-60 minutes per return.

## Why Nobody Has Built This
The determination logic involves both objective tests (day-counting for physical presence) and subjective assessments (bona fide residence requires evaluating "intent to return" through factors like lease agreements, bank accounts, social ties, and visa type). Tax software asks the preparer to enter the conclusion but does not help reach it. Building an analyzer requires encoding the subjective factors as a structured assessment with weighted indicators — something between a rule engine and a decision support tool.

## What to Build
An interactive eligibility analyzer that takes the client's travel history (dates and countries for every trip during the qualifying period), employment details (employer location, self-employment status), and residency facts (lease, bank accounts, family location, visa type). The tool determines: (1) which test(s) the client meets; (2) the optimal qualifying period; (3) the exclusion amount; (4) whether the housing exclusion or deduction provides greater benefit; (5) state filing implications based on the client's domicile and SOFA provisions (for military). The output feeds directly into Form 2555 preparation in the tax software.

## Target Customer
Preparers handling 50+ expat or military returns per season who spend 25-50 hours on FEIE eligibility analysis that follows the same decision tree for every client.

## Impact If Built
Reduces per-return FEIE analysis time from 30-60 minutes to under 10 minutes. Prevents eligibility errors that result in IRS challenges to the exclusion (the FEIE is one of the most commonly audited provisions for expats). Enables the preparer to confidently identify the optimal qualifying period and housing calculation, maximizing the client's tax benefit.
