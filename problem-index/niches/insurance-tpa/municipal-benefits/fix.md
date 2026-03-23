# Multi-Tier Union Benefits Eligibility Chaos

**Niche:** [[niches/insurance-tpa/municipal-benefits/profile|Municipal & Public Entity Benefits]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Fix (Pain Point)
**One-liner:** Municipal employees move between bargaining units, change seniority tiers, and retire under different benefit schedules — and the TPA's eligibility system can't track which plan design applies to whom at any given point.
**Tags:** #data-integration #compliance #workflow-orchestration

## The Problem
A police officer hired in 2008 under CBA version 3 who promoted to sergeant (different bargaining unit) in 2015 under CBA version 5, then retired in 2024 under CBA version 7, may have retiree benefits defined by any combination of these agreements depending on vesting rules and benefit accrual provisions. TPA eligibility systems track current coverage but not the historical chain of bargaining unit assignments and CBA versions that determine what benefits the member earned. When a retiree files a claim, the eligibility analyst must manually research which plan applies by pulling HR records, CBA documents, and benefit accrual calculations.

## Why It's Still Broken
TPA systems are designed for commercial employer groups where plan changes apply uniformly to all members on a specific date. Municipal benefits require member-level tracking of bargaining unit history, CBA version applicability, and benefit accrual — a fundamentally different data model. Building this requires integration with the municipality's HR/payroll system (often a legacy HRIS like Tyler Munis or ADP) that tracks job classification changes, and mapping those changes to benefit eligibility rules in each CBA version.

## What a Fix Looks Like
A member-level benefits timeline that records every job classification change, bargaining unit assignment, and CBA version applicable to each member from hire through retirement. When a claim is submitted, the system automatically determines the correct plan design by traversing this timeline. Integrates with the municipality's HRIS to capture job changes in real-time rather than relying on manual eligibility file updates.

## Who Feels the Pain
TPA eligibility analysts spend 2-4 hours per retiree claim researching the applicable benefit design. Municipal HR directors field angry calls from retirees whose claims are denied or underpaid because the wrong plan design was applied.

## Impact If Fixed
Eliminates 80% of retiree eligibility research time (200-500 hours per year for a TPA managing 10 municipal clients). Reduces retiree claim adjudication errors by 90%, preventing grievances that cost $5,000-$20,000 each to resolve through arbitration.
