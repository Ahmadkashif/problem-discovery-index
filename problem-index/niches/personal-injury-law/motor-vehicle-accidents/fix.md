# Police Report Liability Extraction

**Niche:** [[niches/personal-injury-law/motor-vehicle-accidents/profile|Motor Vehicle Accidents]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Fix (Pain Point)
**One-liner:** Paralegals stop spending 20-40 minutes per case manually reading police reports to extract liability facts, witness info, and contributing factors — the key data points that determine case viability get pulled automatically.
**Tags:** #bert #transformers #large-language-models #transfer-learning #automation #quick-win

## The Problem
Every MVA case starts with a police report. The paralegal must read the narrative section, identify the at-fault driver, extract witness names and contact information, note contributing factors (DUI, distraction, weather, road conditions), identify insurance information for all parties, and determine whether the officer assigned fault or issued citations. Police reports vary wildly by jurisdiction — some are structured forms (Texas CR-3), others are free-text narratives (many local departments), some are handwritten, and formats differ across the 18,000+ law enforcement agencies in the US. A high-volume MVA firm processes 50-100 new police reports per month. Each takes 20-40 minutes to read, extract, and enter into the case management system.

## Why It's Still Broken
OCR handles the digitization of scanned reports, but the extraction problem is harder. Police narrative language is non-standard, uses abbreviations that vary by department ("V1" vs. "Unit 1" vs. "Driver A"), and mixes factual observations with officer opinions. Liability indicators are implicit — "V2 failed to yield" buried in a paragraph means the other driver is at fault, but no keyword search catches the semantic meaning. Generic document extraction tools (DocuSign Insight, Rossum) handle structured forms but fail on the narrative sections that contain the most valuable liability information.

## What a Fix Looks Like
A fine-tuned language model that ingests police reports (PDF/image via OCR, then text extraction) and outputs structured fields: parties involved (name, role, vehicle, insurance), witness list with contact info, officer-assigned fault indicators, citations issued, contributing factors, and a liability confidence score. The model must handle jurisdiction-specific formatting by being trained on reports from the 50-100 most common formats. Output feeds directly into Filevine or SmartAdvocate case fields via API. The paralegal reviews the extraction in 2-3 minutes instead of reading the full report in 20-40 minutes.

## Who Feels the Pain
Intake paralegals and case managers at MVA firms who process dozens of police reports monthly. At firms handling 500+ active MVA cases, this is a full-time job for one person that could be reduced to a review-and-confirm workflow.

## Impact If Fixed
Saves 15-35 minutes per case on police report processing. At 50 new cases per month, that recovers 12-29 paralegal hours monthly. More importantly, surfaces liability red flags (comparative fault indicators, missing witness info, no citation issued) at intake, enabling faster case-viability decisions and earlier rejection of low-probability cases.
