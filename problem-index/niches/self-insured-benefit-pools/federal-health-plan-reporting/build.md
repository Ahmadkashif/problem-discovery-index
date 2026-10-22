# One Data Map for Every Federal Filing

**Niche:** [[niches/self-insured-benefit-pools/federal-health-plan-reporting/profile|Federal Health Plan Reporting & Attestations]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each federal filing is assembled separately from the same vendor data, so a fund re-collects and re-reconciles its own numbers several times a year.
**Tags:** #large-language-models #feature-engineering #data-integration #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to assemble each federal health plan filing from data held by the fund's TPA, PBM and carve-out vendors before its statutory date, and whoever files on time with no vendor data gaps takes the account.

## The Problem
RxDC, 5500 schedules, parity data requests and ACA reporting each pull enrolment, premium-equivalent, claims and vendor fees from overlapping sources, with different definitions. Each is built from scratch by whoever owns it that season.

## Why Nobody Has Built This
Every vendor files its own piece and has no reason to integrate with the others. The fund, the only party that needs the whole picture, rarely has technical staff.

## What to Build
A fund-level data map: each vendor's extract mapped once to a common model of members, months, plans, claims and fees, with LLM-assisted mapping of new file layouts. Every federal filing is generated from that model with lineage to source rows, a calendar of obligations, and automated requests and reminders to vendors.

## Target Customer
Fund administrators and TPAs serving multiemployer health funds, VEBAs and public health pools.

## Impact If Built
Filings built once from reconciled data, on time, with an audit trail the plan auditor and the DOL can follow.
