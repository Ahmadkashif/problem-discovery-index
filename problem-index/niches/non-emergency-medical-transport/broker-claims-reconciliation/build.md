# Multi-Broker Claims Reconciliation Engine

**Niche:** [[niches/non-emergency-medical-transport/broker-claims-reconciliation/profile|Broker Claims Reconciliation]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically matches submitted NEMT trip claims against broker remittance payments across multiple brokers, identifying underpayments, denials, and missing payments.
**Tags:** #automation #data-integration #revenue-impact #ai-platform

## The Problem
An NEMT provider contracting with 3 brokers submits 4,000 claims per month and receives remittance files in 3 different formats (CSV, PDF, broker portal export) with different field names, status codes, and payment cycles. The billing manager must: download remittance data from each broker portal, normalize it into a comparable format, match each payment to the original claim submission, identify claims that were paid correctly, paid at the wrong rate, denied, or not included in the remittance at all, and then investigate each discrepancy. A single billing specialist can reconcile approximately 150-200 claims per day — meaning a 4,000-claim month requires 20-25 dedicated working days of reconciliation.

## Why Nobody Has Built This
Each NEMT broker uses a proprietary data format, denial code taxonomy, and payment schedule. Building a reconciliation engine requires parsing and normalizing data from 5-8 major brokers, mapping their denial codes to a common taxonomy, and handling the edge cases (partial payments, retroactive adjustments, batch denials for authorization issues). The broker landscape is also not static — brokers merge, states change broker contracts, and portals are updated without notice. Maintaining integrations across a fragmented broker ecosystem is an ongoing engineering cost that small NEMT software vendors have not been willing to bear.

## What to Build
A reconciliation platform that ingests trip claim data from the provider's billing system and remittance data from each broker (via API, portal scraping, or file upload), matches claims to payments using authorization numbers and trip details, and surfaces discrepancies in a dashboard: underpayments (paid but at wrong rate), denials (with standardized reason codes and recommended actions), missing payments (submitted but not in any remittance), and overpayments (rare but compliance-relevant). The platform generates appeal packages for denied claims with supporting documentation auto-attached.

## Target Customer
NEMT providers submitting 1,000+ claims per month across 2+ brokers who currently dedicate 1-2 full-time billing staff to manual reconciliation.

## Impact If Built
Reduces reconciliation time from 20-25 staff-days per month to 2-3 days of exception review, recovers 5-10% of revenue currently lost to undetected underpayments and uncontested denials ($50K-$300K annually per provider), and frees billing staff to focus on denial prevention rather than payment chasing.
