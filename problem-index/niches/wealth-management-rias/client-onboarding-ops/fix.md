# ACAT Transfer Tracking and Exception Resolution

**Niche:** [[niches/wealth-management-rias/client-onboarding-ops/profile|Client Onboarding & Account Operations]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Fix (Pain Point)
**One-liner:** Asset transfers via ACAT take 5-10 business days but frequently stall due to account title mismatches, missing cost basis, or delivering firm delays — and the operations team has no visibility into why a transfer is stuck until they manually check the custodian portal.
**Tags:** #automation #workflow-orchestration #worker-facing #quick-win

## The Problem
When a new client transfers assets to the RIA's custodian via ACAT (Automated Customer Account Transfer), the transfer is supposed to complete in 5-7 business days. In practice, 20-30% of transfers encounter exceptions: the delivering firm rejects the request due to an account title mismatch, specific positions are ineligible for in-kind transfer, cost basis information is missing or delayed, or the delivering firm simply does not process the request on time. The operations team discovers these exceptions only by manually checking the custodian portal daily — there are no proactive notifications — and resolution often requires phone calls to the delivering firm's back office with hold times of 30-60 minutes.

## Why It's Still Broken
ACAT exception data exists in the NSCC (National Securities Clearing Corporation) system and surfaces in custodian portals, but custodians do not push proactive alerts to RIA operations teams. The ACAT rejection codes are cryptic (e.g., "Reason Code 21: Invalid Registration") and require institutional knowledge to interpret and resolve. Each delivering firm has different procedures for resolving exceptions, and there is no centralized knowledge base of resolution workflows by firm and rejection type.

## What a Fix Looks Like
A transfer tracking dashboard that: (1) monitors all pending ACAT transfers across custodians and surfaces status changes proactively (via SMS/email alerts, not portal-checking); (2) translates ACAT rejection codes into plain-language explanations with firm-specific resolution steps; (3) tracks resolution workflows with follow-up reminders and escalation paths; and (4) provides the operations team with a complete view of all in-flight transfers, expected completion dates, and items requiring attention — eliminating the daily portal-checking ritual.

## Who Feels the Pain
Client service associates and operations managers who spend 3-5 hours per week manually checking custodian portals for transfer status updates and 30-60 minutes per exception on phone calls to delivering firms — time that could be spent on higher-value client service tasks.

## Impact If Fixed
Transfer exception resolution time drops from 5-10 business days to 2-3 business days, reducing the period during which transferred assets are uninvested and the client experience is poor. Operations teams reclaim 3-5 hours per week from manual portal monitoring, and new clients receive their fully funded portfolios 30-40% faster.
