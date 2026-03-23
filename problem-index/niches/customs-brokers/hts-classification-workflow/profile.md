# HTS Classification Workflow

**Parent Industry:** [[industries/customs-brokers|Customs Brokers]]
**Category:** Highly Automatable

## Profile
**Market Size:** $300-500M (embedded)
**Share of Parent Industry:** ~8% (embedded operational cost)
**Digital Adoption:** Medium — classification analysts use HTS databases (Descartes, USITC) and CBP's CROSS ruling database, but the classification reasoning process itself is manual, undocumented, and locked in individual analysts' expertise
**Target Buyer:** Classification team lead or tariff specialist at customs brokerages
**Automation Potential:** High — for 60-70% of products that fall into clear HTS categories, classification can be automated or semi-automated with confidence scoring; the remaining 30-40% require expert judgment but can be accelerated with prior ruling lookup

## What Makes This a Distinct Niche
HTS classification — assigning the correct 10-digit tariff code to each imported product — is the core technical function of customs brokerage. It determines the duty rate, any special tariff applicability, and quota/licensing requirements. Classification for a new product requires: reading the product description, identifying its essential character, navigating the HTS hierarchy (section → chapter → heading → subheading → statistical suffix), checking the General Rules of Interpretation, and researching CBP rulings for similar products. An experienced classification analyst classifies familiar products in 2-3 minutes; a novel product requiring GRI analysis and CROSS ruling research takes 15-45 minutes. The classification decision is also the primary compliance risk: misclassification that results in underpayment of duty can trigger CBP penalties of up to 4x the unpaid duty.

## Current Tools & Gaps
Descartes CustomsInfo provides HTS database search. USITC provides the official online HTS. CBP's CROSS database provides binding rulings. No tool combines these sources into a classification recommendation workflow that suggests the most likely HTS code from a product description, surfaces relevant CROSS rulings, and provides a confidence score and audit trail for the classification decision.

## Problems
- [[niches/customs-brokers/hts-classification-workflow/build|🔨 Build: ML-Assisted HTS Classification with Ruling Citation]]
- [[niches/customs-brokers/hts-classification-workflow/buy|🛒 Buy: Classification Decision Audit Trail & Quality Review]]
- [[niches/customs-brokers/hts-classification-workflow/fix|🔧 Fix: Classification Inconsistency Across Analysts]]
