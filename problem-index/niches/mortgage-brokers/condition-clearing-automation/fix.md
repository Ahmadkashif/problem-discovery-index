# Borrower Document Chase Loop

**Niche:** [[niches/mortgage-brokers/condition-clearing-automation/profile|Condition Clearing & File Processing]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Processors spend 30-40% of their time chasing borrowers for documents — sending requests, following up, receiving the wrong document, explaining what's actually needed, and repeating the cycle.
**Tags:** #llm #text-generation #nlp #automation #worker-facing

## The Problem
When a condition requires a document the borrower hasn't provided, the processor sends a request — typically via email, text, or the borrower portal. But borrowers are not mortgage professionals: they don't know what a "VOE" is, they send the wrong pay stub (monthly instead of bi-weekly), they submit bank statements with redacted account numbers, they provide last year's tax return instead of this year's. The processor then has to explain what's wrong, what they actually need, and wait for the corrected document. This back-and-forth loop happens 3-5 times per file and is the primary cause of closing delays.

## Why It's Still Broken
Document requests from processors are often written in mortgage jargon that borrowers don't understand. Existing borrower portals send automated requests based on document type checklists, but they can't explain why a specific document was rejected or what specifically needs to be different in the resubmission. The communication is one-directional (processor to borrower) rather than guided — the borrower has no way to ask "is this the right document?" before uploading and waiting for feedback.

## What a Fix Looks Like
A borrower-facing communication layer that translates condition requirements into plain language, shows visual examples of what the correct document looks like (e.g., "Your pay stub should show these fields highlighted"), performs real-time document validation on upload (checking date ranges, required fields, image quality), and provides instant feedback — "This pay stub is from January, but we need one from the last 30 days" — before the processor ever sees it. Reduces the chase loop from 3-5 rounds to 0-1 rounds.

## Who Feels the Pain
Processors who report that borrower document chasing is the most frustrating part of their job — it's unpredictable, time-consuming, and out of their control. Also borrowers, who experience the repeated requests as incompetence or bureaucratic hassle.

## Impact If Fixed
Reduces document chase cycles from an average of 3-5 rounds to 0-1 by catching errors at upload. Saves processors 1-2 hours per file in communication overhead. Shortens average close time by 3-5 days by eliminating the back-and-forth delay. Improves borrower satisfaction — the #1 complaint in mortgage surveys is "too many document requests."
