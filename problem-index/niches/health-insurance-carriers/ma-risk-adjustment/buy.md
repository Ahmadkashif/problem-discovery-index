# Clinical Documentation Integrity Tools Run in Both Directions

**Niche:** [[niches/health-insurance-carriers/ma-risk-adjustment/profile|Medicare Advantage Risk Adjustment & RADV Defence]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hospitals already run documentation integrity software that reads notes and queries physicians about unsupported diagnoses; payer chart review uses similar NLP but mostly to add codes.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to submit every diagnosis a member's chart supports, and none it doesn't, before CMS's final submission deadline, and whoever keeps the most submitted diagnoses standing through a RADV medical-record review takes the account.

## The Problem
Retrospective chart review finds diagnoses documented in records but missing from claims. Under annual RADV, the more valuable finding is the reverse: a diagnosis on a claim that the record does not support, which the plan must delete. Review programmes and vendor contracts are built for the first and rarely do the second.

## What Already Exists
Hospital clinical documentation integrity and computer-assisted coding platforms, which read the record and generate queries; payer-side NLP coding tools from chart review vendors.

## The Customization Gap
The payer version must review in both directions with equal rigour, and report deletions as a first-class output. It needs: the CMS-HCC V28 hierarchy and the plan's model mix; documentation tests aligned with how RADV coders validate; outpatient records from thousands of practices rather than one hospital EHR; provider feedback loops that change documentation at source; and coder adjudication logs that show an auditor the plan looked for unsupported codes as hard as for missing ones.

## Target Customer
Risk adjustment operations leaders at MA plans renegotiating chart-review vendor contracts after the RADV expansion.

## Impact If Solved
A two-way review programme that a plan's compliance officer and CMS can both accept, and fewer recoveries found by someone else.
