# Untracked Out-of-Scope Work on Managed Contracts

**Niche:** [[niches/it-managed-services/billing-reconciliation/profile|Client Billing Reconciliation and Contract Compliance]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians perform project-level work (server migrations, network redesigns, new employee setups beyond contract scope) on managed clients without creating billable tickets — giving away $100K-$300K in annual labor.
**Tags:** #automation #revenue-impact #workflow-orchestration #worker-facing

## The Problem
Managed service agreements define a scope of included services: monitoring, patching, basic troubleshooting, help desk support. But technicians routinely perform work that falls outside the agreement scope without creating a separate billable ticket: setting up a new conference room AV system ("while you're here, can you..."), migrating a department to a new server, configuring a new application stack, or spending 4 hours troubleshooting a legacy LOB application that the agreement explicitly excludes. Technicians do not flag out-of-scope work because they want to maintain client relationships, they are not sure where the scope boundary is, or the process for creating a separate billable ticket is cumbersome.

## Why It's Still Broken
The scope boundary lives in the agreement text (often 10-15 pages of legal language that no technician reads), and the day-to-day interpretation is left to the service manager's judgment. There is no system that, when a technician opens or works on a ticket, checks the ticket's issue type against the client's agreement scope and flags it as potentially out-of-scope. The PSA knows the agreement terms and the ticket category, but these two data sets are not connected in real-time. The result: technicians perform billable work at no charge, and the MSP only discovers the revenue leak when the service manager manually reviews time entries — a review that happens inconsistently.

## What a Fix Looks Like
A scope-checking layer in the PSA that compares each ticket's issue category and time entry against the client's agreement scope at the time of entry. When a technician logs time on a ticket that falls outside the agreement scope (e.g., "new workstation setup" when the agreement covers "monitoring and break/fix only"), the system alerts the technician and offers two paths: "This appears to be out-of-scope. Create a separate billable ticket? Or mark as goodwill/included?" The service manager receives a weekly report of all out-of-scope work performed, with the dollar value of unbilled labor, enabling a data-driven conversation about scope creep.

## Who Feels the Pain
MSP owners who suspect they are giving away significant labor on managed contracts but cannot quantify the problem, and service managers who are surprised to learn that a "simple managed client" consumed 40 hours of project-level work last quarter without generating any additional billing.

## Impact If Fixed
Captures 30-50% of currently unbilled out-of-scope work, recovering $100K-$300K annually at a mid-size MSP. Establishes clear scope boundaries that protect both the MSP's margins and the client relationship by making out-of-scope work explicit rather than hidden.
