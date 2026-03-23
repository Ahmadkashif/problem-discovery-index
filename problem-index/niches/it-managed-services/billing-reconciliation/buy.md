# RMM-to-PSA Asset Count Synchronization

**Niche:** [[niches/it-managed-services/billing-reconciliation/profile|Client Billing Reconciliation and Contract Compliance]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PSA-RMM integrations exist but sync ticket data and alerts, not asset counts — when a client adds or removes devices in the RMM, the PSA agreement count does not update, creating billing drift.
**Tags:** #automation #data-integration #quick-win #revenue-impact

## The Problem
ConnectWise Manage integrates with ConnectWise Automate, and Datto Autotask integrates with Datto RMM. These integrations sync alerts and tickets bidirectionally. But they do not automatically update the agreement's device count when a new device appears in the RMM or when a device is decommissioned. The device count in the agreement (which drives billing) is manually maintained, and it drifts from reality within weeks of any client environment change. Adding 3 workstations at a client? Someone needs to remember to update the agreement count. Decommissioning a server? The agreement still bills for it until someone notices.

## What Already Exists
Native PSA-RMM integrations (ConnectWise Manage to Automate, Datto Autotask to RMM) handle alert-to-ticket escalation and basic device record sync. Gradient MSP and Lifecycle Insights offer reconciliation and reporting features. Custom integrations can be built using APIs.

## The Customization Gap
The tool needs to go beyond device record sync to agreement count sync: when the RMM detects a new device at a client site (a new agent phones home), the system should automatically compare the current RMM device count against the PSA agreement count, identify the discrepancy, and either auto-adjust the agreement (for MSPs that bill on actual count) or generate an adjustment request for review (for MSPs that need to confirm with the client before changing billing). The system must handle the nuances: exclude personal devices from billing counts, distinguish between workstations and servers (different billing rates), and handle temporary devices (loaner laptops should not trigger permanent billing changes).

## Target Customer
MSP billing coordinators and operations managers who manually audit RMM-to-PSA device counts monthly, typically spending 5-10 hours catching and correcting discrepancies.

## Impact If Solved
Eliminates billing drift that accumulates between manual audits, recovering 2-4% of revenue lost to under-billing and preventing over-billing disputes. Reduces monthly billing audit time from 5-10 hours to 30 minutes of exception review.
