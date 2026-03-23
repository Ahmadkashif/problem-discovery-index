# VA Payment Tracking & Reconciliation

**Niche:** [[niches/acupuncture-practices/veterans-military/profile|Veterans & Military Acupuncture Providers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** VA pays acupuncturists on a 60-90 day cycle with no transparent status tracking — practitioners cannot tell if a claim is pending, denied, or lost until weeks after submission.
**Tags:** #automation #data-integration #revenue-impact #workflow-orchestration

## The Problem
VA Community Care payments arrive 60-90 days after service, significantly slower than commercial payers (14-30 days). During this window, practitioners have no visibility into claim status — the VA portal doesn't provide real-time payment tracking for community providers. Claims can be silently denied, lost in processing, or held for additional documentation with no notification. Practitioners discover unpaid claims only during manual reconciliation, often 90-120 days after service when the re-submission window is closing.

## Why It's Still Broken
VA's payment infrastructure was built for internal VA facilities, not for tracking thousands of community provider claims. The Community Care program scaled faster than VA's payment processing systems. Community providers cannot access the same claim-status tools available to VA staff. VA has acknowledged the problem but prioritizes system upgrades for higher-volume provider types (primary care, mental health) over acupuncture.

## What a Fix Looks Like
A payment tracking dashboard that: (1) logs every VA claim submitted with expected payment date, (2) flags claims that exceed the normal payment window (45 days for initial alert, 75 days for escalation), (3) auto-generates follow-up inquiries to VA payment centers for overdue claims, (4) reconciles received payments against submitted claims to identify underpayments, and (5) produces monthly AR aging reports specific to VA receivables. Data sourced from EHR billing records and VA remittance advices (835s when available, manual entry when not).

## Who Feels the Pain
Solo and small-group acupuncturists carrying $15,000-40,000 in VA receivables at any given time, with no visibility into when or whether payment will arrive.

## Impact If Fixed
Recovers 10-15% of VA revenue currently lost to untracked denials and expired re-submission windows, and reduces cash flow uncertainty that causes some practitioners to stop accepting VA patients entirely.
