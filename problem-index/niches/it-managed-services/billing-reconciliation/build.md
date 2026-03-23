# Continuous Contract-to-Deployment-to-Invoice Reconciliation Engine

**Niche:** [[niches/it-managed-services/billing-reconciliation/profile|Client Billing Reconciliation and Contract Compliance]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product continuously reconciles what an MSP contracted to provide, what is actually deployed in the client environment, and what is being invoiced — discrepancies accumulate for months before anyone notices.
**Tags:** #automation #data-integration #anomaly-detection #revenue-impact #quick-win

## The Problem
An MSP contracts with a client for managed services on 50 workstations and 3 servers at $150/user/month. Six months later, the client has 58 workstations (8 added without notification), the RMM shows 55 agents deployed (3 machines with failed agents), and the invoice still reflects 50 units. The MSP is under-billing by 8 units ($1,200/month) and under-monitoring by 3 machines (creating security risk). This scenario plays out across 50-200 clients simultaneously, with each client having a slightly different discrepancy. The CFO discovers the aggregate under-billing during a quarterly review, but by then months of revenue have been lost and retroactive billing creates client friction.

## Why Nobody Has Built This
The reconciliation requires three-way matching across systems with different data models: the contract/agreement in the PSA defines the billing structure (per-device, per-user, tiered), the RMM tracks deployed agents and managed devices, and the invoice records what was actually billed. Each MSP's contract structure is different (some bill per device, some per user, some hybrid), and the PSA and RMM do not share a common device ID scheme. Building a reconciliation engine requires normalizing across these systems and encoding the contract logic for each client — a significant integration and business logic challenge.

## What to Build
A reconciliation engine that continuously (daily or weekly): pulls the contracted device/user counts and service tiers from the PSA agreement, compares against actual deployed devices and users from the RMM, checks that the current invoice matches the larger of contracted vs. deployed counts (or flags for review), identifies discrepancies by type (under-billed, over-billed, unmonitored devices, ghost devices), and generates adjustment recommendations. The system also detects contract violations: devices with no RMM agent (unmonitored risk), devices with the wrong security stack (wrong service tier), and users exceeding license counts.

## Target Customer
CFOs and operations managers at MSPs with 50+ managed clients billing on per-device or per-user contracts, where manual reconciliation happens monthly at best and revenue leakage accumulates between reviews.

## Impact If Built
Recovers 3-8% of gross revenue lost to under-billing ($150K-$500K annually at a $5M MSP), identifies unmonitored devices that represent security liability, and automates a reconciliation process that currently takes the CFO or billing team 15-25 hours per month.
