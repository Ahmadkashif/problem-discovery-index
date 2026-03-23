# ASHRAE Audit Workflow Platform

**Niche:** [[niches/energy-auditors/commercial-ashrae-auditors/profile|Commercial ASHRAE Auditors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No integrated platform takes a commercial energy auditor from field data collection through energy modeling to ASHRAE Standard 211-compliant report delivery in a single workflow.
**Tags:** #workflow-orchestration #automation #data-integration #ai-platform

## The Problem
A commercial ASHRAE Level II audit involves: 1-3 days of field data collection (equipment nameplate data for 50-200 pieces of mechanical equipment, lighting inventory across dozens of spaces, envelope measurements, BAS trend data downloads), 2-4 weeks of energy modeling (building the eQUEST or EnergyPlus model, calibrating to utility bills, running ECM scenarios), and 1-2 weeks of report writing (formatting data, creating charts, writing narrative analysis, preparing financial tables). Each phase uses different tools — clipboard/tablet for field data, modeling software for analysis, Word/Excel for the report — with manual data transfer between them. The transfer points (field notes to model inputs, model outputs to report tables) are where errors compound and time accumulates.

## Why Nobody Has Built This
Commercial energy auditing is a small market (fewer than 5,000 active ASHRAE-certified auditors in the US) with high per-project complexity and heterogeneity — no two buildings are alike, making templating difficult. The modeling engines (eQUEST, EnergyPlus) are mature open-source tools that auditors know well; replacing them is not viable, so any platform must integrate with them rather than substitute for them. The report formatting requirements vary by client and standard (ASHRAE 211, LEED, local benchmarking ordinances), adding customization demands.

## What to Build
A workflow platform that provides: (1) a mobile field data collection app with commercial-specific templates (HVAC equipment schedules, lighting power density surveys, envelope assemblies), (2) automated model input generation that converts field data into eQUEST/EnergyPlus input files, (3) an ECM analysis module that runs scenarios and generates savings/cost/financial tables, and (4) an ASHRAE Standard 211-compliant report generator that pulls results into a formatted deliverable with charts, tables, and narrative sections. Changes to field data cascade through modeling and into the report without manual re-entry.

## Target Customer
Commercial energy audit firms billing $10K-$200K per ASHRAE Level II/III audit who spend 40-60% of project time on data management and report formatting rather than engineering analysis.

## Impact If Built
Reduces total project time by 30-40% (saving 15-80 hours per audit at $100-$200/hour billing rates), eliminates data transfer errors between workflow stages, and enables firms to complete 30-40% more audits per year without adding engineering staff.
