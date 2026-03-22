# HEP Compliance Data Integration for PT EMRs

**Niche:** [[niches/physical-therapy/hep-compliance/profile|Home Exercise Program (HEP) Delivery & Compliance]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** MedBridge delivers exercises and captures some compliance data — but that data never reaches the PT's clinical documentation, where it could support treatment plan adjustments and authorization narratives.
**Tags:** #feature-engineering #data-integration #workflow-orchestration #compliance #revenue-impact

## The Problem
MedBridge and PhysiTrack deliver exercise programs to patients and capture basic engagement metrics — exercise completion rates, session duration, patient feedback. But this data sits in the HEP platform's own dashboard, disconnected from the PT's EMR where clinical decisions are documented. When a PT documents a daily note in WebPT, they don't see the patient's MedBridge compliance data alongside their clinical findings. When they write a medical necessity narrative for an authorization extension, they can't cite objective HEP compliance data because it's not in the clinical record. The HEP compliance data that could strengthen clinical documentation and support authorization requests goes unused because it lives in a separate system.

## What Already Exists
MedBridge captures exercise completion data and provides a therapist dashboard showing patient engagement. PhysiTrack tracks adherence and sends automated reminders. WebPT and Clinicient/Prompt handle clinical documentation, treatment planning, and billing. Both HEP platforms and EMRs have APIs or data export capabilities. But no integration exists that feeds HEP compliance data from MedBridge or PhysiTrack into the clinical note within WebPT or Prompt — making the compliance data clinically invisible.

## The Customization Gap
The integration needs to be more than a raw data dump — it requires clinical interpretation logic. A compliant patient (80%+ exercise completion) who isn't improving has a different clinical story than a non-compliant patient (20% completion) who isn't improving. The integration should: (1) pull exercise completion rates, pain ratings, and difficulty ratings from the HEP platform and present them in the EMR's daily note view, (2) auto-populate a "HEP Compliance" section in the daily note template with structured data (completion percentage, exercises skipped, pain reported, difficulty changes), (3) flag clinically significant compliance patterns (sudden drop in adherence, escalating pain reports on specific exercises, consistent skipping of one exercise), (4) include compliance data in authorization extension narratives ("Patient demonstrated 85% HEP adherence over the past 12 visits, supporting continued skilled PT intervention"), and (5) correlate compliance data with outcome score changes to give the PT evidence of whether the HEP is contributing to improvement.

## Target Customer
PT clinics that already use MedBridge or PhysiTrack for HEP delivery and WebPT or Prompt for clinical documentation — and want the data from these systems to work together rather than existing as parallel, disconnected streams.

## Impact If Solved
Transforms HEP compliance from invisible to documented — giving PTs objective evidence for treatment plan decisions. Strengthens authorization extension narratives with compliance data, improving approval rates. Saves PTs 3-5 minutes per daily note by auto-populating HEP compliance sections rather than manually asking patients about their exercises and documenting self-reported answers.
