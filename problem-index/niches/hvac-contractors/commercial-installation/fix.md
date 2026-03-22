# Commissioning Documentation Gaps

**Niche:** [[niches/hvac-contractors/commercial-installation/profile|Commercial Installation]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Commercial HVAC commissioning requires documenting that every piece of installed equipment meets design specifications — but commissioning reports are assembled manually from handwritten field notes, photos, and spreadsheets, delaying project closeout by weeks and creating liability exposure when documentation is incomplete.
**Tags:** #automation #compliance #workflow-orchestration #large-language-models

## The Problem
When a commercial HVAC installation is complete, the system must be commissioned — every rooftop unit, air handler, VAV box, chiller, and pump is tested against design specifications, and the results are documented in a commissioning report that becomes part of the permanent building record. A typical 100,000 sq ft office building has 50-200 pieces of HVAC equipment, each requiring 10-30 data points recorded during functional performance testing: airflow measurements, temperature differentials, refrigerant charges, control sequences, vibration readings, and balancing data. Field technicians record this data on paper forms or in spreadsheets on tablets, take photos of equipment nameplates and test setups, and hand the raw data to a project manager who spends 20-60 hours compiling it into a formatted commissioning report. Missing data points — a thermostat calibration check that was performed but not recorded, a photo of a nameplate that wasn't taken — require return trips to the site at $500-1,500 each.

## Why It's Still Broken
Commissioning documentation has no standardized digital workflow. ASHRAE Guideline 0 and ASHRAE Standard 202 define commissioning processes, but the documentation format is left to the commissioning agent or contractor. Every project creates its own spreadsheet template. The field data collection happens under time pressure at project end — the general contractor wants the HVAC contractor off-site, the owner wants to occupy the building, and the commissioning documentation is treated as paperwork to rush through rather than a quality assurance process. No commercial HVAC software platform (Trane, Carrier, or field service tools) includes a commissioning documentation module. Third-party commissioning software (CxAlloy, FacilitiesNet) exists but is designed for independent commissioning agents, not for HVAC contractors who need to feed data from their installation crews.

## What a Fix Looks Like
A mobile-first commissioning data collection app that pre-loads the equipment schedule from the project design documents, generates equipment-specific test checklists (different tests for RTUs vs. VAV boxes vs. chillers), captures field data and photos on-site with GPS and timestamp metadata, flags missing data points before the crew leaves the site, and auto-generates a formatted commissioning report (PDF + structured data) that meets ASHRAE Guideline 0 requirements. The project manager's 20-60 hour report compilation drops to 2-4 hours of review. An LLM layer auto-generates narrative descriptions of test results and exception notes from the structured data, producing a professional report without manual writing.

## Who Feels the Pain
Project managers who spend evenings and weekends compiling commissioning reports from field notes and photos, field technicians who get sent back to completed job sites to collect data they forgot to record, and company owners who hold 5-10% retainage ($20K-100K per project) hostage until commissioning documentation is accepted.

## Impact If Fixed
Reduces commissioning documentation time by 80%, saving $3,000-10,000 in labor per commercial project. Eliminates 2-5 return site visits per project ($1,000-7,500 in direct costs). Accelerates retainage release by 2-4 weeks, improving cash flow by $20K-100K per project.
