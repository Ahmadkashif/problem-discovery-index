# HRSA Audit Readiness with Continuous Compliance Monitoring

**Niche:** [[niches/pharmacy-independents/340b-contract-pharmacy/profile|340B Contract Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** When HRSA audits a 340B contract pharmacy, the pharmacy must produce documentation proving each sampled claim was for an eligible patient with a qualifying prescription — but most pharmacies assemble this documentation retrospectively in a multi-week scramble because no system maintains continuous compliance records.
**Tags:** #logistic-regression #feature-engineering #compliance #automation #data-integration

## The Problem
HRSA audits of 340B contract pharmacy arrangements have increased significantly since 2020, driven by manufacturer complaints about contract pharmacy proliferation. An audit typically samples 30-50 claims and requires the pharmacy to produce: (1) proof the patient was registered with the covered entity at the time of dispensing, (2) proof the prescription was written by a provider associated with the entity, (3) proof the NDC was eligible under the contract (not manufacturer-restricted), and (4) proof the claim was not "double-dipped" — that the 340B savings were not claimed alongside Medicaid rebates or other discount programs. Most pharmacies cannot produce this documentation easily because eligibility records are held by the TPA or covered entity, prescriber-entity associations are maintained in HRSA's database (which the pharmacy may not have queried at the time of dispensing), and manufacturer restriction records are not systematically tracked. The pharmacy scrambles for 2-4 weeks to assemble documentation, pulling the pharmacist and owner away from revenue-generating activities.

## Why It's Still Broken
Continuous compliance monitoring requires real-time data feeds from multiple parties: the covered entity (patient eligibility), the TPA (claim processing records), HRSA (covered entity registration and provider associations), and manufacturers (restriction notices). No single party has incentive to build this integration — the TPA's liability exposure is limited, the covered entity manages its own compliance separately, and HRSA provides audit guidance but not compliance tools. The pharmacy is the most audit-exposed party but has the least access to the data needed for continuous compliance verification.

## What a Fix Looks Like
An always-on compliance monitoring system that: (1) maintains a local cache of the covered entity's patient eligibility list with daily or weekly refresh, flagging patients whose eligibility has lapsed, (2) tracks prescriber-entity associations against HRSA's database, alerting when a prescriber's association changes, (3) monitors manufacturer 340B restriction announcements and flags affected claims, (4) runs Medicaid duplicate discount checks against state Medicaid exclusion files, and (5) generates an "audit readiness score" showing the percentage of recent 340B claims with complete, defensible documentation. When an HRSA audit notification arrives, the pharmacy produces a pre-assembled documentation package for each sampled claim within hours instead of weeks. A logistic regression model scores each claim's audit vulnerability at the time of processing, allowing the pharmacy to proactively resolve documentation gaps before they become audit findings.

## Who Feels the Pain
The pharmacy owner who faces personal liability for 340B program violations (repayment demands of $100,000-500,000+), and the pharmacist-in-charge who spends 40-80 hours preparing for an HRSA audit while simultaneously maintaining normal pharmacy operations.

## Impact If Fixed
Reduces HRSA audit preparation time from 2-4 weeks of intensive documentation assembly to 2-3 hours of pre-assembled package review. Eliminates the most common audit findings — inability to document patient eligibility and prescriber-entity association — which together account for 60-70% of adverse audit outcomes. Provides continuous compliance visibility that catches documentation gaps in real time rather than discovering them during an audit.
