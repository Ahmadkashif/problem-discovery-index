# The Assessment-Only Diagnosis

**Niche:** [[niches/health-insurance-carriers/ma-risk-adjustment/profile|Medicare Advantage Risk Adjustment & RADV Defence]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A diagnosis recorded once in an in-home health assessment, and never treated or seen again in any claim, is paid in full and is exactly what auditors look for.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to submit every diagnosis a member's chart supports, and none it doesn't, before CMS's final submission deadline, and whoever keeps the most submitted diagnoses standing through a RADV medical-record review takes the account.

## The Problem
In-home assessments capture conditions that members' own physicians may never document. Some are real and untreated; others are weakly supported. When a diagnosis appears only in the assessment and in no later visit, prescription or claim, its RADV survival is doubtful and it has drawn sustained Inspector General scrutiny (recalled).

## Why It's Still Broken
Assessment vendors are paid per visit, and the diagnosis is submitted as soon as it is coded. Nobody owns the follow-up: confirming the condition with the member's physician, starting treatment, or withdrawing the code.

## What a Fix Looks Like
Flag every assessment-only diagnosis at 90 days. Route clinically important ones to care management and the member's physician for confirmation and treatment. Withdraw codes with no confirmation before the final submission deadline. Report each assessment vendor's confirmation rate.

## Who Feels the Pain
Compliance officers facing audits; members with conditions found and then ignored; finance teams booking revenue that may be recovered.

## Impact If Fixed
Real conditions get treated, unsupported codes are withdrawn voluntarily, and assessment programmes are judged on whether their findings hold.
