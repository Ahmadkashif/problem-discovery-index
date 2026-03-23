# Seasonal Staff Onboarding and Knowledge Transfer

**Niche:** [[niches/accounting-firms-smb/seasonal-tax-prep/profile|Seasonal Tax Preparation Practices]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every January, firms spend 2-3 weeks getting seasonal preparers up to speed on client-specific procedures that were documented nowhere.
**Tags:** #llm #text-generation #nlp #worker-facing #tacit-knowledge-ml

## The Problem
Tax-focused firms hire 2-5 seasonal preparers each January to handle volume. These preparers need to learn the firm's review procedures, software configuration, client-specific quirks (the Smith family always forgets to report their crypto trades; the Johnson LLC has a complex multi-state allocation), and current-year tax law changes. Partners and senior staff spend 40-80 hours in January on training and supervision that could be spent on billable work. When a seasonal preparer encounters an unfamiliar situation, they either interrupt a senior person or make an error that the reviewer catches later — both wasteful.

## Why It's Still Broken
Client-specific knowledge lives in the heads of the partners and senior accountants who have prepared those returns for years. Prior-year workpapers contain some of this information, but the context ("why we took this position" or "watch out for this recurring issue") is not captured systematically. Firms lack the time during tax season to document procedures, and outside of tax season there is no urgency. Practice management tools track tasks but not the reasoning behind them.

## What a Fix Looks Like
A structured knowledge capture process that runs during the slower months (May-December): partners and senior staff record client-specific notes, review points, and common issues in a searchable, client-linked knowledge base. When a seasonal preparer opens a return, they see a briefing page with key preparation notes, prior-year reviewer comments, and flagged items from the last 3 years. An LLM-assisted layer can generate first drafts of these briefings from prior-year workpapers and resolution notes.

## Who Feels the Pain
Seasonal tax preparers who feel lost and unsupported, and senior staff who are pulled away from their own returns to answer questions.

## Impact If Fixed
Cuts seasonal onboarding time from 2-3 weeks to 3-5 days and reduces reviewer corrections by 20-30%, recovering 100-200 billable hours per firm during peak season.
