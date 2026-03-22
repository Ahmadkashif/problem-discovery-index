# Unit Turnover Electrical Checklist Standardization

**Niche:** [[niches/electrical-contractors/multi-family-property-management/profile|Multi-Family Property Management Electrical]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** What must be electrically inspected and repaired when a tenant moves out varies by jurisdiction, building age, and wiring type — no standardized checklist exists, so property managers either skip electrical inspection entirely (liability risk) or rely on whatever the electrician decides to check (inconsistent quality).
**Tags:** #compliance #automation #worker-facing #data-integration

## The Problem
When a tenant vacates an apartment, the property manager coordinates a turnover process: cleaning, painting, appliance inspection, and — theoretically — electrical inspection. In practice, electrical inspection at turnover is skipped in 60-70% of turnovers because there's no standardized checklist, no clear requirement, and the property manager doesn't know what should be checked. When an electrician is called for turnover inspection, different electricians check different things: one tests all outlets for proper grounding and GFCI function, another just checks that the lights work. The checklist should be jurisdiction-specific (some jurisdictions require GFCI upgrades at turnover, others don't), building-specific (aluminum wiring buildings need connection inspection, pre-1960 buildings need cloth wiring assessment), and unit-specific (if the previous tenant added a window A/C unit, check the circuit for damage). No such checklist exists in any standardized form.

## Why It's Still Broken
The intersection of landlord-tenant law, building codes, and electrical codes creates a complex compliance matrix that no single party owns. Property managers know landlord-tenant law but not electrical code. Electricians know NEC but not local landlord-tenant requirements. Building inspectors enforce code at construction/renovation but not at tenant turnover. The result is a gap: everyone assumes someone else is handling electrical safety at turnover. Professional organizations (NFPA, IAEI) publish general electrical inspection checklists but not turnover-specific ones adapted to jurisdiction and building characteristics. Creating a proper checklist requires mapping the intersection of three regulatory domains — something no one has incentive to do for a workflow that happens one unit at a time.

## What a Fix Looks Like
A jurisdiction-aware, building-specific electrical turnover checklist generator. The property manager enters the building's jurisdiction (city/county), year built, wiring type (if known), and the unit being turned over. The system generates a prioritized inspection checklist: (1) safety-critical items required by local code or landlord-tenant law (smoke/CO detectors, GFCI protection where mandated, no exposed wiring); (2) recommended items based on building characteristics (aluminum wiring connection inspection for pre-1975 buildings, outlet grounding test for pre-1965 buildings, AFCI breaker upgrade for jurisdictions requiring it at tenant change); (3) optional upgrades the property manager can authorize (USB outlets, smart switches, EV-ready circuit in parking). The electrician completes the checklist on a mobile device, photos and findings are recorded per unit, and the property manager receives a pass/fail report with estimated remediation costs for any deficiencies.

## Who Feels the Pain
Property managers who don't know what electrical inspection is needed at turnover and default to skipping it (creating liability exposure), electricians who want to provide thorough turnover inspections but have no standardized scope to propose, and incoming tenants who move into units with electrical safety issues that should have been caught between tenancies.

## Impact If Fixed
Establishes a consistent electrical inspection standard at unit turnover, catching safety deficiencies before a new tenant moves in. Reduces property manager liability by creating documented evidence of electrical inspection. Creates a predictable revenue stream for electricians — at $75-150 per unit turnover inspection, a 200-unit property with 40% annual turnover generates $6K-12K per year in inspection revenue.
