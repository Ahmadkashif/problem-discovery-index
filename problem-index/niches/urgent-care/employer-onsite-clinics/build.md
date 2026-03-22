# Unified Occupational Health + UC Workflow Platform

**Niche:** [[niches/urgent-care/employer-onsite-clinics/profile|Employer On-Site Clinics]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** On-site clinic operators get a single platform that handles walk-in urgent care workflow, occupational health assessments, OSHA compliance tracking, and employer-direct billing — instead of running two disconnected systems and bridging data manually.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #compliance

## The Problem
An employer on-site clinic sees three types of visits in a single day: a warehouse worker with a laceration (workers' comp, OSHA-reportable), an office employee with strep throat (employer-funded primary care), and a CDL driver needing a DOT physical (regulatory compliance). Each visit type has different clinical protocols, different billing paths, different compliance documentation requirements, and different reporting destinations. No single platform handles all three. The clinic runs Experity for the urgent care visits and Net Health for occupational health, manually re-entering patient demographics and clinical data between systems. OSHA 300 logs are maintained in a separate spreadsheet. Employer invoicing is done monthly in QuickBooks. The clinic manager spends 30-40% of their time on data bridging and compliance documentation rather than patient care operations.

## Why Nobody Has Built This
The employer on-site clinic market is dominated by three large operators (Concentra, CareHere, Marathon Health) who have built proprietary internal platforms. The remaining independent market — small employers contracting with local occupational health providers or urgent cares — is fragmented and difficult to sell into. The product must bridge two different regulatory worlds (CMS/insurance for clinical care and OSHA/DOT for occupational health) with different terminology, different documentation standards, and different compliance auditing requirements. Building this requires domain expertise in both UC clinical workflow and occupational health regulation — a rare combination.

## What to Build
A unified clinical workflow platform that handles all employer on-site clinic visit types in a single system. Walk-in urgent care visits use standard UC clinical templates and can be billed to insurance when applicable. Workers' comp visits auto-trigger OSHA log entries, First Report of Injury generation, and workers' comp billing workflows. DOT physicals follow FMCSA-mandated exam templates and auto-submit to the National Registry. Drug/alcohol testing follows chain-of-custody documentation with auto-reporting to employer and MRO. All visit types share a single patient record, single login, and single reporting dashboard. Employer-facing portal shows utilization analytics, injury trends, return-to-work timelines, and monthly invoicing detail.

## Target Customer
Independent occupational health providers operating on-site or near-site clinics for employers, currently running dual systems (one clinical, one occupational health) with manual data bridging. Secondary market: mid-size employers (500-5,000 employees) evaluating on-site clinic programs who are deterred by the technology complexity.

## Impact If Built
Eliminates 30-40% of clinic manager time spent on dual-system data entry and reconciliation. Reduces OSHA compliance errors (which carry $15,625 per violation penalties) by auto-generating log entries from clinical documentation. Enables independent operators to compete with Concentra and CareHere on technology capability, expanding the market for employer on-site clinics beyond the three dominant vendors.
