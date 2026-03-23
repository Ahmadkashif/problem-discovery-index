# Rebate & Incentive Matching Engines

**Parent Industry:** [[industries/energy-auditors|Energy Auditors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $200-400M (services and embedded workflow cost)
**Share of Parent Industry:** Cross-cutting function affecting all auditors who recommend measures to homeowners and building owners
**Digital Adoption:** Low-Medium — DSIRE and EnergySage provide rebate databases, but matching specific building conditions to specific available incentives is done manually by auditors
**Target Buyer:** Auditor / sales rep / program administrator
**Automation Potential:** High — Rebate eligibility is rule-based: if building meets criteria X and installs measure Y in utility territory Z, rebate R applies. The matching logic is deterministic but the number of programs and rules is overwhelming for manual lookup

## What Makes This a Distinct Niche
Energy efficiency incentives — utility rebates, federal tax credits (25C, 179D), state incentive programs, municipal grants, and green financing products — can reduce a homeowner's out-of-pocket cost by 30-70%. But identifying which incentives apply to a specific building's recommended measures requires tracking hundreds of overlapping programs with different eligibility criteria, measure specifications, application deadlines, and dollar amounts. An auditor in California must navigate PG&E rebates, SoCalGas rebates, Title 24 requirements, IRA Section 25C tax credits, CalHFA financing, and local government programs — each with different qualifying products, efficiency thresholds, and income limits. Auditors either miss available incentives (reducing the homeowner's financial motivation) or spend 1-2 hours per project researching applicable programs.

## Current Tools & Gaps
DSIRE (Database of State Incentives for Renewables and Efficiency) catalogs programs but is a reference database, not a matching engine — auditors must manually search and evaluate each program against their specific building and measures. EnergySage focuses on solar incentives. Rebate aggregator tools (Sealed, Pearl Certification) serve specific markets but do not cover the full landscape. No tool takes a building's audit data (location, utility territory, recommended measures with specifications) and automatically outputs a matched list of all applicable incentives with dollar amounts and application links.

## Problems
- [[niches/energy-auditors/rebate-matching-engines/build|🔨 Build: Audit-Integrated Incentive Matching Engine]]
- [[niches/energy-auditors/rebate-matching-engines/buy|🛒 Buy: Real-Time Program Rule Database]]
- [[niches/energy-auditors/rebate-matching-engines/fix|🔧 Fix: Stale Incentive Information in Proposals]]
