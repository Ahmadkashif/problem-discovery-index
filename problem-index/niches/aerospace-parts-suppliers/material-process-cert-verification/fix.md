# The Processor Whose Approval Lapsed Mid-Job

**Niche:** [[niches/aerospace-parts-suppliers/material-process-cert-verification/profile|Material & Special-Process Certification Verification]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** A plater or heat treater loses Nadcap accreditation or drops off a prime's approved list, and parts already sent there come back with certs that no longer count.
**Tags:** #data-integration #compliance #workflow-orchestration #automation #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to check every mill cert and special-process cert against the specification, the purchase order and the approved-processor list before material is cut, and whoever catches a non-conforming or falsified cert earliest in the chain takes the account.

## The Problem
Approved-processor status changes: an audit finding suspends a Nadcap accreditation, a prime removes a source for a specific process. Purchasing keeps sending work because the PO template hasn't changed. The problem appears when Form 2 is checked at FAI, or worse, at the customer's audit.

## Why It's Still Broken
Nobody watches accreditation status between jobs; PRI and customer lists are checked when a processor is added, not each time work is sent.

## What a Fix Looks Like
A daily check of every processor in open routings against Nadcap status in eAuditNet and each customer's approved-process-source list, with an alert to purchasing and quality before the next shipment out, and a flag on any lot processed after a lapse.

## Who Feels the Pain
Quality managers who discover the lapse at audit; production control, who must re-route lots; customers who receive parts processed by an unapproved source.

## Impact If Fixed
A daily status check costs almost nothing and avoids the scrap or rework of parts processed after a lapse, often a whole lot at ~$10,000–$100,000 (estimate).
