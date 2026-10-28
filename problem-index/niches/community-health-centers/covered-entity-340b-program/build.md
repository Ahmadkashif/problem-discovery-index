# A 340B Savings Ledger Across Restrictions, Rebates and Audit Risk

**Niche:** [[niches/community-health-centers/covered-entity-340b-program/profile|340B at the Health Center (Covered-Entity Side)]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A health center's 340B savings are split across in-house dispensing, contract pharmacies, restricted manufacturers and, from 2027, rebates, and nobody can show by drug and pharmacy what was earned, what was lost and what carries audit risk.
**Tags:** #descriptive-statistics #feature-engineering #data-integration #compliance #revenue-impact #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep a health center's 340B savings intact, but recovering the discount on restricted manufacturers' drugs and limiting adverse findings in HRSA's covered-entity audits are separate contests, with different vendors, different staff and different winners. Decomposed into contested sub-niches below.

## The Problem
The administrator reports accumulations, the manufacturers report their conditions, and the CFO sees a savings line that falls each year without knowing why.

## Why Nobody Has Built This
Each administrator sees only its own contract pharmacies, and manufacturer conditions differ by company. The rebate pilot is new for 2027.

## What to Build
A ledger per prescription that records the eligibility determination, dispensing channel, manufacturer condition, price realised (ceiling, WAC or pending rebate) and Medicaid status. It rolls up to savings earned, savings lost and savings at risk. It feeds the two sub-niches' workflows: restricted-manufacturer recovery and audit defence.

## Target Customer
CFOs and 340B managers at centers with in-house pharmacies plus 5+ contract pharmacies.

## Impact If Built
If restrictions cost a mid-sized center ~$500,000 a year (estimate), seeing that loss by drug and pharmacy is the first step to recovering part of it.
