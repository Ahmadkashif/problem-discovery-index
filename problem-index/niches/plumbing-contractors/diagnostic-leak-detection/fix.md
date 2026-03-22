# Insurance-Ready Leak Documentation and Evidence Packaging

**Niche:** [[niches/plumbing-contractors/diagnostic-leak-detection/profile|Diagnostic Leak Detection]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Homeowners need documented evidence of leak source, cause, and damage extent for insurance claims — plumbers currently produce handwritten reports that insurance adjusters reject, delaying claims and losing the plumber the repair job.
**Tags:** #large-language-models #transformers #feature-engineering #automation #worker-facing #revenue-impact

## The Problem
When a plumber locates a hidden leak — especially a slab leak, a leak inside a wall, or a leak under a foundation — the homeowner almost always files an insurance claim. The insurance adjuster requires documented evidence: (1) the location of the leak (address, room, specific coordinates), (2) the cause of the leak (pipe material failure, fitting failure, freeze damage, root intrusion), (3) the method of detection (acoustic, thermal, pressure test, visual), (4) photographic and/or thermal imaging evidence, (5) the scope of damage (affected rooms, materials damaged, estimated water volume), and (6) the proposed repair method with cost estimate. Currently, the plumber hands the homeowner a handwritten report — or worse, a verbal description — and the homeowner tries to relay this to their insurance company. Adjusters reject vague or informal documentation, delaying claims by weeks and often requiring a second visit from the plumber to produce proper documentation.

## Why It's Still Broken
Plumbers are trained to find and fix leaks, not to produce insurance documentation. The documentation format insurance adjusters expect — professional report with specific cause language, photographic evidence with annotations, thermal images with interpretation, and code-compliant repair scope — is foreign to most plumbing technicians. Large restoration companies (ServPro, ServiceMaster) have documentation protocols and software (Xactimate, Matterport), but these tools are designed for restoration contractors, not plumbers who perform the initial detection. The plumber's documentation gap means: (1) the homeowner's claim is delayed or denied for insufficient evidence, (2) the homeowner hires a restoration company that brings their own documentation and gets the repair job, and (3) the plumber who found the leak loses the lucrative repair work.

## What a Fix Looks Like
A mobile documentation app that the plumber uses during leak detection to capture: (1) geo-tagged photos of the leak location, damage area, and affected materials, (2) thermal images (imported from FLIR) with auto-generated interpretation text, (3) acoustic readings or pressure test results with standard documentation language, (4) cause determination selected from insurance-standard categories (sudden and accidental, wear and tear, freeze damage, construction defect), and (5) repair scope with materials and labor estimate. The app uses an LLM to generate a professional insurance-ready report in PDF format that includes all evidence, uses industry-standard terminology that adjusters recognize, and formats the cause-and-origin section in the language insurance companies expect. The plumber reviews for accuracy, signs digitally, and emails the report to the homeowner and insurance company before leaving the property. Total documentation time: 10-15 minutes vs. 45-60 minutes for manual report writing (if the plumber writes one at all).

## Who Feels the Pain
The homeowner whose insurance claim is delayed because the plumber's documentation was inadequate, and the plumber who loses $2,000-15,000 repair jobs to restoration companies that capture the work through superior documentation.

## Impact If Fixed
Capturing the repair job (not just the diagnosis) increases per-call revenue from $250-500 (detection fee only) to $3,000-15,000 (detection + repair). Insurance-ready documentation reduces claim processing time from 2-4 weeks to 3-5 days. For a leak detection specialist performing 5-10 detections per week, converting 30-50% more detections into repair jobs through better documentation adds $200K-500K in annual revenue.
