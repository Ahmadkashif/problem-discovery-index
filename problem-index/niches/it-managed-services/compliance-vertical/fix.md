# Compliance Gap Discovery Between Policy Documentation and Actual Implementation

**Niche:** [[niches/it-managed-services/compliance-vertical/profile|Compliance-Heavy Vertical MSPs]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Fix (Pain Point)
**One-liner:** MSPs document compliance policies that say "all endpoints have full-disk encryption" while 15% of actual endpoints have BitLocker disabled — and nobody discovers the gap until an auditor or a breach exposes it.
**Tags:** #anomaly-detection #automation #compliance #data-integration #worker-facing

## The Problem
Compliance-focused MSPs create security policies for each client: "all endpoints encrypted," "MFA enabled for all users," "patches applied within 14 days of release," "backups tested monthly." These policies are documented in compliance platforms and presented to auditors. But the reality on the ground drifts from the documented state: a new laptop is deployed without BitLocker because the technician forgot, a user's MFA is disabled during a support call and never re-enabled, a patch fails on 5 machines and no one follows up, a backup test is skipped during a busy month. The gap between documented compliance and actual compliance is invisible until an audit reveals it or a breach exploits it. For a healthcare MSP, this gap represents direct HIPAA liability; for a CMMC MSP, it can cost the client their certification.

## Why It's Still Broken
Compliance documentation and operational systems are disconnected. The compliance policy says "all endpoints encrypted" in a Compliancy Group checklist. BitLocker status is available in the RMM (ConnectWise Automate, Datto). But no system continuously compares the policy assertion against the operational reality across all clients. Compliance is treated as a periodic exercise (annual assessment, quarterly review) rather than a continuous monitoring function. Between assessments, drift accumulates silently.

## What a Fix Looks Like
A continuous compliance drift detector that maps each policy assertion to a verifiable data source in the MSP's operational tools and checks continuously: "Policy says all endpoints encrypted → check BitLocker status in RMM for every device → flag any devices where BitLocker is not active." The system generates a drift report showing policy vs. reality for each control, with severity scoring (a single unencrypted laptop with ePHI is critical; a missing patch on a non-sensitive workstation is low). Drift alerts are sent to the compliance lead with remediation instructions. The system runs daily, not annually, turning compliance from a point-in-time exercise into continuous assurance.

## Who Feels the Pain
Compliance practice leads who stake their professional reputation on assertions that they cannot continuously verify, and MSP owners who carry liability when a documented control turns out to be absent.

## Impact If Fixed
Catches 90%+ of compliance drift within 24 hours of occurrence instead of discovering it during annual audits. Reduces audit findings by 60-80% and prevents the breach-plus-compliance-gap scenario that can cost an MSP $50K-$500K in HIPAA penalties and client loss.
