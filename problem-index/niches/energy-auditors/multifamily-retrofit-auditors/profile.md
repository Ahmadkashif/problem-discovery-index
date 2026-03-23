# Multifamily Retrofit Auditors

**Parent Industry:** [[industries/energy-auditors|Energy Auditors]]
**Category:** Low Digitized

## Profile
**Market Size:** $500-800M
**Share of Parent Industry:** ~10-16%
**Digital Adoption:** Low — Multifamily energy audits rely on single-family residential tools stretched beyond their design, or commercial tools that miss the split-incentive dynamics unique to rental properties
**Target Buyer:** Property management company / multifamily developer / housing authority
**Automation Potential:** Medium — Unit-level sampling protocols are standardizable, but the building-level systems and tenant coordination add complexity

## What Makes This a Distinct Niche
Multifamily buildings (5+ units) fall between residential and commercial energy audit methodologies — they have residential-style tenant spaces but commercial-scale mechanical systems (central boilers, cooling towers, common area lighting). The audit challenge is compounded by the split-incentive problem: the building owner pays for capital improvements but tenants pay the utility bills (in most cases), so the owner captures no financial benefit from efficiency upgrades unless they can restructure utility billing. Auditing multifamily buildings requires sampling strategies (auditing a representative subset of 10-20% of units rather than every unit), common-area-specific analysis (hallway lighting, lobby HVAC, parking garage ventilation), and tenant coordination (scheduling access to occupied units). No energy modeling tool is designed for this hybrid residential-commercial building type.

## Current Tools & Gaps
TREAT and Ekotrope model individual dwelling units but cannot model a building with 50 units, central mechanical systems, and shared infrastructure. eQUEST and EnergyPlus can model the whole building but require commercial-level expertise and do not handle the unit-level granularity that tenants and programs require. No tool integrates unit sampling, building-level modeling, and split-incentive financial analysis into a single audit workflow.

## Problems
- [[niches/energy-auditors/multifamily-retrofit-auditors/build|🔨 Build: Multifamily-Specific Energy Audit and Modeling Platform]]
- [[niches/energy-auditors/multifamily-retrofit-auditors/buy|🛒 Buy: Unit Sampling Protocol and Extrapolation Engine]]
- [[niches/energy-auditors/multifamily-retrofit-auditors/fix|🔧 Fix: Tenant Access Coordination for Unit Audits]]
