# Broker Claims Reconciliation

**Parent Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1.5-2B (claims processing services and embedded costs)
**Share of Parent Industry:** Cross-cutting billing function affecting all Medicaid-funded providers
**Digital Adoption:** Low-Medium — Brokers provide portals for claim submission, but reconciliation between provider trip records and broker payment records is done manually in spreadsheets
**Target Buyer:** Billing manager / revenue cycle director / NEMT provider owner
**Automation Potential:** High — Claims reconciliation is a matching problem between two structured data sets (provider trip records vs. broker payment records) with deterministic rules — ideal for automation

## What Makes This a Distinct Niche
NEMT providers submit trip claims to transportation brokers (Modivcare, LogistiCare/ModivCare, MTM, Access2Care) who manage Medicaid transportation benefits on behalf of state Medicaid programs. The provider completes a trip, submits a claim with trip details (patient, date, times, miles, authorization number), and expects payment at the contracted rate. In practice, 15-25% of claims are denied, short-paid, or delayed — often for reasons the provider only discovers weeks later when the remittance arrives. Reconciling what was submitted, what was paid, what was denied, and why requires manually comparing provider trip records against broker remittance files line by line. For a 50-vehicle provider submitting 3,000-5,000 claims per month, this reconciliation takes 20-40 hours of billing staff time.

## Current Tools & Gaps
Broker portals (Modivcare's provider portal, MTM's portal) allow claim submission and show claim status, but each broker has a different format, different status codes, and different denial reason taxonomies. Accounting software (QuickBooks, Sage) records payments but cannot parse broker remittance files. NEMT billing software (TripMaster, CTS) generates claims but does not track post-submission lifecycle. No tool aggregates claims across multiple brokers, matches payments to submissions, identifies discrepancies, and generates denial appeal packages.

## Problems
- [[niches/non-emergency-medical-transport/broker-claims-reconciliation/build|🔨 Build: Multi-Broker Claims Reconciliation Engine]]
- [[niches/non-emergency-medical-transport/broker-claims-reconciliation/buy|🛒 Buy: Denial Pattern Analysis and Auto-Appeal]]
- [[niches/non-emergency-medical-transport/broker-claims-reconciliation/fix|🔧 Fix: Remittance File Parsing Across Broker Formats]]
