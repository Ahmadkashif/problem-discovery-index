# Manual CAPA Investigation and Documentation

**Niche:** [[niches/contract-manufacturing/medical-device-cmos/profile|Medical Device CMOs]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Quality engineers spend 15-40 hours per CAPA investigation manually gathering production records, interviewing operators, and drafting root cause analysis reports — a process that should start with automated data assembly and pattern analysis rather than detective work.
**Tags:** #gradient-boosting #evaluation-metrics #compliance #automation #worker-facing

## The Problem
When a non-conformance occurs (defective product, process deviation, customer complaint), FDA 21 CFR Part 820.90 requires a CAPA investigation documenting: problem description, investigation steps, root cause analysis, corrective action, preventive action, and effectiveness verification. Quality engineers currently perform this investigation manually — reviewing production records from MES, pulling SPC data, checking calibration records, interviewing operators, and drafting a root cause analysis report using methods like fishbone diagrams and 5-Why analysis. A typical CAPA takes 15-40 hours of quality engineering time, and a medical device CM may have 5-15 open CAPAs at any time.

## Why It's Still Broken
CAPA investigation is perceived as requiring human judgment — and it does for the root cause analysis and corrective action design. But the data gathering phase (assembling production records, SPC data, maintenance logs, and calibration records relevant to the non-conformance) is purely mechanical and consumes 40-60% of the total CAPA effort. Quality engineers spend hours as data detectives before they can begin the analytical work they're trained for. No tool pre-assembles the relevant production data context for a CAPA investigation.

## What a Fix Looks Like
A CAPA investigation support tool that, given a non-conformance event (product lot, process step, defect type, date), automatically retrieves all related production records from MES (process parameters during that lot), SPC data (was the process trending out of control before the event?), maintenance records (was equipment calibration current?), material lot data (were there other quality events with this material lot?), and historical CAPAs for similar defects. The quality engineer receives a pre-assembled investigation package with relevant data highlighted and similar historical patterns surfaced — reducing data gathering from 8-20 hours to 1-2 hours and enabling them to focus on root cause analysis and corrective action design.

## Who Feels the Pain
Quality engineers who are simultaneously managing 5-15 open CAPAs, each requiring extensive manual data gathering. Late CAPAs (past due date) are one of the top FDA 483 observations at medical device manufacturers.

## Impact If Fixed
Reduces CAPA investigation time by 40-50% — from 15-40 hours to 8-20 hours per investigation. For a CM with 10 open CAPAs at any time, this recovers 70-200 quality engineering hours per quarter. Reduces CAPA cycle time (time from non-conformance to closure) by 30-40%, decreasing the inventory of overdue CAPAs that creates FDA audit risk.
