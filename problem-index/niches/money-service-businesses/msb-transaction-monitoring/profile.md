# MSB Transaction Monitoring & SAR Operations

**Parent Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to resolve each sender across agents, brands and name spellings into one person before a structuring alert is worked, and whoever resolves senders most accurately takes the account.

## Profile
**Market Size:** ~$800M a year on monitoring software, BSA analysts and outsourced investigations at US MSBs (estimate)
**Share of Parent Industry:** ~7% of MSB revenue (estimate)
**Digital Adoption:** Medium — monitoring is automated, but sender linking, investigation and narrative writing are manual
**Target Buyer:** BSA/AML Officer
**Automation Potential:** High for entity resolution, alert triage and narrative drafting; the filing decision stays with the BSA officer

## What Makes This a Distinct Niche
MSB monitoring differs from bank monitoring in its unit of analysis. Banks monitor accounts; most remittance senders have no account, so the transmitter must work out who the person is from names, IDs and phones typed at many counters, often transliterated from non-Latin scripts. Structuring across agents, receiver fan-in, and agent-assisted splitting are the core typologies, and the MSB-specific thresholds — SARs on $2,000 or more, due within 30 days of detection under 31 CFR 1022.320, and (estimate) $3,000 for transfer recordkeeping — differ from banks'. Geographic targeting orders, such as FinCEN's 2025 Southwest Border order at a $200 CTR threshold before it was enjoined, land on MSBs specifically. The bank-side equivalents are covered under [[niches/community-banks/bsa-alert-case-operations/profile|BSA/AML Alert & Case Operations]] and [[niches/credit-unions/bsa-aml-compliance-ops/profile|BSA/AML Compliance Operations]].

## Current Tools & Gaps
Alessa (MSB-specific monitoring and CTR/SAR population), Unit21, Hummingbird for case management and filing, in-house engines at the large transmitters, and sanctions screening data. Gaps: sender resolution done by analysts with search screens; SAR narratives written from scratch; monitoring rules tuned to alert counts, not outcomes.

## Problems
- [[niches/money-service-businesses/msb-transaction-monitoring/build|🔨 Build: Sender Resolution Across Agents and Scripts]]
- [[niches/money-service-businesses/msb-transaction-monitoring/buy|🛒 Buy: Bank Case Management Tuned to MSB Thresholds]]
- [[niches/money-service-businesses/msb-transaction-monitoring/fix|🔧 Fix: Targeting-Order CTRs Filed by Hand]]
