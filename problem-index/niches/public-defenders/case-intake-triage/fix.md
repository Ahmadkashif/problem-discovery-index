# Eligibility Screening Bottleneck Delaying Representation

**Niche:** [[niches/public-defenders/case-intake-triage/profile|Case Intake & Triage]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Fix (Pain Point)
**One-liner:** Defendants wait 3-7 days for a public defender because eligibility determination (proving they can't afford a private attorney) requires income verification through manual document review and phone interviews — while the defendant sits in jail.
**Tags:** #automation #data-integration #quick-win #workflow-orchestration

## The Problem
Before a public defender is appointed, the defendant must prove financial eligibility — that they cannot afford private counsel. This requires submitting pay stubs, tax returns, benefit statements, or other proof of income. In many jurisdictions, this documentation is collected by intake staff through in-person interviews or mailed forms. The defendant is often in custody during this process, unable to access their financial documents. Intake staff are overwhelmed — a busy office processes 50-200 new applications daily. The result is a 3-7 day gap between arrest and attorney appointment, during which the defendant has no legal representation at a time when critical decisions (bail, initial statements, evidence preservation) are being made.

## Why It's Still Broken
Eligibility determination is set by state statute and typically requires documentation that low-income defendants struggle to produce — they may not have pay stubs (if paid cash), may not file tax returns, and may not have organized financial records. Intake staff must verify self-reported income against available records, which requires contacting employers, checking benefits databases, and reviewing financial documents — all manually. Some jurisdictions have moved to "presumptive eligibility" (eligible unless proven otherwise), but most still require affirmative proof before appointment. The process was designed for a walk-in applicant, not someone sitting in jail.

## What a Fix Looks Like
An automated eligibility screening system that pulls from available data sources to verify income: state benefits databases (SNAP, Medicaid, SSI enrollment confirms low income), tax records (IRS or state DOR), employment databases, and jail booking records (which often include employer information). If the defendant is enrolled in any means-tested public benefit, eligibility is automatically confirmed — no additional documentation needed. For borderline cases, a simplified digital application accessible from the jail's tablet system or by phone. The system produces an eligibility determination within 24 hours of arrest, not 3-7 days.

## Who Feels the Pain
Defendants sitting in jail without an attorney for days, missing critical early-case opportunities (bail reduction, witness identification, evidence challenges). Intake staff who spend 70% of their time on eligibility verification that could be automated for 60-70% of applicants.

## Impact If Fixed
Reduces time-to-appointment from 3-7 days to under 24 hours for the 60-70% of defendants whose eligibility can be verified through existing public records. Frees intake staff time for substantive case processing. Ensures defendants have representation during the critical first 48 hours after arrest.
