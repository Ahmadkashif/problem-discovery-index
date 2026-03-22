# Tenant Screening Inconsistency and Fair Housing Risk

**Niche:** [[niches/property-management/self-managing-landlords/profile|Self-Managing Landlords]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Fix (Pain Point)
**One-liner:** Self-managing landlords screen tenants using gut feel during showings — accepting or rejecting applicants based on subjective impressions — exposing themselves to fair housing discrimination claims and placing tenants who later fail to pay rent, while professional screening services require setup and processes these landlords don't implement.
**Tags:** #gradient-boosting #compliance #automation #quick-win #logistic-regression

## The Problem
A self-managing landlord advertises their rental, gets 5-10 inquiries, shows the property, and selects a tenant. The selection criteria: "they seemed responsible," "they had a steady job," "I liked them." This subjective process has two problems. First, discrimination risk: if the landlord rejects a Black applicant and accepts a White applicant with similar qualifications, the landlord faces a fair housing complaint — even if their decision was based on legitimate factors, they have no documented criteria to demonstrate non-discriminatory selection. HUD receives 28,000+ fair housing complaints annually, and individual landlords are disproportionately targeted because they lack documented screening processes. Second, bad selection: without credit checks, eviction history, and income verification, landlords accept tenants who fail to pay rent at 2-3x the rate of professionally screened tenants. An eviction costs $3,000-10,000 in legal fees, lost rent, and property damage.

## Why It's Still Broken
Professional screening services (TransUnion SmartMove, RentPrep, Avail screening) exist and cost $30-45 per applicant. But small landlords don't use them because: (1) setup requires creating an account, understanding the products, and learning the interface — a 30-minute investment for a tool they use 1-2 times per year; (2) they don't know how to interpret a credit report — a 620 FICO with a medical collection means something different than a 620 with a previous eviction; (3) they don't know what criteria to set — what income-to-rent ratio is acceptable? What credit score threshold? What criminal history policy complies with their state's ban-the-box law? Most landlords who do run credit checks don't have documented screening criteria, leaving them vulnerable to discrimination claims.

## What a Fix Looks Like
A screening system designed for landlords who screen 1-5 tenants per year: (1) the landlord enters the rent amount and the system auto-sets screening criteria using industry-standard thresholds (3x income, 620+ credit, no evictions in 5 years, customizable by the landlord) — documented criteria that demonstrate non-discriminatory selection; (2) the applicant receives a link (via text message), enters their information, authorizes the screening, and the system returns a simple pass/fail/conditional recommendation with plain-English explanation ("Approved: income $4,200/month exceeds 3x rent requirement, credit score 680, no evictions" or "Conditional: credit score 590 below 620 threshold, but no evictions and strong income — consider with additional deposit"); (3) every screening decision is logged with the criteria applied, creating a fair housing compliance record; (4) the system generates a state-compliant adverse action notice when an applicant is denied, as required by the FCRA.

## Who Feels the Pain
Landlords who accept bad tenants because they screened by gut feel and are now pursuing eviction. Landlords who face fair housing complaints because they can't demonstrate consistent, non-discriminatory screening criteria. Tenants who are unfairly denied housing by landlords making subjective decisions.

## Impact If Fixed
Reduces bad-tenant placement by 40-60% through standardized screening criteria. Protects landlords from fair housing claims by documenting consistent, criteria-based selection. Reduces eviction costs by $3K-10K per avoided bad placement. Could be offered at $25-35 per screening with the criteria-setting and compliance documentation as the value-add over basic credit pulls.
