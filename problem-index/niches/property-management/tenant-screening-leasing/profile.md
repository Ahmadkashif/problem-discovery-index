# Tenant Screening & Leasing

**Parent Industry:** [[industries/property-management|Property Management]]
**Category:** Highly Automatable

## Profile
**Market Size:** $3-5B (embedded across all PM segments)
**Share of Parent Industry:** Cross-cutting function — every occupied unit requires screening and leasing
**Digital Adoption:** Medium — TransUnion SmartMove, Experian RentBureau, and RealPage screening pull credit and criminal data. But the decision logic (accept/reject/conditional) remains the property manager's subjective judgment, creating fair housing risk and inconsistent outcomes.
**Target Buyer:** Property manager, leasing agent, or landlord making tenant selection decisions
**Automation Potential:** High — applicant scoring is a classification problem with rich feature sets, fair housing compliance is a rules-based automation task, and lease renewal timing optimization is a regression problem

## What Makes This a Distinct Niche
Tenant screening is the most consequential decision in property management: selecting the right tenant prevents eviction, property damage, and neighborhood disruption; selecting the wrong tenant creates $5K-15K in damages, lost rent, and legal costs. Current screening relies on credit reports, criminal background checks, eviction history, income verification, and landlord references — data points that the PM must synthesize into an accept/reject/conditional decision. This synthesis is subjective: one PM accepts a 580 credit score with strong income; another rejects it. One PM ignores a 5-year-old misdemeanor; another rejects the applicant. This inconsistency creates fair housing liability (different standards applied to different applicants = potential discrimination) and suboptimal outcomes (overly strict criteria create extended vacancies; overly lenient criteria create problem tenants).

## Current Tools & Gaps
TransUnion SmartMove and Experian RentBureau pull credit, criminal, and eviction data. RealPage offers AI-assisted screening recommendations. AppFolio integrates screening into the leasing workflow. But the decision-making layer — converting data into a consistent, defensible, fair-housing-compliant decision — remains the PM's judgment in most implementations. No tool monitors for disparate impact: do applicants from one demographic group get rejected at higher rates than another, controlling for the documented criteria?

## Problems
- [[niches/property-management/tenant-screening-leasing/build|🔨 Build: AI-Assisted Application Scoring with Fair Housing Compliance]]
- [[niches/property-management/tenant-screening-leasing/buy|🛒 Buy: TransUnion/Experian with Decision Logic Layer]]
- [[niches/property-management/tenant-screening-leasing/fix|🔧 Fix: Lease Renewal Timing Optimization]]
