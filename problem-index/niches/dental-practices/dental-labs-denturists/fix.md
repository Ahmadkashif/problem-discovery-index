# Standardized Shade Capture and Communication

**Niche:** [[niches/dental-practices/dental-labs-denturists/profile|Dental Labs & Denturists]]
**Industry:** [[industries/dental-practices|Dental Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Shade mismatch is the #1 reason for crown and bridge remakes (8-12% of all cases) — dentists take shade photos with phones under inconsistent lighting and describe colors with subjective names, and labs fabricate from that interpretation.
**Tags:** #cnns #object-detection #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact #worker-facing

## The Problem
When a dentist prepares a tooth for a crown, they must communicate the desired shade to the lab. The current process: hold a physical shade tab (VITA Classical or VITA 3D-Master) next to the prepared tooth, visually match the closest shade, take a photo with a phone camera, and write "A2" or "B1" on the Rx form. This process fails at every step. Operatory lighting varies (fluorescent, LED, natural window light) and dramatically affects how colors appear in photos. Phone cameras auto-adjust white balance, further distorting color. The dentist's color perception is subjective and affected by fatigue (color discrimination degrades after 3 hours of clinical work). The shade tab system reduces the entire visible color spectrum to 16-26 discrete options. And the written notation ("A2 but slightly more yellow at the incisal") is interpreted by a lab technician who has never seen the patient. Experienced lab ceramists develop tacit expertise in interpreting specific dentists' shade preferences — "when Dr. Smith says A2, he really means A2.5" — but this knowledge is personal and fragile.

## Why It's Still Broken
Dedicated shade-matching devices exist (VITA Easyshade, SpectroShade) that use spectrophotometry to objectively measure tooth color. They cost $2,000-4,000 and are used by only ~15% of practices because they add 2-3 minutes to the workflow and require a separate communication step (the reading must be manually transcribed to the lab Rx). The device measures the shade accurately at the chair, but the data doesn't flow digitally to the lab's CAD/CAM system — it's still written on a form or spoken over the phone. Phone-based shade apps exist but produce inconsistent results because they can't control ambient lighting. The fundamental gap is not measurement — it's end-to-end digital communication of color data from the dentist's chair to the lab's fabrication software without any subjective interpretation step.

## What a Fix Looks Like
A phone-based shade capture system with two components: (1) a low-cost clip-on attachment ($50-100) that provides calibrated LED lighting and a color reference target in the field of view, enabling the phone camera to capture shade-accurate photos regardless of operatory lighting, and (2) software that analyzes the photo against the reference target, extracts objective shade coordinates (L*a*b* color space), maps to the closest VITA shade with a confidence score, and transmits the digital shade data directly to the lab's CAD/CAM system (exocad, 3Shape) via API. The lab ceramist sees the calibrated photo alongside objective shade coordinates — eliminating the interpretation step entirely. A CNN trained on thousands of shade-matched restorations can learn the mapping from calibrated photos to final restoration shade, incorporating the subtle adjustments that experienced ceramists make based on tooth position, translucency, and surrounding dentition.

## Who Feels the Pain
Lab ceramists who spend hours on shade matching only to face remakes when their interpretation didn't match the dentist's intent, dentists who lose chair time to unpaid remake appointments, and patients who endure additional visits for shade corrections.

## Impact If Fixed
Reduces shade-related remakes from 8-12% to 2-3% of cases. For a lab processing 500 cases/month, eliminating 30-45 remakes saves $15K-25K/month in material and labor costs. For each referring dentist, avoiding 1-2 remakes/month recovers 2-4 hours of unpaid chair time worth $1,000-2,000/month.
