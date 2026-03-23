# Photo Documentation Organization and Retrieval

**Niche:** [[niches/energy-auditors/home-performance-contractors/profile|Home Performance Contractors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** Auditors take 50-200 photos per home visit on their personal phones, then spend 30-60 minutes sorting, renaming, and attaching them to the correct audit sections — if they can find them at all.
**Tags:** #cnn #multiclass-classification #computer-vision #automation #worker-facing

## The Problem
During a residential energy audit, the auditor photographs: attic insulation (depth, type, condition), basement/crawlspace conditions, HVAC equipment nameplates, window frames, duct connections, electrical panels, blower door setup, combustion safety test results on the manometer, and thermal images from the IR camera. These photos serve as evidence for the energy model inputs, documentation for utility program submissions, and content for the homeowner proposal. The auditor takes them on their personal phone's camera roll, interspersed with personal photos, and must later sort through 50-200 images to identify which photo corresponds to which building component. Mislabeled photos trigger QA rejections. Lost photos require return visits.

## Why It's Still Broken
The auditor's phone camera is the fastest way to capture images in the field — any purpose-built photo app that adds friction (categorization steps, naming requirements) slows the auditor down during a 2-3 hour site visit where they are already juggling measurements, equipment, and homeowner questions. The result is that auditors default to the native camera and deal with the sorting problem later. Photo management apps (Google Photos, Apple Photos) organize by date and location but cannot categorize by building component. No tool understands the content of an energy audit photo well enough to auto-categorize it.

## What a Fix Looks Like
A photo capture app designed for energy auditors that uses the phone's camera with automatic image classification: the auditor takes a photo and the app identifies it as "attic insulation," "HVAC nameplate," "blower door manometer," or "thermal image" using a CNN trained on audit photo datasets. Photos are automatically organized by building component, tagged with the audit project, and ready for attachment to the corresponding audit report section and program submission. Mis-classifications are correctable with one tap. The app adds less than 1 second of overhead per photo versus the native camera.

## Who Feels the Pain
Field auditors who spend 30-60 minutes per project sorting photos after every site visit, office staff who assemble program submissions and proposals from unsorted photo libraries, and auditors who discover missing photos after leaving the site and must schedule return visits.

## Impact If Fixed
Saves 30-60 minutes of photo sorting per audit (150-300 hours annually for a 300-audit company), eliminates return visits for missing photos (estimated 5-10% of audits), and ensures photo documentation meets program QA standards on first submission.
