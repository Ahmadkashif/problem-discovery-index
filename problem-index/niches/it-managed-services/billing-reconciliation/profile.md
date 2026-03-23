# Client Billing Reconciliation and Contract Compliance

**Parent Industry:** [[industries/it-managed-services|IT Managed Services]]
**Category:** Highly Automatable

## Profile
**Market Size:** $6-10B (embedded cost across all MSPs)
**Share of Parent Industry:** Embedded function — billing operations represent 10-15% of MSP operating cost
**Digital Adoption:** Medium — PSA platforms generate invoices, but reconciliation between what is contracted, what is deployed, and what is billed is manual
**Target Buyer:** CFO or operations manager at an MSP with 100+ managed clients generating per-device or per-user billing
**Automation Potential:** High — the reconciliation logic is deterministic (contracted vs. deployed vs. billed), and the data sources are digital (PSA, RMM, contracts)

## What Makes This a Distinct Niche
MSP billing is uniquely complex: contracts may specify per-device, per-user, or flat-rate pricing with tiered inclusions (basic monitoring included, security add-on at $X/endpoint, project work at hourly rates). The MSP must reconcile three data sources every billing cycle: the contract (what they agreed to provide and charge), the RMM (what is actually deployed and monitored), and the PSA (what is being invoiced). Discrepancies are common: a client adds 5 workstations but the MSP does not update the invoice; a security add-on is deployed but never billed; a client removes users but the contract count is not adjusted. Revenue leakage from under-billing is typically 3-8% of gross revenue, and over-billing creates client trust issues when discovered.

## Current Tools & Gaps
PSA platforms (ConnectWise, Datto/Autotask) generate invoices from agreement records. Gradient MSP specifically addresses billing reconciliation. RMM platforms track deployed agents and devices. The gap is automated reconciliation: no tool continuously compares the contract's device/user count and service scope against the RMM's actual deployment data and the PSA's billing records to identify discrepancies.

## Problems
- [[niches/it-managed-services/billing-reconciliation/build|🔨 Build: Continuous Contract-to-Deployment-to-Invoice Reconciliation Engine]]
- [[niches/it-managed-services/billing-reconciliation/buy|🛒 Buy: RMM-to-PSA Asset Count Synchronization]]
- [[niches/it-managed-services/billing-reconciliation/fix|🔧 Fix: Untracked Out-of-Scope Work on Managed Contracts]]
