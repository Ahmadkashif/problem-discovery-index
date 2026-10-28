# A Rebate Claim Desk That Never Misses Day 45

**Niche:** [[niches/community-health-centers/restricted-manufacturer-340b-recovery/profile|Restricted-Manufacturer Claims Data & 340B Rebate Claims]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** From January 2027 a health center pays full price for 25 common drugs, including Eliquis, Jardiance and Ozempic, and must claim the 340B rebate within 45 days of each dispense, a new workflow that no existing system runs.
**Tags:** #feature-engineering #descriptive-statistics #workflow-orchestration #revenue-impact #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to recover the 340B discount on restricted manufacturers' drugs through their claims-data conditions and, from January 2027, the rebate pilot, and whoever recovers the most 340B savings per eligible restricted-drug prescription takes the account.

## The Problem
Every eligible dispense of a pilot drug becomes a receivable with a 45-day filing deadline and a 10-day manufacturer payment clock (Holland & Knight). Missed or incomplete claims are lost savings.

## Why Nobody Has Built This
The pilot was enjoined at the end of 2025 and reissued in August 2026, so vendors waited. Each approved manufacturer can set its own data portal within HRSA's limits.

## What to Build
A desk that picks out pilot-drug dispenses from in-house and contract pharmacy data, checks eligibility, builds each manufacturer's claim file, submits it, tracks the 45-day and 10-day clocks, and posts rebates against the receivable. It produces a denial worklist with the evidence each manufacturer asked for.

## Target Customer
Health centers with in-house pharmacies dispensing the pilot drugs, and the administrators serving them.

## Impact If Built
If pilot drugs carry ~$400,000 of a center's annual 340B savings (estimate), a 5% miss rate on day-45 deadlines is ~$20,000 lost a year, before denials.
