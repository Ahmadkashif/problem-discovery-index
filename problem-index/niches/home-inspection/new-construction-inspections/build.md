# Construction Phase Inspection Checklist by Code Jurisdiction

**Niche:** [[niches/home-inspection/new-construction-inspections/profile|New Construction Inspections]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A jurisdiction-aware checklist system that generates the correct inspection protocol for each construction phase based on the applicable building code version and local amendments — replacing the generic paper checklists that miss jurisdiction-specific requirements and leave inspectors guessing about which code provisions apply to the construction they're evaluating.
**Tags:** #bert #compliance #data-integration #automation

## The Problem
Building codes vary by jurisdiction. Texas has no state building code — each city adopts its own version of the IRC/IBC with local amendments. California uses the California Building Code (Title 24), which adds significant requirements beyond the base IRC. Illinois adopted the 2021 IRC but Cook County has amendments. An inspector performing new construction phase inspections must know which code version applies at the project address and what local amendments modify the base code. Currently, this knowledge is carried in the inspector's head or in paper reference binders. When an inspector works across multiple jurisdictions (common in metro areas that span city and county boundaries), they may apply the wrong code version — checking for 2018 IRC fire blocking requirements when the jurisdiction has adopted 2021 IRC, which changed spacing requirements. The consequence: missed code violations that surface years later as building failures or code enforcement actions.

## Why Nobody Has Built This
Building code data is published by each jurisdiction independently — there is no central database of which jurisdiction has adopted which code version with which amendments. The ICC publishes the base IRC/IBC, but local amendments are published in municipal ordinance databases, often as PDFs of city council resolutions. Extracting structured code requirements from these diverse sources requires NLP capable of parsing legal/regulatory text. The maintenance burden is continuous: jurisdictions update their code adoptions every 3-6 years, and the tool must track these changes across 30,000+ US jurisdictions.

## What to Build
A location-aware inspection checklist generator. Input: project address. The system: (1) identifies the applicable jurisdiction (city, county, or state) and the currently adopted building code version with local amendments from a maintained database; (2) generates phase-specific inspection checklists aligned to the applicable code — pre-slab checklist includes jurisdiction-specific requirements for vapor barriers, rebar specifications, and plumbing rough-in standards; framing checklist includes fire blocking requirements, structural connection standards, and window flashing requirements per the applicable code version; (3) highlights requirements that differ from the base IRC/IBC ("local amendment: R602.10.2 modified — continuous structural panel sheathing required on all braced wall panels, not just Method 3"). The checklist is delivered as a mobile-friendly form the inspector completes on-site with photos, producing a code-referenced report.

## Target Customer
Home inspectors adding new construction phase inspections to their service menu (a growing segment as builders offer warranty inspections and buyers demand independent verification). Code compliance consultants serving builders and developers.

## Impact If Built
Eliminates jurisdiction-specific code errors that currently occur on 15-25% of new construction inspections in multi-jurisdiction markets. Reduces inspector prep time from 30-60 minutes of code research per project to instant checklist generation. Enables inspectors without deep code expertise to offer new construction inspections with confidence, expanding the addressable market for this high-margin service ($600-1,500 per 3-phase inspection versus $400-500 for a standard existing-home inspection).
