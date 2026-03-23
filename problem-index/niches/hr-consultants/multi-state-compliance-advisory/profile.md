# Multi-State Compliance Advisory

**Parent Industry:** [[industries/hr-consultants|HR Consultants]]
**Category:** High Market Share

## Profile
**Market Size:** $8-10B
**Share of Parent Industry:** ~35%
**Digital Adoption:** Medium — compliance tracking tools exist (Mineral, SixFifty) but don't map changes to specific client configurations
**Target Buyer:** Compliance-focused HR consultant managing 20-80 SMB clients across 10-30 states
**Automation Potential:** High — compliance monitoring is rule-matching: legal changes mapped to client attributes (state, headcount, industry) with deterministic outcome (action required or not)

## What Makes This a Distinct Niche
Multi-state employment law compliance is the highest-value, most complex service HR consultants provide. Every state has its own employment laws covering: minimum wage, overtime exemptions, paid leave (sick, family, parental), pay transparency, ban-the-box, non-compete restrictions, harassment training mandates, and wage payment/frequency requirements. Cities and counties layer additional requirements (NYC fair chance hiring, San Francisco HCSO, Seattle secure scheduling). A consultant managing 50 SMB clients across 20 states tracks thousands of legal requirements, each potentially affected by legislative sessions, agency rulemakings, and court decisions. The combinatorial explosion — 50 clients x 20 states x 30 requirement categories — makes this unsustainable without systematic tooling.

## Current Tools & Gaps
Mineral (formerly ThinkHR) and SHRM provide legal update feeds with analysis. SixFifty automates employment document generation with state-specific clauses. ComplianceHR offers jurisdiction-specific compliance assessments. None of these tools provide the mapping layer that a multi-client consultant needs: "This new Colorado law affects clients A, D, and G because they have 50+ employees in Colorado, but not client B because their Colorado headcount is under the threshold." The consultant must manually cross-reference every legal update against every client's configuration.

## Problems
- [[niches/hr-consultants/multi-state-compliance-advisory/build|🔨 Build: Client-Mapped Employment Law Change Alert Engine]]
- [[niches/hr-consultants/multi-state-compliance-advisory/buy|🛒 Buy: Mineral/SixFifty with Multi-Client Portfolio Mapping]]
- [[niches/hr-consultants/multi-state-compliance-advisory/fix|🔧 Fix: State Employment Law Threshold Tracking Per Client]]
