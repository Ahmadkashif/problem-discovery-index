# Identity Governance Extended to Non-Employees

**Niche:** [[niches/hr-tech-platforms/contingent-workforce-management/profile|Contingent Workforce Management]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Identity governance products manage joiner-mover-leaver lifecycles, access certification and orphaned account detection as a mature discipline, and they are driven off an HR system that contains only employees.
**Tags:** #graph-theory #data-integration #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #descriptive-statistics
**Contested on:** Every serious competitor in contingent workforce software is fighting to give an employer one accurate view of everyone doing work for it, employee or not — and whoever can state total workforce and its classification exposure takes the account.

## The Problem
Identity governance works well for employees: a hire in the HCM system provisions access, a role change adjusts it, a termination revokes it, and periodic certification confirms it. A contractor is onboarded by a manager raising a ticket, receives access provisioned manually, is never in the HCM system, and when the engagement ends nobody triggers anything — so their access persists. Orphaned contractor accounts are among the most common findings in access reviews and the most common vector in several well-documented breach patterns, and the cause is that the authoritative source for the identity lifecycle excludes half the population.

## What Already Exists
Identity governance and administration platforms — SailPoint, Saviynt, Okta's governance products and their competitors — provide lifecycle management, access request and certification, segregation of duties and orphaned account detection, all mature. HR-driven provisioning is a standard integration pattern. Vendor management systems hold agency worker records. The capability is fully developed and is simply pointed at an incomplete source.

## The Customization Gap
The adaptation is to an identity population with no single authoritative source. It requires: (1) an authoritative non-employee worker record with a defined owner, which is the foundational organisational change — someone must be accountable for the record's accuracy the way HR is for an employee's; (2) engagement end dates as mandatory and enforced, since contractor engagements routinely have no recorded end and the absence is what produces persistent access — a default expiry with explicit renewal is the single most effective control available here; (3) sponsor attestation rather than manager attestation, since a contractor's internal sponsor may not be a people manager and the certification workflow assumes one; (4) supplier-mediated lifecycle where the worker comes through an agency, so that the agency's own offboarding triggers the client's deprovisioning, which requires a data exchange nobody currently has; and (5) reconciliation against what is actually provisioned, because the population most likely to have access without a record is exactly this one.

## Target Customer
Security and identity governance functions, HR and procurement leaders sharing the risk, and the identity and vendor management vendors on either side of the gap.

## Impact If Solved
Orphaned non-employee access is a well-known and persistent security exposure with an entirely administrative cause. Default engagement expiry with explicit renewal is a small change that addresses most of it, and it also produces the tenure data that the classification work in this niche depends on.
