# AMS-Integrated Commission Tracking Module

**Niche:** [[niches/independent-insurance-agents/commission-reconciliation-ops/profile|Commission Reconciliation Operations]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AMS systems track policies and expected commissions, and accounting tools track payments, but no integration layer automatically reconciles expected vs. actual commissions across carriers.
**Tags:** #data-integration #automation #anomaly-detection #workflow-orchestration

## The Problem
Expected commission data lives in the AMS (policy premium x commission rate = expected commission). Actual commission payments arrive from carriers via direct deposit with separate statements. The bookkeeper must manually match actual payments to expected amounts, policy by policy, across every carrier. Discrepancies — a carrier paying 12% instead of the agreed 15%, a new business commission paid at renewal rate, a policy missing from the statement entirely — are discovered only through this tedious manual comparison.

## What Already Exists
AMS systems (Applied Epic, Vertafore AMS360, HawkSoft) all have commission tracking modules that store expected commission data. Accounting tools (QuickBooks, Xero) track actual deposits. AgencyBloc provides commission tracking for life and health agencies but not P&C. None of these tools automatically reconcile expected vs. actual by ingesting carrier statements and matching at the policy level.

## The Customization Gap
Insurance commission reconciliation requires understanding of producer splits (multiple producers on one account), contingency and bonus commissions (paid annually based on loss ratio), override commissions (paid to the agency on sub-producer business), and mid-term adjustments (endorsements, audits, cancellations that change the premium and therefore the commission). A generic payment reconciliation tool does not handle these insurance-specific commission structures.

## Target Customer
Agency principals and bookkeepers at agencies with $500K+ in annual commission revenue who currently spend 2-3 days per month on manual reconciliation.

## Impact If Solved
Reduces monthly reconciliation from 2-3 days to 2-3 hours. Identifies underpayments within 30 days instead of discovering them at year-end (or never), recovering an estimated 2-4% of commission revenue that agencies are currently losing to carrier payment errors.
