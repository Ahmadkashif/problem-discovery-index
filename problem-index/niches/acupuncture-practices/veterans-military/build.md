# VA-Acupuncture Billing & Authorization Bridge

**Niche:** [[niches/acupuncture-practices/veterans-military/profile|Veterans & Military Acupuncture Providers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool bridges the gap between VA Community Care authorization workflows and private acupuncture practice management systems.
**Tags:** #automation #workflow-orchestration #compliance #data-integration #revenue-impact

## The Problem
When a veteran is authorized for acupuncture through VA Community Care, the acupuncturist receives an authorization with specific visit limits, date ranges, and CPT codes approved. The practitioner must verify authorization before each visit, bill using VA-specific procedures (not standard clearinghouse submission), track remaining authorized visits, and request re-authorization before the current one expires. This entire workflow is manual — checking the VA portal, cross-referencing with the practice schedule, and submitting claims through a separate VA billing channel. Most acupuncturists treating 10-20 VA patients juggle this alongside their commercial practice.

## Why Nobody Has Built This
VA Community Care acupuncture is a new and growing market — the significant expansion only started in 2019-2020. The number of acupuncturists with VA contracts (~3,000-5,000 nationally) is small. VA's systems are notoriously difficult to integrate with, and the authorization/billing workflow changes frequently as VA updates Community Care policies.

## What to Build
A middleware layer that: (1) syncs VA authorization data with the practitioner's scheduling system (auto-flagging VA patients and remaining visits), (2) pre-validates each visit against the authorization before the appointment, (3) generates VA-compliant billing submissions from the EHR's treatment notes, (4) tracks payment status through VA's 60-90 day payment cycle, and (5) auto-generates re-authorization requests before current authorizations expire.

## Target Customer
Acupuncturists treating 10+ VA patients monthly who spend 5-8 hours/week on VA-specific administrative tasks.

## Impact If Built
Reduces VA administrative overhead by 60-70% (saving 3-5 hours/week), eliminates authorization lapses that result in unbillable visits, and accelerates payment receipt from 90 to 45-60 days through cleaner claim submission.
