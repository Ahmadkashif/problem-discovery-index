# Utility Incentive and Rebate Matching

**Industry:** [[energy-auditors|Energy Auditors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rebate databases exist but cannot automatically match a specific building's conditions and proposed measures to the exact incentives it qualifies for across overlapping federal, state, utility, and municipal programs.
**Tags:** #bert #transformers #attention-mechanisms #word-embeddings #transfer-learning #feature-engineering #large-language-models #data-integration

## The Problem
Energy auditors must identify which rebates and incentives apply to each specific retrofit recommendation — IRA tax credits, state energy office programs, utility demand-side management incentives, municipal weatherization grants, and income-qualified programs all have different eligibility criteria, measure specifications, and application deadlines. An auditor proposing attic insulation, air sealing, and a heat pump for a specific home in a specific utility territory might qualify for 4-6 overlapping programs, each with different paperwork. Missing an applicable incentive costs the homeowner money and reduces the auditor's close rate; claiming an inapplicable one wastes time on rejected applications.

## What Already Exists
DSIRE (Database of State Incentives for Renewables & Efficiency) and EnergySage list available programs by state and utility territory. Rewiring America's calculator handles IRA credits. These are lookup tools — the user must manually read program requirements and determine whether a specific building and proposed measure set qualifies. None ingest actual audit data and output a matched incentive package.

## The Customisation Gap
Program eligibility depends on building-specific factors the generic databases do not process: exact insulation R-value being installed (not just "insulation"), equipment AHRI certificate numbers, income verification for low-income programs, building vintage, climate zone, and whether the measure is part of a whole-home package or standalone. The matching system must parse program requirement documents (which are written in inconsistent regulatory language across hundreds of utilities), extract structured eligibility rules, and evaluate them against the specific audit data — then produce pre-filled application forms.

## Impact If Solved
Auditors capture an additional $2,000-8,000 in incentives per project that they currently miss or do not pursue due to research time. Homeowner project ROI improves, driving higher close rates and larger average project sizes for the auditing firm.
