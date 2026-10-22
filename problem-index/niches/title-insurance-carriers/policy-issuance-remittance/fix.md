# Reissue Credits Calculated Three Different Ways

**Niche:** [[niches/title-insurance-carriers/policy-issuance-remittance/profile|Policy Issuance, CPLs & Premium Remittance]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** The same reissue credit is computed one way by the agent's production system, another by the underwriter's rate calculator and a third by the remittance processor, and every mismatch becomes a phone call.
**Tags:** #decision-trees #evaluation-metrics #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to make every policy and closing protection letter an agent issues arrive reported, correctly rated and remitted without rekeying, and whoever closes the gap between CPLs issued and policies remitted fastest takes the account.

## The Problem
Rate manuals give discounts for a recent prior policy (reissue), for simultaneous owner's and lender's policies, and for particular endorsements. Each system that calculates the premium encodes the rules slightly differently, so remittances arrive with small differences that someone must resolve.

## Why It's Still Broken
Rate manuals change by state and filing, production software vendors update on their own schedules, and no one maintains a single machine-readable version of each manual.

## What a Fix Looks Like
One machine-readable encoding of each state rate manual, versioned by effective date and published by the underwriter to its agents' production systems through an API, with a test suite that every vendor implementation must pass.

## Who Feels the Pain
Remittance processors, agents' accounting staff, and consumers overcharged or undercharged at closing.

## Impact If Fixed
Rating discrepancies largely disappear, and rate changes such as Texas's March 2026 cut roll out consistently on the effective date.
