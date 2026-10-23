# Back-End Recognition Tuned to the Account

**Niche:** [[niches/document-preparation-services/medical-transcription-documentation/profile|Medical Transcription & Healthcare Documentation Editing]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Back-end speech-recognition platforms produce good drafts out of the box, but the account's templates, normals and dictator vocabulary still have to be layered on by hand.
**Tags:** #transformers #seq2seq #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to return a health system's residual dictation — the reports front-end speech recognition and ambient scribes don't absorb — inside contract turnaround at an AHDI score of 98 or better, and whoever holds turnaround and accuracy at the fewest editor minutes per line takes the account.

## The Problem
A vendor taking over a new health system's dictation inherits its report templates, departmental "normals" (the standard text for a normal exam), formatting rules, provider list and preferences. Drafts arrive in the recogniser's generic format and editors reformat them by hand. AHDI's back-end recognition guidance itself tells health systems to renegotiate line rates for speech-edited work, so every minute of manual reformatting is unpaid.

## What Already Exists
Back-end recognition and editing platforms such as eScription (now operated by DeliverHealth) and Solventum's Fluency for Transcription, plus general cloud recognisers with custom-vocabulary features. Each supports per-dictator acoustic adaptation and basic templates.

## The Customization Gap
The account-level logic is: template and section mapping per report type, with normals inserted when the dictator says "normal chest" and only then; provider-specific vocabulary and drug lists drawn from the health system's formulary; formatting rules from the AHDI-aligned style guide the contract names; and routing that sends drafts below a confidence threshold to senior editors. It also needs an onboarding workflow that turns a new account's sample reports into these rules in days, not weeks.

## Target Customer
Implementation and operations leads at documentation vendors onboarding new health-system accounts.

## Impact If Solved
Faster account go-lives, fewer reformatting minutes per report, and a defensible line rate on speech-edited work.
