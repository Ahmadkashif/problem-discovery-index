# ISIR to Award Without the Document Chase

**Niche:** [[niches/colleges-and-universities/financial-aid-verification-processing/profile|Financial Aid Verification, ISIR & Packaging Operations]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most of an aid file's delay is waiting for and reading documents a model could request, read and reconcile against the ISIR the day they arrive.
**Tags:** #ai-agent #large-language-models #transformers #compliance #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to take each student's ISIR to a final, disbursable aid offer, and whoever certifies the most files with no later correction or programme-review finding takes the account.

## The Problem
A file selected for verification sits until the family uploads the right documents, a counsellor reads them, compares them with the ISIR, submits corrections and waits for a reprocessed record. Each step waits on a person, and families often send the wrong document first. Offers go out late, and families decide elsewhere.

## Why Nobody Has Built This
Aid systems were built to calculate and disburse, not to read documents. Document-collection tools gather files but leave the reading to staff. Offices worry about automation errors that become programme-review findings.

## What to Build
An agent inside the aid workflow that tells each family exactly which document is missing. It reads each upload on arrival, extracts the values verification needs, compares them with the ISIR, drafts the correction with every value linked to its source, explains any remaining comment codes, and queues the file for counsellor sign-off. A synthetic-file demo (sample ISIRs, tax transcripts and worksheets) is enough to show the workflow without any student data.

## Target Customer
Aid directors at institutions processing thousands of verification files a year, and the aid system vendors and agent start-ups selling into them.

## Impact If Built
Files reach a final offer days or weeks sooner, and counsellors review instead of transcribe. If verification turnaround falls from ~3 weeks to ~3 days, more admitted students see a final offer before the deposit deadline (estimate).
