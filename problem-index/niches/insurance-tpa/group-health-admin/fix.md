# Eligibility File Reconciliation Errors

**Niche:** [[niches/insurance-tpa/group-health-admin/profile|Group Health Benefits Admin]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Fix (Pain Point)
**One-liner:** Employer-submitted eligibility files contain formatting errors, stale terminations, and conflicting records that cause claims to pay for ineligible members or deny eligible ones.
**Tags:** #anomaly-detection #isolation-forest #tabular-ml #data-integration #compliance

## The Problem
TPAs receive eligibility files (834 EDI transactions or CSV exports) from employer HR systems on a weekly or monthly basis. These files are the source of truth for who is covered and under which plan. In practice, 5-15% of files contain errors: terminated employees still listed as active, new hires missing, dependent ages exceeding plan limits without removal, or duplicate records with conflicting effective dates. Each error either pays a claim for an ineligible person (employer eats the cost) or denies a valid claim (member files a complaint, TPA investigates).

## Why It's Still Broken
Eligibility file formats vary by employer — some send 834 EDI, others send CSV, others send Excel with inconsistent column headers. TPAs have built basic validation rules (check for required fields, valid date formats) but lack the ability to detect logical errors like "this employee was terminated in payroll but not in the benefits file" because they don't have access to payroll data. The root cause is that HR systems and benefits systems are maintained by different people at the employer, with no automated reconciliation between them.

## What a Fix Looks Like
An eligibility validation engine that goes beyond format checking to detect logical anomalies: members with coverage effective dates before hire dates, dependents aging out of coverage, employees terminated in the previous eligibility file now reappearing, and coverage-level changes without corresponding life events. The engine flags anomalies for employer HR review before loading into the adjudication system, preventing downstream claims errors.

## Who Feels the Pain
TPA eligibility analysts spend 15-20 hours per week manually investigating and correcting eligibility discrepancies. Employer HR teams receive angry calls from employees whose claims were denied due to eligibility errors they didn't cause.

## Impact If Fixed
Reduces eligibility-related claims errors by 70-80%, saving $200-$500 per error in investigation and correction costs. For a TPA managing 50 employer groups, this eliminates 2,000-5,000 annual eligibility errors and saves $400K-$2.5M.
