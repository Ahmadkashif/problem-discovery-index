# Section 8 Inspection Preparation and Compliance Tracker

**Niche:** [[niches/property-management/affordable-housing-section8/profile|Affordable Housing & Section 8]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A compliance platform that tracks every Section 8/HCV and LIHTC requirement per unit — HQS inspection preparation checklists, HAP payment status, income recertification deadlines, and compliance file completeness — alerting the property manager to upcoming deadlines and documentation gaps before the PHA inspector or state auditor arrives.
**Tags:** #gradient-boosting #automation #compliance #workflow-orchestration #data-integration #logistic-regression

## The Problem
A 200-unit affordable housing property must maintain compliance across multiple programs simultaneously: 80 units with Section 8 HCV vouchers (each requiring annual HQS inspection and HAP recertification), 120 units with LIHTC income restrictions (each requiring annual income recertification with specific documentation), and all 200 units subject to local housing code inspections. The compliance officer tracks: 80 HQS inspection dates (with 30-day advance prep), 200 LIHTC recertification anniversaries (with 120-day advance notice requirements), HAP payment reconciliation for 80 vouchers (each paid by a different PHA at different rates), and compliance file maintenance for all 200 units (each file must contain specific documents in specific order). This is tracked in Excel calendars and paper file checklists. Missing a deadline results in: HAP payment suspension (Section 8 — $800-2,000/month per unit in lost subsidy), tax credit noncompliance findings (LIHTC — potential recapture of $500K+ in tax credits), or failed inspections requiring re-inspection (cost and timeline penalties).

## Why Nobody Has Built This
Affordable housing compliance rules vary by program (Section 8 vs. LIHTC vs. HOME vs. PBRA), by state (state housing finance agencies add requirements beyond federal minimums), and by PHA (each of 3,300+ PHAs has its own HQS inspection scheduling, HAP payment, and recertification processes). Building a comprehensive compliance tracker requires modeling all these variations. The market is mid-sized: approximately 5 million affordable housing units in the US, managed by a mix of nonprofits, public housing authorities, and for-profit affordable housing operators.

## What to Build
A compliance calendar and documentation tracker that: (1) maintains unit-level compliance records — which programs apply to each unit, applicable income limits, inspection requirements, and recertification deadlines; (2) generates a rolling compliance calendar showing upcoming deadlines by urgency — "15 LIHTC recertifications due in the next 60 days, 8 HQS inspections scheduled next month"; (3) tracks compliance file completeness per unit — checking whether each required document is present, current (not expired), and correctly filed; (4) provides HQS inspection preparation checklists — the specific items the PHA inspector will check, with the property manager's pre-inspection verification status; (5) predicts inspection outcomes based on historical patterns — "Units with deferred maintenance on Item X fail HQS inspection 45% of the time, 12 of your units have this item open."

## Target Customer
Affordable housing property managers and compliance officers managing 100+ units across Section 8 and/or LIHTC programs. Nonprofit housing organizations managing compliance across multiple properties and funding sources. State housing finance agencies wanting to reduce compliance failures among their LIHTC properties.

## Impact If Built
Reduces compliance violations by 40-60% through proactive deadline tracking and documentation gap identification. Prevents HAP payment suspensions that cost $800-2,000/month per affected unit. Reduces LIHTC noncompliance findings that risk tax credit recapture. Saves compliance officers 10-20 hours per month in manual calendar management and file auditing. Could be priced at $5-10/unit/month.
