# Wave 4 — Client–Server & ERP (1992–2000)

**Trigger:** SAP R/3 released July 6 1992 — the three-tier client-server rewrite of mainframe R/2 (1979), itself following R/1 (1972)
**What went to ~zero:** the cost of one company holding **one version of its own numbers**
**Failure class produced:** the missing join, industrialised — and then sold back as an integration product

## What Was True The Day Before

By 1990 a large company had computerised in pieces, over thirty years, department by department. Finance ran one system, manufacturing another, sales a third, payroll a fourth. Each was internally correct and mutually contradictory. Asking "what did this customer cost us to serve?" meant asking four systems and reconciling by hand, and the answer was different every time.

Waves 1 and 2 had made each department's data cheap. Nobody had made the *company's* data coherent.

## The Trigger

SAP R/3 moved the enterprise suite onto three tiers — database, application, presentation — running on commodity servers instead of a mainframe. The architecture mattered, but the commercial proposition mattered more: **one data model for the whole company**, with the modules forced to agree because they wrote to the same tables.

Baan, PeopleSoft, JD Edwards and Oracle Applications all expanded into the same opening.

## What Became Possible

A company could close its books in days instead of weeks, cost a product accurately, and answer cross-functional questions without a reconciliation project. The step change was not a capability — it was **the absence of argument about whose number was right**.

And because the schema was shared, work could cross company boundaries too. EDI turned purchase orders into messages, which is what made modern third-party logistics and contract manufacturing structurally possible.

## The Competitive Fight

The fight was **who owns the system of record**, and it was understood at the time to be winner-take-most. Whoever's schema the company's data lived in controlled the roadmap, the integration tax and the exit cost for a decade or more. ERP vendors priced accordingly, and implementation partners built an industry on the gap between what was sold and what was configured.

This is where the modern software moat was invented: not features, but **the cost of leaving**.

## What It Broke

Three things, and all three are still generating revenue for someone in this vault.

**Integration became permanent.** One vendor never covered everything, so the promise of one data model produced, in practice, a hub with a permanent perimeter of connections to things it did not cover. The integration tax was not a transitional cost. It is the steady state.

**The schema became the politics.** Once the data model is shared, changing it requires consent from every department that reads it. Systems ossified — not for technical reasons but because the schema became a treaty.

**The record moved further from the work.** ERP is excellent at what was transacted and poor at what was *decided*. The decision — why this price, why this vendor, why this exception — stayed in mail, meetings and spreadsheets. The vault documents the consequence in almost every industry: a complete record of outcomes and no record of the reasoning that produced them.

## Children in This Vault

**Primary:**
- [[industries/food-distributors|Food Distributors]]
- [[industries/restaurant-suppliers|Restaurant Suppliers]]
- [[industries/auto-body-shops|Auto Body Shops]]
- [[industries/auto-repair-shops|Auto Repair Shops]]
- [[industries/database-platform-vendors|Database Platform Vendors]]
- [[industries/oil-gas-field-services|Oil & Gas Field Services]]
- [[industries/mortgage-brokers|Mortgage Brokers]]
- [[industries/ap-automation-vendors|AP Automation Vendors]]
- [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
- [[industries/insurance-restoration|Insurance Restoration]]
- [[industries/compliance-consulting|Compliance Consulting Firms]]
- [[industries/customs-brokers|Customs Brokers]]
- [[industries/freight-brokerage|Freight Brokerage]]
- [[industries/warehouse-3pl|Warehouse & 3PL]]
- [[industries/medical-supply-retail|Medical Supply Retail]]
- [[industries/utility-contractors|Utility Contractors]]
- [[industries/charter-bus-operators|Charter Bus Operators]]
- [[industries/digital-forensics-firms|Digital Forensics Firms]]

**Secondary:**
- [[industries/fleet-managers|Fleet Managers]]
- [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
- [[industries/revops-consultancies|RevOps Consultancies]]
- [[industries/saas-implementation-partners|SaaS Implementation Partners]]
- [[industries/independent-insurance-agents|Independent Insurance Agents]]
- [[industries/spend-management-platforms|Spend Management Platforms]]
- [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
- [[industries/crm-platforms|CRM Platforms]]
- [[industries/hr-tech-platforms|HR Tech Platforms]]
- [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
- [[industries/contract-manufacturing|Contract Manufacturing]]
- [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
- [[industries/food-manufacturing|Food Manufacturing]]
- [[industries/medical-device-mfg|Medical Device Manufacturing]]
- [[industries/nonprofits-social-services|Social Services Nonprofits]]
- [[industries/it-managed-services|IT Managed Services]]
- [[industries/owner-operator-trucking|Owner-Operator Trucking]]
- [[industries/cold-chain-logistics|Cold Chain Logistics]]
- [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
- [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
- [[industries/freight-tech-platforms|Freight Tech Platforms]]

**Origins:** [[origins/semiconductor-fabs/profile|Semiconductor Fabs]] · [[origins/telecom-carriers/profile|Telecom Carriers]]

**Sources:** SAP corporate history, 1991–2000; itsiti.com, SAP R/3 history and release timeline; Wikipedia, *SAP R/3*, *Enterprise resource planning*.
