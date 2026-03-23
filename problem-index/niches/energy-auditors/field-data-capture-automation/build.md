# Computer Vision Equipment Nameplate Reader

**Niche:** [[niches/energy-auditors/field-data-capture-automation/profile|Field Data Capture Automation]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool can photograph an HVAC nameplate and automatically extract the model number, efficiency rating, capacity, fuel type, and manufacture date into structured audit fields.
**Tags:** #cnn #ocr #object-detection #computer-vision #tacit-knowledge-ml #automation

## The Problem
During every energy audit, the auditor photographs and manually transcribes data from 5-15 equipment nameplates: furnace, boiler, water heater, air conditioner, heat pump, range, dryer, and any other fuel-burning or major electric equipment. Each nameplate contains critical data: manufacturer, model number, serial number, efficiency rating (AFUE, SEER, EF, COP), capacity (BTU/hr, tons), fuel type, and manufacture date. Transcribing this data accurately is tedious and error-prone — nameplates are often faded, dirty, in poorly lit basements, or use non-standard formatting. A single transcription error (misread efficiency rating) produces an incorrect energy model that over- or under-predicts savings by thousands of dollars.

## Why Nobody Has Built This
Generic OCR (Google Lens, Adobe Scan) can read text from clean documents but struggles with: curved and embossed metal nameplates, inconsistent formatting across manufacturers (one uses "AFUE: 80%", another uses "Ann. Fuel Util. Eff. 80", another uses just "80" next to an efficiency symbol), faded or partially obscured text common on 20-year-old equipment, and low-light conditions in basements and utility closets. Building an effective nameplate reader requires training a specialized model on thousands of HVAC nameplate images with labeled fields — a dataset that does not currently exist publicly.

## What to Build
A mobile app where the auditor photographs an equipment nameplate and the system: identifies the equipment type (furnace, water heater, AC unit) from visual context, extracts key fields (manufacturer, model, serial number, efficiency rating, capacity, fuel type, manufacture date) using a CNN + OCR pipeline trained specifically on HVAC equipment nameplates, and populates the corresponding fields in the audit data structure. The auditor reviews extracted values and corrects any errors with one tap. For nameplates too damaged to read, the system uses the model number to look up specifications from manufacturer databases (AHRI directory). The system builds its training dataset from every nameplate photo processed, improving accuracy over time.

## Target Customer
Energy auditors who photograph and transcribe 5-15 equipment nameplates per audit, spending 15-30 minutes per audit on a task that is purely data entry.

## Impact If Built
Saves 15-30 minutes per residential audit and 1-2 hours per commercial audit in nameplate transcription, eliminates transcription errors that compound into inaccurate energy models, and creates a structured equipment database that enables fleet-level analysis of installed equipment across a region.
