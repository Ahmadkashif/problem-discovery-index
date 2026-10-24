# Implant Clearance Done Before the Patient Arrives

**Niche:** [[niches/diagnostic-imaging-centers/mri-ct-technologists/profile|The MRI & CT Technologist]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** MRI implant research happens at the scanner with the patient waiting, though the implant was on the screening form days earlier.
**Tags:** #large-language-models #transformers #bert #k-nearest-neighbors #compliance #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to let one technologist run a scanner safely through a full shift, and whoever lets a single technologist complete the most exams per shift with no rise in repeat scans or safety events takes the account.

## The Problem
A patient lists "spinal cord stimulator, 2019" on the form. On exam day the technologist calls the patient's pain clinic, searches the manufacturer's site, finds two possible models with different MR Conditional limits, and cannot confirm which one. The scan is cancelled.

## Why Nobody Has Built This
Implant labelling is scattered across manufacturers' PDFs and reference sites, device identification depends on documents the centre does not hold, and liability makes vendors cautious about advising on safety.

## What to Build
A pre-visit clearance workflow. It collects implant cards and operative notes from the patient and referrer at booking, identifies device make and model by matching against an implant labelling index, and extracts MR Conditional parameters. It maps them to the scheduled scanner's settings and produces a sourced clearance sheet for technologist sign-off, with escalation rules for radiologist review or device reprogramming.

## Target Customer
Chief technologists and MR safety officers at operators with many 1.5T and 3T magnets.

## Impact If Built
Clearing implants before the day saves 15–30 technologist minutes per implant patient and most same-day "unable to verify" cancellations (estimate). On a busy magnet that is a recovered slot or more per week.
