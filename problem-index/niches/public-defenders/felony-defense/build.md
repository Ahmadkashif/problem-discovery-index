# AI-Powered Discovery Triage for High-Volume Felony Defense

**Niche:** [[niches/public-defenders/felony-defense/profile|Felony Defense]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool exists that automatically ingests felony discovery packages and surfaces the 5% of documents that matter for each defense theory.
**Tags:** #transformer #text-classification #nlp #automation #worker-facing

## The Problem
Felony cases generate 500-10,000 pages of discovery — police reports, witness statements, lab results, body camera transcripts, phone records. Public defenders with 100+ active cases cannot read all of it. They skim, miss exculpatory evidence, and build defense theories on incomplete information. Prosecutors have paralegals who organize discovery; defenders have themselves.

## Why Nobody Has Built This
E-discovery tools (Relativity, Logikcull) are designed for civil litigation with large budgets and cooperative parties. They assume the user has time for iterative review and a team to manage the platform. Public defender discovery is adversarial, arrives in inconsistent formats (paper scans, PDFs, video files), and must be processed by a single attorney in hours, not weeks.

## What to Build
A discovery intake pipeline that OCRs scanned documents, transcribes body camera and interview audio, and classifies every piece of evidence by relevance to common defense theories (alibi, identification challenge, constitutional violation, witness credibility). The system highlights Brady material (exculpatory evidence the prosecution must disclose), flags inconsistencies between police reports and witness statements, and generates a 1-page case summary with the strongest defense angles.

## Target Customer
County and state public defender offices with 20+ attorneys handling felony caseloads. Budget holder is the Chief Public Defender or the county/state agency that funds the office.

## Impact If Built
Reduces per-case discovery review from 4-8 hours to 30-60 minutes. Catches exculpatory evidence that overworked defenders currently miss, directly improving case outcomes for defendants facing years of incarceration.
